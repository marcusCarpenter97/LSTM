
import numpy as np
from keras.utils import to_categorical
from datetime import datetime
from operator import itemgetter

CombinedDataSet = "/mnt/c/Users/mc844/OneDrive - University of exeter/Project/Data/Breach Database - 11.20.19 (Combined).csv"
GPSDataSet = "/mnt/c/Users/mc844/OneDrive - University of exeter/Project/Data/Breach Database - 11.20.19 (GPS).csv"
StateDataSet = "/mnt/c/Users/mc844/OneDrive - University of exeter/Project/Data/Breach Database - 11.20.19 (States).csv"
dataSet = []

def load_data(d_name):
    """load_data

    :param d_name: string
    Load data from an npz file into memory.
    """
    #This is required to change the np.load function into accepting pickle files.
    old_load = np.load
    np.load = lambda *a, **k: old_load(*a, allow_pickle=True, **k)

    # Load the data.
    a = np.load(d_name)

    # Reset the nl.load function.
    np.load = old_load
    return a

def count_states(dataSet):
    """count_states

    :param dataSet: list of lists
    Assign each state with a unique integer.
    """
    statesDict = {}
    maxStates = 51
    statesCount = 1
   # for each line
   # if new state
   #  save state 
   #  inc count
   # if conut > 51 stop
   # for each line
   #  check state in dict and swapin list
    for line in dataSet:
        # If the state is new then add it to the dictionary.
        if line[1] not in statesDict:
            statesDict[line[1]] = statesCount
            statesCount +=1
        # All states have been found.
        if statesCount > maxStates:
            break
    # Replace the states with their count.
    for i, line in enumerate(dataSet):
        dataSet[i][1] = statesDict[line[1]]

    return dataSet

def convert_state_to_onehot(dataSet):
    """convert_state_and_type_to_onehot

    :param dataSet: list of lists
    """

    # Extract relevant sections from the table.
    tempStates = dataSet[:, [1]]
    #tempTypes = dataSet[:, [2]]

    # Convert the strings into integers.	
    #tempStates = count_states(tempStates)
    #tempTypes = count_states(tempTypes)

    # Convert the integers into one-hot vectors.
    tempStates = to_categorical(tempStates)
    #tempTypes = to_categorical(tempTypes)

    for i, line in enumerate(dataSet):
        dataSet[i][1] = tempStates[i] 
        #line[2] = tempTypes[i] 

    return dataSet

def sort_by_date(dataSet):
    """sort_by_date

    :param dataSet: list of lists
    :return dataSet: list of lists 
    """
    # Convert date strings to datetime
    for l, line in enumerate(dataSet):
        dataSet[l][0] = datetime.strptime(line[0], '%m/%d/%Y')

    dataSet = sorted(dataSet, key=itemgetter(0))

    # Convert datetime to strings 
    for l, line in enumerate(dataSet):
        dataSet[l][0] = datetime.strftime(line[0], '%m/%d/%Y')

    return dataSet

def convert_date_to_int(dataSet):
    """convert_date_to_int

    :param dataSet: list of lists
    :return dataSet: list of lists

    Assumes the dates are sorted in ascending order (oldest to newest). 
    Assigns a unique integer to each unique date.
    Two identical dates will have the same integer value.
    """
    datesAsInts = [1]
    dataSet[0][0] = datesAsInts[-1]
    iterData = iter(dataSet)
    prevDate = next(iterData)[0]
    
    for i, line in enumerate(iterData):
        currDate = line[0]
        if currDate == prevDate:
            datesAsInts.append(datesAsInts[-1])
        else:
            # Increment last number in the sequence and add it to the list.
            datesAsInts.append(datesAsInts[-1]+1)
        prevDate = currDate
        dataSet[i+1][0] = datesAsInts[-1]
    
    return dataSet

def read_data_from_csv(d_name):
    """read_data_from_csv

    :param d_name: string
    """
    # Read data from csv.
    with open(d_name) as csv_file:
        for line in csv_file:
            dataSet.append(line.strip().split(','))
    
    return dataSet

if __name__ == "__main__":

    dataSet = read_data_from_csv(CombinedDataSet)
    dataSet = sort_by_date(dataSet)
    dataSet = convert_date_to_int(dataSet)
    
    dataSet = np.array(dataSet) # Change from a python list to a nympy array.
    dataSet = convert_state_to_onehot(dataSet)

    dataSet = np.delete(dataSet, 1, 1) # Remove 'City' columnn.
    dataSet = np.delete(dataSet, 5, 1) # Remove 'Longitude' columnn.
    dataSet = np.delete(dataSet, 4, 1) # Remove 'Latitude' columnn.

    for line in dataSet:
        print(line)
    #dates = []
    # Create a list of dates from the dataSet.
    #for i in dataSet:
     #   dates.append(i[0])
##
#    # save it as integers.
#    intDataSet = np.array(dates)
#    np.savez("intData", intDataSet)
#    #print(dates)
#    # Convert the dates into one-hot vectors.
#    encodedDataSet = to_categorical(dates, num_classes=386)
#    #with np.printoptions(threshold=np.inf):
#    #    print(encodedDataSet) 
#    # Save it in a .npz file. 
#    npDataSet = np.array(encodedDataSet)
#    np.savez("data", npDataSet)
#
#    a = load_data("data.npz")['arr_0']
#    b = load_data("intData.npz")['arr_0']
#    print(a[0])
#    with np.printoptions(threshold=np.inf):
#        print(b)
#    #print(a.shape[1])
#    #print('hello')
#    #print(a['arr_0'])
#    #print(a['arr_0'][0])
#    #print(type(a['arr_0'][0]))
#    #b = list(load_data()['arr_0'])
#    #print(b)
