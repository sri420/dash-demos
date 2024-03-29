from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

app = Dash(__name__)

grid = dag.AgGrid(
    id="get-started-example-basic-df",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
