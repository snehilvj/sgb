import dash

from components.explore.hero import hero
from components.explore.table import table
from components.love import love

dash.register_page(__name__, path="/explore")


def layout():
    return [hero, table(), love]
