import dash
import pandas as pd
import dash_ag_grid as dag
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__, path="/explore")

data = pd.read_csv("./data/sgb_2023-03-23.csv")

grid = dag.AgGrid(
    id="quickstart-grid",
    rowData=data.to_dict("records"),
    columnDefs=[{"field": i, "id": i} for i in data.columns],
    defaultColDef={"resizable": True, "sortable": True, "filter": True},
    columnSize="sizeToFit",
    getRowId="params.data.State",
    className="ag-theme-alpine-dark",
)

layout = html.Div([dmc.Space(h=100), grid, html.Div(id="quickstart-output")])
