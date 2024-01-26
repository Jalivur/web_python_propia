import reflex as rx
from enum import Enum
from .fonts import Font, FontWeight
from .colors import Color, TextColor

STILESHEETS =[
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap",
    ]
#Constanst
MAX_WIDTH="560px"

#Sizes 
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.PRIMARY.value,
    rx.Heading: {
        "color": TextColor.ACCENT.value,
        "font_family": Font.DEFAULT.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.Button: {
        #"width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        #"border_radius": Size.DEFAULT.value,
        "color": TextColor.SECONDARY.value,
        #"background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        #"_hover": {
        #    "background_color": Color.SECONDARY.value
        #}
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    #color=TextColor.HEADER.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    #color=TextColor.BODY.value
)




