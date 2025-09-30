import unittest
from unittest.mock import patch
import requests
import sys
import os

# Adiciona o diretório raiz ao path para encontrar o módulo 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import fetch_users


class TestFetchUsers(unittest.TestCase):
    """
    Suíte de testes focada na função fetch_users.
    """

    # --- Caminhos Felizes (Happy Paths) ---

    @patch('src.main.requests.get')
    def test_fetch_users_success_happy(self, mock_get):
        """
        HAPPY: Testa se a função retorna os dados corretamente em uma chamada de sucesso.
        """
        mock_users = [{'id': 1, 'name': 'Leanne Graham', 'email': 'Sincere@april.biz'}]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_users
        mock_get.return_value.raise_for_status.return_value = None

        users = fetch_users()
        self.assertEqual(users, mock_users)
        mock_get.assert_called_with("https://jsonplaceholder.typicode.com/users")

    @patch('src.main.requests.get')
    def test_fetch_users_returns_list_happy(self, mock_get):
        """
        HAPPY: Testa se a função retorna um tipo 'list' em caso de sucesso.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1}, {'id': 2}]
        mock_get.return_value.raise_for_status.return_value = None

        users = fetch_users()
        self.assertIsInstance(users, list)

    @patch('src.main.requests.get')
    def test_fetch_users_with_multiple_users_happy(self, mock_get):
        """
        HAPPY: Testa o retorno com múltiplos usuários na resposta da API.
        """
        mock_users = [
            {'id': 1, 'name': 'User One', 'email': 'one@test.com'},
            {'id': 2, 'name': 'User Two', 'email': 'two@test.com'}
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_users
        mock_get.return_value.raise_for_status.return_value = None

        users = fetch_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[1]['name'], 'User Two')

    # --- Caminhos Tristes (Sad Paths) ---

    @patch('src.main.requests.get')
    def test_fetch_users_network_error_sad(self, mock_get):
        """
        SAD: Testa se a função retorna None em caso de um erro de rede.
        """
        mock_get.side_effect = requests.exceptions.RequestException("Erro de conexão")
        users = fetch_users()
        self.assertIsNone(users)

    @patch('src.main.requests.get')
    def test_fetch_users_http_error_sad(self, mock_get):
        """
        SAD: Testa se a função retorna None para códigos de status de erro HTTP (ex: 404, 500).
        """
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Não encontrado")
        users = fetch_users()
        self.assertIsNone(users)

    @patch('src.main.requests.get')
    def test_fetch_users_invalid_json_sad(self, mock_get):
        """
        SAD: Testa se a função retorna None quando a API retorna um JSON inválido.
        """
        # CORREÇÃO: Simplificado para testar o novo tratamento de ValueError em main.py
        mock_get.return_value.status_code = 200
        mock_get.return_value.raise_for_status.return_value = None
        mock_get.return_value.json.side_effect = ValueError("JSON inválido")

        users = fetch_users()
        self.assertIsNone(users)

    @patch('src.main.requests.get')
    def test_fetch_users_timeout_sad(self, mock_get):
        """
        SAD: Testa se a função retorna None em caso de timeout na requisição.
        """
        mock_get.side_effect = requests.exceptions.Timeout("Timeout da requisição")
        users = fetch_users()
        self.assertIsNone(users)


if __name__ == '__main__':
    unittest.main()

