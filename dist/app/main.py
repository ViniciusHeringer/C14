# src/main.py

import requests
import json


def fetch_users():
    """
    Busca dados de usuários de uma API pública (JSONPlaceholder).
    """
    api_url = "https://jsonplaceholder.typicode.com/users"
    print("Buscando dados de usuários da API...")

    try:
        response = requests.get(api_url)
        # Verifica se a requisição foi bem-sucedida (código de status 200)
        response.raise_for_status()

        users = response.json()
        print("Dados recebidos com sucesso!")
        return users

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para a API: {e}")
        return None


def display_users(users):
    """
    Exibe os nomes e e-mails dos usuários de forma organizada.
    """
    if not users:
        print("Nenhum usuário para exibir.")
        return

    print("\n--- Lista de Usuários ---")
    for user in users:
        print(f"- Nome: {user.get('name', 'N/A')}, Email: {user.get('email', 'N/A')}")
    print("-----------------------\n")


if __name__ == "__main__":
    # Ponto de entrada do script
    user_data = fetch_users()
    if user_data:
        display_users(user_data)

