import dash_mantine_components as dmc
from dash import html

from components.home.compare import table
from components.home.timeline import timeline

hero = html.Div(
    children=[
        dmc.Center(
            mt=120,
            mx=10,
            children=[
                dmc.Stack(
                    spacing=0,
                    p=0,
                    children=[
                        dmc.Text("Smartest way to invest in Gold"),
                        dmc.Text(
                            "Sovereign Gold Bonds",
                            variant="gradient",
                            size=50,
                            weight=500,
                            gradient={"from": "yellow", "to": "orange"},
                        ),
                    ],
                ),
            ],
        ),
        dmc.Container(
            style={"maxWidth": 550},
            my=40,
            px=10,
            children=[
                dmc.Highlight(
                    "The Government of India introduced Sovereign Gold Bonds (SGB) in November 2015. SGBs are debt "
                    "securities denominated in grams of gold and are issued by the RBI on behalf of the government. "
                    "They are denominated in gold and pay a fixed interest of 2.5% p.a to their investors. ",
                    highlight=["pay a fixed interest of 2.5% p.a"],
                    highlightColor="orange",
                )
            ],
        ),
        dmc.Group(position="center", spacing=65, children=[table, timeline]),
    ]
)
