Set WshShell = CreateObject("WScript.Shell")
Set args = WScript.Arguments

shortcutPath = args(0)
targetPath = args(1)
workingDir = args(2)
iconPath = args(3)
arguments = ""

If args.Count > 4 Then
    arguments = args(4)
End If

Set shortcut = WshShell.CreateShortcut(shortcutPath)
shortcut.TargetPath = targetPath
shortcut.WorkingDirectory = workingDir

If iconPath <> "" Then
    shortcut.IconLocation = iconPath
End If

If arguments <> "" Then
    shortcut.Arguments = arguments
End If

shortcut.Save
