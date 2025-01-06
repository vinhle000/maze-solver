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



    def _draw_cell(self, i, j):
        if self.win is None:
            return
        pass
        cell = self._cells[i][j]

        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        pass
        self.win.redraw()
        time.sleep(0.5)


    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_left_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)