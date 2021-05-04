# Class to handle dataframe selection based on attributes defined
from sklearn.base import BaseEstimator, TransformerMixin
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribs):
        self.attribs = attribs
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.attribs]
    