"""
I would start collecting the data from the API and storing it somewhere, probably in a database. Then, I would module it and start trying
to find correlations between them. If that's the case, I would try to understand the correlations better and see if I can find any
relantionship of cause and effect. I could also use AI to see if the some of the prices are predictable.
"""

import pandas as pd
from plotly.offline import plot

df = pd.read_csv("out/data.csv")

traces = []

traces.append(
    {
        "x": df["Date"],
        "y": df["All items, less food and energy"],
        "name": "All items, less food and energy",
    }
)

traces.append(
    {"x": df["Date"], "y": df["Gasoline (all types)"], "name": "Gasoline (all types)"}
)


plot(traces, filename="out/correlation.html")
