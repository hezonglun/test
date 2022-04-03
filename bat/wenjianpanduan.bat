@echo off

rem bat判断文件是否存在

if exist C:\Windows\notepad.exe (
	echo ok
) else (
	echo no 
)

pause
