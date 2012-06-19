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

if __name__ == '__main__':
    print('running tests...')
    test_read_animals_file()

