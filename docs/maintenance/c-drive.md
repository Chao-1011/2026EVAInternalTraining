# C 盘清理与扩容

按观察空间、卸载软件、清理文件、修改路径、调整分区的顺序处理空间问题。

**内训时间：** 2025 年 12 月 2 日  
**来源课件：** 清C盘.pptx

## 阅读说明

下方按原课件页序保留文字与配图。截图中的个人信息、示例路径及课件中的历史版本要求，请按实际情况更新。

!!! warning "操作前确认"

    涉及分区、格式化或硬件拆装时，先确认数据备份、目标设备和机主授权。分区与系统安装过程中保持供电；拆机前关机、拔掉外部电源并断开内置电池。

## 第 1 页 · 人资部第5次内训

人资部第5次内训

内训时间：2025年12月2日

C盘的清理&扩容

## 第 2 页 · 清理C盘

清理C盘

C盘爆满的原因主要有以下几种：

①C盘太小：大多不足200G

②C盘内下载了过多的软件

③未清理的临时文件过多

④常用软件保存路径在C盘（例如微信、QQ等）

原则：清理C盘可以不彻底，但是不要做高风险内容！

## 第 3 页 · Outline

Outline

Step0：观察磁盘空间分配情况

Step1：使用Geek删除软件

Step2：使用Wiztree扫盘，删除文件

Step3：改变常用软件存储地址

Step4：C盘扩容（调整存储空间的分配）

## 第 4 页 · Step0 观察磁盘

Step0       观察磁盘

## 第 5 页 · 观察磁盘剩余空间

观察磁盘剩余空间

确认事项

1.电脑安装了几块硬盘

2.每块硬盘对应的分区

3.不同分区的剩余空间

注意：此处只能查看分区数量，

无法查看它们是否位于同一块硬盘！

![C 盘清理与扩容，第 5 页配图 1](../assets/ppt/c-drive/957fa9772420275e.png){ loading=lazy }

## 第 6 页 · 观察磁盘剩余空间

观察磁盘剩余空间

硬盘1：

C盘、D盘（Windows）

硬盘2：

5个分区（Linux）

U盘（这里是个PE盘）

![C 盘清理与扩容，第 6 页配图 2](../assets/ppt/c-drive/08759cbc3bc25065.png){ loading=lazy }

## 第 7 页 · Step1 软件删除

Step1       软件删除

## 第 8 页 · 使用Geek卸载软件

使用Geek卸载软件

Geek

Geek是一个可以快速删除无用软件的程序，在每次卸载软件后，Geek会扫描注册表，反正软件残留，这有效减小了360等流氓软件复活的可能性

![C 盘清理与扩容，第 8 页配图 2](../assets/ppt/c-drive/9c30729e23adb8db.png){ loading=lazy }

## 第 9 页 · Step2 文件清除

Step2       文件清除

## 第 10 页 · 使用Wiztree扫描C盘

使用Wiztree扫描C盘

Wiztree

在清理硬盘时， Wiztree是一个很好的选择，它可以进行快速的磁盘扫描并将文件大小以不同大小的方格表示出，此时可以直观地看出应该清理的部分。

![C 盘清理与扩容，第 10 页配图 1](../assets/ppt/c-drive/877c796d752c53c6.png){ loading=lazy }

## 第 11 页 · 如何分析C盘的结构

如何分析C盘的结构

![C 盘清理与扩容，第 11 页配图 1](../assets/ppt/c-drive/a635eadea18d243d.png){ loading=lazy }

## 第 12 页 · 删除安装包（清理下载文件夹）

删除安装包（清理下载文件夹）

如果机主用安装包下载过软件，

那么这些安装包就可能保存在“下载”文件夹中。

软件安装包的特征：后缀多为“.exe”，文件名多含“install”，“setup”

除此之外，还要注意镜像文件：后缀为“.iso”

星露谷模组（可以移动至D盘）

安装包（询问能否删除）

![C 盘清理与扩容，第 12 页配图 1](../assets/ppt/c-drive/abb0e8ee406f431e.png){ loading=lazy }

## 第 13 页 · 删除临时文件

删除临时文件

Windows临时文件，它是Windows系统在运行过程中产生的一些临时性的文件。

临时文件的扩展名通常是.tmp、.bak、.old

![C 盘清理与扩容，第 13 页配图 1](../assets/ppt/c-drive/7313634b69792cfa.png){ loading=lazy }

![C 盘清理与扩容，第 13 页配图 3](../assets/ppt/c-drive/c5c67463a2c79d75.png){ loading=lazy }

## 第 14 页 · 删除临时文件

删除临时文件

一般来说，开启“存储”中的存储感知功能可以定期删除临时文件，但在C盘过满或是未开启此选项时，则需手动删除

临时文件的路径一般为：C:\\Users\\用户名\\AppData\\Local\\Temp

Win+R，输入 %temp% 打开临时文件的存储文件夹并进行删除。

![C 盘清理与扩容，第 14 页配图 1](../assets/ppt/c-drive/6c182745c8123109.png){ loading=lazy }

![C 盘清理与扩容，第 14 页配图 3](../assets/ppt/c-drive/b12dbdb9cf9f799b.png){ loading=lazy }

## 第 15 页 · 删除回收站相关内容

删除回收站相关内容

回收站本质是一个隐藏文件夹：C:\\$Recycle.Bin

