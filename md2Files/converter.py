import pypandoc
import os
import argparse
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import sys
from pandoc_config import find_pandoc_installation, set_pandoc_path, get_saved_pandoc_path

def check_and_install_pandoc():
    """
    检查 pandoc 是否可用，如果不可用则尝试下载安装
    """
    try:
        # 尝试获取 pandoc 版本
        pypandoc.get_pandoc_version()
        print("✓ Pandoc 已安装并可用")
        return True
    except OSError:
        print("⚠ Pandoc 未找到，正在尝试自动下载安装...")
        try:
            # 尝试下载 pandoc
            pypandoc.download_pandoc()
            print("✓ Pandoc 下载安装成功")
            return True
        except Exception as e:
            print(f"✗ 自动安装 Pandoc 失败: {e}")
            print("\n请手动安装 Pandoc:")
            print("1. 访问 https://pandoc.org/installing.html")
            print("2. 下载适合您系统的 Pandoc 安装包")
            print("3. 安装后将 pandoc 添加到系统 PATH 环境变量")
            print("4. 或者运行: pip install pypandoc[extra]")
            return False


def set_pandoc_path(pandoc_path):
    """
    设置 pandoc 的安装路径
    
    参数:
        pandoc_path (str): pandoc 的安装路径
    """
    try:
        # 设置 pypandoc 的 pandoc 路径
        pypandoc.pandoc_path = pandoc_path
        print(f"✓ 已设置 Pandoc 路径: {pandoc_path}")
        
        # 验证路径是否有效
        version = pypandoc.get_pandoc_version()
        print(f"✓ Pandoc 版本: {version}")
        return True
    except Exception as e:
        print(f"✗ 设置 Pandoc 路径失败: {e}")
        return False


# find_pandoc_installation 函数已移动到 pandoc_config.py


# mammoth 相关函数已移除，只使用 pandoc 进行转换


def convert_file_auto(input_file, output_file):
    """
    根据输出文件的后缀名自动选择转换格式
    
    参数:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径（后缀名决定转换格式）
    """
    # 检查并确保 pandoc 可用
    if not check_and_install_pandoc():
        raise RuntimeError("Pandoc 不可用，无法进行文件转换")
    
    # 获取输出文件的扩展名并转换为pypandoc可识别的格式
    output_extension = Path(output_file).suffix.lower()
    
    # 将文件扩展名映射到pypandoc格式
    extension_to_format = {
        '.html': 'html',
        '.htm': 'html',
        '.docx': 'docx',
        '.doc': 'docx',
        '.pdf': 'pdf',
        '.md': 'md',
        '.markdown': 'md',
        '.tex': 'latex',
        '.rst': 'rst',
        '.epub': 'epub',
        # 可以根据需要添加更多映射
    }
    
    # 获取对应的格式
    output_format = extension_to_format.get(output_extension)
    
    if output_format is None:
        raise ValueError(f"不支持的目标文件格式: {output_extension}")
    
    # 执行转换
    try:
        output = pypandoc.convert_file(input_file, output_format, outputfile=output_file)
        print(f"转换成功: {input_file} -> {output_file} (格式: {output_format})")
        return output
    except Exception as e:
        raise RuntimeError(f"文件转换失败: {e}")


def select_input_file():
    """
    打开文件选择器让用户选择要转换的文件
    
    返回:
        str: 选择的文件路径，如果用户取消则返回None
    """
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 设置文件类型过滤器
    filetypes = [
        ('所有支持的文件', '*.md;*.html;*.htm;*.docx;*.doc;*.pdf;*.tex;*.rst;*.epub'),
        ('Markdown文件', '*.md;*.markdown'),
        ('HTML文件', '*.html;*.htm'),
        ('Word文档', '*.docx;*.doc'),
        ('PDF文件', '*.pdf'),
        ('LaTeX文件', '*.tex'),
        ('reStructuredText', '*.rst'),
        ('EPUB文件', '*.epub'),
        ('所有文件', '*.*')
    ]
    
    file_path = filedialog.askopenfilename(
        title="选择要转换的文件",
        filetypes=filetypes
    )
    
    root.destroy()
    return file_path if file_path else None


def get_output_file_path(input_file, target_format):
    """
    根据输入文件和目标格式生成输出文件路径
    
    参数:
        input_file (str): 输入文件路径
        target_format (str): 目标格式（如 'html', 'pdf', 'docx' 等）
    
    返回:
        str: 输出文件路径
    """
    input_path = Path(input_file)
    output_file = input_path.with_suffix(f'.{target_format}')
    return str(output_file)


def main():
    """
    主函数：处理命令行参数并执行转换
    """
    parser = argparse.ArgumentParser(description='文件格式转换工具')
    parser.add_argument('-i', '--input', help='输入文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径')
    parser.add_argument('-f', '--format', help='目标格式 (html, pdf, docx, md, tex, rst, epub)')
    parser.add_argument('--gui', action='store_true', help='使用图形界面选择文件')
    parser.add_argument('--pandoc-path', help='指定 pandoc 的安装路径')
    
    args = parser.parse_args()
    
    # 如果指定了 pandoc 路径，先设置它
    if args.pandoc_path:
        if not set_pandoc_path(args.pandoc_path):
            print("设置 pandoc 路径失败，程序退出")
            return
    else:
        # 自动查找 pandoc 安装
        print("正在查找 Pandoc 安装...")
        pandoc_path = find_pandoc_installation()
        if pandoc_path:
            set_pandoc_path(pandoc_path)
    
    # 如果使用GUI模式或没有提供输入文件
    if args.gui or not args.input:
        print("请选择要转换的文件...")
        input_file = select_input_file()
        if not input_file:
            print("未选择文件，程序退出。")
            return
    else:
        input_file = args.input
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件不存在: {input_file}")
        return
    
    # 确定输出文件路径
    if args.output:
        output_file = args.output
    elif args.format:
        output_file = get_output_file_path(input_file, args.format)
    else:
        # 如果没有指定输出文件或格式，让用户创建新文件
        print("请创建输出文件...")
        root = tk.Tk()
        root.withdraw()
        output_file = filedialog.asksaveasfilename(
            title="创建输出文件",
            defaultextension=".html",
            filetypes=[
                ('HTML文件', '*.html'),
                ('PDF文件', '*.pdf'),
                ('Word文档', '*.docx'),
                ('Markdown文件', '*.md'),
                ('LaTeX文件', '*.tex'),
                ('reStructuredText', '*.rst'),
                ('EPUB文件', '*.epub'),
                ('所有文件', '*.*')
            ]
        )
        root.destroy()
        
        if not output_file:
            print("未创建输出文件，程序退出。")
            return
    
    try:
        # 执行转换
        convert_file_auto(input_file, output_file)
    except Exception as e:
        print(f"转换失败: {e}")


if __name__ == "__main__":
    main()


