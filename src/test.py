import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[0][0].has_left_wall,
        )
        self.assertFalse(
            m1._cells[num_rows-1][num_cols-1].has_right_wall,
        )

    def text_maze_break_walls(self):
        num_rows = 10
        num_cols = 12
        seed = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed)
        m1.break_walls()


    def test_maze_reset_cells_visited(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertFalse(
                    m1._cells[i][j].visited,
                )


    # Always Last method for manual test
    # def test_maze_draw_cell(self):
    #     window = Window(900, 700) # for testing UI graphics look
    #     num_cols = 8
    #     num_rows = 6
    #     m1 = Maze(0, 0, num_rows, num_cols, 100, 100, window)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )

if __name__ == "__main__":
    unittest.main()