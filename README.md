# Projeto de Exemplo: API Fetcher com Pipeline de CI/CD

## 📝 Descrição do Projeto

Este é um projeto simples em Python que demonstra um fluxo de desenvolvimento moderno, incluindo:

* Gerenciamento de dependências com `pip` e `requirements.txt`.
* Consumo de uma API REST pública (JSONPlaceholder) para buscar dados.
* Uma suíte de testes unitários robusta com 20 cenários de teste.
* Um script de build automatizado (`build.sh`) que prepara o ambiente e cria um artefato de distribuição.
* Um pipeline de Integração e Entrega Contínua (CI/CD) completo com GitHub Actions.

O objetivo principal é servir como um modelo para a criação de repositórios, automação de build, testes automatizados e notificação de status.

## 🚀 Status do Pipeline

[![Pipeline de CI/CD para Projeto Python](https://github.com/ViniciusHeringer/C14/actions/workflows/pipeline-principal.yml/badge.svg)](https://github.com/ViniciusHeringer/C14/actions/workflows/pipeline-principal.yml)

## 🛠️ Configuração e Execução Manual

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/)

### Passos para Instalação e Build

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/ViniciusHeringer/C14.git](https://github.com/ViniciusHeringer/C14.git)
   cd C14
   ```
2. **Dê permissão de execução ao script de build (para Linux/macOS/Git Bash):**
   ```bash
   chmod +x build.sh
   ```
3. **Execute o script de build:**

Este script irá criar um ambiente virtual, instalar as dependências e preparar a aplicação.
   ```bash
   ./build.sh
```
**Como Executar a Aplicação:**
1. **Ative o ambiente virtual:**
```bash
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate  # No Windows
```
2. **Execute o script principal:**
```bash
python src/main.py
```
Você deverá ver a lista de usuários buscada da API no seu terminal.

3. **Desative o ambiente virtual ao terminar::**
```bash
deactivate
```
**🧪 Testes Unitários**

O projeto conta com uma suíte de 20 testes unitários para garantir a qualidade e o funcionamento correto das funções.

**Como Executar os Testes Localmente**

*Certifique-se de que as dependências estão instaladas (execute ./build.sh primeiro).*

*Ative o ambiente virtual.*

*Na raiz do projeto, execute o comando de descoberta de testes:*

```bash
python -m unittest discover
```

**⚙️ CI/CD - Integração e Entrega Contínua**

Este projeto utiliza GitHub Actions para automatizar o fluxo de CI/CD. O workflow está definido em ```.github/workflows/pipeline-principal.yml```

**Gatilhos do Pipeline**

O pipeline é acionado automaticamente em duas situações:

1. Quando um push é feito para qualquer branch do repositório.

2. Quando um pull request é aberto ou atualizado.

**Etapas do Pipeline (Jobs)**

O pipeline é dividido em 3 jobs:
1. **Execução dos Testes (```testes```):** 
* Configura o ambiente Python.
* Instala as dependências.
* Executa a suíte completa de testes unitários.
* **Artefato Gerado**: ```relatorio-de-testes```, um arquivo .txt com a saída completa dos testes.
2. Build e Empacotamento (```empacotamento```):
* Roda **em paralelo** com o job de testes para otimizar o tempo.
* Executa o script ```build.sh``` para empacotar a aplicação.
* **Artefato Gerado**: ```pacote-dist```, um arquivo .zip contendo a pasta dist pronta para distribuição.
3. Envio de Notificação (```notificacao```):
* Este job só é executado se os jobs de ```testes``` e ```empacotamento``` forem concluídos com sucesso.
* Executa o script ```scripts/send_notification.py``` para enviar um e-mail de notificação.
* As credenciais de e-mail são gerenciadas de forma segura através de **GitHub Secrets**:

  * ```MAIL_SENDER```: E-mail do remetente.
  * ```MAIL_RECIPIENT```: E-mail do destinatário.
  * ```MAIL_PASSWORD```: Senha de app para o e-mail do remetente.

Os artefatos gerados podem ser baixados diretamente da página de resumo da execução do workflow na aba "Actions" do repositório.