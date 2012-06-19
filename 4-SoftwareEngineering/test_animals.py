import animals

def test_read_animals_file():
    '''
    This is a testing function for read_animals_file.
    '''

    filename = 'animals.txt'
    date, time, animal, counts = animals.read_animals_file(filename)

    # reference data
    # 2011-04-22 21:06 Grizzly 36
    # 2011-04-23 14:12 Elk 25
    # 2011-04-23 10:24 Elk 26
    # 2011-04-23 20:08 Wolverine 31
    # 2011-04-23 18:46 Muskox 20

    ref_date = ['2011-04-22','2011-04-23','2011-04-23',
                '2011-04-23','2011-04-23']

    ref_time = ['21:06', '14:12', '10:24', '20:08', '18:46']

    ref_animal = ['Grizzly','Elk','Elk','Wolverine','Muskox']
    
    ref_counts = [36,25,26,31,20]

    assert date == ref_date, 'dates do not match'
    assert time == ref_time, 'times do not match'
    assert animal == ref_animal, 'animals do not match'
    assert counts == ref_counts , 'counts do not match'


# to use when comparing floating point numbers
from numpy import testing

def test_animal_mean():
    
    ref_numbers = [1.,4.,5.,10.,10.,14.,8.,7.]
    ref_mean = 7.375

    func_mean = animals.animal_mean(ref_numbers)
    assert abs(ref_mean - func_mean) < 1.0e-5, 'func_mean does not match ref_mean'
    testing.assert_almost_equal(animals.animal_mean(ref_numbers),ref_mean)


# to use to check for zero-division errors
from nose.tools import raises

@raises(ZeroDivisionError)
def test_mean_empty_list():
    animals.animal_mean([])


def test_get_animal():
    '''
    Test the get_animal function
    '''

    fname = 'animals.txt'
    animal = 'Elk'

    # reference data
    # 2011-04-22 21:06 Grizzly 36
    # 2011-04-23 14:12 Elk 25
    # 2011-04-23 10:24 Elk 26
    # 2011-04-23 20:08 Wolverine 31
    # 2011-04-23 18:46 Muskox 20

    elk_dates = ['2011-04-23','2011-04-23']
    elk_times = ['14:12','10:24']
    elk_sightings = [25,26]
    
    data = animals.read_animals_file(fname)
    test_dates, test_times, test_sightings = (
        animals.get_animal(data,animal)
        )

    assert test_dates == elk_dates, 'test_dates not same as elk_dates'
    assert test_times == elk_times, 'test_times not same as elk_times'
    assert test_sightings == elk_sightings, 'test_sightings not same as elk_sightings'


def test_get_mean_animal_sightings():
    '''
    Test the get_mean_animal_sightings function
    '''

    fname = 'animals.txt'
    animal = 'Elk'

    data = animals.read_animals_file(fname)
    mean_sightings = animals.get_mean_animal_sightings(data,animal)

    expected_mean_sightings = 25.5

    assert expected_mean_sightings == mean_sightings, 'mean sightings do not match'



# testing the functions manually
# don't need this for nosetests
if __name__ == '__main__':
    print('running test_read_animals_file...')
    test_read_animals_file()

    print('running test_animal_mean...')
    test_animal_mean()


