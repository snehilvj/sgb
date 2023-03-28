import dash_mantine_components as dmc
import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc


def get_data():
    data = pd.read_csv("./data/gold.csv")
    return data["date"], data["price"]


def create_chart():
    x, y = get_data()
    fig = go.Figure(
        data=go.Scatter(
            x=x,
            y=y,
            mode="lines",
            line=dict(color=dmc.theme.DEFAULT_COLORS["green"][8], width=2),
        )
    )
    fig.update_layout(
        width=350,
        height=100,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
    )
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    return fig


hero = dmc.Center(
    mt=80,
    children=[
        dmc.Card(
            p=20,
            children=[
                dmc.CardSection(
                    withBorder=True,
                    p=20,
                    children=[
                        dmc.Text(
                            "Last Updated: 2022/03/31", color="dimmed", align="center"
                        )
                    ],
                ),
                dmc.Text(
                    "Gold Price: ₹6040",
                    weight=500,
                    variant="gradient",
                    gradient={"from": "yellow", "to": "orange"},
                    align="center",
                    mt=20,
                ),
                dmc.Text(
                    "Discount Rate (assumed): 6%", weight=500, align="center", my=10
                ),
                html.Div(
                    style={"width": 350, "height": 100},
                    children=[
                        dcc.Graph(
                            figure=create_chart(),
                            config={"displayModeBar": False, "staticPlot": True},
                        )
                    ],
                ),
            ],
        )
    ],
)
