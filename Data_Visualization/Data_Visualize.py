import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import plotly.express as px

import plotly.graph_objs as go
class Data_Visual:
    def __init__(self):
        super.__init__()
    def  Income_Month(self,data):
        gr_month= data.groupby("Month").sum()["TotalCost"]
    def TotalCost(self,data):
        months = range(1,13)
        plt.bar(months, gr_month, align='center')
        plt.xticks(months)
        plt.xlabel("Months")
        plt.ylabel("TotalCost")