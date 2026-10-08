"""Convert local PowerPoint training decks to Markdown and embedded image assets.
Run from the repository root: .venv/bin/python scripts/convert_ppt.py
"""
from pathlib import Path
import hashlib
from collections import Counter
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
DECKS = [
    ('Markdown.pptx', 'training/markdown.md', 'Markdown 入门', '2025 年 11 月 18 日', '了解 Markdown 的基本语法、编辑工具和记录方法。'),
    ('PE盘的使用.pptx', 'maintenance/pe.md', 'PE 盘的使用', '2025 年 11 月 25 日', '了解 PE 启动方式，以及磁盘、卸载、搜索和压力测试工具。'),
    ('清C盘.pptx', 'maintenance/c-drive.md', 'C 盘清理与扩容', '2025 年 12 月 2 日', '按观察空间、卸载软件、清理文件、修改路径、调整分区的顺序处理空间问题。'),
    ('重装系统.pptx', 'maintenance/reinstall.md', '重装系统', '待补充', '先确认故障与备份，再进入 PE、安装系统，最后检查驱动与授权。'),
    ('更换硅脂与加装硬盘&内存.pptx', 'hardware/upgrades.md', '更换硅脂与加装硬盘、内存', '2025 年 10 月 21 日', '认识散热模组，学习硅脂更换、硬盘与内存拆装及新硬盘分区。'),
    ('内训大回顾.pptx', 'training/review.md', '内训大回顾', '2026 年，具体日期待补充', '回顾清灰、换硅脂、硬件加装、PE 使用与 C 盘维护流程。'),
]

def paragraphs(node):
    result = []
    for para in node.findall('.//a:p', NS):
        text = ''.join('\n' if x.tag == '{'+NS['a']+'}br' else (x.text or '')
                       for x in para.iter() if x.tag in ('{'+NS['a']+'}t', '{'+NS['a']+'}br')).strip()
        if text:
            result.append(text)
    return result

def relations(z, part):
    path = posixpath.join(posixpath.dirname(part), '_rels', posixpath.basename(part)+'.rels')
    if path not in z.namelist():
        return {}
    return {x.attrib['Id']: x.attrib for x in ET.fromstring(z.read(path))}

def resolve(part, target):
    return posixpath.normpath(posixpath.join(posixpath.dirname(part), target))

def escape(text):
    return re.sub(r'([\\`*\[\]<>#|_])', r'\\\1', text)

