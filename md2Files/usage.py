import converter

# 示例用法
if __name__ == "__main__":
    print("=== 文件格式转换工具使用示例 ===\n")
    
    print("1. 直接调用转换函数:")
    # 根据输出文件的后缀自动选择转换格式
    # converter.convert_file_auto('input.md', 'output.html')    # 转换为HTML
    # converter.convert_file_auto('input.md', 'output.docx')   # 转换为Word
    # converter.convert_file_auto('input.md', 'output.pdf')     # 转换为PDF
    # converter.convert_file_auto('input.docx', 'output.pdf')  # Word转PDF
    # converter.convert_file_auto('input.html', 'output.md')   # HTML转Markdown
    
    print("2. 命令行使用方式:")
    print("   python converter.py --gui                    # 使用图形界面选择文件")
    print("   python converter.py -i input.md -f html      # 指定输入文件和目标格式")
    print("   python converter.py -i input.md -o output.pdf # 指定输入和输出文件")
    print("   python converter.py -i input.md              # 只指定输入文件，会弹出创建输出文件")
    
    print("\n3. 支持的命令行参数:")
    print("   -i, --input    输入文件路径")
    print("   -o, --output   输出文件路径")
    print("   -f, --format   目标格式 (html, pdf, docx, md, tex, rst, epub)")
    print("   --gui          使用图形界面选择文件")
    
    print("\n4. 支持的文件格式:")
    print("   输入格式: .md, .html, .htm, .docx, .doc, .pdf, .tex, .rst, .epub")
    print("   输出格式: .html, .htm, .docx, .doc, .pdf, .md, .markdown, .tex, .rst, .epub")
    
    print("\n5. 使用图形界面:")
    # 演示图形界面选择文件
    print("正在打开文件选择器...")
    input_file = converter.select_input_file()
    if input_file:
        print(f"选择的文件: {input_file}")
        # 自动生成输出文件名
        output_file = converter.get_output_file_path(input_file, 'html')
        print(f"将转换为: {output_file}")
        # 执行转换
        try:
            converter.convert_file_auto(input_file, output_file)
        except Exception as e:
            print(f"转换失败: {e}")
    else:
        print("未选择文件")
    
    print("\n6. 使用本地 Pandoc:")
    print("   如果已安装 pandoc 但不在 PATH 中:")
    print("   - 运行: python use_local_pandoc.py")
    print("   - 或指定路径: python converter.py --pandoc-path \"D:\\path\\to\\pandoc.exe\"")
    print("   - 或运行: python pandoc_config.py")
    
    print("\n7. 安装和故障排除:")
    print("   如果遇到 'No pandoc was found' 错误:")
    print("   - 程序会自动尝试下载安装 pandoc")
    print("   - 或者运行: python install.py")
    print("   - 或者手动安装: pip install pypandoc[extra]")
    print("   - 或者访问: https://pandoc.org/installing.html")