from pathlib import Path
from itertools import repeat

def prefix():
    yield '├──'
    yield from repeat('│  ')

def tree(path):
    yield path.name
    if path.is_dir():
        children = path.iterdir()
        for child in children:
            prefix_generator = prefix()
            for line in tree(child):
                yield next(prefix_generator) + line


for line in tree(Path.cwd()):
    print(line)
