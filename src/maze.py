from cell import Cell
import time
import random

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
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows  # Number of vertical cells (rows)
        self.num_cols = num_cols  # Number of horizontal cells (columns)
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win


        # providing a fixed seed, say 0,
        # is that it will ensure you always get the same "random" numbers.
        if seed is not None:
            random.seed(seed)

        self.seed = seed
        self._create_cells()

    def _create_cells(self):
       # Create grid using standard (row, column) indexing
        self._cells = []
        for row in range(self.num_rows):
            self._cells.append([Cell(self.win) for col in range(self.num_cols)])

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)


    def _draw_cell(self, i, j):
        if self.win is None:
            return
        pass
        cell = self._cells[i][j]

        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        pass
        self.win.redraw()
        time.sleep(0.01)


    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_left_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[self.num_rows- 1][self.num_cols - 1]
        exit_cell.has_right_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)


    def break_walls(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _break_walls_r(self, i, j): # Depth First Search
        cell = self._cells[i][j]
        cell.visited = True

        # next directions are stored as
        # (next_i, next_j, curr_wall, next_wall)
        while True:
            next_directions = []
            if self._is_in_bounds(i, j - 1):
                left = self._cells[i][j - 1]
                if not left.visited:
                    next_directions.append((i, j-1, 'left', 'right', 'LEFT'))

            if self._is_in_bounds(i - 1, j):
                top = self._cells[i - 1][j]
                if not top.visited:
                    next_directions.append((i - 1, j, 'top', 'bottom', 'TOP'))

            if self._is_in_bounds(i, j + 1):
                right = self._cells[i][ j+1]
                if not right.visited:
                    next_directions.append((i, j + 1, 'right', 'left', 'RIGHT'))

            if self._is_in_bounds(i + 1, j):
                bottom = self._cells[i +1][j]
                if not bottom.visited:
                    next_directions.append((i +1, j, 'bottom', 'top', 'BOTTOM'))


            if len(next_directions) == 0:
                self._draw_cell(i, j)
                return
            else:
                num = random.randrange(0, len(next_directions))
                next_i, next_j, curr_wall, next_wall, direction = next_directions[num]
                # print(f"breaking wall between ({i}, {j}) and ({next_i}, {next_j})")
                # print(f"moving to {direction} .>>>> curr_wall: {curr_wall} ||| next_wall: {next_wall}")
                # print("")
                self._cells[i][j].set_wall(curr_wall, False)
                self._cells[next_i][next_j].set_wall(next_wall, False)
                self._break_walls_r(next_i, next_j)



    def _reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._cells[row][col].visited = False

    # Valid cell - in bounds
    # i - row index (vertical, 0 to self.num_rows - 1)
    # j - column index (horizontal, 0 to self.num_cols - 1)
    def _is_in_bounds(self, i, j):
        return 0 <= i < self.num_rows and 0 <= j < self.num_cols


    def check_winning_cell(self, i, j):

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

    def solve(self):
       return self._solve_r(0, 0)

    # [ ]] It returns False  -> if the current cell is a loser cell.
    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True

    # [ ] return True  -> if the current cell is an end cell, OR if it leads to the end cell.
        if self.check_winning_cell(i, j):
            return True


        # left path
        # [ ] a cell in that direction,
        if self._is_in_bounds(i , j - 1):
            left = self._cells[i][j-1]
            if not cell.has_wall('left') and not left.has_wall('right') and not left.visited:

                print('')
                print("Move LEFT")
                print(f"Current cell: (row{i}, col{j}) ||| Next cell: (row{i}, col{j-1})")
                cell.draw_move(left)
                if self._solve_r(i, j-1):
                    return True
                print('')
                print("Undo LEFT")
                cell.draw_move(left, True) # undo as red color

        # top path
        if self._is_in_bounds(i-1, j):
            top = self._cells[i-1][j]
            if not cell.has_wall('top') and not top.has_wall('bottom') and not top.visited:

                print('')
                print("Move TOP")
                print(f"Current cell: (row{i}, col{j}) ||| Next cell: (row{i-1}, col{j})")
                cell.draw_move(top)
                if self._solve_r(i-1, j):
                    return True
                else:
                    print('')
                    print("Undo TOP")
                    cell.draw_move(top, True) # undo as red color


        # right path
        if self._is_in_bounds(i , j + 1):
            right = self._cells[i][j+1]
            if not cell.has_wall('right') and not right.has_wall('left') and not right.visited:
                print('')
                print("Move RIGHT")
                print(f"Current cell: (row{i}, col{j}) ||| Next cell: (row{i}, col{j+1})")
                cell.draw_move(right)
                if self._solve_r(i, j+1):
                    return True
                else:
                    print('')
                    print("Undo RIGHT")
                    cell.draw_move(right, True) # undo as red color


        # bottom path
        if self._is_in_bounds(i+1 , j):
            bottom = self._cells[i+1][j]
            if not cell.has_wall('bottom') and not bottom.has_wall('top') and not bottom.visited:
                print('')
                print("Move BOTTOM")
                print(f"Current cell: (row{i}, col{j}) ||| Next cell: (row{i+1}, col{j})")
                cell.draw_move(bottom)
                if self._solve_r(i+1, j):
                    return True
                else:
                    print('')
                    print("Undo BOTTOM")
                    cell.draw_move(bottom, True) # undo as red color
        else:
            return False
