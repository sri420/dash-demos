import dash_ag_grid as dag
from dash import Dash, html

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

app = Dash(__name__)

app.layout = html.Div(
    [
        dag.AgGrid(
            id="full-row-editing-example",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
            dashGridOptions={
                "undoRedoCellEditing": True,
                "undoRedoCellEditingLimit": 20,
                "editType": "fullRow",
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=False)
