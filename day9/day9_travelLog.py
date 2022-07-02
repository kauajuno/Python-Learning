def add_country(country, times_visited, cities_visited):
    new_country = {}
    new_country.update({'country': country, 'times v.': times_visited, 'cities v.': cities_visited.split(', ')})
    travel_log.append(new_country)


travel_log = []
flag = True

while flag is True:
    if input('WDS? y/n\n') == 'y':
        print('Choose an operation: \n')
        print('1. See travel log\n')
        print('2. Update travel log\n')
        operation = input()
        if operation == '1':
            print(travel_log)
        elif operation == '2':
            add_country(input('Country\n'), input('Times visited\n'), input('Cities visited\n'))
    else:
        flag = False
