import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

columnDefs = [
    {"field": "make", "checkboxSelection": True, "headerCheckboxSelection": True},
    {"field": "model"},
    {"field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
    {"make": "BMW", "model": "M50", "price": 60000},
    {"make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="styling-selections",
            className="ag-theme-alpine selection",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
