## Open and execute a marimo notebook

`marimo edit temperature_HD.py`

Note that cells are implemented as individual functions returning values/objects. If you assign a value to a variable in a cell, then assign it another value in another cell, marimo will stop and ask you to pick another name. That includes dummy variable names such as `iii` in for loops.

## Run the notebook as an app

`marimo run temperature_HD.py`

The `print()` statements will be printed to the terminal. Plots require e.g. `mo.ui.plotly()` to be rendered.

## Simple execution thanks to serialized dependencies

The notebook is also executable with `uv run temperature_HD.py`, even if you don't have the dependencies installed! This is thanks to the embedded metadata listing the necessary packages (see [PEP 723](https://peps.python.org/pep-0723/)), written at the top of the script file:

  # /// script
  # requires-python = ">=3.13"
  # dependencies = [
  #     "marimo",
  #     "matplotlib",
  #     "meteostat",
  #     "numpy",
  #     "pandas",
  #     "plotly",
  # ]
  # ///

Which I have added by doing: `uv add --script temperature_HD.py pandas matplotlib` etc. 
