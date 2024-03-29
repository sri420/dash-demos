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
    },
    {"field": "age", "sort": "desc"},
    {"field": "country", "sort": "asc"},
    {"field": "year"},
]

selectedRows = [
    {'athlete': 'Mark Todd', 'age': 56, 'country': 'New Zealand', 'year': 2012, 'date': '12/8/2012',
     'sport': 'Equestrian', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'athlete': 'Mac Cone', 'age': 55, 'country': 'Canada', 'year': 2008, 'date': '24/08/2008',
     'sport': 'Equestrian', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'athlete': 'Ian Millar', 'age': 61, 'country': 'Canada', 'year': 2008, 'date': '24/08/2008',
     'sport': 'Equestrian', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1}
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="styling-inputs-checkboxes",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={'resizable': True},
            selectedRows=selectedRows,
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
            columnSize="sizeToFit",
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
