import tkinter as tk
from tkinter import messagebox
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
        
    def iniciar_limpeza(self):
        # Desabilita o botão enquanto a limpeza está em andamento
        self.limpar_button.config(state=tk.DISABLED)
        
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
            self.limpar_logs()
            self.limpar_update()
            self.limpar_dns()
            self.limpar_edge()
            self.limpar_chrome()
            self.limpar_firefox()
            self.verificar_disco()
            self.desfragmentar_disco()
            self.limpar_desnecessarios()
            self.limpar_atualizacao()
            self.compactar_sistema()
            
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
        self.atualizar_progresso("Limpando arquivos temporários...")
    
    def limpar_logs(self):
        subprocess.run(['wevtutil.exe', 'el'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Application'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'Security'], stdout=subprocess.PIPE)
        subprocess.run(['wevtutil.exe', 'cl', 'System'], stdout=subprocess.PIPE)
        self.atualizar_progresso("Limpando logs de eventos...")
    
    def limpar_update(self):
        # Comando para limpar o cache do Windows Update sem prompt de confirmação
        subprocess.run(['net', 'stop', 'wuauserv'], shell=True)
        subprocess.run(['net', 'stop', 'bits'], shell=True)
        subprocess.run(['rd', '/s', '/q', '%windir%\\SoftwareDistribution'], shell=True)
        subprocess.run(['net', 'start', 'wuauserv'], shell=True)
        subprocess.run(['net', 'start', 'bits'], shell=True)
        self.atualizar_progresso("Limpando cache do Windows Update...")
    
    def limpar_dns(self):
        # Limpar cache de DNS sem prompt de confirmação
        subprocess.run(['ipconfig', '/flushdns'], shell=True)
        self.atualizar_progresso("Limpando cache de DNS...")
    
    def limpar_edge(self):
        # Limpar cache e cookies do Microsoft Edge sem prompt de confirmação
        subprocess.run(['RunDll32.exe', 'InetCpl.cpl,ClearMyTracksByProcess', '255'], shell=True)
        self.atualizar_progresso("Limpando cache e cookies do Microsoft Edge...")
    
    def limpar_chrome(self):
        # Limpar cache e cookies do Google Chrome sem prompt de confirmação
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"'], shell=True)
        self.atualizar_progresso("Limpando cache e cookies do Google Chrome...")
    
    def limpar_firefox(self):
        # Limpar cache e cookies do Mozilla Firefox sem prompt de confirmação
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2"'], shell=True)
        subprocess.run(['cmd', '/c', 'rd', '/s', '/q', '"%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cookies.sqlite"'], shell=True)
        self.atualizar_progresso("Limpando cache e cookies do Mozilla Firefox...")
    
    def verificar_disco(self):
        # Verificar disco sem prompt de confirmação
        subprocess.run(['chkdsk', 'C:', '/f', '/r', '/x'], shell=True)
        self.atualizar_progresso("Verificando o disco rígido...")
    
    def desfragmentar_disco(self):
        # Desfragmentar disco sem prompt de confirmação
        subprocess.run(['defrag', 'C:', '/O'], shell=True)
        self.atualizar_progresso("Desfragmentando o disco...")
    
    def limpar_desnecessarios(self):
        # Limpar componentes desnecessários do Windows sem prompt de confirmação
        subprocess.run(['dism', '/online', '/cleanup-image', '/startcomponentcleanup'], shell=True)
        self.atualizar_progresso("Limpando componentes desnecessários do Windows...")
    
    def limpar_atualizacao(self):
        # Limpar arquivos de atualização do Windows sem prompt de confirmação
        subprocess.run(['dism', '/online', '/cleanup-image', '/spsuperseded', '/hidesp'], shell=True)
        self.atualizar_progresso("Limpando arquivos de atualização do Windows...")
    
    def compactar_sistema(self):
        # Compactar arquivos do sistema sem prompt de confirmação
        subprocess.run(['compact', '/compactos:always', '/exe'], shell=True)
        self.atualizar_progresso("Compactando arquivos do sistema para economizar espaço...")
    
    def atualizar_progresso(self, mensagem):
        self.progress_label.config(text=mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = LimpezaSistema(root)
    root.mainloop()