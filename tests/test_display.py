import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import display_users


class TestDisplayUsers(unittest.TestCase):
    """
    Suíte de testes focada na função display_users.
    """

    def setUp(self):
        """ Prepara o ambiente antes de cada teste. """
        self.held_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        """ Limpa o ambiente depois de cada teste. """
        sys.stdout = self.held_stdout

    # --- Caminhos Felizes (Happy Paths) ---

    def test_display_single_user_happy(self):
        """
        HAPPY: Testa a exibição de um único usuário.
        """
        users = [{'name': 'Test User', 'email': 'test@example.com'}]
        display_users(users)
        output = sys.stdout.getvalue()
        self.assertIn("- Nome: Test User, Email: test@example.com", output)
        self.assertIn("--- Lista de Usuários ---", output)

    def test_display_multiple_users_happy(self):
        """
        HAPPY: Testa a exibição de múltiplos usuários.
        """
        users = [
            {'name': 'User One', 'email': 'one@test.com'},
            {'name': 'User Two', 'email': 'two@test.com'}
        ]
        display_users(users)
        output = sys.stdout.getvalue()
        self.assertIn("- Nome: User One, Email: one@test.com", output)
        self.assertIn("- Nome: User Two, Email: two@test.com", output)

    def test_display_user_with_missing_keys_happy(self):
        """
        HAPPY: Testa se a exibição lida com usuários que não têm 'name' ou 'email'.
        """
        users = [{'id': 1}, {'name': 'Just Name'}, {'email': 'just@email.com'}]
        display_users(users)
        output = sys.stdout.getvalue()
        self.assertIn("- Nome: N/A, Email: N/A", output)
        self.assertIn("- Nome: Just Name, Email: N/A", output)
        self.assertIn("- Nome: N/A, Email: just@email.com", output)

    # --- Caminhos Tristes (Sad Paths) ---

    def test_display_empty_list_sad(self):
        """
        SAD: Testa a mensagem exibida para uma lista de usuários vazia.
        """
        display_users([])
        self.assertIn("Nenhum usuário para exibir.", sys.stdout.getvalue())

    def test_display_none_input_sad(self):
        """
        SAD: Testa a mensagem exibida quando a entrada é None.
        """
        display_users(None)
        self.assertIn("Nenhum usuário para exibir.", sys.stdout.getvalue())

    def test_display_user_with_empty_dict_sad(self):
        """
        SAD: Testa a exibição de uma lista contendo um dicionário vazio.
        """
        users = [{}]
        display_users(users)
        self.assertIn("- Nome: N/A, Email: N/A", sys.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
