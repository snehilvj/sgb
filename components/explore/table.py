import dash_ag_grid as dag
from dash import html

from data.explore import get_data_for_explore_section

inr_cols = ['Issue Price', 'Fair Value', 'Ask Price']




def table():
    data = get_data_for_explore_section()

    grid = dag.AgGrid(
        rowData=data.to_dict("records"),
        columnDefs=[{"field": i, "id": i} for i in data.columns],
        defaultColDef={"sortable": True, "filter": True},
        columnSize="sizeToFit",
        className="ag-theme-alpine-dark",
        dashGridOptions={"pagination": True, "paginationPageSize": 10, "domLayout": 'autoHeight' }
    )

    return html.Div(grid, style={"marginTop": 120})
