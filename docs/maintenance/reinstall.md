# 重装系统

先确认故障与备份，再进入 PE、安装系统，最后检查驱动与授权。

**内训时间：** 待补充  
**来源课件：** 重装系统.pptx

## 阅读说明

下方按原课件页序保留文字与配图。截图中的个人信息、示例路径及课件中的历史版本要求，请按实际情况更新。

!!! warning "操作前确认"

    涉及分区、格式化或硬件拆装时，先确认数据备份、目标设备和机主授权。分区与系统安装过程中保持供电；拆机前关机、拔掉外部电源并断开内置电池。

!!! note "历史课件内容"

    原课件保留了指定 Windows 版本、跳过联网和第三方激活步骤。这些内容仅作为历史培训记录，具体安装流程应按当前系统版本确认。系统激活使用机主的有效许可证或组织授权。

## 第 1 页 · 内训时间：2026年XX月XX日

内训时间：2026年XX月XX日

人资部春夏第二次内训

重装系统

![重装系统，第 1 页配图 3](../assets/ppt/reinstall/e33c53829815a920.jpeg){ loading=lazy }

## 第 2 页 · 前言

前言

重装系统可以解决什么问题呢？

①系统崩溃、系统更新出现问题

②更换新硬盘，进行系统迁移

③帮助摆脱流氓软件

不要盲目重装系统！

重装系统无法解决硬件问题！！！

重装通常需要较长时间，且有数据不慎遗失的风险。

## 第 3 页 · 备份数据

备份数据

备份数据！备份数据！备份数据！

重装系统会格式化C盘，或格式化整块硬盘，因此重装前需要备份

记得提醒机主如毕业设计、实验数据在内的重要资料是否拷贝，以免丢失

备份内容：部分应用数据、C盘内的重要文件

备份工具：协会的备份盘，建议用固态+硬盘盒+C to C数据线（cqh的爱线，使用后请返回原处）

## 第 4 页 · PE盘

PE盘

PE盘（Windows Preinstallation Environment）

其主要作用是为计算机提供一个独立的、精简的Windows运行环境。重装系统时，通过PE盘引导，用户可以在不依赖硬盘原有系统的情况下进入一个功能齐全的操作界面。在此环境中，可以执行重装系统、分区管理等多种操作。

协会可靠的两种PE盘

![重装系统，第 4 页配图 4](../assets/ppt/reinstall/4785b58cfd5820f9.jpeg){ loading=lazy }

![重装系统，第 4 页配图 5](../assets/ppt/reinstall/f9a17006dff45bed.jpeg){ loading=lazy }

## 第 5 页 · 重装系统需要的工具

重装系统需要的工具

目前的PE盘存在的工具：

图吧工具箱2025：

内部含有多种重要工具，如FurMark、Crystal Disk Info等

Windows以及其他系统的镜像：

用于重装系统

win11版本一定要是“24H2”或“25H2” ！！

![重装系统，第 5 页配图 4](../assets/ppt/reinstall/2279e657e55a5071.png){ loading=lazy }

![重装系统，第 5 页配图 5](../assets/ppt/reinstall/0bfbfeb440b7fd07.png){ loading=lazy }

## 第 6 页 · 重装系统的步骤

重装系统的步骤

重装系统的步骤大概是以下几步：

①对需要格式化的硬盘备份数据

②进BIOS修改启动顺序，让电脑从PE盘启动

③对C盘进行格式化操作

④使用镜像中的程序安装系统

⑤用新系统启动电脑，完成各种设置、安装驱动、激活系统

重装系统前，

请确保连接电源适配器，

不要在离电情况下重装系统！

## 第 7 页 · BIOS修改启动顺序

BIOS修改启动顺序

电脑默认进入内置的硬盘的系统。重装系统时，需要从PE盘启动电脑，因此需要进入BIOS修改操作系统的引导顺序。

开机时反复按下特定按键进入 BIOS（具体按键自行搜索），进入 BIOS 后找到操作系统引导顺序，进行修改。

![重装系统，第 7 页配图 4](../assets/ppt/reinstall/f6d76442c9b68e36.png){ loading=lazy }

![重装系统，第 7 页配图 5](../assets/ppt/reinstall/b5dcdd197a1ffc7e.jpeg){ loading=lazy }

## 第 8 页 · BitLocker

BitLocker

在PE中对原硬盘进行操作时，有可能会在硬盘上发现一个锁状标记，这代表着这块盘开启了BitLocker

这代表着硬盘已经被加密，此时无法对这块盘进行访问的。需要登录Microsoft账户查询解锁代码进行解锁。密码有48位，而且解密需要很多时间。

如果能进入原系统，也可以在“设置\>设备加密”中关闭加密选项进行BitLocker解密

密码可以在https://aka.ms/myrecoverykey查询

