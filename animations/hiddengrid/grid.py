import manim as ma
from cell import CellType, GridCell


class HiddenGrid:
    def __init__(self, rows: int, cols: int, cell_size: int, animator: ma.Scene) -> None:
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.animator = animator

        self.grid = None
        self.start = None
        self.destination = None
        self._build()

    def set_start(self, row: int, col: int) -> "HiddenGrid":
        self.start = (row, col)
        self.grid[row][col].set_type(CellType.START)
        return self

    def set_destination(self, row: int, col: int) -> "HiddenGrid":
        self.destination = (row, col)
        self.grid[row][col].set_type(CellType.DESTINATION)
        return self

    def set_obstacles(self, coords: list[tuple[int, int]] | None = None) -> "HiddenGrid":
        if not coords:
            return self
        for row, col in coords:
            self.grid[row][col].set_type(CellType.OBSTACLE)
        return self

    def _build(self) -> None:
        grid = ma.VGroup()
        for r in range(self.rows):
            row = ma.VGroup()

            for c in range(self.cols):
                square = GridCell(row=r, col=c, side_length=self.cell_size)

                mv_x = (c - self.cols / 2 + 0.5) * self.cell_size
                mv_y = (self.rows / 2 - r - 0.5) * self.cell_size
                mv_z = 0

                square.move_to((mv_x, mv_y, mv_z))
                row.add(square)

            grid.add(row)
        self.grid = grid

    def get_grid(self):
        return self.grid
