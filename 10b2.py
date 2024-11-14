import json
import numpy as np  
import pandas as pd  
import plotly.express as px

# Uncomment below lines to render map on your browser
import plotly.io as pio
pio.renderers.default = 'browser'
india_states = json.load(open("states_india.geojson", "r"))  
df = pd.read_csv("india_census.csv")

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]  
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
df = pd.read_csv("india_census.csv")
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))  
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])
print(df.head())
fig = px.choropleth(  df,  locations="id", geojson=india_states,  color="Population",
                      hover_name="State or union territory",
                      hover_data=["Density", "Sex ratio", "Population"],
                      title="India Population Statewise")
#fig.update_geos(fitbounds="locations", visible=False)
fig.show()