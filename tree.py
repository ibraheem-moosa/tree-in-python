from pathlib import Path
from itertools import repeat


def not_last_prefix():
    yield '├── '
    yield from repeat('│   ')


def last_prefix():
    yield '└── '
    yield from repeat('    ')


def get_child_lines(child, prefix_generator):
    for line in tree(child):
        yield next(prefix_generator) + line


def tree(path):
    yield path.name
    if path.is_dir():
        children = path.iterdir()
        try:
            child = next(children)
        except StopIteration:
            # No child
            return
        try:
            while True:
                next_child = next(children)
                yield from get_child_lines(child, not_last_prefix())
                child = next_child
        except StopIteration:
            # Currently at last child
            yield from get_child_lines(child, last_prefix())


for line in tree(Path.cwd()):
    print(line)
