from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash(__name__)

columnDefs = [
    { 'field': 'country', 'filter': True },
    { 'field': 'pop', 'headerName': 'Population'},
    { 'field': 'lifeExp', 'headerName': 'Life Expectancy', 'filter': True },
]


grid = dag.AgGrid(
    id="getting-started-headers",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
    dashGridOptions={'animateRows': False,'pagination':True },
    className="ag-theme-alpine-dark"
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
