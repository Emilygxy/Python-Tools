#!/usr/bin/env python3
"""
文件转换工具安装脚本
自动安装所需的依赖包
"""

import subprocess
import sys
import os

def run_command(command, description):
    """运行命令并显示结果"""
    print(f"正在{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description}成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description}失败: {e}")
        if e.stdout:
            print(f"输出: {e.stdout}")
        if e.stderr:
            print(f"错误: {e.stderr}")
        return False

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 6):
        print("✗ 需要Python 3.6或更高版本")
        return False
    print(f"✓ Python版本: {sys.version}")
    return True

def install_dependencies():
    """安装依赖包"""
    print("=== 安装依赖包 ===")
    
    # 安装pypandoc
    if not run_command("pip install pypandoc", "安装pypandoc"):
        return False
    
    # 尝试安装pypandoc的额外依赖
    run_command("pip install pypandoc[extra]", "安装pypandoc额外依赖")
    
    return True

def test_installation():
    """测试安装是否成功"""
    print("\n=== 测试安装 ===")
    try:
        import pypandoc
        print("✓ pypandoc导入成功")
        
        # 测试pandoc是否可用
        try:
            version = pypandoc.get_pandoc_version()
            print(f"✓ Pandoc版本: {version}")
            return True
        except OSError:
            print("⚠ Pandoc未找到，尝试自动下载...")
            try:
                pypandoc.download_pandoc()
                print("✓ Pandoc下载成功")
                return True
            except Exception as e:
                print(f"✗ Pandoc下载失败: {e}")
                print("\n尝试其他安装方法...")
                
                # 尝试使用conda安装
                if run_command("conda install -c conda-forge pandoc -y", "使用conda安装pandoc"):
                    return True
                
                # 尝试使用包管理器安装
                if sys.platform.startswith('win'):
                    # Windows
                    if run_command("choco install pandoc -y", "使用Chocolatey安装pandoc"):
                        return True
                    if run_command("scoop install pandoc", "使用Scoop安装pandoc"):
                        return True
                elif sys.platform.startswith('darwin'):
                    # macOS
                    if run_command("brew install pandoc", "使用Homebrew安装pandoc"):
                        return True
                elif sys.platform.startswith('linux'):
                    # Linux
                    if run_command("sudo apt-get update && sudo apt-get install -y pandoc", "使用apt安装pandoc"):
                        return True
                    if run_command("sudo yum install -y pandoc", "使用yum安装pandoc"):
                        return True
                
                print("\n自动安装失败，请手动安装:")
                print_manual_install_guide()
                return False
                
    except ImportError as e:
        print(f"✗ 导入pypandoc失败: {e}")
        return False

def print_manual_install_guide():
    """打印手动安装指导"""
    print("\n" + "="*50)
    print("手动安装指导")
    print("="*50)
    
    if sys.platform.startswith('win'):
        print("\nWindows 用户:")
        print("1. 访问 https://pandoc.org/installing.html")
        print("2. 下载 Windows 安装包 (.msi)")
        print("3. 运行安装包并按照提示安装")
        print("4. 确保 pandoc 添加到系统 PATH")
        print("\n或者使用包管理器:")
        print("  choco install pandoc")
        print("  scoop install pandoc")
        
    elif sys.platform.startswith('darwin'):
        print("\nmacOS 用户:")
        print("1. 使用 Homebrew: brew install pandoc")
        print("2. 或访问 https://pandoc.org/installing.html 下载安装包")
        
    elif sys.platform.startswith('linux'):
        print("\nLinux 用户:")
        print("Ubuntu/Debian:")
        print("  sudo apt-get update")
        print("  sudo apt-get install pandoc")
        print("\nCentOS/RHEL:")
        print("  sudo yum install pandoc")
        print("\n或访问 https://pandoc.org/installing.html 下载安装包")
    
    print("\n安装完成后，重新运行此脚本测试安装")
    print("="*50)

def main():
    """主函数"""
    print("=== 文件转换工具安装程序 ===\n")
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 安装依赖
    if not install_dependencies():
        print("\n安装失败，请手动安装依赖包")
        sys.exit(1)
    
    # 测试安装
    if not test_installation():
        print("\n安装完成，但Pandoc可能不可用")
        print("请手动安装Pandoc: https://pandoc.org/installing.html")
    else:
        print("\n✓ 安装完成！现在可以使用文件转换工具了")
        print("运行命令: python converter.py --gui")
    
    print("\n=== 安装完成 ===")

if __name__ == "__main__":
    main()
