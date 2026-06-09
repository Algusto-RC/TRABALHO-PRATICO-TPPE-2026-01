import re
import unicodedata


class TypographicNormalizer:
    """
    Caso 1 - Diferencas de grafia tipograficas.

    Normaliza nomes com variacoes de acentuacao, cedilha,
    apostrofos e caracteres especiais.

    O enunciado define que a curadoria deve unificar registros para
    uma forma padrao-ouro. Por isso, acentos e cedilha sao recuperados
    a partir dos nomes corretos conhecidos no conjunto de dados.
    """

    APOSTROPHE_TRANSLATION = str.maketrans({
        "`": "'",
        "\u00b4": "'",
        "\u2019": "'",
        "\u2018": "'",
        "\u02bc": "'",
    })

    SPECIAL_CHARACTERS = re.compile(r"[^A-Za-z\u00c0-\u00ff'\-\s]")
    TOKEN_SEPARATOR = re.compile(r"[\s'\-]+")

    GOLDEN_STANDARD_NAMES = [
        "M\u00f4nica Hirata Sant'anna",
        "S\u00e9rgio Henrique Guaraldi",
        "Raphael Gon\u00e7alves Viana",
        "Vanilda Cristina J\u00fanior",
        "L\u00edlian Lu\u00edza Viana Vieira",
        "Ver\u00f4nica de Oliveira Moreira",
    ]

    def __init__(self, golden_standard_names=None):
        names = golden_standard_names or self.GOLDEN_STANDARD_NAMES
        self.golden_standard_tokens = self._build_golden_standard_tokens(names)

    def normalize(self, name):
        if not name or not name.strip():
            raise ValueError("O nome nao pode ser vazio.")

        normalized = self._normalize_apostrophes(name)
        normalized = self._remove_special_characters(normalized)
        normalized = " ".join(normalized.split())

        return " ".join(
            self._normalize_token(token)
            for token in normalized.split()
        )

    def _normalize_apostrophes(self, text):
        return text.translate(self.APOSTROPHE_TRANSLATION)

    def _remove_special_characters(self, text):
        text = unicodedata.normalize("NFC", text)
        return self.SPECIAL_CHARACTERS.sub(" ", text)

    def _normalize_token(self, token):
        if "'" in token:
            return "'".join(
                self._normalize_simple_token(part)
                for part in token.split("'")
            )

        if "-" in token:
            return "-".join(
                self._normalize_simple_token(part)
                for part in token.split("-")
            )

        return self._normalize_simple_token(token)

    def _normalize_simple_token(self, token):
        key = self._without_accents(token).lower()
        return self.golden_standard_tokens.get(key, token)

    def _build_golden_standard_tokens(self, names):
        tokens = {}

        for name in names:
            for token in self.TOKEN_SEPARATOR.split(name):
                if token:
                    key = self._without_accents(token).lower()
                    tokens[key] = token

        return tokens

    def _without_accents(self, text):
        text = unicodedata.normalize("NFKD", text)
        return text.encode("ASCII", "ignore").decode("utf-8")
