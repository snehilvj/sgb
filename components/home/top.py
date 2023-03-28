import dash_mantine_components as dmc
import pandas as pd
from babel.numbers import format_currency
from dash import html, clientside_callback, Output, Input, State
from dash_iconify import DashIconify


def fc(amount):
    return format_currency(amount, "INR", locale="en_IN")


def get_bond_with_top_yield():
    data = pd.read_csv("./data/sgb.csv")
    best = data.sort_values(by="YTM", ascending=False).iloc[0]
    symbol = best["Symbol"]
    ytm = best["YTM"]
    fv = best["Fair Value"]
    discount = best["Disc to Fair Value"]
    ask = "4243.12"
    gold = "2221.00"
    units = 10
    maturity = "Jul 2019"
    return symbol, ytm, fv, discount, ask, gold, units, maturity


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
                                    id="remove-units",
                                ),
                                dmc.NumberInput(
                                    min=1,
                                    max=units,
                                    value=1,
                                    rightSection=dmc.Text("Units", size="sm"),
                                    rightSectionWidth=50,
                                    w=100,
                                    id="units",
                                ),
                                dmc.ActionIcon(
                                    DashIconify(icon="material-symbols:add"),
                                    variant="outline",
                                    w=20,
                                    id="add-units",
                                ),
                            ],
                        ),
                        dmc.Text(
                            f"Face value: {fc(fv)}", align="center", size="sm", my=15
                        ),
                    ]
                ),
                dmc.CardSection(
                    [
                        dmc.Accordion(
                            styles={
                                "item": {"border": "none"},
                                "control": {"paddingRight": 16},
                                "chevron": {"width": 100, "justifyContent": "end"},
                            },
                            mb=-5,
                            chevron=dmc.Text(f"{discount}%", weight=500),
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
                                                        dmc.Text(
                                                            fc(ask),
                                                            id="current-ask-price",
                                                            weight=500,
                                                        ),
                                                    ],
                                                ),
                                                dmc.Group(
                                                    position="apart",
                                                    children=[
                                                        dmc.Text("Current gold price"),
                                                        dmc.Text(fc(gold), weight=500),
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
                        dmc.Text(fc(ask), id="investment-amount", weight=500),
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
            w=340,
        ),
    )


clientside_callback(
    """
    function updateUnits(a, r, units, min, max) {
        const triggered = window.dash_clientside.callback_context.triggered[0]
        if (triggered.prop_id.includes("add")) {
            return Math.min(max, units + 1)
        } else {
            return Math.max(units - 1, min)
        }
    }
    """,
    Output("units", "value"),
    Input("add-units", "n_clicks"),
    Input("remove-units", "n_clicks"),
    State("units", "value"),
    State("units", "min"),
    State("units", "max"),
    prevent_initial_call=True,
)

clientside_callback(
    """
    function updateUnits(units, currentAsk) {
        const ask = currentAsk.replace("₹", "").replace(",", "")
        const amount = units * parseFloat(ask)
        return `₹${amount.toLocaleString('hi')}` 
    }
    """,
    Output("investment-amount", "children"),
    Input("units", "value"),
    State("current-ask-price", "children"),
)
