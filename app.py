import os

import dash
import dash_mantine_components as dmc
from dash import Dash

from components.header import header

external_scripts = [
    ""
    if os.environ.get("dev")
    else "https://unpkg.com/dash.nprogress@latest/dist/dash.nprogress.js"
]

app = Dash(__name__, external_scripts=external_scripts, use_pages=True)

app.layout = dmc.MantineProvider(
    withNormalizeCSS=True,
    withGlobalStyles=True,
    theme={
        "colorScheme": "dark",
        "fontFamily": "'Inter', sans-serif",
        "components": {"NavLink": {"styles": {"root": {"borderRadius": 3}}}},
    },
    children=[
        dmc.Container(
            fluid=True,
            children=[header, dash.page_container],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
