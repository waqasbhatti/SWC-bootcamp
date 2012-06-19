#!/usr/bin/env python

def read_animals_file(fname):
    '''
    Reads an animal file and returns the columns as lists.
    '''

    # open the file
    f = open(fname,'r')
    
    # setup the lists
    date, time, animal, number = [], [], [], []
    
    # iterate through the file and get the columns into the lists
    for line in f:
        d, t, a, n = line.split()
        date.append(d)
        time.append(t)
        animal.append(a)
        number.append(int(n))

    # close the file
    f.close()

    # return the lists
    return (date, time, animal, number)

