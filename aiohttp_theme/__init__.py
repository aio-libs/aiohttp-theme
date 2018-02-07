import os

from aiohttp_theme import _version as version


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def setup(app):
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('aiohttp_theme', theme_path)
    return {'version': version.__version__,
            'parallel_read_safe': True}
