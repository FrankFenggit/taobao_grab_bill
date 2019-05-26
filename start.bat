@echo off

echo start to open chrome.exe...

::加参数启动chrome
::	--remote-debugging-port
::    可以指定任何打开的端口，selenium启动时要用这个端口。
::    --user-data-dir
::    指定创建新chrome配置文件的目录。它确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。
set path_chrome="C:/Program Files (x86)/Google/Chrome/Application"
echo your chrome path setted: %path_chrome%
cd /d %path_chrome%
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

pause