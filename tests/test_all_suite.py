import pytest
import sys


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