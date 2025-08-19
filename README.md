# Projeto de Exemplo: API Fetcher em Python

## 📝 Descrição do Projeto

Este é um projeto simples em Python que demonstra um fluxo de desenvolvimento moderno, incluindo:
-   Gerenciamento de dependências com `pip` e `requirements.txt`.
-   Consumo de uma API REST pública (JSONPlaceholder) para buscar dados.
-   Um script de build automatizado (`build.sh`) que prepara o ambiente e cria um artefato de distribuição.

O objetivo principal é servir como um modelo para a criação de repositórios, automação de build e versionamento com Git e GitHub.

---

## 🚀 Configuração e Execução

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

-   [Python 3](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads/)

### Passos para Instalação e Build

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    cd NOME-DO-REPOSITORIO
    ```

2.  **Dê permissão de execução ao script de build (para Linux/macOS/Git Bash):**
    ```bash
    chmod +x build.sh
    ```

3.  **Execute o script de build:**
    Este script irá criar um ambiente virtual, instalar as dependências e preparar a aplicação.
    ```bash
    ./build.sh
    ```

### Como Executar a Aplicação

Após o build ser concluído com sucesso, siga os passos abaixo para rodar o script:

1.  **Ative o ambiente virtual:**
    ```bash
    source venv/Scripts/activate
    ```

2.  **Execute o script principal:**
    ```bash
    py dist/app/main.py
    ```
    Você deverá ver a lista de usuários buscada da API no seu terminal.

3.  **Desative o ambiente virtual ao terminar:**
    ```bash
    deactivate
    ```
