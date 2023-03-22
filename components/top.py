import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

top = dmc.Center(
    mt=65,
    children=dmc.Card(
        [
            dmc.Stack(
                align="center",
                children=[
                    dmc.Text("Bond with highest YTM", weight=500),
                    dmc.Text(
                        "SGBOCT23",
                        variant="gradient",
                        gradient={"from": "yellow", "to": "orange"},
                    ),
                    html.Div(
                        [
                            dmc.Text("3.65%", color="green", align="center"),
                            dmc.Text("Yield to maturity", size="md", align="center"),
                        ]
                    ),
                ],
            ),
            dmc.CardSection(
                [
                    dmc.Group(
                        mt=20,
                        position="center",
                        children=[
                            dmc.ActionIcon(
                                DashIconify(icon="material-symbols:add"),
                                variant="outline",
                                w=20,
                            ),
                            dmc.NumberInput(
                                min=0,
                                max=32,
                                value=1,
                                rightSection=dmc.Text("Units", size="sm"),
                                rightSectionWidth=50,
                                w=100,
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="material-symbols:remove"),
                                variant="outline",
                                w=20,
                            ),
                        ],
                    ),
                    dmc.Text("Face value: ₹4,852.0", align="center", size="sm", my=15),
                ]
            ),
            dmc.CardSection(
                [
                    dmc.Accordion(
                        styles={"item": {"border": "none"}},
                        mb=-5,
                        chevron=dmc.Text("7.5%", mr=29),
                        disableChevronRotation=True,
                        children=[
                            dmc.AccordionItem(
                                value="ytm",
                                children=[
                                    dmc.AccordionControl(
                                        dmc.Group(
                                            position="apart",
                                            children=[
                                                dmc.Group(
                                                    [
                                                        dmc.Text("Discount"),
                                                        DashIconify(
                                                            icon="mdi:chevron-down"
                                                        ),
                                                    ]
                                                )
                                            ],
                                        )
                                    ),
                                    dmc.AccordionPanel(
                                        [
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Current ask price"),
                                                    dmc.Text("₹5,451.07", weight=500),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Current gold price"),
                                                    dmc.Text("₹5,864.00", weight=500),
                                                ],
                                                my=10,
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ],
                    )
                ]
            ),
            dmc.Group(
                position="apart",
                mb=10,
                children=[
                    dmc.Text("Units available"),
                    dmc.Text("100", weight=500),
                ],
            ),
            dmc.Group(
                position="apart",
                children=[
                    dmc.Text("Maturity"),
                    dmc.Text("Jul 2009", weight=500),
                ],
            ),
            dmc.CardSection(dmc.Divider(my=10)),
            dmc.Group(
                position="apart",
                children=[
                    dmc.Text("Investment Amount"),
                    dmc.Text("₹5,45,107", weight=500),
                ],
            ),
            dmc.Button(
                "Explore other SGBs",
                rightIcon=DashIconify(icon="mdi:chevron-right"),
                mt=30,
                variant="filled",
                fullWidth=True,
                color="green",
                styles={"root": {"fontWeight": 300}},
            ),
        ],
        withBorder=True,
        shadow="md",
        radius="md",
        style={"width": 350},
        mb=2000,
    ),
)
