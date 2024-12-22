from collections import defaultdict, deque

import manim as ma
from grid import CellType, GridCell
from interface import GridInterface
from movements import Moves, OppositeMoves


class PathDiscoverer:
    def __init__(self, interface: GridInterface, animator: ma.Scene):
        self.discovered = defaultdict(GridCell)
        self.destination = None
        self.interface = interface
        self.animator = animator

    def traverse(self, row: int = 0, col: int = 0) -> None:

        cell = self.interface.curr_cell

        self.discovered[(row, col)] = cell
        cell.set_discovered(self.animator)

        if cell.is_destination:
            self.destination = (row, col)

        for move in Moves:
            delta_row, delta_col = move.value

            new_row = row + delta_row
            new_col = col + delta_col

            if (new_row, new_col) not in self.discovered and self.interface.move(move):

                self.traverse(new_row, new_col)
                opposite_move = getattr(OppositeMoves, move.name).value
                self.interface.move(opposite_move)


class ShortestPathFinder:
    def __init__(self, discoverer: PathDiscoverer, animator: ma.Scene) -> None:

        self.discoverer = discoverer
        self.discovered = self.discoverer.discovered
        self.animator = animator
        self.queue = deque()
        self.seen = set()
        self.path = None

    def traverse(self) -> None:

        start_cell = self.discovered[(0, 0)]

        self.queue.append((0, 0, start_cell, [start_cell]))
        self.seen.add((0, 0))
        start_cell.set_visited(self.animator)

        while self.queue:

            row, col, cell, path = self.queue.popleft()

            if cell.type == CellType.DESTINATION:
                self.path = path
                return

            for move in Moves:

                delta_row, delta_col = move.value
                new_row = row + delta_row
                new_col = col + delta_col

                if (new_row, new_col) in self.discovered and (new_row, new_col) not in self.seen:

                    new_cell = self.discovered[(new_row, new_col)]

                    candidate = (new_row, new_col, new_cell, path + [new_cell])
                    self.queue.append(candidate)
                    self.seen.add((new_row, new_col))
                    new_cell.set_visited(self.animator)

    def build_path(self) -> None:

        if not self.path:
            return

        pointer = ma.Dot(radius=self.path[0].width / 4)
        pointer.set_fill(ma.RED, opacity=1)
        pointer.set_stroke(ma.WHITE, opacity=1, width=2)

        path = [cell.get_center() for cell in self.path]
        full_path = ma.VMobject().set_color(ma.WHITE)
        full_path.set_points_as_corners(path)

        drawn_path = ma.VMobject().set_color(ma.ORANGE)

        self.animator.add(drawn_path, pointer)

        tracker = ma.ValueTracker(0)

        def line_updater(mob: ma.VMobject):
            mob.pointwise_become_partial(full_path, 0, tracker.get_value())

        drawn_path.add_updater(line_updater)

        self.animator.play(tracker.animate.set_value(1), ma.MoveAlongPath(pointer, full_path))
