from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows #rows : horizont cell count -> size of row
        self.num_cols = num_cols #colums : vertical cell count -> size of column
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append( [ Cell(self.win) for i in range(self.num_rows) ] )
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell( i, j)


    ######
    # This method should calculate the x/y position of the Cell based on i, j, the cell_size,
    # and the x/y position of the Maze itself.
    # The x/y position of the maze represents how many pixels from the top
    # and left the maze should start from the side of the window.
    #####
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        pass
        cell = self._cells[i][j]

        # TODO:  calc x and y for cell, based i - row, j - col and cell_size
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)

        self._animate()

    ######
    # Once that's calculated, it should draw the cell and call the maze's _animate() method.
    # The animate method is what allows us to visualize what the algorithms are doing in real time.
    # It should simply call the window's redraw() method, then use time.sleep()
    # for a short amount of time so your eyes keep up with each render frame.
    # I slept for 0.05 seconds.
    ######
    def _animate(self):
        pass
        self.win.redraw()
        time.sleep(0.5)