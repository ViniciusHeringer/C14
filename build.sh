#!/bin/bash

# Script para automatizar o build do projeto Python.
# Ele irá:
# 1. Criar um ambiente virtual para isolar as dependências.
# 2. Ativar o ambiente virtual.
# 3. Instalar as dependências listadas em requirements.txt.
# 4. Criar um "artefato" final no diretório 'dist'.

echo "--- Iniciando o processo de build ---"

# Parar o script se algum comando falhar
set -e

# 1. Limpar builds anteriores (diretório venv e dist)
echo "[PASSO 1/4] Limpando builds anteriores..."
rm -rf venv
rm -rf dist
echo "Limpeza concluída."

# 2. Criar um ambiente virtual
# Alterado para 'py' para usar o Python Launcher do Windows, que é mais confiável.
echo "[PASSO 2/4] Criando ambiente virtual 'venv'..."
py -m venv venv
echo "Ambiente virtual criado."

# 3. Ativar o ambiente virtual e instalar dependências
echo "[PASSO 3/4] Instalando dependências de requirements.txt..."
source venv/Scripts/activate # Caminho de ativação para Git Bash no Windows
pip install -r requirements.txt
deactivate # Desativa o ambiente após a instalação
echo "Dependências instaladas com sucesso."

# 4. Gerar o artefato final
echo "[PASSO 4/4] Criando o artefato de distribuição em 'dist/'..."
mkdir -p dist/app
cp -r src/* dist/app/
echo "Artefato criado em dist/app."

echo ""
echo "--- Build concluído com sucesso! ---"
echo ""
echo "Para executar a aplicação, use os seguintes comandos:"
echo "1. Ative o ambiente virtual: source venv/Scripts/activate"
echo "2. Execute o script: py dist/app/main.py"
echo "3. Desative o ambiente ao terminar: deactivate"
echo "-------------------------------------"

