import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="styling-popups",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={'filter': True, 'editable': True},
            dashGridOptions={'suppressMenuHide': True, "animateRows": False},
            columnSize="sizeToFit",
            className="ag-theme-alpine popups",
        )
    ], className="styling-popups-example",

)

if __name__ == "__main__":
    app.run(debug=True)