实际清C盘时，发现很多机主以为“Delete”后文件就直接删除了。

所以当你发现回收站图标不是空的，或者扫描时有一大块Recycle bin的时候，可以询问垃圾桶内的文件有无保存的必要，并进行清理。

图文无关

![C 盘清理与扩容，第 15 页配图 2](../assets/ppt/c-drive/1714436a56ca2957.png){ loading=lazy }

## 第 16 页 · Step3 修改路径

Step3       修改路径

## 第 17 页 · 微信、QQ以及钉钉文件

微信、QQ以及钉钉文件

大部分软件的默认文件保存路径在C盘

微信 C:\\Users\\用户名\\Documents\\xwechat \\（新版本微信为WeChat Files）

在更改完路径后，文件也会被移动到对应位置(需要一定时间)

①微信左下角打开设置

②在另一个盘内新建文件夹，并更改地址

③更改完成后，微信会开始自动移动文件，

完成后查询原文件是否已被删除

![C 盘清理与扩容，第 17 页配图 1](../assets/ppt/c-drive/29006c2b3c4ec0e7.png){ loading=lazy }

![C 盘清理与扩容，第 17 页配图 2](../assets/ppt/c-drive/7912196d34adc1a1.png){ loading=lazy }

![C 盘清理与扩容，第 17 页配图 3](../assets/ppt/c-drive/40c7dbdb8275b755.png){ loading=lazy }

## 第 18 页 · 微信、QQ以及钉钉文件

微信、QQ以及钉钉文件

不影响使用，可以直接删

![C 盘清理与扩容，第 18 页配图 2](../assets/ppt/c-drive/0e59c1f8290f24b4.png){ loading=lazy }

![C 盘清理与扩容，第 18 页配图 3](../assets/ppt/c-drive/edb36b7b0b22a714.png){ loading=lazy }

## 第 19 页 · 修改音视频的软件下载与缓存路径

修改音视频的软件下载与缓存路径

打开音视频软件设置，

选择下载与缓存，更改下载与缓存路径。

以网易云音乐为例：

打开设置 -\> 音质与下载  -\> 下载 / 缓存

迁移完成后检查 D 盘是否已有下载和缓存文件，检查 C 盘文件是否已经自动删除，

若没有，则手动清理。

![C 盘清理与扩容，第 19 页配图 1](../assets/ppt/c-drive/c3ee56747ce3f89b.png){ loading=lazy }

## 第 20 页 · ②选择移动

②选择移动

①右键桌面，选择属性

③选择D盘，新建Desktop

④选择文件夹

移动桌面

由于Windows路径移动经常会出问题，所以不推荐移动桌面路径，请谨慎使用

![C 盘清理与扩容，第 20 页配图 1](../assets/ppt/c-drive/8199799980a76baf.png){ loading=lazy }

![C 盘清理与扩容，第 20 页配图 2](../assets/ppt/c-drive/c6127a8f34e728fe.png){ loading=lazy }

## 第 21 页 · Step4 扩容C盘

Step4        扩容C盘

## 第 22 页 · 重新分配硬盘空间（扩容C盘）

重新分配硬盘空间（扩容C盘）

官方要求 Windows11 系统的最低硬盘要求是 64G，当前 Windows11 系统硬盘空间占用普遍达到 40 - 70G。

因此，这里建议一块512G的硬盘，C 盘至少 200G ；一块1T的硬盘，C 盘空间建议300～400G。

如果在清 C 盘过程中，发现机主 C 盘空间分配本身较小，D 盘有较多富余空间；同时清 C 盘之后 C 盘空间还是相对紧张，就可以考虑进行 C 盘扩容。

## 第 23 页 · 扩容C盘

扩容C盘

插上PE盘，进入WinPE系统

具体步骤看上次内训PPT

## 第 24 页 · 图解

图解

①右键选中目标磁盘

②选择分配空闲空间

![C 盘清理与扩容，第 24 页配图 1](../assets/ppt/c-drive/ff63e124af958771.png){ loading=lazy }

## 第 25 页 · 图解

图解

③调整想要分配的空闲空间大小

④选择C盘

⑤点击确定后返回主界面提交

![C 盘清理与扩容，第 25 页配图 1](../assets/ppt/c-drive/25ea05ef54c4a1d9.png){ loading=lazy }

## 第 26 页 · One more thing...

One more thing...

![C 盘清理与扩容，第 26 页配图 1](../assets/ppt/c-drive/540a5f3f27c45c1d.jpeg){ loading=lazy }

## 第 27 页 · 注意⚠️

注意⚠️

在清理C盘的过程中，

不要随意打开一些未知的文件夹，

尤其是存放了照片等个人隐私的文件夹！

请尊重机主的隐私，

避免不必要的尴尬

![C 盘清理与扩容，第 27 页配图 1](../assets/ppt/c-drive/540a5f3f27c45c1d.jpeg){ loading=lazy }

![C 盘清理与扩容，第 27 页配图 2](../assets/ppt/c-drive/1390e0d80e55b672.png){ loading=lazy }

## 第 28 页 · Thank you

Thank you

for watching!

感谢观看

## 课件重复配图

课件中多页重复出现的标识与装饰图在此集中保留。

??? info "展开查看原课件标识与装饰图"

    ![课件重复配图 1](../assets/ppt/c-drive/448489dfe66ad1da.png){ width=180 loading=lazy }
