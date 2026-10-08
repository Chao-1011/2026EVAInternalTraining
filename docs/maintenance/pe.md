# PE 盘的使用

了解 PE 启动方式，以及磁盘、卸载、搜索和压力测试工具。

**内训时间：** 2025 年 11 月 25 日  
**来源课件：** PE盘的使用.pptx

## 阅读说明

下方按原课件页序保留文字与配图。截图中的个人信息、示例路径及课件中的历史版本要求，请按实际情况更新。

!!! warning "操作前确认"

    涉及分区、格式化或硬件拆装时，先确认数据备份、目标设备和机主授权。分区与系统安装过程中保持供电；拆机前关机、拔掉外部电源并断开内置电池。

!!! note "诊断提示"

    SMART 指标需要结合硬盘类型及厂商定义判断；原课件的 0E 描述不能套用到所有硬盘。发现读取异常时先备份，再进行检测。

## 第 1 页 · 人资部第4次内训

人资部第4次内训

内训时间：2025年11月25日

PE盘的使用

![PE 盘的使用，第 1 页配图 1](../assets/ppt/pe/4df15ae7b1c5d04a.jpeg){ loading=lazy }

## 第 2 页 · Preview

Preview

之前内训过的内容

第一次内训：清灰 & 换硅脂

第二次内训：更换硅脂 & 加装硬盘 / 内存

第三次内训（Some simple but useful tools）：Markdown

第四次内训：To be continue

## 第 3 页 · 什么是PE盘

什么是PE盘

协会可靠的两种PE盘

PE盘是指安装在U盘或光盘中的Windows预安装环境（Preinstallation Environment），是一种微型系统。

PE启动盘是将这个精简系统放在U盘等小容量的硬盘中，作为应急启动系统盘，可以在系统崩溃时引导电脑启动然后执行各种修复或重装操作。

注：协会的PE盘部分版本过老，

可能无法正常使用

![PE 盘的使用，第 3 页配图 1](../assets/ppt/pe/ecef4980a6afa3c8.jpeg){ loading=lazy }

![PE 盘的使用，第 3 页配图 3](../assets/ppt/pe/f9a17006dff45bed.jpeg){ loading=lazy }

## 第 4 页 · Outline

Outline

什么是PE盘

PE盘简介

如何进入WinPE系统

PE盘的使用-图吧工具箱简介

## 第 5 页 · PE盘简介

PE盘简介

目前协会的PE盘内存在

“两项”工具和一个“系统”：

图吧工具箱2025：

内部含有多种重要工具，

如FurMark、Crystal Disk Info等。

Windows以及其他系统的镜像：

用于重装系统

以及自带的WinPE系统

win11版本一定要是“24H2”！！

![PE 盘的使用，第 5 页配图 1](../assets/ppt/pe/821865cae3e3fcae.png){ loading=lazy }

![PE 盘的使用，第 5 页配图 2](../assets/ppt/pe/0bfbfeb440b7fd07.png){ loading=lazy }

## 第 6 页 · 制作一个PE盘

制作一个PE盘

首先，

制作PE盘一定要有U盘！

![PE 盘的使用，第 6 页配图 2](../assets/ppt/pe/ca2aff7a5dce1caa.png){ loading=lazy }

![PE 盘的使用，第 6 页配图 3](../assets/ppt/pe/b242d390c957e6bc.png){ loading=lazy }

![PE 盘的使用，第 6 页配图 4](../assets/ppt/pe/8926d711c80bac19.png){ loading=lazy }

## 第 7 页 · Outline

Outline

什么是PE盘

PE盘简介

如何进入WinPE系统

1. BIOS

2. 快速启动

PE盘的使用-图吧工具箱简介

## 第 8 页 · 如何进入WinPE系统

如何进入WinPE系统

如果只是使用PE盘里的各项工具，那么插上PE盘直接打开即可。但是如果需要进入WinPE系统进行操作的话，那么就需要进入BIOS或使用Windows的高级启动选项修改启动顺序。

常见的需要进入WinPE解决的问题有：

①重装系统

②调整磁盘分区的大小-如扩容C盘

③无法进入电脑原系统

![PE 盘的使用，第 8 页配图 1](../assets/ppt/pe/570318268af5bb55.png){ loading=lazy }

## 第 9 页 · 什么是BIOS

什么是BIOS

BIOS（Basic Input Output System）全名“基本输入输出系统”，电脑开机时，BIOS会进行自检，检查硬件的状态，之后对 CPU 、内存等设备进行初始化。最后，BIOS 会将操作系统从硬盘加载到内存中。

