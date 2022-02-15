The generator module
====================

The generator module is the heart of the minesweeperPy module.
It contains all the required code for grid generation.


Generator class
---------------

.. py:class:: Generator(size_x=12, size_y=10, blank_id=' ', mine_id='M')

    Creates a generator object that can be used to generate minesweeper grids based off its configuration.

    :param int size_x: Number of columns to be generated.
    :param int size_y: Number of rows to be generated.
    :param str blank_id: An identifier for a blank cell in the grid.
    :param str mine_id: An identifier for a mine in the grid.

    :raises: :py:exc:`InvalidGridSize()` if the defined `size_x` or `size_y` args have a negative number parsed.

Methods
^^^^^^^

.. py:method:: Generator.generateRaw(mines=5)

    Generate a new minesweeper grid and return just the grid in the form of a 2D list object.

    :param int mines: Number of mines to be placed in this grid.

    :raises: :py:exc:`InvalidMineCount()` if the mine count is either under 0 or to many for the grid.

    :returns: A generated grid in a list object in the format `[row, row, row, etc...]`
    :rtype: list

.. py:method:: Generator.generate(mines=5)

    Generate a new minesweeper grid and return the grid along with some other useful info in a :py:class:`GeneratedGrid()` object.

    :param int mines: Number of mines to be placed in this grid.

    :raises: :py:exc:`InvalidMineCount()` if the mine count is either under 0 or to many for the grid.

    :returns: A :py:class:`GeneratedGrid()` object containing the grid along with some helpful information, to get a legacy dict output please refer to :py:meth:`GeneratedGrid.toJSON()`.
    :rtype: :py:class:`GeneratedGrid()`

.. py:method:: Generator.config(size_x, size_y, blank_id, mine_id)

    Configure the setup for this generator.

    :param int size_x: Number of columns to be generated.
    :param int size_y: Number of rows to be generated.
    :param str blank_id: An identifier for a blank cell in the grid.
    :param str mine_id: An identifier for a mine in the grid.

    :raises: :py:exc:`InvalidGridSize()` if the defined `size_x` or `size_y` args have a negative number parsed.


Generated grid class
--------------------

New in 2.1 :py:meth:`Generator.generate()` will now return a :py:class:`GeneratedGrid()` object instead of a dict.

.. py:class:: GeneratedGrid(grid, mines, generator)

    An object oriented response from a generated grid from :py:meth:`Generator.generate()` instead of a JSON dict object.

    :param list grid: A generated minesweeper grid.
    :param int mines: Number of mines that are in the generated grid.
    :param Generator generator: Original generator that created this grid.

Methods
^^^^^^^

.. py:method:: GeneratedGrid.toJSON()

    Returns important values from this object as a dict.
    Can be used to get a similar output from legacy versions of minesweeperPy.

    .. code-block::

        {
            'grid': [row, row, row, etc...],
            'generator': <minesweeper.generator.Generator object at 0x...>,
            'size_x': 12,
            'size_y': 10,
            'mines': 5,
            'blank_id': ' ',
            'mine_id': 'M',
        }

    :returns: A dict object of the values from this object.
    :rtype: dict
