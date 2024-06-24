@echo off
setlocal

:: Verificar permissões administrativas
echo Verificando permissões administrativas...
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Por favor, execute este script como administrador.
    pause
    exit /b
)

:: Função para verificar o último comando executado
:check_error
if %errorlevel% NEQ 0 (
    echo O comando anterior falhou com o código de erro %errorlevel%.
    pause
    exit /b
)
goto :eof

:: Limpando arquivos temporários
echo Limpando arquivos temporários...
del /q/f/s %TEMP%\* 2>nul
call :check_error
del /q/f/s C:\Windows\Temp\* 2>nul
call :check_error
del /q/f/s C:\Windows\Prefetch\* 2>nul
call :check_error

:: Limpando logs de eventos
echo Limpando logs de eventos...
for /F "tokens=*" %%1 in ('wevtutil.exe el') DO (wevtutil.exe cl "%%1" 2>nul)
call :check_error

:: Limpando cache do Windows Update
echo Limpando cache do Windows Update...
net stop wuauserv 2>nul
call :check_error
net stop bits 2>nul
call :check_error
rd /s /q %windir%\SoftwareDistribution 2>nul
call :check_error
net start wuauserv 2>nul
call :check_error
net start bits 2>nul
call :check_error

:: Limpando cache de DNS
echo Limpando cache de DNS...
ipconfig /flushdns 2>nul
call :check_error

:: Limpando cache e cookies do Microsoft Edge
echo Limpando cache e cookies do Microsoft Edge...
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255 2>nul
call :check_error

:: Limpando cache e cookies do Google Chrome
echo Limpando cache e cookies do Google Chrome...
rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache" 2>nul
call :check_error
rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cookies" 2>nul
call :check_error

:: Limpando cache e cookies do Mozilla Firefox
echo Limpando cache e cookies do Mozilla Firefox...
rd /s /q "%APPDATA%\Mozilla\Firefox\Profiles\*.default-release\cache2" 2>nul
call :check_error
rd /s /q "%APPDATA%\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite" 2>nul
call :check_error

:: Limpando cache e cookies do Opera
echo Limpando cache e cookies do Opera...
rd /s /q "%APPDATA%\Opera Software\Opera Stable\Cache" 2>nul
call :check_error
rd /s /q "%APPDATA%\Opera Software\Opera Stable\Cookies" 2>nul
call :check_error

:: Limpando cache e cookies do Brave
echo Limpando cache e cookies do Brave...
rd /s /q "%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Cache" 2>nul
call :check_error
rd /s /q "%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Cookies" 2>nul
call :check_error

:: Removendo programas não utilizados (exemplo: Adobe Flash Player)
echo Removendo programas não utilizados...
if exist "%SystemRoot%\System32\Macromed\Flash\FlashUtil*.exe" (
    "%SystemRoot%\System32\Macromed\Flash\FlashUtil*.exe" -uninstall 2>nul
    call :check_error
)

:: Limpando espaço em disco
echo Limpando espaço em disco...
cleanmgr /sagerun:1 2>nul
call :check_error

:: Verificando o disco rígido
echo Verificando o disco rígido...
chkdsk C: /f /r /x 2>nul
call :check_error

:: Desfragmentando o disco
echo Desfragmentando o disco...
defrag C: /O 2>nul
call :check_error

:: Limpando componentes desnecessários do Windows
echo Limpando componentes desnecessários do Windows...
dism /online /cleanup-image /startcomponentcleanup 2>nul
call :check_error

:: Limpando arquivos de atualização do Windows
echo Limpando arquivos de atualização do Windows...
dism /online /cleanup-image /spsuperseded /hidesp 2>nul
call :check_error

:: Compactando arquivos do sistema para economizar espaço
echo Compactando arquivos do sistema para economizar espaço...
compact /compactos:always /exe 2>nul
call :check_error

:: Desativando hibernação para economizar espaço em disco
echo Desativando hibernação para economizar espaço em disco...
powercfg -h off 2>nul
call :check_error

:: Limpando arquivos temporários adicionais
echo Limpando arquivos temporários adicionais...
del /q/f/s "%USERPROFILE%\AppData\Local\Temp\*" 2>nul
call :check_error
del /q/f/s "%USERPROFILE%\AppData\LocalLow\Temp\*" 2>nul
call :check_error

:: Desabilitando programas de inicialização desnecessários
echo Desabilitando programas de inicialização desnecessários...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "UnwantedProgram" /f 2>nul
call :check_error

:: Reduzindo tempo de espera de desligamento do Windows
echo Reduzindo tempo de espera de desligamento do Windows...
reg add "HKCU\Control Panel\Desktop" /v "WaitToKillAppTimeout" /t REG_SZ /d "2000" /f 2>nul
call :check_error
reg add "HKCU\Control Panel\Desktop" /v "HungAppTimeout" /t REG_SZ /d "1000" /f 2>nul
call :check_error
reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v "WaitToKillServiceTimeout" /t REG_SZ /d "2000" /f 2>nul
call :check_error

echo Limpeza e otimização concluídas!
pause
endlocal
exit /b