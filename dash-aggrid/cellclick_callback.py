from dash import Dash, html, Input, Output, callback
import dash_ag_grid as dag
import pandas as pd
import json

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = Dash(__name__)

grid = dag.AgGrid(
    id="cell-selection-simple-click-callback",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"filter": True},
    columnSize="sizeToFit",
    getRowId="params.data.State",
    dashGridOptions={"animateRows": False}
)

app.layout = html.Div([grid, html.Pre(id="pre-cell-selection-simple-click-callback")])


@callback(
    Output("pre-cell-selection-simple-click-callback", "children"),
    Input("cell-selection-simple-click-callback", "cellClicked")
)
def display_cell_clicked_on(cell):
    return f"Clicked on cell:\n{json.dumps(cell, indent=2)}" if cell else "Click on a cell"


if __name__ == "__main__":
    app.run(debug=True)
