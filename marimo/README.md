## Open and execute a marimo notebook

`marimo edit temperature_HD.py`

Note that cells are implemented as individual functions returning values/objects. If you assign a value to a variable in a cell, then assign it another value in another cell, marimo will stop and ask you to pick another name. That includes dummy variable names such as `iii` in for loops.

## Run the notebook as an app

`marimo run temperature_HD.py`

The `print()` statements will be printed to the terminal. Plots require e.g. `mo.ui.plotly()` to be rendered.
