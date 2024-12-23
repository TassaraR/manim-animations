import manim as ma
from grid import HiddenGrid
from interface import GridInterface
from traversal import PathDiscoverer, ShortestPathFinder
from utils import load_config


class HiddenGridAnimation(ma.Scene):
    def construct(self):
        cfg = load_config(__file__, "config.toml")

        hidden_grid = (
            HiddenGrid(
                rows=cfg["rows"], cols=cfg["cols"], cell_size=cfg["cell_size"], animator=self
            )
            .set_start(*cfg["start"])
            .set_destination(*cfg["dest"])
            .set_obstacles(coords=cfg["obstacles"])
        )

        interface = GridInterface(hidden_grid=hidden_grid, animator=self)
        discoverer = PathDiscoverer(interface=interface, animator=self)
        pathfinder = ShortestPathFinder(discoverer=discoverer, animator=self)

        self.wait(1)
        discoverer.traverse()
        pathfinder.traverse()
        pathfinder.build_path()
        self.wait(4)
