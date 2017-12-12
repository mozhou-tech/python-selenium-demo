## 介绍 Instruction

已测试操作系统  Mac OS

## 安装 Setup
### 安装依赖的Python库
```
pip install -r requirements.txt
```
### 下载driver
https://sites.google.com/a/chromium.org/chromedriver/downloads 需下载最新版本

## 参考文档 Reference
http://selenium-python-zh.readthedocs.io/en/latest/index.html
http://blog.csdn.net/column/details/12694.html

## 目录结构

1. config层，放配置文件，把所有的项目相关的配置均放到这里，用Python支持较好的配置文件格式如ini或yaml等进行配置。实现配置与代码分离。
1. data层，放数据文件，可以把所有的testcase的参数化相关的文件放到这里，一般可采用xlsx、csv、xml等格式。实现数据与代码分离。
1. drivers层，放所需的驱动，如Chromedriver、IEDriverServer等。
1. log层，所有生成的日志均存放在这里，可将日志分类，如运行时日志test log，错误日志error log等。
1. report层，放程序运行生成的报告，一般可有html报告、excel报告等。
1. src源码层，放所有程序代码。其中还需要进行更进一步的分层： 
1. test层，放所有测试相关的文件，如case——测试用例、common——项目相关的抽象通用代码、page——页面类（Page-Object思想）、suite——组织的测试套件。
1. utils层，所有的支撑代码都在这里，包括读取config的类、写log的类、读取excel、xml的类、生成报告的类（如HTMLTestRunner）、数据库连接、发送邮件等类和方法，都在这里。

## 软件版本 Version
python 3.6
