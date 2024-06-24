import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
from threading import Thread

class LimpezaSistema:
    def __init__(self, root):
        self.root = root
        self.root.title("Limpeza do Sistema")
                
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        
        self.label = tk.Label(self.frame, text="Clique em Limpar para iniciar a limpeza do sistema:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.limpar_button = tk.Button(self.frame, text="Limpar", command=self.iniciar_limpeza)
        self.limpar_button.grid(row=1, column=0, padx=5)
        
        self.atualizar_button = tk.Button(self.frame, text="Atualizar", command=self.iniciar_atualizacao)
        self.atualizar_button.grid(row=1, column=1, padx=5)
        
        self.progress_label = tk.Label(self.frame, text="")
        self.progress_label.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Adicionando a barra de progresso
        self.progress_bar = ttk.Progressbar(self.frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=3, column=0, columnspan=2, pady=10)
        
    def iniciar_limpeza(self):
        # Desabilita o botão enquanto a limpeza está em andamento
        self.limpar_button.config(state=tk.DISABLED)
        
        # Configura a barra de progresso
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100
        
        # Configura a barra de progresso
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100
        
        # Executa a limpeza em uma thread para não travar a interface gráfica
        self.progress_label.config(text="Iniciando limpeza...")
        self.thread_limpeza = Thread(target=self.executar_limpeza)
        self.thread_limpeza.start()
        
    def iniciar_atualizacao(self):
        # Desabilita o botão enquanto a atualização está em andamento
        self.atualizar_button.config(state=tk.DISABLED)
        
        # Executa a atualização em uma thread para não travar a interface gráfica
        self.progress_label.config(text="Iniciando atualização...")
        self.thread_atualizacao = Thread(target=self.executar_atualizacao)
        self.thread_atualizacao.start()
        
    def executar_limpeza(self):
        try:
            # Verifica permissões administrativas
            self.verificar_administrador()
            
            # Funções de limpeza e otimização
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
            
            # Mostra mensagem de conclusão
            self.progress_label.config(text="Limpeza concluída!")
            messagebox.showinfo("Concluído", "Limpeza concluída!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a limpeza: {str(e)}")
        finally:
            # Habilita o botão novamente
            self.limpar_button.config(state=tk.NORMAL)
    
    def executar_atualizacao(self):
        try:
            # Verifica permissões administrativas
            self.verificar_administrador()
            
            # Executa o comando winget upgrade --all
            subprocess.run(['winget', 'upgrade', '--all'], check=True)
            
            # Mostra mensagem de conclusão
            self.progress_label.config(text="Atualização concluída!")
            messagebox.showinfo("Concluído", "Atualização concluída!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a atualização: {str(e)}")
        finally:
            # Habilita o botão novamente
            self.atualizar_button.config(state=tk.NORMAL)
    
    def verificar_administrador(self):
        # Verifica se está executando como administrador (apenas no Windows)
        if subprocess.run("net session >nul 2>&1", shell=True).returncode != 0:
            raise Exception("Por favor, execute este programa como administrador.")
    
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
    
    def remover_programas(self):
        if subprocess.run('where FlashUtil*.exe', shell=True).returncode == 0:
            subprocess.run('FlashUtil*.exe -uninstall', shell=True)
    
    def limpar_espaco_disco(self):
        subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)
    
    def verificar_disco(self):
        p = subprocess.Popen(['chkdsk', 'C:', '/f', '/r', '/x'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate(input=b'y\n')  # Responde 'y' para agendar no próximo reinício
    
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

if __name__ == "__main__":
    root = tk.Tk()
    app = LimpezaSistema(root)
    root.mainloop()