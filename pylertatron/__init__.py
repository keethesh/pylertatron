"""
Pylertatron is a Python library for sending alerts to Alertatron.
"""
from . import async_
from . import sync
from .alert import Alert
from .commands import *

__version__ = "1.0.0"
__all__ = ['async_', 'sync', 'commands', 'alert']
