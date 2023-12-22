import reflex as rx
from enum import Enum
from .fonts import Fonts
from .colors import Color, TextColor
STILESHEETS =[
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
    ]
#Constanst
MAX_WIDTH="500px"

#Sizes 
class Size(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em"

#Styles
BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
}


