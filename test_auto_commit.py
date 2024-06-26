import os
import datetime
from time import sleep
from git import Repo

# Caminho para o repositório local
repo_path = r'G:\projects\cleancrow'

# URL do repositório remoto
repo_url = 'https://github.com/EduardoDosSantosFerreira/cleancrow'

# Função para realizar o commit e push
def commit_and_push(repo_path, repo_url):
    try:
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

        print(f"Commit realizado com sucesso às {datetime.datetime.now()}")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Loop para executar o commit a cada 1 minuto
while True:
    commit_and_push(repo_path, repo_url)
    # Espera 1 minuto antes de executar o próximo commit
    sleep(60)
