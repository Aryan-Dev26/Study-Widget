# Get Desktop path
$Desktop = [Environment]::GetFolderPath("Desktop")
$ShortcutPath = Join-Path $Desktop "StudyTimerPro.lnk"
$CurrentDir = $PSScriptRoot

# Create icon if it doesn't exist
$IconPath = Join-Path $CurrentDir "icon.ico"
if (-not (Test-Path $IconPath)) {
    Write-Host "Creating icon..."
    python (Join-Path $CurrentDir "create_icon.py")
}

# Check if executable exists
$ExePath = Join-Path $CurrentDir "dist\StudyTimerPro.exe"
if (Test-Path $ExePath) {
    $TargetPath = $ExePath
    $Arguments = ""
} else {
    # Find Python
    $PythonPath = (Get-Command pythonw -ErrorAction SilentlyContinue).Source
    if (-not $PythonPath) {
        $PythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
    }
    
    if (-not $PythonPath) {
        Write-Host "Error: Python not found"
        pause
        exit 1
    }
    
    $TargetPath = $PythonPath
    $Arguments = Join-Path $CurrentDir "study_timer_pro.py"
}

# Create shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.WorkingDirectory = $CurrentDir

if ($Arguments) {
    $Shortcut.Arguments = "`"$Arguments`""
}

if (Test-Path $IconPath) {
    $Shortcut.IconLocation = $IconPath
}

$Shortcut.Save()

if (Test-Path $ShortcutPath) {
    Write-Host ""
    Write-Host "✅ Success! Desktop shortcut created at:"
    Write-Host "   $ShortcutPath"
    Write-Host ""
    Write-Host "📋 Next Steps:"
    Write-Host ""
    Write-Host "1. 🖱️  Double-click the shortcut to launch"
    Write-Host "2. 📌 Right-click the shortcut and 'Pin to taskbar'"
    Write-Host "3. ⌨️  Set a keyboard shortcut:"
    Write-Host "   - Right-click the shortcut"
    Write-Host "   - Select 'Properties'"
    Write-Host "   - Click in 'Shortcut key' field"
    Write-Host "   - Press Ctrl+Alt+S (or your preferred combo)"
    Write-Host "   - Click OK"
    Write-Host ""
    Write-Host "Now you can press Ctrl+Alt+S anywhere to open the app!"
} else {
    Write-Host ""
    Write-Host "❌ Error: Failed to create desktop shortcut."
}

Write-Host ""
pause
