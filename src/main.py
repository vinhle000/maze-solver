from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    window = Window(900, 700)
    test_maze_graphic(window)
    window.wait_for_close()

def test_maze_graphic(window):
    num_cols = 20
    num_rows = 20
    m1 = Maze(0, 0, num_rows, num_cols, 35, 35, window)
    m1.break_walls()
    m1.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()