import reflex as rx
from web_jalivur.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twich","https://www.twitch.tv/aestella92", "arrow_forward","arrow_back"),
        link_button("GitHub", "https://github.com/Jalivur/web_python_propia", "arrow_forward", "arrow_back"),
        link_button("Youtube (Canal principal)", "https://www.youtube.com/channel/UC0doqISuLkdkmiThl7EEwBQ","arrow_forward", "arrow_back"),
        link_button("Instagram", "https://www.instagram.com/jalivur/","arrow_forward", "arrow_back")

    )