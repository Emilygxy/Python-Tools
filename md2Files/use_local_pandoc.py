#!/usr/bin/env python3
"""
使用本地 Pandoc 进行文件转换的示例
适用于已经安装了 pandoc 但不在 PATH 中的情况
"""

import converter
import os

def main():
    """主函数"""
    print("=== 使用本地 Pandoc 进行文件转换 ===\n")
    
    # 你的 pandoc 安装路径
    pandoc_path = r"D:\SolftWarePakages\pandoc-2.11.4-windows-x86_64\pandoc.exe"
    
    # 检查文件是否存在
    if not os.path.exists(pandoc_path):
        print(f"✗ Pandoc 文件不存在: {pandoc_path}")
        print("请检查路径是否正确")
        return
    
    print(f"✓ 找到 Pandoc: {pandoc_path}")
    
    # 设置 pandoc 路径
    if converter.set_pandoc_path(pandoc_path):
        print("✓ Pandoc 路径设置成功")
    else:
        print("✗ Pandoc 路径设置失败")
        return
    
    # 创建示例 Markdown 文件
    sample_md = """# 使用本地 Pandoc 转换示例

这是一个使用本地安装的 Pandoc 进行转换的示例。

## 功能特性

- **粗体文本**
- *斜体文本*
- `代码文本`

### 列表示例

1. 第一项
2. 第二项
3. 第三项

## 代码块

```python
def hello():
    print("Hello, World!")
```

## 表格

| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 数据1 | 数据2 | 数据3 |
| 数据4 | 数据5 | 数据6 |

## 结论

这个示例展示了如何使用本地安装的 Pandoc 进行文件转换。
"""
    
    # 保存示例文件
    with open('local_pandoc_sample.md', 'w', encoding='utf-8') as f:
        f.write(sample_md)
    
    print("✓ 创建示例文件: local_pandoc_sample.md")
    
    # 测试不同的转换格式
    test_conversions = [
        ('local_pandoc_sample.md', 'output_html.html', 'html'),
        ('local_pandoc_sample.md', 'output_docx.docx', 'docx'),
        ('local_pandoc_sample.md', 'output_pdf.pdf', 'pdf'),
    ]
    
    print("\n开始转换测试...")
    
    for input_file, output_file, format_name in test_conversions:
        try:
            print(f"\n正在转换: {input_file} -> {output_file}")
            converter.convert_file_auto(input_file, output_file)
            print(f"✓ {format_name} 转换成功")
        except Exception as e:
            print(f"✗ {format_name} 转换失败: {e}")
    
    print("\n=== 转换完成 ===")
    print("生成的文件:")
    for file in ['local_pandoc_sample.md', 'output_html.html', 'output_docx.docx', 'output_pdf.pdf']:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} (未生成)")

if __name__ == "__main__":
    main()
