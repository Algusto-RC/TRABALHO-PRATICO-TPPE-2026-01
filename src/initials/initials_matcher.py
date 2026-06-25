import unicodedata


class InitialsMatcher:
    """
    Caso 2 - Sobrenome + Iniciais dos nomes.

    Identifica a equivalência entre um nome completo e sua versão
    abreviada no formato "Sobrenome + Iniciais" (com ou sem pontos),
    unificando sempre para a versão completa.

    Exemplos de equivalência:
        Ana de Mattos Seabra  <->  Seabra A. M.
        Ana de Mattos Seabra  <->  Seabra AM
        Cassius de Souza      <->  Souza C.
    """

    PARTICLES = {"de", "da", "do", "dos", "das", "e"}

    def normalize(self, text):
        """Remove acentos, pontos e converte para minusculas."""
        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ASCII", "ignore").decode("utf-8")
        text = text.replace(".", " ")
        return text.lower()

    def _tokens(self, name):
        """Tokeniza o nome ignorando as particulas (de, da, dos, ...)."""
        tokens = self.normalize(name).split()
        return [token for token in tokens if token not in self.PARTICLES]

    def _surname_and_initials(self, full_name):
        """
        A partir do nome completo, devolve o sobrenome (ultimo nome)
        e a sequencia de iniciais dos demais nomes.

        "Ana de Mattos Seabra" -> ("seabra", "am")
        """
        tokens = self._tokens(full_name)
        surname = tokens[-1]
        initials = "".join(token[0] for token in tokens[:-1])
        return surname, initials

    def matches(self, full_name, abbreviated_name):
        """
        Indica se o nome completo e o abreviado representam o mesmo autor.

        Levanta ValueError se algum dos nomes estiver vazio.
        """
        return InitialsMatch(
            matcher=self,
            full_name=full_name,
            abbreviated_name=abbreviated_name,
        ).matches()

    def expand(self, abbreviated_name, full_names):
        """
        Recebe um nome abreviado e uma lista de nomes completos
        candidatos e devolve o nome completo equivalente.

        Retorna None quando nenhum nome completo corresponde.
        """
        for full_name in full_names:
            if self.matches(full_name, abbreviated_name):
                return full_name
        return None


class InitialsMatch:
    """
    Objeto-metodo responsavel por comparar um nome completo com sua versao
    abreviada no formato "Sobrenome + Iniciais".
    """

    def __init__(self, matcher, full_name, abbreviated_name):
        self.matcher = matcher
        self.full_name = full_name
        self.abbreviated_name = abbreviated_name
        self.surname = None
        self.initials = None
        self.abbreviated_tokens = None

    def matches(self):
        if not self.full_name.strip() or not self.abbreviated_name.strip():
            raise ValueError("Os nomes nao podem ser vazios.")

        self.surname, self.initials = self.matcher._surname_and_initials(
            self.full_name
        )
        self.abbreviated_tokens = self.matcher._tokens(self.abbreviated_name)

        if self.surname not in self.abbreviated_tokens:
            return False

        abbreviated_initials = self._abbreviated_initials()

        return abbreviated_initials == self.initials

    def _abbreviated_initials(self):
        return "".join(
            token for token in self.abbreviated_tokens if token != self.surname
        )
