from dash import Dash, html
import dash_ag_grid as dag
import plotly.express as px

app = Dash(__name__)

df = px.data.gapminder()
df = df[['country', 'continent', 'year', 'pop']]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="getting-started-themes-example",
            columnDefs= [{"field": x, } for x in df.columns],
            rowData= df.to_dict('records'),
            className="ag-theme-alpine-dark",
            #ag-theme-quartz-dark, ag-theme-alpine, ag-theme-alpine-dark, ag-theme-balham, ag-theme-balham-dark, ag-theme-material.
            columnSize="sizeToFit",
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
