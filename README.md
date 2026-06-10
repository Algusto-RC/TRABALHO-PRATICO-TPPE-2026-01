## UnB - Universidade de Brasília  
### FCTE - Faculdade de Ciências e Tecnologias em Engenharias  
### Disciplina: Técnicas de Programação para Plataformas Emergentes (TPPE)

---

## Integrantes do Grupo

| Nome | Matrícula |
| :--- | :---: | 
| [Algusto Rodrigues Caldas](https://github.com/Algusto-RC) | 202017521 |
| [Augusto Campos Duarte](https://github.com/AugCamp) | 202045965 |
| [Eric Rabelo Borges](https://github.com/rabelzx) | 211030729 |
| [Filipe Carvalho da Silva](https://github.com/filipe-002) | 211030747 |
| [Hian Praxedes de Souza Oliveira](https://github.com/HianPraxedes) | 200019520 |

---

## Tecnologias Utilizadas

* **Linguagem de Programação:** Python (Orientada a Objetos)
* **Framework de Testes Unitários:** [Pytest](https://docs.pytest.org/) 
* **Versão do Framework:** v8.2.2 (ou superior)

---

## Sobre o Projeto

O projeto consiste no desenvolvimento de uma ferramenta de curadoria e deduplicação de registros de publicações científicas para unificação no padrão-ouro. Foram implementadas soluções baseadas em **Test-Driven Development (TDD)** englobando os seguintes cenários:

1. **Caso 1: Diferenças de grafia (tipográficas)** (`TypographicNormalizer`)
2. **Caso 2: Sobrenome + Iniciais dos nomes** (`InitialsMatcher`)
3. **Caso 3: Partículas *de* e uso de ponto opcional** (`ParticleNormalizer`)
4. **Caso 4: Iniciais dos nomes agrupadas + sobrenome** (`GroupedInitialsMatcher`)
5. **Caso 5: IDs diferentes para o mesmo autor** (`AuthorIdResolver`)

---

## Instruções de Execução dos Testes

Para rodar os testes unitários garantindo que todas as validações de curadoria de dados estejam funcionando, siga as instruções abaixo:

### 1. Instalação do Framework

Certifique-se de que o Pytest está instalado no seu ambiente. Caso não esteja, instale-o via pip:

```bash
pip install pytest
```

### 2. Execução da Suíte de Testes

Abra o terminal, certifique-se de estar na raiz do diretório do projeto e execute o script criado para rodar todos os testes em conjunto:

```bash
python tests/test_all_suite.py
```

### 3. Execução Alternativa (Descoberta Automática)

Também é possível executar todos os testes utilizando o mecanismo de descoberta automática do Pytest. O argumento `-v` (*verbose*) exibirá detalhes de cada teste executado:

```bash
pytest tests/ -v
```

### Resultado Esperado

Ao final da execução, todos os testes devem ser concluídos com sucesso, indicando que as implementações dos cinco casos de deduplicação estão funcionando corretamente.

Exemplo:

```text
=================== test session starts ===================
collected 10 items

tests/test_author_id_merge.py ..                    [20%]
tests/test_grouped_initials.py ..                   [40%]
tests/test_initials_matching.py ..                  [60%]
tests/test_particle_normalization.py ..             [80%]
tests/test_typographic_normalization.py ..          [100%]

=================== 10 passed =============================
```