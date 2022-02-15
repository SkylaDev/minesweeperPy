minesweeperPy
=============

Release v\ |version|.

.. image:: https://pepy.tech/badge/minesweeperPy
    :target: https://pepy.tech/project/minesweeperPy

.. image:: https://img.shields.io/pypi/v/minesweeperPy.svg
    :target: https://pypi.org/project/minesweeperPy/

.. image:: https://img.shields.io/pypi/pyversions/minesweeperPy.svg
    :target: https://pypi.org/project/minesweeperPy/

.. image:: https://img.shields.io/pypi/l/minesweeperPy.svg
    :target: https://pypi.org/project/minesweeperPy/

A simple minesweeper generator for Python 3

-------------------

**Simple and easy to learn usage**

.. code-block:: python

    import minesweeper

    # Create a generator that can generate 10x10 grids
    generator = minesweeper.Generator(size_x=10, size_y=10)

    # Generate a new Minesweeper game using our generator, make it also place 25 mines on the grid.
    grid = generator.generate(mines=25)

    # Print out the new grid
    print(grid.grid)


Overview
--------
.. toctree::
    :maxdepth: 2

    reference/index.rst
    releasenotes/index.rst


Installation
------------

Install with pip
^^^^^^^^^^^^^^^^
::

    $ pip install minesweeperPy

Update with pip
^^^^^^^^^^^^^^^
::

    $ pip install minesweeperPy --upgrade

Install from source
^^^^^^^^^^^^^^^^^^^
::

    $ python setup.py install


Support
-------
If you encounter any problems with minesweeperPy please let me know via `the GitHub issue tracker <https://github.com/stshrewsburyDev/minesweeperPy/issues>`_.


Some useful links
-----------------

- Issue tracker: https://github.com/stshrewsburyDev/minesweeperPy/issues
- Source code: https://github.com/stshrewsburyDev/minesweeperPy


License
-------

This project is licensed under the MIT license.
