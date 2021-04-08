import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pydeck as pdk
import lightgbm as lgb

admin = False
c1 = st.sidebar.checkbox('Admin Mode', False)
if c1:
      admin = True
      # st.sidebar.text(admin)
else:
    admin = False
    # st.sidebar.text(admin)

# st.sidebar.image('./images/mcgill_logo.png')


# Import data
@st.cache(persist=True)
def load_data(path1, path2, path3, path4, path5, path6, path7):
    # Raw data
    data = pd.read_csv(path1)
    data['latitude'] = pd.to_numeric(data['Latitude'])
    data['longitude'] = pd.to_numeric(data['Longitude'])
    data['Location'] = data['Inside/Outside']
    data = data.drop(columns=['Latitude', 'Longitude', 'Inside/Outside'])
    # data['Count_By_Neighborhood'] = data.groupby(['Neighborhood'])['Total Incidents'].transform('count')
    data = data.dropna()
    data_sample = data.sample(frac=0.025)

    # Model
    file = open(path6)
    model_txt = file.read()

    # Accuracy
    model_metrics = pd.read_csv(path7, dtype={'Measure': 'str', 'Score': 'float'})
    # model_metrics = pd.DataFrame(data=[['F1', 43.95], ['Accuracy', 40.40], ['Recall', 40.40], ['Precision', 51.56]] , columns=['Measure', 'Score'])

    # Decoders/Encoders
    description_decoder = pd.read_csv(path2, names=['value', 'key']).set_index('key')['value'].to_dict()
    district_decoder = pd.read_csv(path3, names=['key', 'value']).set_index('key')['value'].to_dict()
    neighborhood_decoder = pd.read_csv(path4, names=['key', 'value']).set_index('key')['value'].to_dict()
    premise_decoder = pd.read_csv(path5, names=['key', 'value']).set_index('key')['value'].to_dict()

    # Check minimal accuracy


    return data, data_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder


df, df_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder = load_data('../data/BPD_CRIME_DATA_CLEAN_ST.csv', '../data/Description_decoder_2.csv',
                                                                         '../data/District_decoder.csv', '../data/Neighborhood_decoder.csv', '../data/Premise_decoder.csv', './MODEL.txt', '../data/Score_metrics.csv')


def predict_description(X, model_txt):
    model = lgb.Booster(model_str=model_txt)
    prediction_prob = model.predict(X)
    prediction = np.argmax(prediction_prob, axis=1)[0]
    print(prediction)
    return prediction_prob, prediction


st.title('Dazed Confusion Matrix App')
st.sidebar.markdown('**By:** Marek, Andrea, Tiancheng, Sam, Bogdan')
st.sidebar.markdown('**McGill MMA** - Enterprise Data Science & ML in Production')
st.sidebar.markdown('**GitHub:** https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix')

st.sidebar.header('Get Prediction')
nb_types = st.sidebar.selectbox(
    'Chose Neighborhood',
    df.Neighborhood.unique()
)

location_types = st.sidebar.selectbox(
    'Chose Location',
    df.Location.unique()
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

st.sidebar.markdown('**Version:** 1.0')

c2 = st.checkbox("Show/Hide Historical Data", False)
if c2:
      st.subheader("Rows")
      st.write(df.head(10))


st.header('Model Information')
st.text('Running on Light Gradient Boosting Machine')


col1, col2,  = st.beta_columns(2)
col1.subheader('Score Metrics')
col1.write(model_metrics)

col2.subheader('Features')
col2.image('./images/feature_importance.png')

st.header('Our Prediction')

# st.text('Hour: {}, Month: {}, Neighborhood: {}, Location {}, Premise: {}, Weapon: {}'.format(hours, months, nb_types, location_types, premise_types, weapon_types))

# Get prediction
column_names = ['Outside', 'Weapon_FIREARM', 'Weapon_HANDS', 'Weapon_KNIFE', 'Weapon_NONE',
                'Weapon_OTHER', 'Neighborhood', 'Premise', 'Month','Hour']

# Encode outside
outside = 0
if location_types == 'OUTSIDE':
    outside = 1

# Encode weapons
wp_firearm, wp_hands, wp_knife, wp_none, wp_other = 0, 0, 0, 0, 0
if weapon_types == 'FIREARM':
    wp_firearm = 1
if weapon_types == 'HANDS':
    wp_hands = 1
if weapon_types == 'KNIFE':
    wp_knife = 1
if weapon_types == 'NONE':
    wp_none = 1
if weapon_types == 'OTHER':
    wp_other = 1

neighborhood_enc = neighborhood_decoder[nb_types]
premise_enc = premise_decoder[premise_types]

X = pd.DataFrame(data=[outside, wp_firearm, wp_hands, wp_knife, wp_none, wp_other, neighborhood_enc, premise_enc, months, hours])

col3, col4,  = st.beta_columns(2)

col3.subheader('Prediction Input')
X_disp = X.T
X_disp.columns = column_names
X_disp = X_disp.transpose()
X_disp.columns = ['Values']
col3.write(X_disp)

prediction_prob, prediction = predict_description(X.T, model_txt)

col4.subheader('Types Of Crimes')
#print(description_decoder.values())
prediction_prob_df = pd.DataFrame(columns=description_decoder.values(), data=np.round(prediction_prob, 2))
prediction_prob = prediction_prob_df.transpose()
prediction_prob.columns = ['Probability']
col4.write(prediction_prob)

#st.text(prediction)
st.text('Most likely crime type given the profile: {}'.format(description_decoder[prediction]))
midpoint = [np.average(df['latitude']), np.average(df['longitude'])]
st.header('Searching Map Based On Historical Data')
st.map((df.query('(Location == @location_types) & (Month == @months) & (Weapon == @weapon_types) & (Hour == @hours) & (Premise == @premise_types)')[['latitude', 'longitude']]))

expander_1 = st.beta_expander('3D Map')
expander_1.pydeck_chart(pdk.Deck(
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

expander_2 = st.beta_expander('Data Exploration Plots')
expander_2.subheader('Crimes By Neighborhood')
expander_2.image('./images/map2.png')

#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#ax.scatter(x=df['longitude'], y=df['latitude'], alpha=0.3,
#            c=df['Count_By_Neighborhood'], cmap=plt.get_cmap('jet')

expander_2.subheader('Total Incidents By Weapon')
expander_2.image('./images/cat_plot2.png')

if admin:
    expander_3 = st.beta_expander('Model Text Output')
    expander_3.text(model_txt)