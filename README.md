# Funcionalidades do Software de Limpeza e Atualização do Sistema

Este software desenvolvido em Python utilizando a biblioteca Tkinter oferece uma interface gráfica para realizar diversas operações de limpeza, otimização e atualização do sistema operacional Windows.

## Funcionalidades Detalhadas:

1. **Limpeza do Sistema:**
   - Remove arquivos temporários das pastas %TEMP%, C:\\Windows\\Temp e C:\\Windows\\Prefetch.
   - Limpa logs do sistema utilizando o utilitário wevtutil.exe.
   - Interrompe serviços de atualização do Windows, limpa a pasta SoftwareDistribution e reinicia os serviços.
   - Executa o comando ipconfig /flushdns para limpar o cache DNS.
   - Utiliza RunDll32.exe para limpar dados de navegação do Microsoft Edge.

2. **Limpeza de Navegadores:**
   - Remove cache e cookies dos navegadores Google Chrome, Mozilla Firefox, Opera e Brave utilizando comandos de linha.

3. **Remoção de Programas:**
   - Verifica a existência do utilitário FlashUtil*.exe e o remove caso encontrado.

4. **Otimização do Sistema:**
   - Executa o utilitário cleanmgr /sagerun:1 para liberar espaço em disco.
   - Verifica a integridade do disco com chkdsk e agenda uma verificação completa no próximo reinício.
   - Desfragmenta o disco utilizando o comando defrag C: /O.
   - Utiliza o utilitário dism para limpeza de componentes de sistema desnecessários e atualizações supercedidas.

5. **Outras Operações de Otimização:**
   - Compacta arquivos do sistema utilizando o comando compact /compactos:always /exe.
   - Desativa a hibernação com powercfg -h off.
   - Limpa diretórios de arquivos temporários adicionais em %USERPROFILE%\\AppData\\Local\\Temp e %USERPROFILE%\\AppData\\LocalLow\\Temp.
   - Configura a inicialização de programas indesejados no registro do Windows para evitar execuções automáticas.

6. **Otimização de Desligamento:**
   - Ajusta os tempos de espera para encerramento de aplicativos e serviços no registro do Windows para otimizar o processo de desligamento.

7. **Atualização de Pacotes:**
   - Implementa a funcionalidade de atualização de pacotes utilizando o comando `winget upgrade --all`, garantindo que todos os pacotes instalados via Windows Package Manager (winget) estejam na versão mais recente.

## Como Usar:

- **Interface Gráfica:** Basta clicar no botão "Limpar" para iniciar todas as operações de limpeza e otimização. Uma barra de progresso acompanha cada operação.
- **Atualização de Pacotes:** Utilize o botão "Atualizar" para executar a atualização de pacotes via `winget upgrade --all`. A barra de progresso indica o progresso da atualização.

### Importante:

- **Execução como Administrador:** Para garantir que todas as operações sejam concluídas com sucesso, execute o software com permissões de administrador.
- **Feedback de Erros:** Caso ocorra algum erro durante qualquer uma das operações, uma mensagem de erro será exibida para orientar o usuário sobre o problema.

Este software proporciona uma maneira conveniente e eficiente de manter seu sistema operacional Windows limpo, otimizado e atualizado, contribuindo para melhorar o desempenho e a segurança do seu computador.
