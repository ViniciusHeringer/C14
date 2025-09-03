import unittest
from unittest.mock import patch, mock_open, call
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import save_users


class TestSaveUsers(unittest.TestCase):
    """
    Suíte de testes focada na função save_users.
    """

    # --- Caminhos Felizes (Happy Paths) ---

    @patch("builtins.open", new_callable=mock_open)
    def test_save_single_user_happy(self, mock_file):
        """
        HAPPY: Testa se um único usuário é salvo corretamente no arquivo.
        """
        users = [{'name': 'File User', 'email': 'file@example.com'}]
        save_users(users)

        mock_file.assert_called_with("UserData.txt", "a")
        handle = mock_file()

        # CORREÇÃO: Verifica a chamada única de 'write' com o texto completo.
        expected_output = "Nome: File User\nE-Mailfile@example.com\n\n"
        handle.write.assert_called_with(expected_output)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_multiple_users_happy(self, mock_file):
        """
        HAPPY: Testa se múltiplos usuários são salvos corretamente.
        """
        users = [
            {'name': 'User One', 'email': 'one@test.com'},
            {'name': 'User Two', 'email': 'two@test.com'}
        ]
        save_users(users)
        handle = mock_file()

        # CORREÇÃO: A contagem de chamadas de 'write' deve ser 2 (uma por usuário).
        self.assertEqual(handle.write.call_count, 2)

        # CORREÇÃO: Verifica as chamadas exatas que foram feitas.
        expected_calls = [
            call("Nome: User One\nE-Mailone@test.com\n\n"),
            call("Nome: User Two\nE-Mailtwo@test.com\n\n")
        ]
        # CORREÇÃO FINAL: A asserção agora foca apenas no método 'write', ignorando o 'close'.
        handle.write.assert_has_calls(expected_calls, any_order=True)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_user_missing_keys_happy(self, mock_file):
        """
        HAPPY: Testa se usuários com dados faltando são salvos com 'N/A'.
        """
        users = [{'name': 'Just Name'}]
        save_users(users)
        handle = mock_file()

        # CORREÇÃO: Verifica a chamada única com o texto completo, incluindo 'N/A'.
        expected_output = "Nome: Just Name\nE-MailN/A\n\n"
        handle.write.assert_called_with(expected_output)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_empty_list_does_not_write_happy(self, mock_file):
        """
        HAPPY: Testa se a função não escreve nada quando a lista de usuários está vazia.
        """
        save_users([])
        handle = mock_file()
        handle.write.assert_not_called()

    # --- Caminhos Tristes (Sad Paths) ---

    @patch("builtins.open")
    def test_save_users_permission_error_sad(self, mock_open_func):
        """
        SAD: Testa o comportamento ao tentar salvar sem permissão de escrita.
        """
        users = [{'name': 'Error User', 'email': 'error@test.com'}]
        mock_open_func.side_effect = PermissionError("Permissão negada")

        with self.assertRaises(PermissionError):
            save_users(users)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_users_io_error_on_write_sad(self, mock_file):
        """
        SAD: Testa o comportamento se ocorrer um erro durante a escrita no arquivo.
        """
        users = [{'name': 'IO Error User', 'email': 'io@test.com'}]
        handle = mock_file()
        handle.write.side_effect = IOError("Disco cheio")

        with self.assertRaises(IOError):
            save_users(users)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_repeated_user_sad(self, mock_file):
        """
        SAD: Testa se usuários repetidos são simplesmente adicionados novamente,
             já que a lógica atual não previne duplicatas.
        """
        users = [{'name': 'Repeated', 'email': 'repeated@test.com'}]
        save_users(users)
        save_users(users)  # Salva o mesmo usuário duas vezes

        handle = mock_file()
        # CORREÇÃO: A contagem deve ser 2, uma para cada chamada de save_users.
        self.assertEqual(handle.write.call_count, 2)


if __name__ == '__main__':
    unittest.main()

