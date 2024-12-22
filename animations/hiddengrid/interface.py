import manim as ma
from cell import CellType, GridCell
from grid import HiddenGrid
from movements import Moves


class GridInterface:
    def __init__(self, hidden_grid: HiddenGrid, animator: ma.Scene) -> None:

        self.animator = animator
        self.hidden_grid = hidden_grid
        self.grid = hidden_grid.get_grid()

        self.start_cell = self.hidden_grid.start
        self.start_row, self.start_col = self.start_cell
        self.curr_cell = self.grid[self.start_row][self.start_col]
        self.destination_cell = None

        self.pointer = ma.Dot(radius=self.curr_cell.width / 4)
        self.pointer.set_fill(color=ma.GREEN_B)
        self.pointer.set_stroke(color=ma.WHITE, width=2)
        self.pointer.move_to(self.curr_cell.get_center())
        self.animator.play(ma.FadeIn(self.pointer), run_time=1)

    def move(self, moves: Moves) -> bool:

        row, col = self.curr_cell.get_coords()
        delta_row, delta_col = moves.value

        new_row = row + delta_row
        new_col = col + delta_col

        if (
            0 <= new_row < self.hidden_grid.rows
            and 0 <= new_col < self.hidden_grid.cols
            and self.grid[new_row][new_col].get_type() != CellType.OBSTACLE
        ):
            new_cell = self.grid[new_row][new_col]
            movement = self.pointer.animate.move_to(new_cell.get_center())

            self.animator.play(movement, run_time=0.1)
            new_cell.set_discovered(self.animator)

            self.curr_cell = new_cell

            return True
        return False

    @property
    def is_destination(self) -> bool:
        return self.curr == self.grid.destination

    def get_current_cell(self) -> GridCell:
        return self.curr_cell

    def get_start_cell(self) -> GridCell | None:
        return self.start_cell
