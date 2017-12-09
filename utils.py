import logging
from config import *

_LOGGER = None

def formatter(s):    
    return s.format(**GITHUB_CONFIG)

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

    fh = logging.FileHandler('log/github-cli.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    l.addHandler(sh)
    l.addHandler(fh)
    return l