def convert(filename, output, title, date, summary):
    destination = ROOT/'docs'/output
    if destination.exists() and 'manually-maintained-guide:' in destination.read_text(encoding='utf-8'):
        print(f'Skipped manually maintained guide: {output}')
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    slug = destination.stem
    asset_dir = ROOT/'docs/assets/ppt'/slug
    asset_dir.mkdir(parents=True, exist_ok=True)
    content = [f'# {title}', '', summary, '', f'**内训时间：** {date}  ', f'**来源课件：** {filename}', '',
               '## 阅读说明', '', '下方按原课件页序保留文字与配图。截图中的个人信息、示例路径及课件中的历史版本要求，请按实际情况更新。', '']
    if slug in ('reinstall', 'c-drive', 'upgrades', 'pe'):
        content += ['!!! warning "操作前确认"', '', '    涉及分区、格式化或硬件拆装时，先确认数据备份、目标设备和机主授权。分区与系统安装过程中保持供电；拆机前关机、拔掉外部电源并断开内置电池。', '']
    if slug == 'reinstall':
        content += ['!!! note "历史课件内容"', '', '    原课件保留了指定 Windows 版本、跳过联网和第三方激活步骤。这些内容仅作为历史培训记录，具体安装流程应按当前系统版本确认。系统激活使用机主的有效许可证或组织授权。', '']
    if slug == 'pe':
        content += ['!!! note "诊断提示"', '', '    SMART 指标需要结合硬盘类型及厂商定义判断；原课件的 0E 描述不能套用到所有硬盘。发现读取异常时先备份，再进行检测。', '']
    image_count = 0
    with zipfile.ZipFile(ROOT/'PPT'/filename) as z:
        presentation = ET.fromstring(z.read('ppt/presentation.xml'))
        pres_rels = relations(z, 'ppt/presentation.xml')
        slides = [resolve('ppt/presentation.xml', pres_rels[x.attrib['{'+NS['r']+'}id']]['Target'])
                  for x in presentation.findall('./p:sldIdLst/p:sldId', NS)]
        frequencies = Counter()
        for part in slides:
            rels = relations(z, part)
            root = ET.fromstring(z.read(part))
            frequencies.update(set(resolve(part, rels[blip.get('{'+NS['r']+'}embed')]['Target'])
                                   for blip in root.findall('.//a:blip', NS)
                                   if blip.get('{'+NS['r']+'}embed') in rels))
        recurring = {media for media, count in frequencies.items() if count >= max(4, len(slides) // 2)}
        recurring_links = {}
        for number, part in enumerate(slides, 1):
            root = ET.fromstring(z.read(part))
            rels = relations(z, part)
            shapes = root.findall('./p:cSld/p:spTree/p:sp', NS)
            title_text = ''
            for shape in shapes:
                placeholder = shape.find('./p:nvSpPr/p:nvPr/p:ph', NS)
                if placeholder is not None and placeholder.get('type') in ('title', 'ctrTitle'):
                    title_text = ' '.join(paragraphs(shape)); break
            all_text = paragraphs(root)
            heading = title_text or (all_text[0] if all_text and len(all_text[0]) < 65 else '课件内容')
            heading = re.sub(r'\s+', ' ', heading)
            content += [f'## 第 {number} 页 · {escape(heading)}', '']
            for text in all_text:
                # Literal slide copy must not accidentally become Markdown directives.
                content += [escape(text).replace('\n', '  \n'), '']
            seen = set()
            for blip in root.findall('.//a:blip', NS):
                rid = blip.get('{'+NS['r']+'}embed')
                if rid not in rels: continue
                media = resolve(part, rels[rid]['Target'])
                if media in seen: continue
                seen.add(media)
                data = z.read(media)
                suffix = Path(media).suffix.lower()
                if suffix not in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'):
                    if data.startswith(b'\x89PNG'): suffix = '.png'
                    elif data.startswith(b'\xff\xd8'): suffix = '.jpg'
                    else: raise ValueError(f'Unsupported image: {filename}: {media}')
                asset = asset_dir/(hashlib.sha256(data).hexdigest()[:16]+suffix)
                asset.write_bytes(data)
                link = posixpath.relpath(asset.relative_to(ROOT/'docs').as_posix(), destination.parent.relative_to(ROOT/'docs').as_posix())
                if media in recurring:
                    recurring_links[media] = link
                else:
                    content += [f'![{title}，第 {number} 页配图 {len(seen)}]({link})' + '{ loading=lazy }', '']
                image_count += 1
            for rel in rels.values():
                if rel.get('Type', '').endswith('/notesSlide'):
                    note = ET.fromstring(z.read(resolve(part, rel['Target'])))
                    notes = []
                    for shape in note.findall('.//p:sp', NS):
                        ph = shape.find('./p:nvSpPr/p:nvPr/p:ph', NS)
                        if ph is not None and ph.get('type') == 'body': notes.extend(paragraphs(shape))
                    if notes: content += ['**讲者备注**', ''] + [escape(x)+'\n' for x in notes]
        if recurring_links:
            content += ['## 课件重复配图', '', '课件中多页重复出现的标识与装饰图在此集中保留。', '', '??? info "展开查看原课件标识与装饰图"', '']
            for i, link in enumerate(recurring_links.values(), 1):
                content += [f'    ![课件重复配图 {i}]({link})' + '{ width=180 loading=lazy }', '']
    destination.write_text('\n'.join(content), encoding='utf-8')
    print(f'{filename}: {len(slides)} slides, {image_count} images -> {output}')

if __name__ == '__main__':
    for deck in DECKS: convert(*deck)
