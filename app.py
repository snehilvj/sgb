import dash_mantine_components as dmc
from dash import Dash

from components.header import header
from components.hero import hero

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
            children=[header, hero],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
