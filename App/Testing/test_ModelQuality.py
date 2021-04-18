# local imports
import pytest
from App import app
import os.path as path
two_up = path.abspath(path.join(__file__ ,"../.."))

df, df_sample, model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder = app.load_data('./data/BPD_CRIME_DATA_CLEAN_ST.csv', './data/Description_decoder_2.csv',
                                                                         './data/District_decoder.csv', './data/Neighborhood_decoder.csv', './data/Premise_decoder.csv', './MODEL.txt', './data/Score_metrics.csv')


def test_null_model_input():
    assert len(model_txt) > 0, 'Null model text file'


def test_null_metrics_input():
    assert len(model_metrics) > 0, 'Null metrics'


def test_null_description_decoder_input():
    assert len(description_decoder) > 0, 'Null description decoder'


def test_null_district_decoder_input():
    assert len(district_decoder) > 0, 'Null district decoder'


def test_null_neighborhood_decoder_input():
    assert len(neighborhood_decoder) > 0, 'Null neighborhood decoder'


def test_null_premise_decoder_input():
    assert len(premise_decoder) > 0, 'Null premise decoder'