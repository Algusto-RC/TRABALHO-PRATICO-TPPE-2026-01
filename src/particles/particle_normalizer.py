import unicodedata

class ParticleNormalizer:
    """
    Caso 3 - Partículas 'de' e uso de ponto nas abreviações opcionais.

    Identifica a equivalência entre um nome completo e suas variações
    que omitem partículas de ligação (de, da, do, etc.) ou abreviam
    nomes intermediários com ou sem ponto.
    """

    PARTICLES = {"de", "da", "do", "dos", "das", "e"}

    def _normalize_and_tokenize(self, text):
        """Remove acentos, pontos, converte para minúsculas e remove partículas."""
        if not text or not text.strip():
            raise ValueError("O nome nao pode ser vazio.")

        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ASCII", "ignore").decode("utf-8").lower()
        text = text.replace(".", " ")
        
        tokens = text.split()
        return [t for t in tokens if t not in self.PARTICLES]

    def _tokens_match(self, full_token, variant_token):
        is_exact_match = full_token == variant_token
        is_initial_match = (
            len(variant_token) == 1
            and full_token.startswith(variant_token)
        )

        return is_exact_match or is_initial_match

    def matches(self, full_name, variant_name):
        """
        Indica se o nome completo e a variante (com abreviações intermediárias
        ou oclusão de partículas) representam o mesmo autor.
        """
        full_tokens = self._normalize_and_tokenize(full_name)
        variant_tokens = self._normalize_and_tokenize(variant_name)

        if len(full_tokens) != len(variant_tokens):
            return False

        for full_tok, var_tok in zip(full_tokens, variant_tokens):
            if not self._tokens_match(full_tok, var_tok):
                return False

        return True

    def expand(self, variant_name, full_names):
        """
        Devolve o nome completo correspondente à variante fornecida,
        ou None se não houver correspondência.
        """
        for full_name in full_names:
            if self.matches(full_name, variant_name):
                return full_name
        return None
