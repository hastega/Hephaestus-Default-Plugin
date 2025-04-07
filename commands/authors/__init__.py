from hep.util.manifest_dto import ManifestDTO


class Authors:
    @staticmethod
    def authors(manifest:ManifestDTO) -> str:
        return str(manifest.authors)