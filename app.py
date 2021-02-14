import numpy as np
import pandas as pd
import streamlit as st
import streamlit_theme as stt
import matplotlib.pyplot as plt
import pydeck as pdk

stt.set_theme({'primary': '#1b3388'})

# Import data
@st.cache(persist=True)
def load_data(path):
    data = pd.read_csv(path)
    data['latitude'] = pd.to_numeric(data['latitude'])
    data['longitude'] = pd.to_numeric(data['longitude'])
    data['Count_By_Neighborhood'] = data.groupby(['Neighborhood'])['Total Incidents'].transform('count')
    data = data.dropna()
    data_sample = data.sample(frac=0.1)
    return data, data_sample

df, df_sample = load_data('BPD_CRIME_DATA_CLEAN_ST.csv')


st.title('Dazed Confusion Matrix App')
st.text('Marek, Andrea, Tiancheng, Sam, Bogdan')
if st.checkbox("Show/Hide Data", False):
      st.subheader("Rows")
      st.write(df.head(10))

col1, col2, = st.beta_columns(2)

col1.text('Column 1')
col2.text('Column 2')

st.header('Crimes By Month')
months = st.slider('Month To Look At', 1, 12)
st.map(df.query('Month == @months')[['latitude', 'longitude']])

st.header('Crimes By Weapon')
crime_types = st.selectbox(
    'Chose Crime Weapon',
    ('KNIFE', 'FIREARM', 'HANDS', 'OTHER')
)
st.map(df.query('Weapon == @crime_types')[['latitude', 'longitude']])

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
            data=df_sample,
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