# Limpeza e Otimização de Sistema

Este código implementa uma interface gráfica para realizar diversas tarefas de limpeza e otimização no sistema Windows. A seguir, estão descritas todas as funcionalidades que o código é capaz de realizar:

## Funcionalidades de Limpeza

1. **Limpeza de Arquivos Temporários:**
   - Remove arquivos temporários do diretório `%TEMP%`, `C:\Windows\Temp` e `C:\Windows\Prefetch`.

2. **Limpeza de Logs de Eventos:**
   - Limpa logs de eventos do Windows, incluindo Application, Security e System.

3. **Limpeza de Cache do Windows Update:**
   - Para os serviços `wuauserv` e `bits`.
   - Remove o conteúdo do diretório `%windir%\SoftwareDistribution`.
   - Reinicia os serviços `wuauserv` e `bits`.

4. **Limpeza de Cache DNS:**
   - Executa o comando `ipconfig /flushdns` para limpar o cache DNS.

5. **Limpeza de Cache e Cookies de Navegadores:**
   - **Microsoft Edge:** Utiliza `RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255` para limpar o cache e cookies.
   - **Google Chrome:** Remove o conteúdo dos diretórios de cache e cookies.
   - **Mozilla Firefox:** Remove o conteúdo dos diretórios de cache e cookies.
   - **Opera:** Remove o conteúdo dos diretórios de cache e cookies.
   - **Brave:** Remove o conteúdo dos diretórios de cache e cookies.

6. **Limpeza de Arquivos Temporários Adicionais:**
   - Remove arquivos temporários dos diretórios `%USERPROFILE%\AppData\Local\Temp` e `%USERPROFILE%\AppData\LocalLow\Temp`.

7. **Remoção de Programas Não Utilizados:**
   - Exemplo: Verifica e remove o Adobe Flash Player se encontrado.

8. **Limpeza de Espaço em Disco:**
   - Executa `cleanmgr /sagerun:1` para realizar uma limpeza abrangente do disco.

## Funcionalidades de Otimização

1. **Verificação e Reparo de Disco:**
   - Executa `chkdsk C: /f /r /x` para verificar e reparar o disco.

2. **Desfragmentação do Disco:**
   - Executa `defrag C: /O` para desfragmentar o disco.

3. **Limpeza de Componentes Desnecessários do Windows:**
   - Executa `dism /online /cleanup-image /startcomponentcleanup`.

4. **Limpeza de Arquivos de Atualização do Windows:**
   - Executa `dism /online /cleanup-image /spsuperseded /hidesp`.

5. **Compactação de Arquivos do Sistema:**
   - Executa `compact /compactos:always /exe` para compactar arquivos do sistema.

6. **Desativação da Hibernação:**
   - Executa `powercfg -h off` para desativar a hibernação, economizando espaço em disco.

7. **Desabilitação de Programas de Inicialização:**
   - Remove entradas de programas indesejados na inicialização do Windows.

8. **Otimização do Tempo de Desligamento:**
   - Configura o Registro do Windows para reduzir o tempo de espera para finalizar aplicativos e serviços durante o desligamento.

## Uso

Para utilizar este script, é necessário executá-lo como administrador. A interface gráfica permite iniciar o processo de limpeza clicando em um botão, enquanto uma barra de progresso e mensagens de status informam o andamento da limpeza e otimização do sistema.

Este script oferece uma solução abrangente para manter o sistema Windows limpo e otimizado, melhorando o desempenho e liberando espaço em disco.
