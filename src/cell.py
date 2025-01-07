from point import Point
from line import Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "grey"
        if undo:
            fill_color = "red" #  For backtracking

         # self cell coordinates (center)
        start_x = (self._x2 + self._x1) / 2
        start_y = (self._y2 + self._y1) / 2
        start_point = Point(start_x, start_y)

        # to_cell coordinates (center)
        end_x = (to_cell._x2 + to_cell._x1) / 2
        end_y = (to_cell._y2 + to_cell._y1) / 2
        end_point = Point(end_x, end_y)
        move_line = Line(start_point, end_point)
        move_line.draw(self._win.canvas, fill_color)


    def set_wall(self, wall_dir, has_wall=True):
        if wall_dir == "left":
            self.has_left_wall = has_wall
        elif wall_dir == "right":
            self.has_right_wall = has_wall
        elif wall_dir == "top":
            self.has_top_wall = has_wall
        elif wall_dir == "bottom":
            self.has_bottom_wall = has_wall

    def has_wall(self, wall_dir):
        if wall_dir == "left":
            return self.has_left_wall
        elif wall_dir == "right":
            return self.has_right_wall
        elif wall_dir == "top":
            return self.has_top_wall
        elif wall_dir == "bottom":
            return self.has_bottom_wall
        return False