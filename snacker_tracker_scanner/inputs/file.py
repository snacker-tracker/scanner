class File:
    def __init__(self, path, **options):
        self.path = path
        self.options = options

    def events(self):
        with open(self.path, 'r') as fp:
            for row in fp.readlines():
                yield {
                    "code": row.strip()
                }
