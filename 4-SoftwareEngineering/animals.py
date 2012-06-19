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

def animal_mean(numbers):
    '''
    Gets the mean of the list numbers.
    '''

    mean = sum(numbers)/float(len(numbers))

    return mean


def get_animal(data, wanted_animal):
    '''
    Get the dates, times, and sightings of a given animal
    '''

    d, t, a, n = data
    
    animal_dates, animal_times, animal_sightings = [], [], []

    for date, time, animal, sightings in zip(d, t, a, n):

        if animal == wanted_animal:

            animal_dates.append(date)
            animal_times.append(time)
            animal_sightings.append(sightings)

    return animal_dates, animal_times, animal_sightings


def get_mean_animal_sightings(data, wanted_animal):
    '''
    Get the average numbers of sightings for a specified animal.
    '''

    dates, times, sightings = get_animal(data,wanted_animal)
    mean_sightings = animal_mean(sightings)

    return mean_sightings


def get_mean_animal_sightings_from_file(animal, fname):

    data = read_animals_file(fname)
    mean_sightings = get_mean_animal_sightings(data,animal)

    return mean_sightings
