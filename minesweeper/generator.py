from .error import *
from random import randint


class Generator:
    def __init__(
        self,
        size_x: int=12,
        size_y: int = 10,
        blank_id: str = ' ',
        mine_id: str = 'M'
    ):
        """Setup a new Generator instance.

        Args:
            size_x (int, optional): Number of columns to be generated. Defaults to 12.
            size_y (int, optional): Number of rows to be generated. Defaults to 10.
            blank_id (str, optional): An identifier for a blank cell in the grid. Defaults to ' '.
            mine_id (str, optional): An identifier for a mine in the grid. Defaults to 'M'.

        Raises:
            InvalidGridSize: Raised when an invalid grid size has been parsed into size_x or size_y.
        """
        self.size_x = size_x
        self.size_y = size_y
        self.blank_id = blank_id
        self.mine_id = mine_id
        
        if size_x < 1:
            raise InvalidGridSize('Expected size_x to be an int of value 1+, got: %s' % size_x)
        if size_y < 1:
            raise InvalidGridSize('Expected size_y to be an int of value 1+, got: %s' % size_y)
        
        # Aliases for functions (For old module funcion name support)
        self.check_near = self.checkNear
        self.generate_raw = self.generateRaw

    @staticmethod
    def checkNear(x: int, y: int, locations: list):
        """Check nearby mines of a defined X Y cell compared to a list of mine locations.

        Args:
            x (int): Column of cell to be checking from.
            y (int): Row of cell to be checking from.
            locations (list): List of mine locations to check from.

        Returns:
            int: Number of mines that are around the defined cell.
        """
        found = 0
        
        for p in [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]:
            if p in locations:
                found += 1
        
        return found

    def generateRaw(self, mines: int = 5):
        """Generate a grid and return just a 2D list.

        Args:
            mines (int, optional): Number of mines to be placed in this grid. Defaults to 5.

        Raises:
            InvalidMineCount: Raised if either a negative value of mines has been defined or the number of mines parsed is more than possible cells on the resulting grid.
            
        Returns:
            list: The generated grid as a 2D list of [row, row, row, etc...]
        """
        
        if mines < 0:
            raise InvalidMineCount('Expected mines to be an int of value 0+, got %s' % mines)
        if mines > (self.size_x * self.size_y):
            raise InvalidMineCount('Expected mines to be an int of max value %s (max grid size), got %s' % (self.size_x * self.size_y, mines))
        
        grid = []
        
        # Setup mine locations
        locations = []
        for _ in range(mines):
            # Simple loop to prevent dupe mines
            found = False
            while not found:
                pos = [randint(0, self.size_x - 1), randint(0, self.size_y - 1)]
                if pos not in locations:
                    locations.append(pos)
                    found = True

        # Generate grid
        for row in range(self.size_y):
            rowContent = []
            
            for column in range(self.size_x):
                # If the current cell is a mine location
                if [column, row] in locations:
                    rowContent.append(self.mine_id)
                else:
                    nearby = self.checkNear(column, row, locations)
                    rowContent.append(self.blank_id if nearby == 0 else '%s' % nearby)
            
            grid.append(rowContent)
        
        return grid

    def generate(self, mines: int = 5):
        """Generate a new grid and return a GeneratedGrid object containing the raw grid from generateRaw along with some other helpful functions/variables.

        Args:
            mines (int, optional): Number of mines to be placed in this grid. Defaults to 5.

        Raises:
            InvalidMineCount: Raised if either a negative value of mines has been defined or the number of mines parsed is more than possible cells on the resulting grid.

        Returns:
            GeneratedGrid: Generated grid parsed into a GeneratedGrid object.
        """
        
        return GeneratedGrid(grid=self.generate_raw(mines), mines=mines, generator=self)

    def config(self, size_x: int = None, size_y: int = None, blank_id: str = None, mine_id: str = None):
        """Config the setup for this generator.

        Args:
            size_x (int, optional): Number of columns to be generated. Defaults to None.
            size_y (int, optional): Number of rows to be generated. Defaults to None.
            blank_id (str, optional): An identifier for a blank cell in the grid. Defaults to None.
            mine_id (str, optional): An identifier for a mine in the grid. Defaults to None.
        
        Raises:
            InvalidGridSize: Raised when an invalid grid size has been parsed into size_x or size_y.
        """
        
        if size_x and size_x < 1:
            raise InvalidGridSize('Expected size_x to be an int of value 1+, got: %s' % size_x)
        if size_y and size_y < 1:
            raise InvalidGridSize('Expected size_y to be an int of value 1+, got: %s' % size_y)
        
        self.size_x = size_x if size_x else self.size_x
        self.size_y = size_y if size_y else self.size_y
        self.blank_id = blank_id if blank_id else self.blank_id
        self.mine_id = mine_id if mine_id else self.mine_id


class GeneratedGrid:
    def __init__(self, grid: list, mines: int, generator: Generator):
        """An object oriented response from a generated grid from Generator.generate instead of a JSON dict object.

        Args:
            grid (list): A generated minesweeper grid.
            mines (int): Number of mines that are in the generated grid.
            generator (Generator): Original generator that created this grid.
        """
        self.grid = grid
        self.generator = generator
        
        self.size_x = generator.size_x
        self.size_y = generator.size_y
        self.mines = mines
        self.blank_id = generator.blank_id
        self.mine_id = generator.mine_id

    def toJSON(self):
        """Returns important values from this object as a dict.

        Returns:
            dict: Object values formatted into a dict object.
        """
        
        return {
            'grid': self.grid,
            'generator': self.generator,
            'size_x': self.size_x,
            'size_y': self.size_y,
            'mines': self.mines,
            'blank_id': self.blank_id,
            'mine_id': self.mine_id,
        }
