import reflex as rx
from dotenv import load_dotenv
load_dotenv()
config = rx.Config(
    app_name="web_jalivur",
    db_url="DB_URL"
)