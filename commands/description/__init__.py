from hep.util.manifest_dto import ManifestDTO


class Description:
    @staticmethod
    def description(manifest:ManifestDTO) -> str:
        return manifest.description