## 介绍 Instruction

Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。
支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。

## 安装 Setup
### 安装Python运行环境

https://www.python.org/  下载3.6版本并安装

### 安装依赖的Python库
```
pip install -r requirements.txt
```
### 下载driver
https://sites.google.com/a/chromium.org/chromedriver/downloads 需下载最新版本
下载后需要安放在特定位置，并修改config.py中对应的配置

### Selenium IDE 安装
一款基于Firefox的浏览器插件 http://www.importnew.com/25509.html

## 目录结构

目录名 | 描述
----|----
config | 放配置文件，把所有的项目相关的配置均放到这里，用Python支持较好的配置文件格式如ini或yaml等进行配置。实现配置与代码分离。
data | 放数据文件，可以把所有的testcase的参数化相关的文件放到这里，一般可采用xlsx、csv、xml等格式。实现数据与代码分离。
drivers | 放所需的驱动，如Chromedriver、IEDriverServer等。
log | 所有生成的日志均存放在这里，可将日志分类，如运行时日志test log，错误日志error log等。
report | 放程序运行生成的报告，一般可有html报告、excel报告等。
src | 放所有程序代码。其中还需要进行更进一步的分层： 
test | 放所有测试相关的文件，如case——测试用例、common——项目相关的抽象通用代码、page——页面类（Page-Object思想）、suite——组织的测试套件。
utils | 所有的支撑代码都在这里，包括读取config的类、写log的类、读取excel、xml的类、生成报告的类（如HTMLTestRunner）、数据库连接、发送邮件等类和方法，都在这里。

## 参考文档 Reference
1. http://selenium-python-zh.readthedocs.io/en/latest/index.html
2. http://blog.csdn.net/column/details/12694.html