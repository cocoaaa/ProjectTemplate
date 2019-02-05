from src.dataops import read_raw_data, preprocess_data, get_features, get_label

def test_raw_shape():
    data = read_raw_data()
    assert (data.shape == (1300,1300,3))

def test_get_features_shape():
    data = read_raw_data()
    processed = preprocess_data(data)
    features = get_features(processed)
    labels = get_labels(processed)
    
    assert( features.shape == (1300,1300,3) )
    assert( labels.shape = (1300,1300,1))