import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation

import keras
import string

# fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = [series[s : s + window_size] for s in range(len(series) - window_size)]
    y = [series[s + window_size] for s in range(len(series) - window_size)]

    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
              
    return model              
              
              
### return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):

    ascii_letters = string.ascii_letters
    punctuation = ['!', ',', '.', ':', ';', '?']

    for t in text:
        if t not in ascii_letters and t not in punctuation:
            text = text.replace(t, ' ')

    return text.lower()

###  fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs=[]
    outputs=[]
    
    for t in range(0, len(text)-window_size, step_size):
        #get current text window array and append it to x:
        inputs.append(text[t:(t+window_size)])
        #append output
        outputs.append(text[(t+window_size)])

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
              
    return model              
