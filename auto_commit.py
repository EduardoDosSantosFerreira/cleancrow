import os
import datetime
from git import Repo

# Caminho para o repositório local
repo_path = r'G:\projects\cleancrow'

# URL do repositório remoto
repo_url = 'https://github.com/EduardoDosSantosFerreira/cleancrow'

# Função para realizar o commit diário
def daily_commit(repo_path, repo_url):
    # Verifica se o repositório já existe localmente
    if not os.path.exists(repo_path):
        # Clona o repositório se não existir localmente
        Repo.clone_from(repo_url, repo_path)

    # Abre o repositório
    repo = Repo(repo_path)

    # Adiciona todos os arquivos modificados para o commit
    repo.git.add('--all')

    # Cria uma mensagem de commit com a data atual
    today = datetime.date.today()
    commit_message = f"Auto commit {today}"

    # Realiza o commit
    repo.index.commit(commit_message)

    # Push para o repositório remoto
    origin = repo.remote('origin')
    origin.push()

# Chamada da função para fazer o commit diário
daily_commit(repo_path, repo_url)
