import subprocess
from datetime import datetime

def run_git_command(command):
    """Executa um comando Git e retorna a saída como string."""
    try:
        return (
            subprocess.check_output(command, stderr=subprocess.DEVNULL).decode().strip()
        )
    except subprocess.CalledProcessError:
        return ""

def auto_commit():
    """Executa o fluxo de commit e push automático."""
    print(f"Criando commit...")

    subprocess.run(["git", "pull", "origin", "main"], check=True)

    subprocess.run(["git", "add", "."], check=True)

    commit_message = (
        f'Atualização automática: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    )
    subprocess.run(["git", "commit", "--allow-empty", "-m", commit_message], check=True)

    subprocess.run(["git", "push", "origin", "main"], check=True)

    print(f"Commit realizado com sucesso: {commit_message}")


if __name__ == "__main__":
    if not run_git_command(["git", "config", "user.name"]):
        subprocess.run(
            ["git", "config", "--global", "user.name", "Seu Nome"], check=True
        )
    if not run_git_command(["git", "config", "user.email"]):
        subprocess.run(
            ["git", "config", "--global", "user.email", "seuemail@example.com"],
            check=True,
        )

    auto_commit()