import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, callback, Patch
import pandas as pd
import json

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [{"field": i} for i in ["country", "year", "athlete", "age", "sport", "total"]]

app.layout = html.Div(
    [
        dcc.RadioItems(
            id='radio-row-selection-type',
            options={'single': 'Single Row Selection', 'multiple': 'Multi Row Selection'},
            value='single'
        ),
        dcc.Checklist(
            id='chk-row-selection-options',
            options=[
                {'label': 'Enable Multi Row Selection On Click', "value": 'rowMultiSelectWithClick'},
                {'label': "Disable deselection holding 'Ctrl'", "value": 'suppressRowDeselection'}
            ],
            value=[]
        ),
        html.Pre(id="pre-row-selection-options"),
        dag.AgGrid(
            id="row-selection-options",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={"animateRows": False}
        ),
    ],
)


@callback(
    Output("row-selection-options", "dashGridOptions"),
    Output("pre-row-selection-options", "children"),
    Input('radio-row-selection-type', "value"),
    Input('chk-row-selection-options', "value")
)
def set_grid_options(row_selection, selected_options):
    grid_options = {
        "rowSelection": row_selection,
        "rowMultiSelectWithClick": row_selection == 'multiple' and 'rowMultiSelectWithClick' in selected_options,
        "suppressRowDeselection": 'suppressRowDeselection' in selected_options,
    }
    output = {k: v for k, v in grid_options.items() if v is not False}

    return grid_options, f'dashGridOptions = {json.dumps(output, indent=2).replace("true", "True") if selected_options else output}'


@callback(
    Output("chk-row-selection-options", "options"),
    Output("row-selection-options", "selectedRows"),
    Input('radio-row-selection-type', "value")
)
def disable__checkbox(row_selection):
    options_patch = Patch()
    options_patch[0]['disabled'] = row_selection == 'single'
    return options_patch, []


if __name__ == "__main__":
    app.run(debug=True)
