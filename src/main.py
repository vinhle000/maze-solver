from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    print("Hello, World!")
    window = Window(800, 600)

    line1 = Line(Point(30, 100), Point(500, 500))
    window.draw_line(line1)

    test_cell(window)

    window.wait_for_close()


def test_cell(window):
    cell1 = Cell(50, 50, 150, 150, window)
    cell2 = Cell(200, 50, 300, 150, window)
    cell3 = Cell(350, 50, 450, 150, window)
    cell4 = Cell(450, 50, 550, 150, window)

    cell1.remove_wall("left")
    cell2.remove_wall("right")
    cell3.remove_wall("top")
    cell4.remove_wall("bottom")

    cell1.enable_wall("left")
    cell2.enable_wall("right")
    cell3.enable_wall("top")
    cell4.enable_wall("bottom")

    cells = [cell1, cell2, cell3, cell4]

    for cell in cells:
        cell.draw()

if __name__ == "__main__":
    main()