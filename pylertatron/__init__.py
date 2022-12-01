"""
Pylertatron is a Python library for sending alerts to Alertatron.
"""
from .alert import Alert
import async_
from .commands import *
import sync

__version__ = "1.0.0"
__all__ = ['async_', 'sync', 'commands', 'alert']
