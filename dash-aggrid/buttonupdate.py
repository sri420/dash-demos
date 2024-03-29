from dash import Dash, html, callback, Input, Output
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash(__name__)

all_columns = [
    { 'field': 'country' },
    { 'field': 'pop'},
    { 'field': 'continent' },
    { 'field': 'lifeExp'},
    { 'field': 'gdpPercap'},
]

two_columns = [
    { 'field': 'country' },
    { 'field': 'pop'},
]

grid = dag.AgGrid(
    id="grid-callback-example",
    rowData=df.to_dict("records"),
)

app.layout = html.Div(
    [
        html.Button(id='update-columns', children='Update columns'),
        grid,
    ]
)

@callback(
    Output("grid-callback-example", "columnDefs"),
    Input("update-columns", "n_clicks")
)
def update_columns(n_clicks):
    if n_clicks and n_clicks % 2 != 0:
        return two_columns
    return all_columns

if __name__ == "__main__":
    app.run(debug=True)
