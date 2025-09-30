#!/bin/bash

set -e

echo "--- Iniciando o processo de build ---"

echo "[PASSO 1/4] Limpando builds anteriores..."
rm -rf venv
rm -rf dist
echo "Limpeza concluída."

echo "[PASSO 2/4] Criando ambiente virtual 'venv'..."
python3 -m venv venv
echo "Ambiente virtual criado."

echo "[PASSO 3/4] Instalando dependências..."
source venv/bin/activate
pip install -r requirements.txt
deactivate
echo "Dependências instaladas."

echo "[PASSO 4/4] Empacotando a aplicação..."
mkdir -p dist/app
cp src/main.py dist/app/
echo "Empacotamento concluído."

echo "--- Build finalizado com sucesso! ---"
