import reflex as rx
from enum import Enum

#Constanst
MAX_WIDTH="500px"

#Sizes 
class Spacer(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em"

#Styles
BASE_STYLE = {
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"flex",
        "padding": Spacer.SMALL.value
    }
}


