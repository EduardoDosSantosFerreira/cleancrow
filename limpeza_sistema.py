import subprocess
import ctypes
import sys


class SistemaLimpeza:
    def __init__(self):
        self.verificar_e_solicitar_administrador()

    def verificar_e_solicitar_administrador(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(
                None,
                "Este programa requer privilégios de administrador. Por favor, execute como administrador.",
                "Erro de Privacidade",
                0x10,
            )
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit(0)

    def executar_limpeza(self, progress_callback=None):
        try:
            operacoes = [
                (self.limpar_temporarios, 3),
                (self.limpar_logs, 6),
                (self.limpar_update, 9),
                (self.limpar_dns, 12),
                (self.limpar_edge, 15),
                (self.limpar_chrome, 18),
                (self.limpar_firefox, 21),
                (self.limpar_opera, 24),
                (self.limpar_brave, 27),
                (self.limpar_vivaldi, 30),
                (self.limpar_safari, 33),
                (self.limpar_tor, 36),
                (self.limpar_maxthon, 39),
                (self.limpar_waterfox, 42),
                (self.limpar_pale_moon, 45),
                (self.remover_programas, 48),
                (self.limpar_espaco_disco, 51),
                (self.verificar_disco, 54),
                (self.desfragmentar_disco, 57),
                (self.limpar_desnecessarios, 60),
                (self.limpar_atualizacao, 63),
                (self.compactar_sistema, 66),
                (self.desativar_hibernacao, 69),
                (self.limpar_temp_adicional, 72),
                (self.desabilitar_inicializacao, 75),
                (self.otimizar_desligamento, 78),
                (self.limpar_miniaturas, 81),
                (self.limpar_dumps_memoria, 84),
                (self.limpar_relatorios_erros, 87),
                (self.limpar_logs_windows_update, 90),
                (self.reiniciar_servicos_essenciais, 93),
                (self.limpar_cache_loja_windows, 96),
                (self.remover_bloatware, 100),
            ]

            for operacao, progresso in operacoes:
                operacao()
                if progress_callback:
                    progress_callback(progresso)

            return True, "Limpeza concluída com sucesso!"
        except Exception as e:
            return False, f"Erro durante a limpeza: {str(e)}"

    def executar_atualizacao(self):
        try:
            subprocess.run(["winget", "upgrade", "--all"], check=True)
            return True, "Atualização concluída com sucesso!"
        except subprocess.CalledProcessError as e:
            return False, f"Erro durante a atualização: {str(e)}"
        except FileNotFoundError:
            return (
                False,
                "Winget não encontrado. Certifique-se de que o Winget está instalado.",
            )

    # Métodos de limpeza
    def limpar_temporarios(self):
        subprocess.run(["cmd", "/c", "del /q/f/s %TEMP%\\*"], shell=True)
        subprocess.run(["cmd", "/c", "del /q/f/s C:\\Windows\\Temp\\*"], shell=True)
        subprocess.run(["cmd", "/c", "del /q/f/s C:\\Windows\\Prefetch\\*"], shell=True)

    def limpar_logs(self):
        subprocess.run(["wevtutil.exe", "el"], stdout=subprocess.PIPE)
        subprocess.run(["wevtutil.exe", "cl", "Application"], stdout=subprocess.PIPE)
        subprocess.run(["wevtutil.exe", "cl", "Security"], stdout=subprocess.PIPE)
        subprocess.run(["wevtutil.exe", "cl", "System"], stdout=subprocess.PIPE)

    def limpar_update(self):
        subprocess.run(["net", "stop", "wuauserv"], shell=True)
        subprocess.run(["net", "stop", "bits"], shell=True)
        subprocess.run(["rd", "/s", "/q", "%windir%\\SoftwareDistribution"], shell=True)
        subprocess.run(["net", "start", "wuauserv"], shell=True)
        subprocess.run(["net", "start", "bits"], shell=True)

    def limpar_dns(self):
        subprocess.run(["ipconfig", "/flushdns"], shell=True)

    def limpar_edge(self):
        subprocess.run(
            ["RunDll32.exe", "InetCpl.cpl,ClearMyTracksByProcess", "255"], shell=True
        )

    def limpar_chrome(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"',
            ],
            shell=True,
        )

    def limpar_firefox(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cookies.sqlite"',
            ],
            shell=True,
        )

    def limpar_opera(self):
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Opera Software\\Opera Stable\\Cache"'],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Opera Software\\Opera Stable\\Cookies"',
            ],
            shell=True,
        )

    def limpar_brave(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies"',
            ],
            shell=True,
        )

    def limpar_vivaldi(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Cache"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Cookies"',
            ],
            shell=True,
        )

    def limpar_safari(self):
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Apple Computer\\Safari\\Cache"'],
            shell=True,
        )
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Apple Computer\\Safari\\Cookies"'],
            shell=True,
        )

    def limpar_tor(self):
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Tor Browser\\Browser\\Caches"'],
            shell=True,
        )
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Tor Browser\\Browser\\Cookies"'],
            shell=True,
        )

    def limpar_maxthon(self):
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Maxthon3\\Cache"'],
            shell=True,
        )
        subprocess.run(
            ["cmd", "/c", 'rd /s /q "%APPDATA%\\Maxthon3\\Cookies"'],
            shell=True,
        )

    def limpar_waterfox(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Waterfox\\Profiles\\*.default-release\\cache2"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Waterfox\\Profiles\\*.default-release\\cookies.sqlite"',
            ],
            shell=True,
        )

    def limpar_pale_moon(self):
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Moonchild Productions\\Pale Moon\\Profiles\\*.default\\cache2"',
            ],
            shell=True,
        )
        subprocess.run(
            [
                "cmd",
                "/c",
                'rd /s /q "%APPDATA%\\Moonchild Productions\\Pale Moon\\Profiles\\*.default\\cookies.sqlite"',
            ],
            shell=True,
        )

    def remover_programas(self):
        if subprocess.run("where FlashUtil*.exe", shell=True).returncode == 0:
            subprocess.run("FlashUtil*.exe -uninstall", shell=True)

    def limpar_espaco_disco(self):
        subprocess.run(["cleanmgr", "/sagerun:1"], shell=True)

    def verificar_disco(self):
        p = subprocess.Popen(
            ["chkdsk", "C:", "/f", "/r", "/x"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output, err = p.communicate(input=b"y\n")

    def desfragmentar_disco(self):
        subprocess.run(["defrag", "C:", "/O"], shell=True)

    def limpar_desnecessarios(self):
        subprocess.run(
            ["dism", "/online", "/cleanup-image", "/startcomponentcleanup"], shell=True
        )

    def limpar_atualizacao(self):
        subprocess.run(
            ["dism", "/online", "/cleanup-image", "/spsuperseded", "/hidesp"],
            shell=True,
        )

    def compactar_sistema(self):
        subprocess.run(["compact", "/compactos:always", "/exe"], shell=True)

    def desativar_hibernacao(self):
        subprocess.run(["powercfg", "-h", "off"], shell=True)

    def limpar_temp_adicional(self):
        subprocess.run(
            ["cmd", "/c", "del /q/f/s %USERPROFILE%\\AppData\\Local\\Temp\\*"],
            shell=True,
        )
        subprocess.run(
            ["cmd", "/c", "del /q/f/s %USERPROFILE%\\AppData\\LocalLow\\Temp\\*"],
            shell=True,
        )

    def limpar_miniaturas(self):
        subprocess.run(
            ["cmd", "/c", "del /q/f/s %LOCALAPPDATA%\\Microsoft\\Windows\\Explorer\\thumbcache_*"],
            shell=True,
        )

    def limpar_dumps_memoria(self):
        subprocess.run(["cmd", "/c", "del /q/f/s C:\\Windows\\Minidump\\*"], shell=True)
        subprocess.run(["cmd", "/c", "del /q/f/s C:\\Windows\\MEMORY.DMP"], shell=True)

    def limpar_relatorios_erros(self):
        subprocess.run(
            ["cmd", "/c", "del /q/f/s C:\\ProgramData\\Microsoft\\Windows\\WER\\*"],
            shell=True,
        )

    def limpar_logs_windows_update(self):
        subprocess.run(
            ["cmd", "/c", "del /q/f/s %windir%\\Logs\\WindowsUpdate\\*"], shell=True
        )

    def reiniciar_servicos_essenciais(self):
        subprocess.run(["net", "start", "wuauserv"], shell=True)
        subprocess.run(["net", "start", "bits"], shell=True)
        subprocess.run(["net", "start", "Dnscache"], shell=True)

    def limpar_cache_loja_windows(self):
        subprocess.run(["wsreset.exe"], shell=True)

    def remover_bloatware(self):
        apps = [
            "Microsoft.3DBuilder",
            "Microsoft.BingWeather",
            "Microsoft.MicrosoftSolitaireCollection",
        ]
        for app in apps:
            subprocess.run(
                ["powershell", "-Command", f"Get-AppxPackage {app} | Remove-AppxPackage"],
                shell=True,
            )

    def desabilitar_inicializacao(self):
        subprocess.run(
            [
                "reg",
                "add",
                '"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"',
                "/v",
                '"UnwantedProgram"',
                "/f",
            ],
            shell=True,
        )

    def otimizar_desligamento(self):
        subprocess.run(
            [
                "reg",
                "add",
                '"HKCU\\Control Panel\\Desktop"',
                "/v",
                '"WaitToKillAppTimeout"',
                "/t",
                "REG_SZ",
                "/d",
                '"2000"',
                "/f",
            ],
            shell=True,
        )
        subprocess.run(
            [
                "reg",
                "add",
                '"HKCU\\Control Panel\\Desktop"',
                "/v",
                '"HungAppTimeout"',
                "/t",
                "REG_SZ",
                "/d",
                '"1000"',
                "/f",
            ],
            shell=True,
        )
        subprocess.run(
            [
                "reg",
                "add",
                '"HKLM\\SYSTEM\\CurrentControlSet\\Control"',
                "/v",
                '"WaitToKillServiceTimeout"',
                "/t",
                "REG_SZ",
                "/d",
                '"2000"',
                "/f",
            ],
            shell=True,
        )