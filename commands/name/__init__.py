from hep.util.manifest_dto import ManifestDTO


class Name:
    @staticmethod
    def name(manifest:ManifestDTO) -> str:
        return manifest.name