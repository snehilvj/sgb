import dash_mantine_components as dmc
from dash_iconify import DashIconify

love = dmc.Center(
    my=65,
    children=dmc.Group(
        spacing="xs",
        children=[
            dmc.Text("Made with"),
            DashIconify(
                icon="akar-icons:heart",
                width=19,
                color=dmc.theme.DEFAULT_COLORS["red"][8],
            ),
            dmc.Text("by Snehil Vijay"),
        ],
    ),
)
