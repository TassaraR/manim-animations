from enum import Enum


class Moves(Enum):
    U = (-1, 0)
    UR = (-1, 1)
    R = (0, 1)
    DR = (1, 1)
    D = (1, 0)
    DL = (1, -1)
    L = (0, -1)
    UL = (-1, -1)


class OppositeMoves(Enum):
    U = Moves.D
    UR = Moves.DL
    R = Moves.L
    DR = Moves.UL
    D = Moves.U
    DL = Moves.UR
    L = Moves.R
    UL = Moves.DR
