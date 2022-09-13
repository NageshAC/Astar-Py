RED         = (255, 0, 0)       # SOURCE
GREEN       = (0, 255, 0)       # DESTINATION
BLUE        = (0, 0, 255)       # ACTIVE or CURRENT
YELLOW      = (255, 255, 0)     # VISITED
WHITE       = (255, 255, 255)   # EMPTY PATH
BLACK       = (0, 0, 0)         # WALL
PURPLE      = (128, 0, 128)     # OPTIMISED PATH
ORANGE      = (255, 165 ,0)     # OPEN
GREY        = (128, 128, 128)   # GRID LINES
TURQUOISE   = (64, 224, 208)

color_switch = {
    "SRC"   : RED  ,
    "DEST"  : GREEN,
    "VSTD"  : YELLOW,
    "EMT"   : WHITE ,
    "WALL"  : BLACK ,
    "PATH"  : PURPLE,
    "OPEN"  : ORANGE,
    "GRID"  : GREY,
    "CRT"   : BLUE 
}