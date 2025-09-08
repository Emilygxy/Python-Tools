# Python-Tools
这是一个Python语言实现的一些小工具的集合。

## 环境准备
安装Python虚拟环境：
```
pip install virtualenv
```

创建Python虚拟环境：
```
virtualenv python-tools-venv
```

激活Python虚拟环境：
```
python-tools-venv\Scripts\activate
or
cd python-tools-venv/Scripts
activate.bat
```

## 目录
- [Python-Tools](#python-tools)
  - [环境准备](#环境准备)
  - [目录](#目录)
  - [工具列表](#工具列表)
    - [1. md转换器](#1-md转换器)

## 工具列表
### 1. md转换器
将markdown文件转换为html/pdf/word等格式的工具。
运行：
```
python install.py #安装依赖
python convert.py --gui #已图形界面方式运行转换器（选取转换的源文件和目标文件）
```
详情参见：[md2Files](https://github.com/Python-Tools/md2Files)
