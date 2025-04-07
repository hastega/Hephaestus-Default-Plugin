from argparse import ArgumentParser

from hep.util.manifest_dto import ManifestDTO
from hep.util.plugin import HepPlugin

from .commands import Authors, Description, Name, NewPage, Repository, Version
from .utils import CONSTANT_VALUE


class Example(HepPlugin):
    def __init__(self) -> None:
        self.manifest = ManifestDTO.from_path(__file__)

    def name(self, hepParser: ArgumentParser) -> None:
        print(Name.name(self.manifest))

    def description(self, hepParser: ArgumentParser) -> None:
        print(Description.description(self.manifest))

    def version(self, hepParser: ArgumentParser) -> None:
        print(Version.version(self.manifest))

    def authors(self, hepParser: ArgumentParser) -> None:
        print(Authors.authors(self.manifest))

    def repository(self, hepParser: ArgumentParser) -> None:
        print(Repository.repository(self.manifest))

    def new_page(self, hepParser: ArgumentParser) -> None:
        print(NewPage.newPage(hepParser=hepParser))
    
    def const(self, hepParser: ArgumentParser) -> None:
        print(CONSTANT_VALUE)