![重装系统，第 8 页配图 4](../assets/ppt/reinstall/979e4df615cea1f1.png){ loading=lazy }

![重装系统，第 8 页配图 5](../assets/ppt/reinstall/8a71fbd4be964c15.png){ loading=lazy }

## 第 9 页 · 格式化硬盘

格式化硬盘

如果只需要格式化C盘，那么可以直接在安装过程中进行格式化。

如果需要对整块硬盘进行操作，那么推荐使用 分区助手 进行操作。

一般分区表格式都是对的，不需要操作。但是在新的没有初始化过的硬盘上安装系统时需要初始化分区表，这时就需要注意了。对于UEFI启动的电脑，需要把硬盘格式化为 GUID 分区表（GPT格式）。

注意：修改分区表格式会格式化整块硬盘！请提前备份数据！！！

硬性要求：在格式化之前，一定一定要询问机主是否确认保存好所有重要文件，并且让机主亲自按下格式化按钮。

## 第 10 页 · 使用Windows镜像

使用Windows镜像

操作系统的镜像（.iso文件）里面有一个 Set Up 程序，运行Set Up 即可进行系统的安装。

运行 Setup 程序后，就进入了Windows 安装的界面，选择语言、键盘设置、安装选项、安装映像后，我们就进入了选择安装位置的界面。

![重装系统，第 10 页配图 4](../assets/ppt/reinstall/4de757b98212faaf.png){ loading=lazy }

![重装系统，第 10 页配图 5](../assets/ppt/reinstall/03a32f1dbd94cef5.png){ loading=lazy }

![重装系统，第 10 页配图 6](../assets/ppt/reinstall/f0f77639382a8f9e.png){ loading=lazy }

![重装系统，第 10 页配图 7](../assets/ppt/reinstall/52a523d98cec177f.png){ loading=lazy }

![重装系统，第 10 页配图 8](../assets/ppt/reinstall/0bfbfeb440b7fd07.png){ loading=lazy }

## 第 11 页 · 使用Windows镜像进行系统重装

使用Windows镜像进行系统重装

Windows 安装程序也是可以对硬盘进行格式化和分区的，但还是建议使用 分区助手 进行分区等操作。

选择要安装系统的盘符，可以根据大小帮助寻找目标盘。

等待安装即可。

安装完毕后，程序会提示重启电脑，拔掉PE盘重启即可。

![重装系统，第 11 页配图 4](../assets/ppt/reinstall/17d04274968f98c6.png){ loading=lazy }

## 第 12 页 · 跳过联网

跳过联网

Win10可以直接选择“我没有网络连接”选项以跳过联网；Win11没有该选项，需要通过其他方式跳过网络连接。

打开cmd命令行（在安装界面按shift+F10，或shift+Fn+F10），输入oobe\\bypassnro，在回车后重启，即出现“我没有网络连接”

![重装系统，第 12 页配图 4](../assets/ppt/reinstall/ce2854d92abd8c23.png){ loading=lazy }

## 第 13 页 · 系统激活

系统激活

注意：激活需要联网！！

重装系统之后，

需要先下载网卡驱动在激活

打开浏览器，输入网址

https://massgrave.dev/

找到红框中的指令并复制

![重装系统，第 13 页配图 4](../assets/ppt/reinstall/704e98c798ea5dfd.png){ loading=lazy }

## 第 14 页 · 系统激活

系统激活

使用管理员方式打开powershell，

输入刚刚复制的指令：

irm https://get.activated.win \| iex

会弹出界面如下

键盘直接按下数字键“1”即可，

此后等待即可，电脑会自动激活

![重装系统，第 14 页配图 4](../assets/ppt/reinstall/d361ec7ffc191326.jpeg){ loading=lazy }

![重装系统，第 14 页配图 5](../assets/ppt/reinstall/d72785fdc8165aae.jpeg){ loading=lazy }

## 第 15 页 · Any question？

Any question？

![重装系统，第 15 页配图 4](../assets/ppt/reinstall/448489dfe66ad1da.png){ loading=lazy }

## 第 16 页 · 内训时间：2025年XX月XX日

内训时间：2025年XX月XX日

驳回感谢各位的批评指正！

THANK YOU FOR WATCHING

![重装系统，第 16 页配图 1](../assets/ppt/reinstall/448489dfe66ad1da.png){ loading=lazy }

## 课件重复配图

课件中多页重复出现的标识与装饰图在此集中保留。

??? info "展开查看原课件标识与装饰图"

    ![课件重复配图 1](../assets/ppt/reinstall/6f6120cba8ffa046.jpeg){ width=180 loading=lazy }

    ![课件重复配图 2](../assets/ppt/reinstall/72f668537210a0fe.jpeg){ width=180 loading=lazy }

    ![课件重复配图 3](../assets/ppt/reinstall/ed4f211557a0adc7.jpeg){ width=180 loading=lazy }
