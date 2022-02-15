from .generator import Generator
from .error import *


class Presets:
    easy = {"size_x": 10, "size_y": 8, "mines": 10}
    medium = {"size_x": 16, "size_y": 16, "mines": 40}
    hard = {"size_x": 25, "size_y": 20, "mines": 100}
    expert = {"size_x": 50, "size_y": 30, "mines": 200}


def generatePresetRaw(level=None, blank_id: str = ' ', mine_id: str = 'M'):
    """Quickly generate a grid using a preset and only return the raw 2D grid.

    Args:
        level (_type_, optional): Preset for grid generation. Defaults to None.
        blank_id (str, optional): An identifier for a blank cell in the grid. Defaults to ' '.
        mine_id (str, optional): An identifier for a mine in the grid. Defaults to 'M'.

    Raises:
        NoPresetGiven: No level preset was defined.

    Returns:
        list: The generated grid as a 2D list of [row, row, row, etc...]
    """
    if not level:
        raise NoPresetGiven('Expected level to be a variable from %s.Presets, got: %s' % (__name__, level))

    return Generator(size_x=level['size_x'], size_y=level['size_y'], blank_id=blank_id, mine_id=mine_id).generateRaw(level['mines'])


def generatePreset(level=None, blank_id: str = ' ', mine_id: str = 'M'):
    """Quickly generate a grid using a preset and return it in a GeneratedGrid object.

    Args:
        level (_type_, optional): Preset for grid generation. Defaults to None.
        blank_id (str, optional): An identifier for a blank cell in the grid. Defaults to ' '.
        mine_id (str, optional): An identifier for a mine in the grid. Defaults to 'M'.

    Raises:
        NoPresetGiven: No level preset was defined.

    Returns:
        GeneratedGrid: Generated grid parsed into a GeneratedGrid object.
    """
    if not level:
        raise NoPresetGiven('Expected level to be a variable from %s.Presets, got: %s' % (__name__, level))

    return Generator(size_x=level['size_x'], size_y=level['size_y'], blank_id=blank_id, mine_id=mine_id).generate(level['mines'])


generate_preset = generatePreset
generate_preset_raw = generatePresetRaw
