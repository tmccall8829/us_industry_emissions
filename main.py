import pandas as pd
import plotly.express as px
from math import floor as fl

# load the data
df = pd.read_csv("emissions_data.csv")

# melt and clean up the data so it's easy to get the years and emissions numbers
df_melted = df.melt(id_vars=["Emissions by Economic Sector, MMT CO2 eq."], value_vars=None, var_name="Year", value_name="MMTCO2e")
df_melted.rename(columns={"Emissions by Economic Sector, MMT CO2 eq.": "Industry"}, inplace=True)

# plotly express area chart
# exclude total emissions (bc graph shows that itself) and U.S. territories (too small)
fig = px.area(
    df_melted.loc[(df_melted.Industry != "Total") & (df_melted.Industry != "U.S. territories")],
    x="Year",
    y="MMTCO2e",
    color="Industry",
    color_discrete_sequence= px.colors.sequential.Aggrnyl,
    title="Greenhouse Gas Emissions by Sector, U.S. (1990-2019)")

# make the ticks look better
fig.update_yaxes(
    tickmode="array",
    tickvals=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
    ticktext=["1k", "2k", "3k", "4k", "5k", "6k", "7k", "8k"]
)

fig.show()
