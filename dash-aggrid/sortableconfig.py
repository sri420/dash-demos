import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "country"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total", "sortable": False},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="row-sorting-simple",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={"filter": True},
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": False}
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
