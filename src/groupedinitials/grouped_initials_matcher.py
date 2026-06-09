import unicodedata


class GroupedInitialsMatcher:

    def normalize(self, text):
        """
        Remove acentos e converte para lowercase.
        """

        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ASCII", "ignore").decode("utf-8")

        return text.lower()

    def extract_initials_without_surname(self, full_name):

        parts = full_name.split()

        initials = ""

        for part in parts[:-1]:
            initials += part[0].upper()

        return initials


    def extract_initials_with_surname(self, full_name):

        parts = full_name.split()

        initials = ""

        for part in parts:
            initials += part[0].upper()

        return initials


    def expand(self, abbreviated_name, full_names):
        """
        Expande nomes abreviados como:
        SH Guaraldi -> Sérgio Henrique Guaraldi
        """

        abbreviated_parts = abbreviated_name.split()

        grouped_initials = abbreviated_parts[0].upper()
        surname = self.normalize(abbreviated_parts[-1])

        for full_name in full_names:

            parts = full_name.split()

            full_surname = self.normalize(parts[-1])


            initials_without_surname = (
                self.extract_initials_without_surname(full_name)
            )

            initials_with_surname = (
                self.extract_initials_with_surname(full_name)
            )

            if (
                (
                    initials_without_surname == grouped_initials
                    or initials_with_surname == grouped_initials
                )
                and full_surname == surname
            ):
                return full_name