开机时，我们可以进入 BIOS 修改各种设置，包括操作系统的加载顺序、禁用安全启动等等。

![PE 盘的使用，第 9 页配图 1](../assets/ppt/pe/201a9d390589990b.jpeg){ loading=lazy }

## 第 10 页 · BIOS修改启动顺序

BIOS修改启动顺序

电脑默认进入内置的硬盘的系统。如果需要进入WinPE系统，需要从PE盘启动电脑。

首先需要进入BIOS修改操作系统的引导顺序。

开机时反复按下特定按键进入 BIOS（具体按键自行搜索，常见的有F2，F10，F12，Delete），进入 BIOS 后找到操作系统引导顺序，进行修改。

![PE 盘的使用，第 10 页配图 1](../assets/ppt/pe/f6d76442c9b68e36.png){ loading=lazy }

![PE 盘的使用，第 10 页配图 2](../assets/ppt/pe/8607537df53c23b6.jpeg){ loading=lazy }

## 第 11 页 · 安全启动相关

安全启动相关

如果不做任何设置的话，可能会因为Secure Boot而无法进入WinPE系统。

在启动项找不到EFI USB Device时或在重装系统前，请注意安全启动是否关闭。否则重装系统时可能因为 安全启动 原因在开机时无法正确启动。

![PE 盘的使用，第 11 页配图 1](../assets/ppt/pe/4de039dc7f90f81a.jpeg){ loading=lazy }

![PE 盘的使用，第 11 页配图 3](../assets/ppt/pe/953f4f2e8e7336d5.jpeg){ loading=lazy }

## 第 12 页 · Outline

Outline

什么是PE盘

PE盘简介

如何进入WinPE系统

1. BIOS

2. 快速启动

PE盘的使用-图吧工具箱简介

## 第 13 页 · Windows的高级启动选项

Windows的高级启动选项

除了进入BIOS修改启动顺序外，Windows也存在着自身的高级启动选项。

①在重启时按住键盘上的“Shift”。

②在“设置-系统-恢复”中找到“恢复“高级启动”并选择“立即重新启动”。重启后即为高级设置界面。

（PS：有时直接重启即可）

这个环境称为WinRE环境，主要用于Windows的恢复，在这个界面上我们选择“使用设备”启动并选择“USB设备”启动即可进入PE盘。

![PE 盘的使用，第 13 页配图 1](../assets/ppt/pe/c0cd371c8a1b99a6.png){ loading=lazy }

![PE 盘的使用，第 13 页配图 2](../assets/ppt/pe/f68ad4695c3e2b8c.jpeg){ loading=lazy }

![PE 盘的使用，第 13 页配图 3](../assets/ppt/pe/fa46f41ca688e6d7.jpeg){ loading=lazy }

## 第 14 页 · Outline

Outline

什么是PE盘

PE盘简介

如何进入WinPE系统

PE盘的使用-图吧工具箱简介

## 第 15 页 · PE盘的使用-图吧工具箱的简介

PE盘的使用-图吧工具箱的简介

图吧工具箱是一个集合了多项实用工具的软件，主要以各种不同的硬件功能来划分，如图为硬件信息面，在此界面你可以检查电脑的各种硬件信息、型号信息与系统信息等。

此外，图吧工具箱内还有数种维修常用的工具，下面将以不同的分类来介绍较为重要的工具。

在平时的维修中，磁盘工具和烤机工具等使用的频率较高，这两种工具需要熟练掌握。

![PE 盘的使用，第 15 页配图 1](../assets/ppt/pe/d87e7ac0f3d325ef.png){ loading=lazy }

![PE 盘的使用，第 15 页配图 2](../assets/ppt/pe/95100445e99e7588.png){ loading=lazy }

## 第 16 页 · Outline

Outline

PE盘的使用-图吧工具箱简介

1.磁盘工具 Crystal Disk Info

2.磁盘工具 分区助手

3.磁盘工具 Wiztree

4.卸载工具 Geek Uninstaller

5.烤机工具 Furmark

6.搜索工具 Everything

## 第 17 页 · 磁盘工具

磁盘工具

Crystal Disk Info

碰到硬盘问题时，可以查看硬盘的SMART（ Self-Monitoring Analysis and Reporting Technology ）信息，初步判定问题的出处。

当硬盘开始出现0E信息时，代表着该硬盘已经出现坏块，会有部分文件开始报错并无法读取，且随着使用，数据的丢失会越来越严重。

