import pandas as pd
import plotly.express as px
df = pd.read_csv('project.csv')
fig = px.scatter(df,x='date',y='cases',color ='country',title='COVID-19 in Fighting')
fig.show()