# CleanCrow - Otimizador e Atualizador de Sistema para Windows

CleanCrow é um software desenvolvido em Python com interface gráfica moderna baseada em PyQt5, projetado para facilitar a limpeza, otimização e atualização do sistema operacional Windows de forma simples, visual e eficiente.

## Principais Funcionalidades

- **Limpeza Completa do Sistema:**  
  Remove arquivos temporários (%TEMP%, C:\Windows\Temp, C:\Windows\Prefetch), limpa logs do Windows, cache DNS, arquivos de atualização antigos, miniaturas, dumps de memória, relatórios de erros, cache da loja do Windows, entre outros resíduos que ocupam espaço e podem afetar o desempenho.

- **Limpeza de Navegadores:**  
  Limpa cache, cookies e dados de navegação dos principais navegadores, incluindo Google Chrome, Mozilla Firefox, Opera, Brave, Vivaldi, Safari, Tor, Maxthon, Waterfox e Pale Moon.

- **Remoção de Programas e Bloatware:**  
  Remove utilitários desnecessários (como FlashUtil*.exe) e bloatwares comuns do Windows, liberando recursos e melhorando a inicialização.

- **Otimização de Disco e Sistema:**  
  Executa limpeza de disco (cleanmgr), verifica e agenda correção de erros no disco (chkdsk), desfragmenta o disco (defrag), limpa componentes de sistema (DISM), compacta arquivos do sistema, desativa hibernação e inicialização automática de programas indesejados.

- **Ajustes de Desligamento:**  
  Otimiza o tempo de desligamento do Windows ajustando parâmetros no registro para encerramento mais rápido de aplicativos e serviços.

- **Atualização de Pacotes:**  
  Atualiza todos os programas instalados via Windows Package Manager (winget) com um clique, mantendo o sistema sempre atualizado e seguro.

## Como Usar

- **Limpeza do Sistema:**  
  Clique no botão **"LIMPAR SISTEMA"** para iniciar todas as operações de limpeza e otimização. O progresso é exibido em tempo real na barra de progresso e no status.

- **Atualização do Sistema:**  
  Clique no botão **"ATUALIZAR SISTEMA"** para atualizar todos os pacotes instalados via winget. O status da operação será exibido na interface.

- **Interface Moderna:**  
  A interface é intuitiva, com botões grandes, ícones e feedback visual para cada etapa. Mensagens de sucesso ou erro são exibidas ao final de cada operação.

## Requisitos e Observações

- **Permissões de Administrador:**  
  Execute o CleanCrow como administrador para garantir que todas as operações sejam realizadas corretamente.

- **Compatibilidade:**  
  Compatível apenas com Windows (requer Python 3.x, PyQt5 e winget instalado para atualização de pacotes).

- **Feedback de Erros:**  
  Caso ocorra algum erro durante as operações, uma mensagem detalhada será exibida para auxiliar na resolução.

## Licença

Este software é licenciado sob a GNU GPL v3.0. Consulte o arquivo LICENSE para mais informações.

---

Mantenha seu Windows limpo, otimizado e atualizado com praticidade e segurança usando o CleanCrow!
