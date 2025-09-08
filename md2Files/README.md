# 文件格式转换工具

一个基于 pypandoc 的 Python 文件格式转换工具，支持多种文件格式之间的相互转换。

## 功能特性

- 🎯 **自动格式识别**：根据输出文件扩展名自动选择转换格式
- 🖱️ **图形界面选择**：支持通过文件选择器选择输入和输出文件
- ⌨️ **命令行支持**：支持命令行参数指定文件和格式
- 📁 **多格式支持**：支持 Markdown、HTML、Word、PDF、LaTeX、reStructuredText、EPUB 等格式

## 安装依赖

### 方法一：使用安装脚本（推荐）

#### Windows 用户
```cmd
# 使用批处理脚本
install_windows.bat

# 或使用PowerShell脚本
powershell -ExecutionPolicy Bypass -File install_windows.ps1
```

#### 跨平台
```bash
python install.py
```

### 方法二：手动安装
```bash
# 推荐：安装包含pandoc的版本
pip install pypandoc[extra]

# 或者分别安装
pip install pypandoc
pip install pandoc
```

### 方法三：使用包管理器

#### Windows
```cmd
# 使用Chocolatey
choco install pandoc
pip install pypandoc

# 或使用Scoop
scoop install pandoc
pip install pypandoc
```

#### macOS
```bash
# 使用Homebrew
brew install pandoc
pip install pypandoc
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install pandoc
pip install pypandoc

# CentOS/RHEL
sudo yum install pandoc
pip install pypandoc
```

### 方法四：使用 conda
```bash
conda install pandoc
pip install pypandoc
```

### 方法五：使用本地 Pandoc
如果你已经安装了 pandoc 但不在系统 PATH 中：

```bash
# 方法1：使用配置工具
python pandoc_config.py

# 方法2：直接指定路径
python converter.py --pandoc-path "D:\path\to\pandoc.exe" -i input.md -o output.docx

# 方法3：运行示例脚本
python use_local_pandoc.py
```

## 故障排除

### 常见问题

1. **"No pandoc was found" 错误**
   - 运行 `python install.py` 自动安装
   - 或手动安装：`pip install pypandoc[extra]`

2. **"无法打开安装包" 错误**
   - 尝试使用 `pip install pypandoc[extra]`
   - 或访问 [pandoc官网](https://pandoc.org/installing.html) 手动下载安装

3. **权限问题**
   - 使用 `--user` 参数：`pip install --user pypandoc[extra]`
   - 或使用虚拟环境

4. **网络问题**
   - 使用国内镜像：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pypandoc[extra]`

5. **Windows 用户特别说明**
   - 如果遇到安装问题，请使用 `install_windows.bat` 或 `install_windows.ps1`
   - 确保以管理员权限运行安装脚本

## 使用方法

### 1. 图形界面模式

```bash
python converter.py --gui
```

这将打开文件选择器，让你选择要转换的文件，然后选择输出位置。

### 2. 命令行模式

#### 指定输入文件和目标格式
```bash
python converter.py -i input.md -f html
```

#### 指定输入和输出文件
```bash
python converter.py -i input.md -o output.pdf
```

#### 只指定输入文件
```bash
python converter.py -i input.md
```
（会弹出文件创建对话框创建输出文件）

### 3. 编程接口

```python
import converter

# 直接转换
converter.convert_file_auto('input.md', 'output.html')

# 选择文件
input_file = converter.select_input_file()
if input_file:
    output_file = converter.get_output_file_path(input_file, 'pdf')
    converter.convert_file_auto(input_file, output_file)
```

## 支持的文件格式

### 输入格式
- Markdown: `.md`, `.markdown`
- HTML: `.html`, `.htm`
- Word: `.docx`, `.doc`
- PDF: `.pdf`
- LaTeX: `.tex`
- reStructuredText: `.rst`
- EPUB: `.epub`

### 输出格式
- HTML: `.html`, `.htm`
- Word: `.docx`, `.doc`
- PDF: `.pdf`
- Markdown: `.md`, `.markdown`
- LaTeX: `.tex`
- reStructuredText: `.rst`
- EPUB: `.epub`

## 命令行参数

- `-i, --input`: 输入文件路径
- `-o, --output`: 输出文件路径
- `-f, --format`: 目标格式 (html, pdf, docx, md, tex, rst, epub)
- `--gui`: 使用图形界面选择文件

## 示例

### 基本使用
查看 `usage.py` 文件获取更多使用示例。

### 使用本地 Pandoc 示例
```bash
# 运行本地 pandoc 示例
python use_local_pandoc.py

# 直接转换 Markdown 到 Word
python converter.py -i sample.md -o output.docx
```

## 注意事项

1. 确保系统已安装 pandoc
2. 某些格式转换可能需要额外的依赖（如 PDF 转换需要 LaTeX）
3. 大文件转换可能需要较长时间
