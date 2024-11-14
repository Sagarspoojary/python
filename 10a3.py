#case3
#Bar Graph of Runs scored every Over
import pandas as pd
import plotly.express as px


runs_scored = pd.read_csv('AusVsInd.csv')

fig = px.bar(runs_scored, x='Overs', y=['AUS_RPO', 'IND_RPO'], barmode='group')
fig.update_layout(title='Australia vs India ODI Match', xaxis_title='OVERS', yaxis_title='RUNS',  legend_title='Country')


fig.show()