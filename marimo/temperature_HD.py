import marimo

__generated_with = "0.11.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import warnings
    warnings.filterwarnings("ignore")
    # Because meteostat causes Pandas to panic sometimes

    # Import Meteostat library and dependencies
    from datetime import datetime
    from meteostat import Hourly, Point
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    all_data = {}

    years_to_query = [2012,2020,2021,2022,2023,2024,2025]

    for yyy in years_to_query:
        print(yyy)
        if yyy not in all_data.keys():
            # Set time period
            start = datetime(yyy, 1, 1)
            end = datetime(yyy, 12, 31, 23, 59)

            # Get hourly data
            heidelberg = Point(49.398750, 8.672434, 114)
            data = Hourly(heidelberg, start, end)
            data = data.fetch()
            all_data[yyy] = data
    return (
        Hourly,
        Point,
        all_data,
        data,
        datetime,
        end,
        heidelberg,
        np,
        pd,
        plt,
        start,
        warnings,
        years_to_query,
        yyy,
    )


@app.cell
def _(all_data, np, years_to_query):
    import marimo as mo
    import plotly.graph_objects as go


    fig = go.Figure()
    for yyyear in years_to_query:
        day = (all_data[yyyear].index - all_data[yyyear].index.min()) / np.timedelta64(24, 'h') # every hour is a float
        n_day = all_data[yyyear].index.map(lambda t: t.replace(year=2000)) # every hour is a datetime in the year 2000
        # We don't mind doing this because in the plot we won't display the year.
        fig.add_trace(go.Scatter(x=n_day , y=all_data[yyyear]['temp'], mode="lines", name=str(yyyear)))

    fig.update_layout(xaxis=dict(tickformat="%d-%m"),
                     title='Heidelberg - hourly temperature',
                     xaxis_title="Date", yaxis_title="temperature (Celsius)")
    fig.show() # displays it in the notebook
    mo.ui.plotly( fig ) # displays it in app mode when run with command "marimo run temperature_HD.py"
    return day, fig, go, mo, n_day, yyyear


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
