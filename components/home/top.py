import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from data.top import get_bond_with_top_yield


def top():
    symbol, ytm, fv, discount, ask, gold, units, maturity = get_bond_with_top_yield()
    return dmc.Center(
        mt=65,
        children=dmc.Card(
            [
                dmc.Stack(
                    align="center",
                    children=[
                        dmc.Text("Bond with highest YTM", weight=500),
                        dmc.Text(
                            symbol,
                            variant="gradient",
                            gradient={"from": "yellow", "to": "orange"},
                        ),
                        html.Div(
                            [
                                dmc.Text(f"{ytm}%", color="green", align="center"),
                                dmc.Text(
                                    "Yield to maturity", size="md", align="center"
                                ),
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
                                    DashIconify(icon="material-symbols:remove"),
                                    variant="outline",
                                    w=20,
                                ),
                                dmc.NumberInput(
                                    min=0,
                                    max=units,
                                    value=1,
                                    rightSection=dmc.Text("Units", size="sm"),
                                    rightSectionWidth=50,
                                    w=100,
                                ),
                                dmc.ActionIcon(
                                    DashIconify(icon="material-symbols:add"),
                                    variant="outline",
                                    w=20,
                                ),
                            ],
                        ),
                        dmc.Text(
                            f"Face value: ₹{fv}", align="center", size="sm", my=15
                        ),
                    ]
                ),
                dmc.CardSection(
                    [
                        dmc.Accordion(
                            styles={"item": {"border": "none"}, "control": {"paddingRight": 16},
                                    "chevron": {"width": 100, "justifyContent": "end"}},
                            mb=-5,
                            chevron=dmc.Text(f"{discount}%"),
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
                                                        dmc.Text(f"₹{ask}", weight=500),
                                                    ],
                                                ),
                                                dmc.Group(
                                                    position="apart",
                                                    children=[
                                                        dmc.Text("Current gold price"),
                                                        dmc.Text(
                                                            f"₹{gold}", weight=500
                                                        ),
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
                        dmc.Text(units, weight=500),
                    ],
                ),
                dmc.Group(
                    position="apart",
                    children=[
                        dmc.Text("Maturity"),
                        dmc.Text(maturity, weight=500),
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
                dmc.Anchor(
                    dmc.Button(
                        "Explore other SGBs",
                        rightIcon=DashIconify(icon="mdi:chevron-right"),
                        mt=30,
                        variant="filled",
                        fullWidth=True,
                        color="green",
                        styles={"root": {"fontWeight": 300}},
                    ),
                    href="/explore",
                    underline=False,
                ),
            ],
            withBorder=True,
            shadow="md",
            radius="md",
            w=350,
        ),
    )
