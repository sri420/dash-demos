import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, callback, Patch
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {
        "field": "athlete",
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Input(id="input-radio-row-selection-checkbox-header-default", placeholder="Quick filter..."),
        dag.AgGrid(
            id="row-selection-checkbox-header-default",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={
                "rowSelection": "multiple",
                "pagination": True,
                "paginationAutoPageSize": True,
                "animateRows": False,
            },
        ),
    ],
)


@callback(
    Output("row-selection-checkbox-header-default", "dashGridOptions"),
    Input("input-radio-row-selection-checkbox-header-default", "value"),
)
def update_filter(filter_value):
    gridOptions_patch = Patch()
    gridOptions_patch["quickFilterText"] = filter_value
    return gridOptions_patch


if __name__ == "__main__":
    app.run(debug=True)
