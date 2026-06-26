import unicodedata

from src.particles.particle_token_matcher import ParticleTokenMatcher


class ParticleNormalizer:
    """
    Caso 3 - Partículas 'de' e uso de ponto nas abreviações opcionais.

    Identifica a equivalência entre um nome completo e suas variações
    que omitem partículas de ligação (de, da, do, etc.) ou abreviam
    nomes intermediários com ou sem ponto.
    """

    PARTICLES = {"de", "da", "do", "dos", "das", "e"}

    def __init__(self, token_matcher=None):
        self.token_matcher = token_matcher or ParticleTokenMatcher()

    def _normalize_and_tokenize(self, text):
        """Remove acentos, pontos, converte para minúsculas e remove partículas."""
        if not text or not text.strip():
            raise ValueError("O nome nao pode ser vazio.")

        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ASCII", "ignore").decode("utf-8").lower()
        text = text.replace(".", " ")

        tokens = text.split()
        return [t for t in tokens if t not in self.PARTICLES]

    def matches(self, full_name, variant_name):
        """
        Indica se o nome completo e a variante (com abreviações intermediárias
        ou ocultação de partículas) representam o mesmo autor.
        """
        full_tokens = self._normalize_and_tokenize(full_name)
        variant_tokens = self._normalize_and_tokenize(variant_name)

        if len(full_tokens) != len(variant_tokens):
            return False

        return all(
            self.token_matcher.matches(full_tok, var_tok)
            for full_tok, var_tok in zip(full_tokens, variant_tokens)
        )

    def expand(self, variant_name, full_names):
        """
        Devolve o nome completo correspondente à variante fornecida,
        ou None se não houver correspondência.
        """
        for full_name in full_names:
            if self.matches(full_name, variant_name):
                return full_name
        return None
