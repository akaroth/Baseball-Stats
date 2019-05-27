import pandas as pd
import numpy as np
from sklearn import linear_model
from scipy import stats
import matplotlib.pyplot as plt
%matplotlib inline

# Read games logs from the 2015 season into a dataframe
input_df = pd.read_table("GL2015.TXT", sep=",", header=None)
