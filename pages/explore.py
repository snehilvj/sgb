import dash

from components.explore.hero import hero
from components.explore.table import table

dash.register_page(__name__, path="/explore")


def layout():
    return [hero, table()]
