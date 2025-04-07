from hep.util.manifest_dto import ManifestDTO


class Repository:
    @staticmethod
    def repository(manifest: ManifestDTO) -> str:
        return "\n".join(
            [f"Repository: {manifest.repository}", f"Branch: {manifest.branch}"]
        )
