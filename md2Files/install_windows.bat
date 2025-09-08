@echo off
chcp 65001 >nul
echo ========================================
echo 文件转换工具安装程序 (Windows)
echo ========================================
echo.

echo 正在检查Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python未安装或不在PATH中
    echo 请先安装Python: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✓ Python已安装

echo.
echo 正在安装pypandoc...
pip install pypandoc
if errorlevel 1 (
    echo ✗ pypandoc安装失败
    echo 尝试使用国内镜像...
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pypandoc
    if errorlevel 1 (
        echo ✗ 使用镜像安装也失败
        pause
        exit /b 1
    )
)
echo ✓ pypandoc安装成功

echo.
echo 正在安装pypandoc额外依赖...
pip install pypandoc[extra]
if errorlevel 1 (
    echo ⚠ pypandoc[extra]安装失败，继续尝试其他方法
)

echo.
echo 正在测试pandoc...
python -c "import pypandoc; print('✓ pypandoc导入成功'); print('Pandoc版本:', pypandoc.get_pandoc_version())" 2>nul
if errorlevel 1 (
    echo ⚠ pandoc未找到，尝试自动下载...
    python -c "import pypandoc; pypandoc.download_pandoc(); print('✓ pandoc下载成功')" 2>nul
    if errorlevel 1 (
        echo ✗ 自动下载失败
        echo.
        echo 请手动安装pandoc:
        echo 1. 访问 https://pandoc.org/installing.html
        echo 2. 下载Windows安装包 (.msi)
        echo 3. 运行安装包
        echo 4. 确保pandoc添加到系统PATH
        echo.
        echo 或者使用包管理器:
        echo   choco install pandoc
        echo   scoop install pandoc
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ✓ 安装完成！现在可以使用文件转换工具了
echo 运行命令: python converter.py --gui
echo.
pause
