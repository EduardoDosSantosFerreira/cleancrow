import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
from threading import Thread
import sys
import os
import ctypes

class LimpezaSistema:
    def __init__(self, root):
        self.root = root
        self.root.title("Limpeza do Sistema")
        self.root.configure(bg="white")

        # Frame principal
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(padx=20, pady=20)

        # Label de instrução
        self.label = tk.Label(self.frame, text="Clique em Limpar para iniciar a limpeza do sistema:", bg="white", fg="black", font=("Arial", 12))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Botão Limpar
        self.limpar_button = tk.Button(self.frame, text="Limpar", command=self.iniciar_limpeza, bg="red", fg="white", font=("Arial", 10, "bold"))
        self.limpar_button.grid(row=1, column=0, padx=5)

        # Botão Atualizar
        self.atualizar_button = tk.Button(self.frame, text="Atualizar", command=self.iniciar_atualizacao, bg="black", fg="white", font=("Arial", 10, "bold"))
        self.atualizar_button.grid(row=1, column=1, padx=5)

        # Label de progresso
        self.progress_label = tk.Label(self.frame, text="", bg="white", fg="black", font=("Arial", 10))
        self.progress_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Adicionando a barra de progresso
        self.progress_bar = ttk.Progressbar(self.frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=3, column=0, columnspan=2, pady=10)

        # Verificar e solicitar privilégios de administrador
        self.verificar_e_solicitar_administrador()

    def verificar_e_solicitar_administrador(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            # Não é administrador, solicitar elevação
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Este programa requer privilégios de administrador. Por favor, execute como administrador.', 'Erro de Privacidade', 0x10)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

            # Fechar o programa se não for executado como administrador
            sys.exit(0)

    def iniciar_limpeza(self):
        self.limpar_button.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100
        self.progress_label.config(text="Iniciando limpeza...")
        self.thread_limpeza = Thread(target=self.executar_limpeza)
        self.thread_limpeza.start()

    def iniciar_atualizacao(self):
        self.atualizar_button.config(state=tk.DISABLED)
        self.progress_label.config(text="Iniciando atualização...")
        self.thread_atualizacao = Thread(target=self.executar_atualizacao)
        self.thread_atualizacao.start()

    def executar_limpeza(self):
        try:
            self.limpar_temporarios()
            self.atualizar_progresso(5)
            self.limpar_logs()
            self.atualizar_progresso(10)
            self.limpar_update()
            self.atualizar_progresso(15)
            self.limpar_dns()
            self.atualizar_progresso(20)
            self.limpar_edge()
            self.atualizar_progresso(25)
            self.limpar_chrome()
            self.atualizar_progresso(30)
            self.limpar_firefox()
            self.atualizar_progresso(35)
            self.limpar_opera()
            self.atualizar_progresso(40)
            self.limpar_brave()
            self.atualizar_progresso(45)
            self.remover_programas()
            self.atualizar_progresso(50)
            self.limpar_espaco_disco()
            self.atualizar_progresso(55)
            self.verificar_disco()
            self.atualizar_progresso(60)
            self.desfragmentar_disco()
            self.atualizar_progresso(65)
            self.limpar_desnecessarios()
            self.atualizar_progresso(70)
            self.limpar_atualizacao()
            self.atualizar_progresso(75)
            self.compactar_sistema()
            self.atualizar_progresso(80)
            self.desativar_hibernacao()
            self.atualizar_progresso(85)
            self.limpar_temp_adicional()
            self.atualizar_progresso(90)
            self.desabilitar_inicializacao()
            self.atualizar_progresso(95)
            self.otimizar_desligamento()
            self.atualizar_progresso(100)

            self.progress_label.config(text="Limpeza concluída!")
            messagebox.showinfo("Concluído", "Limpeza concluída!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a limpeza: {str(e)}")
        finally:
            self.limpar_button.config(state=tk.NORMAL)

    def executar_atualizacao(self):
        try:
            subprocess.run(['winget', 'upgrade', '--all'], check=True)
            self.progress_label.config(text="Atualização concluída!")
            messagebox.showinfo("Concluído", "Atualização concluída!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a atualização: {str(e)}")
        finally:
            self.atualizar_button.config(state=tk.NORMAL)

    def limpar_temporarios(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s %TEMP%\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del /q/f/s C:\\Windows\\Temp\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del /q/f/s C:\\Windows\\Prefetch\\*'], shell=True)

    def limpar_logs(self):
        subprocess.run(['wevtutil.exe', 'el'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Application'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Security'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'System'], stdout=subprocess.PIPE)

    def limpar_update(self):
        subprocess.run(['net', 'stop', 'wuauserv'], shell=True)
        subprocess.run(['net', 'stop', 'bits'], shell=True)
        subprocess.run(['rd', '/s', '/q', '%windir%\\SoftwareDistribution'], shell=True)
        subprocess.run(['net', 'start', 'wuauserv'], shell=True)
        subprocess.run(['net', 'start', 'bits'], shell=True)

    def limpar_dns(self):
        subprocess.run(['ipconfig', '/flushdns'], shell=True)

    def limpar_edge(self):
        subprocess.run(['RunDll32.exe', 'InetCpl.cpl,ClearMyTracksByProcess', '255'], shell=True)

    def limpar_chrome(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"'], shell=True)

    def limpar_firefox(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cookies.sqlite"'], shell=True)

    def limpar_opera(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Opera Software\\Opera Stable\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Opera Software\\Opera Stable\\Cookies"'], shell=True)

    def limpar_brave(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies"'], shell=True)

    def limpar_safari(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Apple Computer\\Safari\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%APPDATA%\\Apple Computer\\Safari\\Cookies"'], shell=True)

    def limpar_vivaldi(self):
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd /s /q "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Cookies"'], shell=True)

    def remover_programas(self):
        if subprocess.run('where FlashUtil*.exe', shell=True).returncode == 0:
            subprocess.run('FlashUtil*.exe -uninstall', shell=True)

    def limpar_espaco_disco(self):
        subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)

    def verificar_disco(self):
        p = subprocess.Popen(['chkdsk', 'C:', '/f', '/r', '/x'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate(input=b'y\n')

    def desfragmentar_disco(self):
        subprocess.run(['defrag', 'C:', '/O'], shell=True)

    def limpar_desnecessarios(self):
        subprocess.run(['dism', '/online', '/cleanup-image', '/startcomponentcleanup'], shell=True)

    def limpar_atualizacao(self):
        subprocess.run(['dism', '/online', '/cleanup-image', '/spsuperseded', '/hidesp'], shell=True)

    def compactar_sistema(self):
        subprocess.run(['compact', '/compactos:always', '/exe'], shell=True)

    def desativar_hibernacao(self):
        subprocess.run(['powercfg', '-h', 'off'], shell=True)

    def limpar_temp_adicional(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s %USERPROFILE%\\AppData\\Local\\Temp\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del /q/f/s %USERPROFILE%\\AppData\\LocalLow\\Temp\\*'], shell=True)

    def desabilitar_inicializacao(self):
        subprocess.run(['reg', 'add', '"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"', '/v', '"UnwantedProgram"', '/f'], shell=True)

    def otimizar_desligamento(self):
        subprocess.run(['reg', 'add', '"HKCU\\Control Panel\\Desktop"', '/v', '"WaitToKillAppTimeout"', '/t', 'REG_SZ', '/d', '"2000"', '/f'], shell=True)
        subprocess.run(['reg', 'add', '"HKCU\\Control Panel\\Desktop"', '/v', '"HungAppTimeout"', '/t', 'REG_SZ', '/d', '"1000"', '/f'], shell=True)
        subprocess.run(['reg', 'add', '"HKLM\\SYSTEM\\CurrentControlSet\\Control"', '/v', '"WaitToKillServiceTimeout"', '/t', 'REG_SZ', '/d', '"2000"', '/f'], shell=True)

    def atualizar_progresso(self, valor):
        self.progress_bar["value"] = valor
        self.frame.update_idletasks()
    
    def limpar_miniaturas(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s %LOCALAPPDATA%\\Microsoft\\Windows\\Explorer\\thumbcache_*'], shell=True)

    def limpar_dumps_memoria(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s C:\\Windows\\Minidump\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del /q/f/s C:\\Windows\\MEMORY.DMP'], shell=True)

    def limpar_relatorios_erros(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s C:\\ProgramData\\Microsoft\\Windows\\WER\\*'], shell=True)

    def limpar_logs_windows_update(self):
        subprocess.run(['cmd', '/c', 'del /q/f/s %windir%\\Logs\\WindowsUpdate\\*'], shell=True)

    def reiniciar_servicos_essenciais(self):
        subprocess.run(['net', 'start', 'wuauserv'], shell=True)
        subprocess.run(['net', 'start', 'bits'], shell=True)
        subprocess.run(['net', 'start', 'Dnscache'], shell=True)

    def limpar_cache_loja_windows(self):
        subprocess.run(['wsreset.exe'], shell=True)

    def remover_bloatware(self):
        apps = ["Microsoft.3DBuilder", "Microsoft.BingWeather", "Microsoft.MicrosoftSolitaireCollection"]
        for app in apps:
            subprocess.run(['powershell', '-Command', f'Get-AppxPackage {app} | Remove-AppxPackage'], shell=True)

    def limpar_windows_old(self):
        subprocess.run(['cmd', '/c', 'rd /s /q C:\\Windows.old'], shell=True)

    def resetar_rede(self):
        subprocess.run(['netsh', 'winsock', 'reset'], shell=True)
        subprocess.run(['netsh', 'int', 'ip', 'reset'], shell=True)

    def verificar_corrigir_arquivos_sistema(self):
        subprocess.run(['sfc', '/scannow'], shell=True)
        subprocess.run(['dism', '/online', '/cleanup-image', '/restorehealth'], shell=True)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LimpezaSistema(root)
    root.mainloop()