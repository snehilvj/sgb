import dash_mantine_components as dmc
from dash import html

returns = {
    "Sovereign Gold Bond": [100, 180, "Gold appreciation + 2.5% p.a."],
    "Gold ETFs": [90, 170, "Gold appreciation - Expense Ratio"],
    "Digital Gold": [80, 170, "Gold appreciation - Platform Charges"],
    "Physical Gold": [70, 170, "Gold appreciation - Making Charges"],
}

columns = ["Investment Method", "Returns"]
header = html.Thead(html.Tr([html.Th(col) for col in columns]))

body = []
for k, v in returns.items():
    row = [
        html.Td(k),
        html.Td(
            dmc.FloatingTooltip(
                label=v[2],
                children=dmc.Progress(
                    sections=[
                        {
                            "value": v[0],
                            "color": "green",
                        },
                    ],
                    size="xl",
                    w=v[1],
                ),
            )
        ),
    ]
    body.append(html.Tr(row))

table = dmc.Center(
    dmc.Table(
        verticalSpacing="md",
        w=360,
        mt=25,
        id="compare-table",
        children=[header, html.Tbody(body)],
    )
)
