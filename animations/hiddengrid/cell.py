from enum import StrEnum

import manim as ma


class CellType(StrEnum):
    OBSTACLE = "obstacle"
    EMPTY = "empty"
    START = "start"
    DESTINATION = "destination"


class CellStatus(StrEnum):
    UNSEEN = "unseen"
    VISITED = "visited"
    DISCOVERED = "discovered"


class GridCell(ma.Square):
    def __init__(self, row: int, col: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.row = row
        self.col = col

        self.type = CellType.EMPTY
        self.status = CellStatus.UNSEEN

    def set_visited(self, animator: ma.Scene) -> "GridCell":
        self.status = CellStatus.VISITED

        if self.type not in (CellType.START, CellType.DESTINATION):
            fill = self.set_fill(ma.BLUE_B, opacity=0.4)
            animator.play(ma.FadeIn(fill), run_time=0.1)

        return self

    def set_discovered(self, animator: ma.Scene) -> "GridCell":
        if self.status == CellStatus.UNSEEN:

            if self.type == CellType.START:
                type_color = ma.GREEN
                type_opacity = 1
            elif self.type == CellType.DESTINATION:
                type_color = ma.RED
                type_opacity = 1
            else:
                type_color = ma.WHITE
                type_opacity = 0.1

            self.status = CellStatus.DISCOVERED
            self.set_stroke(ma.WHITE, opacity=1)
            self.set_fill(type_color, opacity=type_opacity)
            animator.bring_to_back(self)
            animator.play(ma.GrowFromCenter(self), run_time=0.1)
        return self

    def set_type(self, _type: CellType) -> "GridCell":
        self.type = _type
        return self

    def get_coords(self) -> tuple[int, int]:
        return (self.row, self.col)

    def get_type(self) -> CellType:
        return self.type

    @property
    def is_destination(self) -> bool:
        return self.type == CellType.DESTINATION
