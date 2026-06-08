class AuthorIdResolver:
    """Unifica os IDs de registros que pertencem ao mesmo autor."""

    def resolve(self, records):
        canonical_ids = {}

        for record in records:
            author_name = record["name"]
            author_id = record["id"]

            if (
                author_name not in canonical_ids
                or author_id < canonical_ids[author_name]
            ):
                canonical_ids[author_name] = author_id

        return [
            {
                **record,
                "id": canonical_ids[record["name"]],
            }
            for record in records
        ]
