# src/main.py

import requests
import os

userDataPath = "UserData.txt"
if os.path.exists(userDataPath):
    os.remove(userDataPath)


def fetch_users():
    """
    Busca dados de usuários de uma API pública (JSONPlaceholder).
    """
    api_url = "https://jsonplaceholder.typicode.com/users"
    print("Buscando dados de usuários da API...")

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        users = response.json()
        print("Dados recebidos com sucesso!")
        return users

    # CORREÇÃO: Adicionado 'ValueError' para capturar erros de decodificação de JSON.
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Erro ao fazer a requisição ou processar dados da API: {e}")
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


def save_users(users):
    stream = open(userDataPath, "a")
    for user in users:
        # A implementação original com uma única chamada de 'write' está correta.
        stream.write(f"Nome: {user.get('name', 'N/A')}\nE-Mail{user.get('email', 'N/A')}\n\n")
    stream.close()


if __name__ == "__main__":
    user_data = fetch_users()
    if user_data:
        display_users(user_data)
        save_users(user_data)
