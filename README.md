# EVA 人资部内训网站

基于 Zensical，资料位于 `docs/`，原课件位于 `PPT/`。

## 本地预览

```sh
uv venv .venv
uv pip install --python .venv/bin/python zensical
.venv/bin/zensical serve
```

## 构建

```sh
.venv/bin/zensical build --clean
```

输出目录为 `site/`。现有 GitHub Pages 工作流会在推送至 main/master 时构建与部署。

## 编辑位置

- `zensical.toml`：站名、导航、主题与站点地址
- `docs/index.md`：首页入口
- `docs/about.md`：部门、联系人和服务信息
- `docs/training/`：内训课程
- `docs/maintenance/`：系统与磁盘资料
- `docs/hardware/`：硬件维护资料
- `docs/assets/ppt/`：课件配图

## 重新转换 PPT

```sh
.venv/bin/python scripts/convert_ppt.py
```

转换脚本仅使用 Python 标准库，保留课件页序、段落、嵌入图片与正文讲者备注。它会覆盖 6 份转换文档，手动修改文档后请谨慎重新执行。生成的 Markdown 不复现幻灯片的空间排版，文字标签与原图分别呈现。

“C盘的清理&扩容.pptx”是 macOS 替身，完整内容采用“清C盘.pptx”。原课件中的历史 Windows 版本、联网与激活方式保留为历史资料，重装页另有阅读提示。

上线前将 `zensical.toml` 中注释的 `site_url` 换成实际地址，并按需填写 `docs/about.md`。

## 字体

`project.theme.font = false` 关闭 Google Fonts 自动加载。`docs/stylesheets/fonts.css` 使用本地字体文件，并通过原生主题变量设置回退列表。

- 正文：LXGW WenKai Screen v1.522，回退至 Microsoft YaHei 和系统无衬线字体。
- 代码：JetBrains Mono v2.304，回退至 Sarasa Mono SC、Consolas 和系统等宽字体。

首选字体与 OFL 许可证位于 `docs/assets/fonts/`，无需访问外部字体服务。回退字体需安装在访问者电脑上。加粗与斜体由浏览器合成。
