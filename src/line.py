from point import Point


# The line class has a bit more logic in it.
# Its constructor should take 2 points as input,
# and save them as data members.

# draw() method
# The Line class needs a draw() method that takes a Canvas and a "fill color" as input. The fill_color will just be a string like "black" or "red".

# Next it should call the Canvas's create_line method.
#####################
class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas):
       fill_color = "black"

       canvas.create_line(
           self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2
       )