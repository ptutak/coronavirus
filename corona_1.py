import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

#%matplotlib inline


# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# plt.rcParams["figure.figsize"] = [15, 5]
# from IPython import display
# from ipywidgets import interact, widgets


confirmed_cases_raw = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
)
deaths_raw = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
)
recoveries_raw = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
)


def cleandata(df_raw):
    df_cleaned = df_raw.melt(
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        value_name="Cases",
        var_name="Date",
    )
    df_cleaned = df_cleaned.set_index(["Country/Region", "Province/State", "Date"])
    return df_cleaned


# Clean all datasets
confirmed_cases = cleandata(confirmed_cases_raw)
deaths = cleandata(deaths_raw)
recoveries = cleandata(recoveries_raw)

print(confirmed_cases)

polska = confirmed_cases.loc["Poland"]

print(polska.tail(10))

polska.tail(20).plot(
    y="Cases",
    figsize=(12, 8),
    marker="o",
    title="Przypadki potwierdzone wykrycia COVID-19",
)

hubei = confirmed_cases.loc["China", "Hubei"]

razem = polska.merge(hubei, left_on="Date", right_on="Date")

print(razem.tail(10))

razem.plot(
    y=["Cases_x", "Cases_y"],
    figsize=(12, 8),
    marker="o",
    title="Przypadki potwierdzone wykrycia COVID-19",
    logy=True,
)
plt.show()
