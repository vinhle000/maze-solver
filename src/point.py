

# Point class
# Let's make a little Point class. It should simply store 2 public data members:

# x - the x-coordinate (horizontal) in pixels of the point
# y - the y-coordinate (vertical) in pixels of the point
# x=0 is the left of the screen.

# y=0 is the top of the screen.
####################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
