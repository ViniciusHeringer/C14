Projeto de Exemplo: API Fetcher em Python
📝 Descrição do Projeto
Este é um projeto simples em Python que demonstra um fluxo de desenvolvimento moderno, incluindo:

Gerenciamento de dependências com pip e requirements.txt.

Consumo de uma API REST pública (JSONPlaceholder) para buscar dados.

Uma suíte de testes unitários robusta utilizando o framework unittest e unittest.mock.

Um script de build automatizado (build.sh) que prepara o ambiente e cria um artefato de distribuição.

O objetivo principal é servir como um modelo para a criação de repositórios, automação de build, práticas de teste e versionamento com Git e GitHub.

🚀 Configuração e Execução
Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos
Python 3

Git

Passos para Instalação e Build
Clone o repositório:

git clone https://github.com/ViniciusHeringer/C14/tree/tradução-ptbr
cd C14

Dê permissão de execução ao script de build (para Linux/macOS/Git Bash):

chmod +x build.sh

Execute o script de build:
Este script irá criar um ambiente virtual, instalar as dependências e preparar a aplicação.

./build.sh

Como Executar a Aplicação
Após o build ser concluído com sucesso, siga os passos abaixo para rodar o script:

Ative o ambiente virtual:

source venv/Scripts/activate

Execute o script principal:

py dist/app/main.py

Você deverá ver a lista de usuários buscada da API no seu terminal.

Desative o ambiente virtual ao terminar:

deactivate

🧪 Testes Unitários
O projeto conta com uma suíte de 20 testes unitários, divididos por funcionalidade, localizados na pasta tests/.

Como Executar os Testes
Ative o ambiente virtual:

source venv/Scripts/activate

Execute o comando de descoberta de testes na raiz do projeto:

python -m unittest discover

O resultado deve indicar que todos os 20 testes passaram com sucesso.

Evolução e Correção dos Testes (Caso de Estudo: test_save.py)
Durante o desenvolvimento dos testes para a função save_users, surgiram desafios que ilustram bem o processo de depuração de testes unitários.

Problema Inicial: Divergência de Expectativas

Comportamento da Função: A função save_users em src/main.py foi implementada para escrever os dados de um usuário (nome e e-mail) em uma única operação de escrita (stream.write(...)) por usuário.

Falha nos Testes: A primeira versão de tests/test_save.py foi escrita sob a premissa de que haveria duas operações de escrita por usuário (uma para o nome, outra para o e-mail). Isso causou AssertionError nos testes, pois a contagem de chamadas (call_count) e o conteúdo de cada chamada não batiam com a realidade.

Primeira Correção: Alinhamento dos Testes

Solução: Os testes foram ajustados para refletir o comportamento real da função. As asserções que verificavam duas chamadas (assert_any_call) foram substituídas por uma única verificação (assert_called_with) que esperava o texto completo e formatado para cada usuário. A contagem de chamadas esperada também foi corrigida (ex: de 4 para 2 em um teste com dois usuários).

Problema Final: Detalhe Sutil do Mock

Falha Persistente: Mesmo após a correção principal, um teste continuou falhando (test_save_multiple_users_happy). O erro indicava que a lista de chamadas registradas pelo mock continha uma chamada extra: call.close().

Causa: A função save_users corretamente fecha o arquivo (stream.close()) após a escrita. O teste, ao usar handle.assert_has_calls(...), validava todas as chamadas feitas ao objeto de arquivo mockado, incluindo o close que não estava na lista de chamadas esperadas.

Correção Final: Especificidade na Asserção

Solução: A asserção foi refinada de handle.assert_has_calls(...) para handle.write.assert_has_calls(...). Essa pequena mudança instruiu o teste a validar apenas o histórico de chamadas do método write, ignorando a chamada ao método close e resolvendo o problema. O teste passou a focar exclusivamente no que queria validar: a operação de escrita.

Este processo demonstra a importância de entender tanto o código de produção quanto o funcionamento detalhado das ferramentas de mock para criar testes precisos e confiáveis.