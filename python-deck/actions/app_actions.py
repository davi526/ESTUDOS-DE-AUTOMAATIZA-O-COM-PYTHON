"""Ações para abrir aplicativos do Windows."""

import subprocess


def _abrir_aplicativo(comando):
    """Abre um aplicativo usando o executável informado."""
    try:
        subprocess.Popen([comando])
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def abrir_calculadora():
    """Abre a calculadora do Windows e retorna se a operação foi iniciada."""
    return _abrir_aplicativo("calc.exe")


def abrir_notepad():
    """Abre o Bloco de Notas do Windows e retorna se a operação foi iniciada."""
    return _abrir_aplicativo("notepad.exe")


def abrir_explorer():
    """Abre o Explorador de Arquivos do Windows e retorna se a operação foi iniciada."""
    return _abrir_aplicativo("explorer.exe")