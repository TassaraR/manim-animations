import manim as ma
from grid import HiddenGrid
from interface import GridInterface
from traversal import PathDiscoverer, ShortestPathFinder


class HiddenGridAnimation(ma.Scene):
    def construct(self):

        start = (1, 1)
        start = (0, 10)
        dest = (7, 9)
        rows = 14
        cols = 14
        cell_size = 0.4
        # fmt: off
        stoppers = [
            (0, 7), (0, 9),
            (1, 2), (1, 4), (1, 9), (1, 10), (1, 11), (1, 12),
            (2, 1), (2, 4), (2, 4), (2, 7), (2, 10), (2, 11),
            (3, 1), (3, 7),
            (4, 6), (4, 7), (4, 11), (4, 12), (4, 13),
            (5, 3), (5, 4), (5, 5), (5, 6), (5, 11),
            (6, 2), (6, 3), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12),
            (7, 1), (7, 2), (7, 7), (7, 8), (7, 12),
            (8, 4), (8, 7), (8, 8), (8, 9), (8, 10), (8, 12),
            (9, 3), (9, 8), (9, 9),
            (10, 1), (10, 3), (10, 8), (10, 11), (10, 12),
            (11, 1), (11, 2), (11, 3), (11, 7), (11, 8), (11, 11),
            (12, 1), (12, 2), (12, 3), (12, 6), (12, 7),
            (13, 3), (13, 10), (13, 11), (13, 12)
        ]
        # fmt: on

        hidden_grid = (
            HiddenGrid(rows=rows, cols=cols, cell_size=cell_size, animator=self)
            .set_start(*start)
            .set_destination(*dest)
            .set_stoppers(coords=stoppers)
        )

        interface = GridInterface(hidden_grid=hidden_grid, animator=self)
        discoverer = PathDiscoverer(interface=interface, animator=self)
        pathfinder = ShortestPathFinder(discoverer=discoverer, animator=self)

        self.wait(1)
        discoverer.traverse()
        pathfinder.traverse()
        pathfinder.build_path()
        self.wait(4)
