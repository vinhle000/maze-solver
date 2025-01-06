from point import Point
from line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            left_wall_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            left_wall_line.draw(self._win.canvas)

        if self.has_right_wall:
            right_wall_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            right_wall_line.draw(self._win.canvas)

        if self.has_top_wall:
            top_wall_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_wall_line.draw(self._win.canvas)

        if self.has_bottom_wall:
            bottom_wall_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bottom_wall_line.draw(self._win.canvas)

    #  To set a Window object as input and save it as a data member.
    def set_window(self, win):
        self._win = win
        self.draw()

    def remove_wall(self, wall):
        if wall == "left":
            self.has_left_wall = False
        elif wall == "right":
            self.has_right_wall = False
        elif wall == "top":
            self.has_top_wall = False
        elif wall == "bottom":
            self.has_bottom_wall = False
        self.draw()

    def enable_wall(self, wall):
        if wall == "left":
            self.has_left_wall = True
        elif wall == "right":
            self.has_right_wall = True
        elif wall == "top":
            self.has_top_wall = True
        elif wall == "bottom":
            self.has_bottom_wall = True
        self.draw()