from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash(__name__)

columnDefs = [
    { 'field': 'country', 'sortable': False },
    { 'field': 'pop', 'headerName': 'Population'},
    { 'field': 'lifeExp', 'headerName': 'Life Expectancy'},
]

grid = dag.AgGrid(
    id="getting-started-sort",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
