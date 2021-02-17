import numpy as np
import pandas as pd
import streamlit as st
import streamlit_theme as stt
import matplotlib.pyplot as plt
import pydeck as pdk

stt.set_theme({'primary': '#1b3388'})

admin = False
c1 = st.sidebar.checkbox('Admin Mode', True)
if c1:
      admin = True
      # st.sidebar.text(admin)
else:
    admin = False
    # st.sidebar.text(admin)

st.sidebar.image('./images/mcgill_logo.png')

# Import data
@st.cache(persist=True)
def load_data(path):
    # Raw data
    data = pd.read_csv(path)
    data['latitude'] = pd.to_numeric(data['latitude'])
    data['longitude'] = pd.to_numeric(data['longitude'])
    data['Count_By_Neighborhood'] = data.groupby(['Neighborhood'])['Total Incidents'].transform('count')
    data = data.dropna()
    data_sample = data.sample(frac=0.03)

    # Model
    file = open('./YOLO_SWAG.txt')
    assert(file != None)
    model_txt = file.read()

    # Accuracy
    model_metrics = pd.DataFrame(data=[['F1', '43.95 %'], ['Accuracy', '40.40 %'], ['Recall', '40.40 %'], ['Precision', '51.56 %']] ,
                                 columns=['Measure', 'Score'])

    # Check that we are not returning null information
    #assert(data != None & data_sample != None & model_txt != None & model_metrics != None)

    return data, data_sample, model_txt, model_metrics

df, df_sample, model_txt, model_metrics = load_data('BPD_CRIME_DATA_CLEAN_ST.csv')


st.title('Dazed Confusion Matrix App')

st.sidebar.markdown('**By:** Marek, Andrea, Tiancheng, Sam, Bogdan')
st.sidebar.markdown('**McGill MMA** - Enterprise Data Science & ML in Production')
st.sidebar.markdown('**GitHub:** https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix')

st.sidebar.header('Get Prediction')
nb_types = st.sidebar.selectbox(
    'Chose Neighborhood',
    df.Neighborhood.unique()
)

outside = st.sidebar.selectbox(
    'Chose Location',
    df['Inside/Outside'].unique()
)

premise_types = st.sidebar.selectbox(
    'Chose Premise',
    df.Premise.unique()
)

weapon_types = st.sidebar.selectbox(
    'Chose Crime Weapon',
    df.Weapon.unique()
)

hours = st.sidebar.slider('Hour To Look At', int(min(df.Hour.unique())), int(max(df.Hour.unique())))
months = st.sidebar.slider('Month To Look At', int(min(df.Month.unique())), int(max(df.Month.unique())))

c2 = st.checkbox("Show/Hide Historical Data", False)
if c2:
      st.subheader("Rows")
      st.write(df.head(10))


st.header('Model Information')
st.text('Running on Light Gradient Boosting Machine')


col1, col2, = st.beta_columns(2)
col1.subheader('Score Metrics')
col1.write(model_metrics)

col2.subheader('Features')
col2.image('./images/feature_importance.png')

st.header('Our Prediction')
st.text('Predicting crime based off parameters:')
st.text('Hour: {}, Month: {}, Neighborhood: {}, Location {}, Premise: {}, Weapon: {}'.format(hours, months, nb_types, outside, premise_types, weapon_types))
st.text('Prediction: {}'.format('ROBBERY - RESIDENCE'))

st.header('Searching Map Based On Historic Data')
st.map(df.query('(Month == @months) & (Weapon == @weapon_types) & (Hour == @hours) & (Premise == @premise_types)')[['latitude', 'longitude']])

expander_1 = st.beta_expander('Crimes By Neighborhood')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x=df['longitude'], y=df['latitude'], alpha=0.3,
            c=df['Count_By_Neighborhood'], cmap=plt.get_cmap('jet'))
expander_1.write(fig)

expander_2 = st.beta_expander('3D Map')
midpoint = [np.average(df['latitude']), np.average(df['longitude'])]
expander_2.pydeck_chart(pdk.Deck(
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

if admin:
    expander_3 = st.beta_expander('Model Text Output')
    expander_3.text(model_txt)