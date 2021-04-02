import pytest
from .. app import load_data
model_txt, model_metrics, description_decoder, district_decoder, neighborhood_decoder, premise_decoder = load_data('../data/BPD_CRIME_DATA_CLEAN_ST.csv', '../data/Description_decoder_2.csv',
                                                                         '../data/District_decoder.csv', '../data/Neighborhood_decoder.csv', '../data/Premise_decoder.csv', '../MODEL.txt', '../data/Score_metrics.csv')

def test_null_inputs():
    # Check that we are not returning null information
    # assert len(data) > 0, 'Null data'
    # assert len(data_sample) > 0, 'Null data sample'
    assert len(model_txt) > 0, 'Null model text file'
    assert len(model_metrics) > 0, 'Null metrics'
    assert len(description_decoder) > 0, 'Null description decoder'
    assert len(district_decoder) > 0, 'Null district decoder'
    assert len(neighborhood_decoder) > 0, 'Null neighborhood decoder'
    assert len(premise_decoder) > 0, 'Null premise decoder'