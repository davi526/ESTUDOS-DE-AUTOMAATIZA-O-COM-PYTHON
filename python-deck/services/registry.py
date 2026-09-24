"""Registro central das ações disponíveis no Python Deck."""

from actions.app_actions import abrir_calculadora, abrir_explorer, abrir_notepad


ACTIONS = {
    "calculadora": abrir_calculadora,
    "notepad": abrir_notepad,
    "explorer": abrir_explorer,
}


def get_action(action_id):
    """Retorna a função associada ao identificador ou None se não existir."""
    return ACTIONS.get(action_id)