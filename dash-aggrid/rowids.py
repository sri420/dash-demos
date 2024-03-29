import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

columnDefs = [
    {"headerName": "Row ID", "valueGetter": {"function": "params.node.id"}},
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

data = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
    {"make": "BMW", "model": "M50", "price": 60000},
    {"make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="row-ids-grid-assigned",
            rowData=data,
            columnDefs=columnDefs,
            defaultColDef={"filter": True},
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": False}
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
