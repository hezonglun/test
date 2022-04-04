@echo off

:main
echo 1.show ip address
echo 2.show TCP LISTENING Port
echo 3.open notepad
echo 4.open powershell
echo 5.ping baidu
echo 6.exit

echo Enter your option
set /p opt=

if %opt%==1 goto one
if %opt%==2 goto two
if %opt%==3 goto three
if %opt%==4 goto four
if %opt%==5 goto five
if %opt%==6 goto six
echo Invalid option
goto main

:one
ipconfig /all
pause>nul
goto main

:two
netstat -an | find "LISTENING"
pause>nul
goto main

:three
notepad
pause>nul
goto main

:four
powershell
pause>nul
goto main

:five
ping baidu.com
pause>nul
goto main

:six
exit
