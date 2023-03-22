import dash_mantine_components as dmc
from dash import Dash

from components.faq import faqs
from components.header import header
from components.hero import hero
from components.love import love
from components.top import top

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    withNormalizeCSS=True,
    withGlobalStyles=True,
    theme={
        "colorScheme": "dark",
        "fontFamily": "'Inter', sans-serif",
    },
    children=[
        dmc.Container(
            fluid=True,
            children=[header, hero, top, faqs, love],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
