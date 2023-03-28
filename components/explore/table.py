import pandas as pd
from dash import html
from dash_mantine_react_table import DashMantineReactTable


def get_data_for_explore_section():
    raw = pd.read_csv("./data/sgb.csv")
    return raw


def table():
    data = get_data_for_explore_section()

    grid = DashMantineReactTable(
        data=data.to_dict("records"),
        columns=[{"accessorKey": i, "header": i, "maxSize": 100} for i in data.columns],
        mrtProps={
            "enableHiding": False,
            "enableColumnFilters": False,
            "enableDensityToggle": False,
            "enableColumnActions": False,
            "enableFullScreenToggle": False,
            "enableMultiRowSelection": False,
            "initialState": {"density": "sm", "showGlobalFilter": True},
            "mantineTableProps": {
                "fontSize": "sm",
                "sx": {"fontFamily": "'Inter', sans-serif"},
            },
            "mantineTableHeadCellProps": {"style": {"fontWeight": 500}},
            "mantineSearchTextInputProps": {"icon": None, "rightSection": None},
        },
        mantineProviderProps={
            "theme": {
                "colorScheme": "dark",
                "components": {"ActionIcon": {"styles": {"root": {"marginLeft": 5}}}},
            },
        },
    )

    return html.Div(grid, style={"marginTop": 45})
