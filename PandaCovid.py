import pandas as pd
from pandasgui import show

covid = pd.read_csv('Global_Mobility_Report2.csv')
covid2=pd.read_csv('owid-covid-data2.csv')
gui = show(covid)

#gui=show(covid2)
