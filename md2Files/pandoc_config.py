#!/usr/bin/env python3
"""
Pandoc 配置文件
用于存储和管理 pandoc 的安装路径
"""

import os
import json
from pathlib import Path

CONFIG_FILE = "pandoc_config.json"

def get_pandoc_config():
    """
    获取 pandoc 配置
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    
    return {}

def save_pandoc_config(config):
    """
    保存 pandoc 配置
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"保存配置失败: {e}")
        return False

def set_pandoc_path(pandoc_path):
    """
    设置并保存 pandoc 路径
    """
    config = get_pandoc_config()
    config['pandoc_path'] = pandoc_path
    config['last_updated'] = str(Path().cwd())
    
    if save_pandoc_config(config):
        print(f"✓ 已保存 Pandoc 路径: {pandoc_path}")
        return True
    else:
        print("✗ 保存 Pandoc 路径失败")
        return False

def get_saved_pandoc_path():
    """
    获取已保存的 pandoc 路径
    """
    config = get_pandoc_config()
    pandoc_path = config.get('pandoc_path', '')
    
    if pandoc_path and os.path.exists(pandoc_path):
        return pandoc_path
    else:
        return None

def find_pandoc_installation():
    """
    查找系统中的 pandoc 安装
    """
    # 首先检查已保存的路径
    saved_path = get_saved_pandoc_path()
    if saved_path:
        print(f"✓ 使用已保存的 Pandoc 路径: {saved_path}")
        return saved_path
    
    # Windows 常见安装路径
    possible_paths = [
        r"D:\SolftWarePakages\pandoc-2.11.4-windows-x86_64\pandoc.exe",
        r"D:\SolftWarePakages\pandoc\pandoc.exe",
        r"C:\Program Files\Pandoc\pandoc.exe",
        r"C:\Program Files (x86)\Pandoc\pandoc.exe",
        r"C:\Users\{}\AppData\Local\Pandoc\pandoc.exe".format(os.getenv('USERNAME', '')),
        r"C:\tools\pandoc\pandoc.exe",
        r"D:\pandoc\pandoc.exe",
    ]
    
    # 检查可能的路径
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✓ 找到 Pandoc 安装: {path}")
            # 保存找到的路径
            set_pandoc_path(path)
            return path
    
    # 尝试在 PATH 中查找
    try:
        import shutil
        pandoc_path = shutil.which('pandoc')
        if pandoc_path:
            print(f"✓ 在 PATH 中找到 Pandoc: {pandoc_path}")
            set_pandoc_path(pandoc_path)
            return pandoc_path
    except:
        pass
    
    print("✗ 未找到 Pandoc 安装")
    return None

def main():
    """
    配置 pandoc 路径的主函数
    """
    print("=== Pandoc 路径配置工具 ===\n")
    
    # 显示当前配置
    current_path = get_saved_pandoc_path()
    if current_path:
        print(f"当前配置的 Pandoc 路径: {current_path}")
    else:
        print("当前未配置 Pandoc 路径")
    
    print("\n正在查找系统中的 Pandoc 安装...")
    found_path = find_pandoc_installation()
    
    if found_path:
        print(f"\n✓ 找到 Pandoc: {found_path}")
        print("配置已自动保存")
    else:
        print("\n✗ 未找到 Pandoc 安装")
        print("\n请手动指定 Pandoc 路径:")
        print("1. 运行: python converter.py --pandoc-path \"D:\\SolftWarePakages\\pandoc-2.11.4-windows-x86_64\\pandoc.exe\"")
        print("2. 或者将 pandoc.exe 添加到系统 PATH 环境变量")

if __name__ == "__main__":
    main()
