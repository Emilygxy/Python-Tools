# 文件转换工具安装脚本 (PowerShell)
# 设置控制台编码为UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================" -ForegroundColor Green
Write-Host "文件转换工具安装程序 (Windows PowerShell)" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# 检查Python
Write-Host "正在检查Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Python已安装: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python未找到"
    }
} catch {
    Write-Host "✗ Python未安装或不在PATH中" -ForegroundColor Red
    Write-Host "请先安装Python: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "按回车键退出"
    exit 1
}

# 安装pypandoc
Write-Host ""
Write-Host "正在安装pypandoc..." -ForegroundColor Yellow
try {
    pip install pypandoc
    if ($LASTEXITCODE -ne 0) {
        throw "pip安装失败"
    }
    Write-Host "✓ pypandoc安装成功" -ForegroundColor Green
} catch {
    Write-Host "✗ pypandoc安装失败，尝试使用国内镜像..." -ForegroundColor Red
    try {
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pypandoc
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ 使用镜像安装成功" -ForegroundColor Green
        } else {
            throw "镜像安装也失败"
        }
    } catch {
        Write-Host "✗ 所有安装方法都失败" -ForegroundColor Red
        Read-Host "按回车键退出"
        exit 1
    }
}

# 安装额外依赖
Write-Host ""
Write-Host "正在安装pypandoc额外依赖..." -ForegroundColor Yellow
pip install pypandoc[extra] 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠ pypandoc[extra]安装失败，继续尝试其他方法" -ForegroundColor Yellow
}

# 测试pandoc
Write-Host ""
Write-Host "正在测试pandoc..." -ForegroundColor Yellow
try {
    $testResult = python -c "import pypandoc; print('✓ pypandoc导入成功'); print('Pandoc版本:', pypandoc.get_pandoc_version())" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host $testResult -ForegroundColor Green
    } else {
        throw "pandoc未找到"
    }
} catch {
    Write-Host "⚠ pandoc未找到，尝试自动下载..." -ForegroundColor Yellow
    try {
        python -c "import pypandoc; pypandoc.download_pandoc(); print('✓ pandoc下载成功')" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ pandoc下载成功" -ForegroundColor Green
        } else {
            throw "自动下载失败"
        }
    } catch {
        Write-Host "✗ 自动下载失败" -ForegroundColor Red
        Write-Host ""
        Write-Host "请手动安装pandoc:" -ForegroundColor Yellow
        Write-Host "1. 访问 https://pandoc.org/installing.html" -ForegroundColor White
        Write-Host "2. 下载Windows安装包 (.msi)" -ForegroundColor White
        Write-Host "3. 运行安装包" -ForegroundColor White
        Write-Host "4. 确保pandoc添加到系统PATH" -ForegroundColor White
        Write-Host ""
        Write-Host "或者使用包管理器:" -ForegroundColor Yellow
        Write-Host "  choco install pandoc" -ForegroundColor White
        Write-Host "  scoop install pandoc" -ForegroundColor White
        Write-Host ""
        Read-Host "按回车键退出"
        exit 1
    }
}

Write-Host ""
Write-Host "✓ 安装完成！现在可以使用文件转换工具了" -ForegroundColor Green
Write-Host "运行命令: python converter.py --gui" -ForegroundColor Cyan
Write-Host ""
Read-Host "按回车键退出"
