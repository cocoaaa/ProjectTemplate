import sys
import pickle
sys.path.append('src') #because we assume this script will be accessed from the project root directory
from sklearn.ensemble import RandomForestClassifier
from dataops import get_features, get_label

class RandomForestModel(object):
    def __init__(self):
        self.clf = RandomForestClassifier(n_estimator=50, max_depth=700)
        self.name = 'RandomForest'
        pass
    
    def get_params(self):
        pass
    
    def train(self, data):
        X = get_features(data)
        y = get_label(data)
        self.clf.fit(X,y)
    
    def predict(self, X):
        y_pred = self.clf.predict(X)
        return y_pred
    
    def save(self, fname):
        with open(fname, 'wb') as ofile:
            pickle.dump(self.clf, ofile, pickle.HIGHEST_PROTOCOL)
    
    def load(self, fname):
        with open(fname, 'rb') as ifile:
            self.clf = pickle.load(ifile)
            