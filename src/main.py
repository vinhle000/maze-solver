from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    print("Hello, World!")
    window = Window(800, 600)

    # test Line
    # line1 = Line(Point(30, 100), Point(500, 500))
    # window.draw_line(line1)

    # test_cell(window)
    test_maze_graphic()

    window.wait_for_close()

def test_maze_graphic():
    window = Window(800, 600)
    num_cols = 8
    num_rows = 6
    m1 = Maze(0, 0, num_rows, num_cols, 100, 100, window)
    m1.break_walls()
    window.wait_for_close()

def test_cell(window):
    cell1 = Cell(window)
    cell1.has_left_wall = False
    cell1.draw(50, 50, 150, 150)
    cell2 = Cell(window)
    cell2.draw(200, 50, 300, 150)
    cell3 = Cell(window)
    cell3.draw(350, 50, 450, 150)
    cell4 = Cell(window)
    cell4.draw(450, 50, 550, 150)




    # vertical cells
    cell5 = Cell(window)
    cell5.draw(50, 150, 150, 250)
    cell6 = Cell(window)
    cell6.draw(50, 500, 150, 650)


    cells = [cell1, cell2, cell3, cell4, cell5, cell6]



    cell1.draw_move(cell2)
    cell4.draw_move(cell3)
    cell5.draw_move(cell6, True)

if __name__ == "__main__":
    main()