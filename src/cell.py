from point import Point
from line import Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "grey" #  For backtracking

        # self cell coordinates
        x = (self._x2 - self._x1)/2 + self._x1
        y = (self._y2 - self._y1)/2 + self._y1
        start_point = Point(x, y)

        # to_cell coordinates
        x = (to_cell._x2 - to_cell._x1)/2  + to_cell._x1
        y = (to_cell._y2 - to_cell._y1)/2 + to_cell._y1
        end_point = Point(x,y)

        move_line = Line(start_point, end_point)
        move_line.draw(self._win.canvas, fill_color)


    # #  Access to set a Window object as input and save it as a data member.
    # def set_window(self, win):
    #     self._win = win


    # def remove_wall(self, wall):
    #     if wall == "left":
    #         self.has_left_wall = False
    #     elif wall == "right":
    #         self.has_right_wall = False
    #     elif wall == "top":
    #         self.has_top_wall = False
    #     elif wall == "bottom":
    #         self.has_bottom_wall = False


    # def enable_wall(self, wall):
    #     if wall == "left":
    #         self.has_left_wall = True
    #     elif wall == "right":
    #         self.has_right_wall = True
    #     elif wall == "top":
    #         self.has_top_wall = True
    #     elif wall == "bottom":
    #         self.has_bottom_wall = True
