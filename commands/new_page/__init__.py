from argparse import ArgumentParser


class NewPage:
    @staticmethod
    def newPage(hepParser: ArgumentParser):
        hepParser.add_argument("page", type=str, help="Page name")

        args = hepParser.parse_args()
        return f"[EXAMPLE] new page named {args.page}"