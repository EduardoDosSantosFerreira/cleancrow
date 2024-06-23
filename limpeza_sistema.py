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
        self.label.pack(pady=10)
        
        self.limpar_button = tk.Button(self.frame, text="Limpar", command=self.iniciar_limpeza)
        self.limpar_button.pack(pady=10)
        
        self.progress_label = tk.Label(self.frame, text="")
        self.progress_label.pack(pady=10)
        
        # Adicionando a barra de progresso
        self.progress_bar = ttk.Progressbar(self.frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)
        
    def iniciar_limpeza(self):
        # Desabilita o botão enquanto a limpeza está em andamento
        self.limpar_button.config(state=tk.DISABLED)
        
        # Configura a barra de progresso
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100
        
        # Executa a limpeza em uma thread para não travar a interface gráfica
        self.progress_label.config(text="Iniciando limpeza...")
        self.thread_limpeza = Thread(target=self.executar_limpeza)
        self.thread_limpeza.start()
        
    def executar_limpeza(self):
        try:
            # Verifica permissões administrativas
            self.verificar_administrador()
            
            # Funções de limpeza
            self.limpar_temporarios()
            self.atualizar_progresso(10)
            self.limpar_logs()
            self.atualizar_progresso(20)
            self.limpar_update()
            self.atualizar_progresso(30)
            self.limpar_dns()
            self.atualizar_progresso(40)
            self.limpar_edge()
            self.atualizar_progresso(50)
            self.limpar_chrome()
            self.atualizar_progresso(60)
            self.limpar_firefox()
            self.atualizar_progresso(70)
            self.verificar_disco()
            self.atualizar_progresso(80)
            self.desfragmentar_disco()
            self.atualizar_progresso(90)
            self.limpar_desnecessarios()
            self.atualizar_progresso(95)
            self.limpar_atualizacao()
            self.atualizar_progresso(98)
            self.compactar_sistema()
            self.atualizar_progresso(100)
            
            # Mostra mensagem de conclusão
            self.progress_label.config(text="Limpeza concluída!")
            messagebox.showinfo("Concluído", "Limpeza concluída!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a limpeza: {str(e)}")
        finally:
            # Habilita o botão novamente
            self.limpar_button.config(state=tk.NORMAL)
    
    def verificar_administrador(self):
        # Verifica se está executando como administrador (apenas no Windows)
        if subprocess.run("net session >nul 2>&1", shell=True).returncode != 0:
            raise Exception("Por favor, execute este programa como administrador.")
    
    def limpar_temporarios(self):
        subprocess.run(['cmd', '/c', 'del', '/q/f/s', '%TEMP%\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del', '/q/f/s', 'C:\\Windows\\Temp\\*'], shell=True)
        subprocess.run(['cmd', '/c', 'del', '/q/f/s', 'C:\\Windows\\Prefetch\\*'], shell=True)
        self.atualizar_progresso(5)
    
    def limpar_logs(self):
        subprocess.run(['wevtutil.exe', 'el'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Application'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Security'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'System'], stdout=subprocess.PIPE)
        self.atualizar_progresso(10)
    
    def limpar_update(self):
        # Comando para limpar o cache do Windows Update sem prompt de confirmação
        subprocess.run(['net', 'stop', 'wuauserv'], shell=True)
        subprocess.run(['net', 'stop', 'bits'], shell=True)
        subprocess.run(['rd', '/s', '/q', '%windir%\\SoftwareDistribution'], shell=True)
        subprocess.run(['net', 'start', 'wuauserv'], shell=True)
        subprocess.run(['net', 'start', 'bits'], shell=True)
        self.atualizar_progresso(15)
    
    def limpar_dns(self):
        # Limpar cache de DNS sem prompt de confirmação
        subprocess.run(['ipconfig', '/flushdns'], shell=True)
        self.atualizar_progresso(20)
    
    def limpar_edge(self):
        # Limpar cache e cookies do Microsoft Edge sem prompt de confirmação
        subprocess.run(['RunDll32.exe', 'InetCpl.cpl,ClearMyTracksByProcess', '255'], shell=True)
        self.atualizar_progresso(25)
    
    def limpar_chrome(self):
        # Limpar cache e cookies do Google Chrome sem prompt de confirmação
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"'], shell=True)
        self.atualizar_progresso(30)
    
    def limpar_firefox(self):
        # Limpar cache e cookies do Mozilla Firefox sem prompt de confirmação
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cookies.sqlite"'], shell=True)
        self.atualizar_progresso(40)
    
    def verificar_disco(self):
        # Verificar disco sem prompt de confirmação
        # Utiliza input para responder automaticamente ao CHKDSK se necessário
        p = subprocess.Popen(['chkdsk', 'C:', '/f', '/r', '/x'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate(input=b'y\n')  # Responde 'y' para agendar no próximo reinício
        self.atualizar_progresso(50)
    
    def desfragmentar_disco(self):
        # Desfragmentar disco sem prompt de confirmação
        subprocess.run(['defrag', 'C:', '/O'], shell=True)
        self.atualizar_progresso(60)
    
    def limpar_desnecessarios(self):
        # Limpar componentes desnecessários do Windows sem prompt de confirmação
        subprocess.run(['dism', '/online', '/cleanup-image', '/startcomponentcleanup'], shell=True)
        self.atualizar_progresso(70)
    
    def limpar_atualizacao(self):
        # Limpar arquivos de atualização do Windows sem prompt de confirmação
        subprocess.run(['dism', '/online', '/cleanup-image', '/spsuperseded', '/hidesp'], shell=True)
        self.atualizar_progresso(80)
    
    def compactar_sistema(self):
        # Compactar arquivos do sistema sem prompt de confirmação
        subprocess.run(['compact', '/compactos:always', '/exe'], shell=True)
        self.atualizar_progresso(90)
    
    def atualizar_progresso(self, valor):
        self.progress_bar["value"] = valor
        self.frame.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = LimpezaSistema(root)
    root.mainloop()
