Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c hidden.cmd"
oShell.Run strArgs, 0, false