因此，一旦出现0E，就需要提醒机主换盘并做好数据备份，不建议继续使用该硬盘。

![PE 盘的使用，第 17 页配图 1](../assets/ppt/pe/6e4ec27d82eed56c.png){ loading=lazy }

![PE 盘的使用，第 17 页配图 2](../assets/ppt/pe/167d86063211902b.png){ loading=lazy }

## 第 18 页 · 磁盘工具

磁盘工具

分区助手

分区助手的功能非常多，

可用于C盘扩容，系统迁移，修改盘符，格式化硬盘……

后续内训会详细介绍

![PE 盘的使用，第 18 页配图 1](../assets/ppt/pe/ff63e124af958771.png){ loading=lazy }

## 第 19 页 · 分区助手的使用注意：

分区助手的使用注意：

分区助手的操作往往涉及到硬盘、系统与数据。这些操作通常需要非常长的时间，因此你需要保证：

一定要在插电情况下使用软件！！！

数据无价，一定确认操作正确再提交！

## 第 20 页 · 磁盘工具

磁盘工具

Wiztree

在清理硬盘时， Wiztree是一个很好的选择，它可以进行快速的磁盘扫描并将文件大小以不同大小的方格表示出，此时就可以直观地看出我们应该清理的部分。（例如装在C盘的游戏或者没删除干净的内容等）

![PE 盘的使用，第 20 页配图 1](../assets/ppt/pe/ffba734d6b69faee.png){ loading=lazy }

## 第 21 页 · 卸载工具

卸载工具

Geek Uninstaller

Geek是一款能够快速删除并彻底去除残留（例如注册表）的卸载软件。

在重装某软件时，需要卸载这一软件的历史版本，并清除该软件的注册表与残留。

使用Geek可以进行注册表的清除，同时，Geek也可以在软件删除之后检查系统内的注册表残留并进行清除。

Geek界面图

Office问题图

![PE 盘的使用，第 21 页配图 1](../assets/ppt/pe/d4b8bca8ed648bd6.png){ loading=lazy }

![PE 盘的使用，第 21 页配图 2](../assets/ppt/pe/9c30729e23adb8db.png){ loading=lazy }

![PE 盘的使用，第 21 页配图 3](../assets/ppt/pe/fec4717c1d36bbf5.png){ loading=lazy }

## 第 22 页 · 烤机工具

烤机工具

Furmark（甜甜圈）

烤机指的是使用特定软件，使GPU、CPU或其他硬件处于100%占用，可以起到检测电脑的稳定性、温度表现及噪音表现。

在维修中通常使用烤机的方法来放大风扇的噪音，使风扇转速上升从而使其问题得到凸显。当机主反映风扇有异响时，可能是风扇轴体有问题或是卡进异物，则可以使用烤机的方法来听风扇发出的噪音。

调整分辨率

烤CPU

进行GPU压力测试

因其烤机使用的渲染图形类似甜甜圈而得名

![PE 盘的使用，第 22 页配图 1](../assets/ppt/pe/db78246402ebd42b.png){ loading=lazy }

![PE 盘的使用，第 22 页配图 2](../assets/ppt/pe/bc6adf01797c17f4.png){ loading=lazy }

![PE 盘的使用，第 22 页配图 3](../assets/ppt/pe/4ddf63e731da63ea.png){ loading=lazy }

## 第 23 页 · 搜索工具

搜索工具

Everything

Windows搜索与Everything搜索的速度差距

Everything是一款搜索软件，能够快速并轻量化地搜索你想要的文件，当你想要在维修中快速定位某个文件的位置时，不妨可以使用Everything进行快速查找。

相对于Windows搜索来说，Everything

1.速度更快

2.占用资源更少

3.可新建多个搜索窗口，保留搜索结果

![PE 盘的使用，第 23 页配图 1](../assets/ppt/pe/f376797cc1619d8a.png){ loading=lazy }

![PE 盘的使用，第 23 页配图 2](../assets/ppt/pe/4b0d7295f8990fb7.png){ loading=lazy }

## 第 24 页 · Any questions？

Any questions？

## 第 25 页 · THANK YOU

THANK YOU

FOR WATCHING

内训时间：2025年11月25日

## 课件重复配图

课件中多页重复出现的标识与装饰图在此集中保留。

??? info "展开查看原课件标识与装饰图"

    ![课件重复配图 1](../assets/ppt/pe/448489dfe66ad1da.png){ width=180 loading=lazy }
