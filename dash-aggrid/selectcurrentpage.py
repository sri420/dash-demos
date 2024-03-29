import dash_ag_grid as dag
from dash import Dash, html
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
        "headerCheckboxSelectionCurrentPageOnly": True,
    },
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="row-selection-checkbox-header-current-page-only",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={
                "rowSelection": "multiple",
                "pagination": True,
                "paginationAutoPageSize": True,
                "animateRows": False
            },
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
