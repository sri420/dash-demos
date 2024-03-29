from dash import Dash, html, Input, Output, callback
import dash_ag_grid as dag
import pandas as pd
import json

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris.csv")
df["index"] = df.index

app = Dash(__name__)

grid = dag.AgGrid(
    id="cell-selection-double-click-callback",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"filter": True},
    columnSize="sizeToFit",
    getRowId="params.data.index",
    dashGridOptions={"animateRows": False}
)

app.layout = html.Div([grid, html.Pre(id="pre-cell-selection-double-click-callback")])


@callback(
    Output("pre-cell-selection-double-click-callback", "children"),
    Input("cell-selection-double-click-callback", "cellDoubleClicked"),
)
def display_cell_double_clicked_on(cell):
    return f"Double-clicked on cell:\n{json.dumps(cell, indent=2)}" if cell else "Double-click on a cell"


if __name__ == "__main__":
    app.run(debug=True)
