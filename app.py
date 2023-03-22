import dash_mantine_components as dmc
from dash import Dash

from components.header import header
from components.hero import hero
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
            children=[header, hero, top],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
