# univariate lstm example
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from preprocessDataBreach import load_data

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    x, y = list(), list()
    length = sequence.shape[1]
    for i in range(length):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > length-1:
                break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

# define input sequence
#raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
raw_seq = load_data("data.npz")['arr_0'] # convert numpy array to list
#print(raw_seq)
# choose a number of time steps
n_steps = 3 # how many samples at once
# split into samples
x, y = split_sequence(raw_seq, n_steps)
#print(f'x\n {x}')
#print(f'y\n {y}')
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 386 # size of each sample
print(x.shape)
#x = x.reshape(x, (x.shape[0], x.shape[1]))
#print(x.shape)
#print(f'reshape x\n {x}')
# define model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(386))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(x, y, epochs=200, verbose=0)
# demonstrate prediction
x_input = x[-1] 
x_input = x_input.reshape((1, n_steps, n_features))
print(x_input.shape)
yhat = model.predict(x_input, verbose=0)
print(yhat)
