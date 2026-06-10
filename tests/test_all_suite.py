import pytest
import sys
import os

# Resolve o problema de importacao do modulo 'src'.
# Pega o caminho absoluto do diretorio pai (raiz do projeto) e adiciona ao sys.path.
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if diretorio_raiz not in sys.path:
    sys.path.insert(0, diretorio_raiz)


def run_all_tests():
    """
    Executa toda a suite de testes do projeto utilizando o pytest.
    Garante que todos os casos de deduplicacao sejam rodados em conjunto,
    conforme exigido pelo enunciado do trabalho.
    """
    print("Iniciando a bateria completa de testes de Curadoria de Dados...")
    
    # O argumento "-v" aumenta o detalhamento (verbose), mostrando cada teste executado.
    # "tests/" indica o diretorio onde os testes estao localizados.
    exit_code = pytest.main(["-v", "tests/"])
    
    sys.exit(exit_code)


if __name__ == "__main__":
    run_all_tests()