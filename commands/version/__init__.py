from hep.util.manifest_dto import ManifestDTO


class Version:
    @staticmethod
    def version(manifest: ManifestDTO) -> str:
        return manifest.version
