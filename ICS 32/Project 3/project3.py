import api
import method

def directions():
    '''Gives directions and more'''
    try:
        num = int(input())
        if num < 2:
            print('You must specify at least two locations')
            return

        places = _locations(num)

        url = api.create_url(places)

        json = api.get_json(url)

        elev_url = api.create_elev_url(json)
        elev_json = api.get_elev_json(elev_url)

        latlong, direct, time, distance, elevates = api.parse_json(json, elev_json)

        stats = method.map(latlong, direct, time, distance, elevates)

        num_options = int(input())
        response = []
        for i in range(num_options):
            options = input()
            if options == 'STEPS':
                response.append(stats.steps())
                response.append('')
            elif options == 'TOTALDISTANCE':
                response.append(stats.totaldistance())
                response.append('')
            elif options == 'TOTALTIME':
                response.append(stats.totaltime())
                response.append('')
            elif options == 'LATLONG':
                response.append(stats.latlong())
                response.append('')
            elif options == 'ELEVATION':
                response.append(stats.elevation())
                response.append('')

        if None in response:
            print()
            print('NO ROUTE FOUND')
        else:
            print()
            for i in response:
                print(i)

            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except:
        print('\n')
        print('MAPQUEST ERROR')

def _locations(num_of_loc: int) -> [tuple]:
    loc = []

    start_place = input()
    loc.append(('from', start_place))

    for i in range(num_of_loc - 1):
        next_place = input()
        loc.append(('to', next_place))

    return loc

if __name__ == "__main__":
    directions()