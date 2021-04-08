# local imports
import pytest
from App import app
df, df_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder = app.load_data('app/data/BPD_CRIME_DATA_CLEAN_ST.csv', 'app/data/Description_decoder_2.csv',
                                                                         'app/data/District_decoder.csv', 'app/data/Neighborhood_decoder.csv', 'app/data/Premise_decoder.csv', './MODEL.txt', 'app/data/Score_metrics.csv')


def test_minimum_model_accuracy():
    assert model_metrics.iloc[0, 1] >= 40, 'Model accuracy below 40%'


def test_null_prediction():
    assert len(app.prediction_prob) > 0, 'Null prediction probability'

def test_valid_prediction():
    prediction = app.predict_description(app.X.T, model_txt)
    print(prediction)
    assert (prediction[1] > -1) or (prediction[1] < 14), 'Invalid prediction'