@echo off
echo Verificando permissões administrativas...
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Por favor, execute este script como administrador.
    pause
    exit /b
)

echo Limpando arquivos temporários...
del /q/f/s %TEMP%\*
del /q/f/s C:\Windows\Temp\*
del /q/f/s C:\Windows\Prefetch\*

echo Limpando logs de eventos...
for /F "tokens=*" %%1 in ('wevtutil.exe el') DO wevtutil.exe cl "%%1"

echo Limpando cache do Windows Update...
net stop wuauserv
net stop bits
rd /s /q %windir%\SoftwareDistribution
net start wuauserv
net start bits

echo Limpando cache de DNS...
ipconfig /flushdns

echo Limpando cache e cookies do Microsoft Edge...
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255

echo Limpando cache e cookies do Google Chrome...
rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"
rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cookies"

echo Limpando cache e cookies do Mozilla Firefox...
rd /s /q "%APPDATA%\Mozilla\Firefox\Profiles\*.default-release\cache2"
rd /s /q "%APPDATA%\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite"

echo Verificando o disco rígido...
chkdsk C: /f /r /x

echo Desfragmentando o disco...
defrag C: /O

echo Limpando componentes desnecessários do Windows...
dism /online /cleanup-image /startcomponentcleanup

echo Limpando arquivos de atualização do Windows...
dism /online /cleanup-image /spsuperseded /hidesp

echo Compactando arquivos do sistema para economizar espaço...
compact /compactos:always /exe

echo Limpeza concluída!
pause
