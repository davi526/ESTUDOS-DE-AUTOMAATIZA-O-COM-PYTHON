"""Execução das ações cadastradas no Python Deck."""

from actions.registry import get_action


def execute_action(action_id):
    """Executa a ação identificada por action_id e retorna seu resultado."""
    print(f"Buscando ação: {action_id}")

    action = get_action(action_id)

    if action is None:
        print(f"Ação não encontrada: {action_id}")
        return False

    try:
        result = action()
        print(f"Ação executada: {action_id}")
        return bool(result)
    except Exception as error:
        print(f"Erro ao executar a ação '{action_id}': {error}")
        return False


from pathlib import Path
import subprocess
import webbrowser

from services.registry import get_action


def _remover_aspas_externas(valor):
    """Remove somente aspas que envolvem todo o valor informado."""
    valor = valor.strip()

    if len(valor) >= 2 and valor[0] == valor[-1] == '"':
        return valor[1:-1].strip()

    return valor


def _executar_executavel(valor):
    """Valida e executa um arquivo .exe informado pelo usuário."""
    caminho = _remover_aspas_externas(valor)

    try:
        executavel = Path(caminho)

        if not executavel.exists():
            print(f"Arquivo não encontrado: {caminho}")
            return False

        if not executavel.is_file():
            print(f"O caminho não é um arquivo: {caminho}")
            return False

        if executavel.suffix.lower() != ".exe":
            print(f"O arquivo não possui extensão .exe: {caminho}")
            return False

        print(f"Abrindo executável: {executavel}")
        subprocess.Popen([str(executavel)])
        return True
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except PermissionError:
        print(f"Permissão negada para abrir: {caminho}")
    except (OSError, subprocess.SubprocessError) as error:
        print(f"Erro ao abrir executável '{caminho}': {error}")
    except Exception as error:
        print(f"Erro inesperado ao abrir executável '{caminho}': {error}")

    return False


def execute_action(action_id):
    """Executa uma ação registrada, uma URL ou um arquivo executável."""
    print(f"Buscando ação registrada: {action_id}")

    if not isinstance(action_id, str):
        print("Formato de ação não reconhecido: o valor deve ser texto.")
        return False

    valor = action_id.strip()
    action = get_action(valor)

    if action is not None:
        try:
            resultado = action()
            print(f"Ação registrada executada: {valor}")
            return bool(resultado)
        except FileNotFoundError:
            print(f"Arquivo não encontrado ao executar a ação: {valor}")
        except PermissionError:
            print(f"Permissão negada ao executar a ação: {valor}")
        except (OSError, subprocess.SubprocessError) as error:
            print(f"Erro ao executar a ação '{valor}': {error}")
        except Exception as error:
            print(f"Erro inesperado ao executar a ação '{valor}': {error}")

        return False

    if valor.startswith(("http://", "https://")):
        try:
            print(f"Abrindo site: {valor}")
            return bool(webbrowser.open(valor))
        except OSError as error:
            print(f"Erro ao abrir site '{valor}': {error}")
        except Exception as error:
            print(f"Erro inesperado ao abrir site '{valor}': {error}")

        return False

    if _remover_aspas_externas(valor).lower().endswith(".exe"):
        return _executar_executavel(valor)

    print(f"Formato de ação não reconhecido: {valor}")
    return False


def executar_acao(action_id):
    """Mantém compatibilidade com chamadas existentes ao executor."""
    return execute_action(action_id)