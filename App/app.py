import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import matplotlib.pyplot as plt
import pydeck as pdk
import lightgbm as lgb
from SessionState import get

import os.path as path

st.title('Dazed Confusion Matrix App')
two_up = path.abspath(path.join(__file__ ,"../.."))

# Initialize empty session
session_state = get(password='')

def main():
    # ADMIN MODE
    ##################################################################################################################
    admin = False
    c1 = st.sidebar.checkbox('Admin Mode', False)
    if c1:
          admin = True
          # st.sidebar.text(admin)
    else:
        admin = False
        # st.sidebar.text(admin)
    ##################################################################################################################

    # LOAD DATA
    ##################################################################################################################
    @st.cache(persist=True)
    def load_data(path0, path1, path2, path3, path4, path5, path6, path7, path8):
        # Raw data
        data_new = pd.read_csv(path0)
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

        # Decoders/Encoders
        description_decoder = pd.read_csv(path2, names=['value', 'key']).set_index('key')['value'].to_dict()
        district_decoder = pd.read_csv(path3, names=['key', 'value']).set_index('key')['value'].to_dict()
        neighborhood_decoder = pd.read_csv(path4, names=['key', 'value']).set_index('key')['value'].to_dict()
        premise_decoder = pd.read_csv(path5, names=['key', 'value']).set_index('key')['value'].to_dict()
        call_desc = pd.read_csv(path8, names=['key', 'value'])
        call_desc_decoder = call_desc.set_index('key')['value'].to_dict()
        # Check minimal accuracy


        return data_new, data, data_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder, call_desc, call_desc_decoder


    df_new, df, df_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder, call_desc, call_desc_decoder = load_data('./data/TRAIN_911_DEMO_MERGED_ENCODED.CSV', './data/BPD_CRIME_DATA_CLEAN_ST.csv', './data/Description_decoder_2.csv',
                                                                             './data/District_decoder.csv', './data/Neighborhood_decoder.csv', './data/Premise_decoder.csv', './911MODEL.txt', './data/Score_metrics.csv', './data/911_Call_Description_decoder.csv')

    ##################################################################################################################

    # PREDICT
    ##################################################################################################################
    def predict_description(X, model_txt):
        model = lgb.Booster(model_str=model_txt)
        prediction_prob = model.predict(X)
        prediction = np.argmax(prediction_prob, axis=1)[0]
        print(prediction)
        return prediction_prob, prediction
    ##################################################################################################################

    # SIDEBAR
    ##################################################################################################################
    st.sidebar.image('./images/bpd_logo.png', width=150)
    st.sidebar.markdown('**By:** Marek, Andrea, Tiancheng, Sam, Bogdan')
    st.sidebar.markdown('**McGill MMA** - Enterprise Data Science & ML in Production II')
    st.sidebar.markdown('**GitHub:** https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix')

    st.sidebar.subheader('Original Features')
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

    st.sidebar.subheader('911 Features')
    call_desc = st.sidebar.selectbox(
        'Call Description',
        call_desc
    )
    call_desc_decoded = call_desc_decoder[call_desc]
    priority = st.sidebar.selectbox(
        'Priority',
        ('HIGH', 'MEDIUM', 'LOW', 'NON-EMERGENCY', 'OUT OF SERVICE', 'UNKNOWN')
    )
    holiday = st.sidebar.selectbox(
        'Holiday',
        ('YES', 'NO')
    )
    weekend = st.sidebar.selectbox(
        'Weekend',
        ('YES', 'NO')
    )
    crime_hour = st.sidebar.slider('Crime Hour', int(min(df_new.crime_hour.unique())), int(max(df_new.crime_hour.unique())))

    st.sidebar.subheader('Average Of Demographic Features')
    median_household_income = df_new.median_household_income.mean()
    st.sidebar.write('Median House Income: {}'.format(round(median_household_income, 2)))
    households_below_poverty = df_new.households_below_poverty.mean()
    st.sidebar.write('Households below poverty: {}'.format(round(households_below_poverty, 2)))
    perc18_24 = df_new.perc18_24.mean()
    st.sidebar.write('Percentage 18-24: {}'.format(round(perc18_24, 2)))
    perc25_64 = df_new.perc25_64.mean()
    st.sidebar.write('Percentage 25-54: {}'.format(round(perc25_64, 2)))
    perc65up = df_new.perc65up.mean()
    st.sidebar.write('Percentage 65+: {}'.format(round(perc65up, 2)))
    perc_asian = df_new.perc_asian.mean()
    st.sidebar.write('Percentage Asian: {}'.format(round(perc_asian, 2)))
    perc_aa = df_new.perc_aa.mean()
    st.sidebar.write('Percentage African American: {}'.format(round(perc_aa, 2)))
    perc_hisp = df_new.perc_hisp.mean()
    st.sidebar.write('Percentage Hispanic: {}'.format(round(perc_hisp, 2)))
    perc_white= df_new.perc_white.mean()
    st.sidebar.write('Percentage White {}'.format(round(perc_white, 2)))
    median_price_homes_sold = df_new.median_price_homes_sold.mean()
    st.sidebar.write('Median Price Homes Sold {}'.format(round(median_price_homes_sold, 2)))
    racial_diversity_index = df_new.racial_diversity_index.mean()
    st.sidebar.write('Racial Diversity Index {}'.format(round(racial_diversity_index, 2)))
    num_households = df_new.num_households.mean()
    st.sidebar.write('Number Of Households {}'.format(round(num_households, 2)))
    st.sidebar.write(
        'Average demographic data per neighborhood only is used to reduce bias and cannot be taken as an input. Please note that despite this, predictions might still contain demographic biases'
        'This has to be kept in mind when taking action based off a predicted description. Please look at the Causal Lift section to learn more.')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('**Version:** 2.0')
    st.sidebar.image('./images/mcgill_logo.png')
    ##################################################################################################################


    # MODEL INFO
    ##################################################################################################################
    c2 = st.checkbox("Show/Hide Historical Data", False)
    if c2:
          st.subheader("Rows")
          st.write(df_new.head(10))


    st.header('Model Information')
    st.text('Running on Light Gradient Boosting Machine - Tuned with MLfLow Autolog')

    col1, col2,  = st.beta_columns(2)
    col1.subheader('Score Metrics')
    col1.write(model_metrics)

    col2.subheader('Features')
    col2.image('./images/feature_importance.png', width=400)

    mflow_exp = st.beta_expander('MLflow Reporting')
    mflow_exp.subheader('Training Run One')
    mflow_exp.image('./images/911_1.JPG')
    mflow_exp.subheader('Testing Run Two')
    mflow_exp.image('./images/911_2.JPG')
    ##################################################################################################################

    st.header('Our Prediction')

    # GET PREDICTION WITH INPUT
    ##################################################################################################################
    # Get prediction
    column_names = ['Holiday', 'Weekend', 'Neighborhood', 'Premise', 'CallDescription',
                    'median_household_income', 'households_below_poverty', 'perc18_24', 'perc25_64', 'perc65up',
                    'perc_asian', 'perc_aa', 'perc_hisp', 'perc_white', 'median_price_homes_sold', 'racial_diversity_index', 'num_households',
                    'Outside', 'Weapon_FIREARM', 'Weapon_HANDS', 'Weapon_KNIFE', 'Weapon_NONE', 'Weapon_OTHER', 'Month','Hour',
                    'Priority_HIGH', 'Priority_LOW', 'Priority_MEDIUM', 'Priority_NON-EMERGENCY', 'Priority_OUT OF SERVICE', 'Priority_UNKNOWN', 'crime_hour']


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

    p_high, p_low, p_med, p_non_em, p_out_service, p_ukn = 0, 0, 0, 0, 0, 0
    if priority == 'HIGH':
        p_high = 1
    if priority == 'MEDIUM':
        p_med = 1
    if priority == 'LOW':
        p_low = 1
    if priority == 'NON-EMERGENCY':
        p_non_em = 1
    if priority == 'OUT OF SERVICE':
        p_ukn = 1
    if priority == 'UNKNOWN':
        p_ukn = 1

    holiday_bn = 0
    if holiday == 'YES':
        holiday_bn = 1

    weekend_bn = 0
    if weekend == 'YES':
        weekend_bn = 1


    neighborhood_enc = neighborhood_decoder[nb_types]
    premise_enc = premise_decoder[premise_types]

    X = pd.DataFrame(data=[holiday_bn, weekend_bn, neighborhood_enc, premise_enc, call_desc_decoded,
                           median_household_income, households_below_poverty, perc18_24, perc25_64, perc65up, perc_asian,
                           perc_aa, perc_hisp, perc_white, median_price_homes_sold, racial_diversity_index, num_households,
                           outside, wp_firearm, wp_hands, wp_knife, wp_none, wp_other,
                           months, hours, p_high, p_med, p_low, p_non_em, p_out_service, p_ukn, crime_hour])

    col3, col4,  = st.beta_columns(2)

    col3.subheader('Prediction Input')
    X_disp = X.T
    X_disp.columns = column_names
    X_disp = X_disp.transpose()
    X_disp.columns = ['Values']
    col3.write(X_disp)

    prediction_prob, prediction = predict_description(X.T, model_txt)


    #print(description_decoder.values())
    prediction_prob_df = pd.DataFrame(columns=description_decoder.values(), data=np.round(prediction_prob, 2))
    prediction_prob = prediction_prob_df
    # prediction_prob.columns = ['Probability']
    # prediction_prob['Probability'] = None]
    prediction_prob['Index'] = 'Probability'
    prediction_prob.set_index(['Index'], inplace=True)
    st.write(prediction_prob)
    st.subheader('Types Of Crimes')
    #st.text(prediction)
    st.text('Most likely crime type given the profile: {}'.format(description_decoder[prediction]))



    midpoint = [np.average(df['latitude']), np.average(df['longitude'])]
    st.header('Searching Map Based On Historical Data')
    st.map((df.query('(Location == @location_types) & (Month == @months) & (Weapon == @weapon_types) & (Hour == @hours) & (Premise == @premise_types)')[['latitude', 'longitude']]))
    ##################################################################################################################

    # CAUSAL LIFT
    ##################################################################################################################
    exp_causal = st.beta_expander('Demographic Causal Lift Analysis')
    exp_causal.text('An example of causal model setup we want to predict. '
            'Where we use demographic data as treatment to analyze effects on description. '
            'This helps us better understand issues related to bias/fairness.')
    exp_causal.image('./images/causal_model.png')
    exp_causal.text('Here we present some of our significant findings. We used a mean total value and assign treatment to false if it is below it.')

    demographic_type = exp_causal.selectbox(
        'Chose a demographic treatment variable',
        ('Median House Income', 'Poverty Level', 'Percentage 18-24', 'Percentage 25-64', 'Percentage Asian',
         'Percentage African American', 'Percentage  Hispanic', 'Percentage White', 'Median Price Homes Sold')
    )
    if demographic_type == 'Median House Income':
        exp_causal.image('./images/cl_1.png')
    if demographic_type == 'Poverty Level':
        exp_causal.image('./images/cl_9.png')
    if demographic_type == 'Percentage 18-24':
        exp_causal.image('./images/cl_2.png')
    if demographic_type == 'Percentage 25-64':
        exp_causal.image('./images/cl_3.png')
    if demographic_type == 'Percentage Asian':
        exp_causal.image('./images/cl_4.png')
    if demographic_type == 'Percentage African American':
        exp_causal.image('./images/cl_5.png')
    if demographic_type == 'Percentage Hispanic':
        exp_causal.image('./images/cl_6.png')
    if demographic_type == 'Percentage White':
        exp_causal.image('./images/cl_7.png')
    if demographic_type == 'Median Price Homes Sold':
        exp_causal.image('./images/cl_8.png')
    ##################################################################################################################

    # OTHER INFO
    ##################################################################################################################
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

    if admin:
        expander_2 = st.beta_expander('Model Text Output')
        expander_2.text(model_txt)
    ##################################################################################################################

    st.write('A subset of the training data has been used for demonstration purposed when predicting descriptions.')

# AUTHENTICATION
if session_state.password != 'dzcm21bpd':
    st.text('Please enter the administrator password')
    pwd_placeholder = st.empty()
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    session_state.password = pwd
    if session_state.password == 'dzcm21bpd':
        pwd_placeholder.empty()
        main()
    else:
        st.error("the password you entered is incorrect")
else:
    main()