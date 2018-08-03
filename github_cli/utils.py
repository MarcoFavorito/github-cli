import logging

from github_cli.base.Path import Path

_LOGGER = None

def get_logger()->logging.Logger:
    global _LOGGER
    if not _LOGGER:
        _LOGGER = _init_logger()
    return _LOGGER


def _init_logger():
    l = logging.getLogger("github-cli")
    l.setLevel(logging.INFO)

    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(fmt)

    fh = logging.FileHandler('github-cli.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    l.addHandler(sh)
    l.addHandler(fh)
    return l


def _extract_absolute_path(input_path, context_path):
    if input_path is None:
        absolute_path = context_path
    else:
        input_path = Path(input_path)
        absolute_path = input_path if input_path.is_absolute() else _make_full_path(context_path, input_path)

    return absolute_path


def _make_full_path(context, path):
    if path.is_absolute():
        actual_path = path
    else:
        separator = "/" if not context.is_root() else ""
        actual_path = Path(str(context) + separator + str(path))

    return actual_path