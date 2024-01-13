"""
You can add your own functions here according to your decision tree implementation.
There is no restriction on following the below template, these fucntions are here to simply help you.
"""

import pandas as pd
import numpy as np

def check_ifreal(y: pd.Series) -> bool:
    """
    Function to check if the given series has real or discrete values
    """
    # print(y.dtype)
    if(y.dtype=='float64'):
        return True
    else:
        return False

    pass


def entropy(Y: pd.Series) -> float:
    """
    Function to calculate the entropy
    """
    return Y.value_counts(normalize=True).apply(lambda x: -x*np.log2(x+1e-6)).sum()
    
    pass


def gini_index(Y: pd.Series) -> float:
    """
    Function to calculate the gini index
    """
    return 1-Y.value_counts(normalize=True).apply(lambda x: x**2).sum()
    pass


def information_gain(Y: pd.Series, attr: pd.Series) -> float:
    """
    Function to calculate the information gain
    """
    entropy_y=entropy(Y)
    info_gain=entropy_y
    total_vals=len(attr)
    for attribute,val in attr.value_counts().items():
        info_gain-=val/total_vals*(entropy(Y[attr == attribute]))

    pass


def opt_split_attribute(X: pd.DataFrame, y: pd.Series, criterion, features: pd.Series):
    """
    Function to find the optimal attribute to split about.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.
    features: pd.Series is a list of all the attributes we have to split upon
    return: attribute to split upon
    """
    if check_ifreal(y):
        pass
    else:
        if(criterion=="information_gain"):
            max_entropy_gain=0
            chosen_attribute=""
            for attribute in features:
                if(y!=X[attribute]):
                    if(information_gain(y,X[attribute])>max_entropy_gain):
                        chosen_attribute=attribute
                        max_entropy_gain=information_gain(y,X[attribute])
        return chosen_attribute
    
    
    # According to wheather the features are real or discrete valued and the criterion, find the attribute from the features series with the maximum information gain (entropy or varinace based on the type of output) or minimum gini index (discrete output).

    pass


def split_data(X: pd.DataFrame, y: pd.Series, attribute, value):
    """
    Funtion to split the data according to an attribute.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    attribute: attribute/feature to split upon
    value: value of that attribute to split upon

    return: splitted data(Input and output)
    """

    # Split the data based on a particular value of a particular attribute. You may use masking as a tool to split the data.
    X_match, y_match = X[X["Outlook"] == "Sunny"], y[X["Outlook"] == "Sunny"]
    return (X_match,y_match)
    pass
