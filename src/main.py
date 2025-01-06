from window import Window
from line import Line
from point import Point


def main():
    print("Hello, World!")
    window = Window(800, 600)

    line1 = Line(Point(30, 100), Point(500, 500))

    window.draw_line(line1)

    window.wait_for_close()


if __name__ == "__main__":
    main()