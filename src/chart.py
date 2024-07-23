import pandas as pd
import plotly.express as px
from plotly.offline import plot

df = pd.read_csv("out/data.csv")

fig = px.line(
    df,
    x="Date",
    y="All items, less food and energy",
    title="Price series with year-over-year percentage variation",
)

plot(fig, filename="out/chart.html", auto_open=False)
