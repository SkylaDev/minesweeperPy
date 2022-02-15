"""
minesweeperPy
A simple minesweeper grid generator for Python 3

Version 2.1
"""


__title__ = 'minesweeperPy'
__author__ = 'stshrewsburyDev'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2019-present stshrewsburyDev'
__version__ = '2.1'
__URL__ = 'https://github.com/stshrewsburyDev/minesweeperPy'


from .generator import Generator
from .error import *
from .preset import Presets, generatePreset, generate_preset, generatePresetRaw, generate_preset_raw
