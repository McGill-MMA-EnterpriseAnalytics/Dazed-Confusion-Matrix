import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pydeck as pdk

# Import data
@st.cache(persist=True)
def load_data(path):
    data = pd.read_csv(path)
    data['latitude'] = pd.to_numeric(data['latitude'])
    data['longitude'] = pd.to_numeric(data['longitude'])
    data['Count_By_Neighborhood'] = data.groupby(['Neighborhood'])['Total Incidents'].transform('count')
    data = data.dropna()
    return data

df = load_data('BPD_CRIME_DATA_CLEAN_ST.csv')


st.title('Dazed Confusion Matrix App')
if st.checkbox("Show/Hide Data", False):
      st.subheader("Rows")
      st.write(df.head(10))

st.header('Crimes By Month')
months = st.slider('Month To Look At', 1, 12)
st.map(df.query('Month == @months')[['latitude', 'longitude']])

st.header('Crimes By Neighborhood')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x=df['longitude'], y=df['latitude'], alpha=0.3,
            c=df['Count_By_Neighborhood'], cmap=plt.get_cmap('jet'))
st.write(fig)

st.header('3D Map')
midpoint = [np.average(df['latitude']), np.average(df['longitude'])]
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state={
        'latitude': midpoint[0],
        'longitude': midpoint[1],
        'zoom': 11.5,
        'pitch': 60,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=pd.DataFrame(df.sample(frac=0.3)),
            get_position=['longitude', 'latitude'],
            radius=50,
            elevation_scale=4,
            elevation_rang=[0, 3000],
            pickable=True,
            extruded=True,
            auto_highlight=True,
            coverage=1,
        ),
    ])
)