from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QFrame
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap
from limpeza_sistema import SistemaLimpeza

class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)
    operation_completed = pyqtSignal(bool, str)

    def __init__(self, operation, parent=None):
        super().__init__(parent)
        self.operation = operation
        self.sistema = SistemaLimpeza()

    def run(self):
        if self.operation == "limpeza":
            success, message = self.sistema.executar_limpeza(self.progress_updated.emit)
        else:
            success, message = self.sistema.executar_atualizacao()
        self.operation_completed.emit(success, message)

class CleanCrowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CleanCrow - Otimizador de Sistema")
        self.setFixedSize(700, 700)  # Aumentado para acomodar os ícones maiores
        self.setWindowIcon(QIcon("crowico.ico"))
        self.setup_ui()

    def setup_ui(self):
        # Configuração principal da janela
        self.setStyleSheet("""
            QMainWindow {
                background-color: #111111;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(25, 25, 25, 25)
        self.main_layout.setSpacing(20)
        self.central_widget.setLayout(self.main_layout)

        # Cabeçalho com logo
        header_widget = QWidget()
        header_layout = QHBoxLayout()
        header_widget.setLayout(header_layout)
        
        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("crowico.ico").scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        header_layout.addWidget(logo_label)
        
        # Título
        title_label = QLabel("CLEANCROW")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #e74c3c;
                padding-left: 10px;
            }
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        self.main_layout.addWidget(header_widget)

        # Descrição
        description = QLabel("Otimizador de Sistema Completo")
        description.setStyleSheet("""
            font-size: 16px; 
            color: #bdc3c7;
            padding-bottom: 10px;
        """)
        description.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(description)

        # Separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border: 1px solid #333333;")
        self.main_layout.addWidget(separator)

        # Label de instrução
        self.label = QLabel("Selecione a operação desejada:")
        self.label.setStyleSheet("""
            font-size: 14px; 
            color: #ecf0f1;
            padding-top: 10px;
        """)
        self.main_layout.addWidget(self.label)

        # Layout dos botões
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(20)
        self.main_layout.addLayout(self.button_layout)

        # Botão Limpar
        self.limpar_button = QPushButton(" LIMPAR SISTEMA")
        self.limpar_button.setIcon(QIcon("103414.png"))
        self.limpar_button.setIconSize(QSize(32, 32))  # Ícone maior
        self.limpar_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 15px;
                border-radius: 6px;
                font-size: 16px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:disabled {
                background-color: #7f8c8d;
            }
        """)
        self.limpar_button.clicked.connect(self.iniciar_limpeza)
        self.button_layout.addWidget(self.limpar_button)

        # Botão Atualizar
        self.atualizar_button = QPushButton(" ATUALIZAR SISTEMA")
        self.atualizar_button.setIcon(QIcon("159612.png"))
        self.atualizar_button.setIconSize(QSize(32, 32))  # Ícone maior
        self.atualizar_button.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                font-weight: bold;
                border: none;
                padding: 15px;
                border-radius: 6px;
                font-size: 16px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #1a252f;
            }
            QPushButton:disabled {
                background-color: #7f8c8d;
            }
        """)
        self.atualizar_button.clicked.connect(self.iniciar_atualizacao)
        self.button_layout.addWidget(self.atualizar_button)

        # Área de status
        status_frame = QFrame()
        status_frame.setStyleSheet("""
            background-color: #222222; 
            border-radius: 8px; 
            padding: 15px;
        """)
        status_layout = QVBoxLayout()
        status_layout.setSpacing(15)
        status_frame.setLayout(status_layout)

        # Label de progresso
        self.progress_label = QLabel("Pronto para iniciar")
        self.progress_label.setStyleSheet("""
            font-size: 18px; 
            color: #ecf0f1;
            font-weight: bold;
            padding: 10px;
        """)
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.progress_label.setMinimumHeight(50)  # Garante espaço suficiente
        status_layout.addWidget(self.progress_label)

        # Barra de progresso
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #333333;
                border-radius: 6px;
                text-align: center;
                height: 24px;
            }
            QProgressBar::chunk {
                background-color: #e74c3c;
                width: 12px;
                border-radius: 5px;
            }
        """)
        status_layout.addWidget(self.progress_bar)

        self.main_layout.addWidget(status_frame)

        # Rodapé
        footer = QLabel("© 2025 CleanCrow - Todos os direitos reservados")
        footer.setStyleSheet("""
            font-size: 11px; 
            color: #7f8c8d; 
            padding-top: 15px;
        """)
        footer.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(footer)

        self.worker_thread = None

    def iniciar_limpeza(self):
        self.limpar_button.setEnabled(False)
        self.atualizar_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.progress_label.setText("Iniciando limpeza do sistema...")
        
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #333333;
                border-radius: 6px;
                text-align: center;
                height: 24px;
            }
            QProgressBar::chunk {
                background-color: #e74c3c;
                width: 12px;
                border-radius: 5px;
            }
        """)

        self.worker_thread = WorkerThread("limpeza")
        self.worker_thread.progress_updated.connect(self.atualizar_progresso)
        self.worker_thread.operation_completed.connect(self.operacao_concluida)
        self.worker_thread.start()

    def iniciar_atualizacao(self):
        self.limpar_button.setEnabled(False)
        self.atualizar_button.setEnabled(False)
        self.progress_label.setText("Iniciando atualização do sistema...")
        
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #333333;
                border-radius: 6px;
                text-align: center;
                height: 24px;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                width: 12px;
                border-radius: 5px;
            }
        """)

        self.worker_thread = WorkerThread("atualizacao")
        self.worker_thread.operation_completed.connect(self.operacao_concluida)
        self.worker_thread.start()

    def atualizar_progresso(self, valor):
        self.progress_bar.setValue(valor)
        self.progress_label.setText(f"Progresso: {valor}% - Limpando sistema...")

    def operacao_concluida(self, success, message):
        if success:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Sucesso")
            msg_box.setText(message)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: #111111;
                    color: white;
                }
                QLabel {
                    color: white;
                }
            """)
            msg_box.exec_()
            
            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 2px solid #333333;
                    border-radius: 6px;
                    text-align: center;
                    height: 24px;
                }
                QProgressBar::chunk {
                    background-color: #2ecc71;
                    width: 12px;
                    border-radius: 5px;
                }
            """)
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Erro")
            msg_box.setText(message)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: #111111;
                    color: white;
                }
                QLabel {
                    color: white;
                }
            """)
            msg_box.exec_()

        self.limpar_button.setEnabled(True)
        self.atualizar_button.setEnabled(True)
        self.progress_label.setText(message)
        if success:
            self.progress_bar.setValue(100)