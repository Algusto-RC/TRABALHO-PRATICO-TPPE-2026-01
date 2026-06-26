class ParticleTokenMatcher:
    """
    Classe extraída de ParticleNormalizer para concentrar a regra de
    equivalência entre tokens no Caso 3.

    Um token da variante corresponde ao token completo quando:
    - ambos são exatamente iguais; ou
    - o token da variante é uma inicial do token completo.
    """

    def matches(self, full_token, variant_token):
        is_exact_match = full_token == variant_token
        is_initial_match = (
            len(variant_token) == 1
            and full_token.startswith(variant_token)
        )

        return is_exact_match or is_initial_match
