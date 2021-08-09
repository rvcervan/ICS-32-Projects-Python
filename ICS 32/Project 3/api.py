import urllib.request
import urllib.parse
import json

def create_url(locations: [[list]]) -> str:
    '''gets the mapquest url'''

    url = 'http://open.mapquestapi.com/directions/v2/route?'

    key = 'E2fG3jnDpGP4wf4UlBr1HsWEIztceKAk'
    key = 'key=' + key + '&'

    query = urllib.parse.urlencode(locations)

    return url + key + query

def get_json(url: str) -> json:
    '''from url, gets json'''

    response = urllib.request.urlopen(url)

    data = response.read()
    response.close()

    text = data.decode(encoding = 'utf-8')

    return text

def parse_json(string_json: str, elev_json: list):
    '''parses through json to get key info'''
    try:
        obj = json.loads(string_json)

        LL = []
        latlong = obj['route']['locations']
        for i in latlong:
            if i['latLng']['lat'] < 0:
                x = ("{:.2f}S".format(abs(i["latLng"]['lat'])))
            else:
                x = ("{:.2f}N".format(abs(i['latLng']['lat'])))
            if i['latLng']['lng'] < 0:
                y = ("{:.2f}W".format(abs(i["latLng"]['lng'])))
            else:
                y = ("{:.2f}E".format(abs(i["latLng"]['lnt'])))
            LL.append(x + ' ' + y)



        direct = []
        steps = obj['route']['legs']
        for i in steps:
            for x in i['maneuvers']:
                direct.append(x['narrative'])

        time = 0
        totaltime = obj['route']['legs']
        for i in totaltime:
            time += i['time']


        distance = 0
        totaldistance = obj['route']['legs']
        for i in totaldistance:
            distance += i['distance']



        elevates = []
        for i in elev_json:
            elev_obj = json.loads(i)
            for x in elev_obj['elevationProfile']:
                elevates.append(str(round(x['height'] * 3.28084)))

        return LL, direct, time, distance, elevates
    except KeyError:
        LL = None
        direct = None
        time = None
        distance = None
        elevates = None
        return LL, direct, time, distance, elevates


def create_elev_url(string_json: str):
    try:
        url = 'http://open.mapquestapi.com/elevation/v1/profile?'

        key = 'E2fG3jnDpGP4wf4UlBr1HsWEIztceKAk'
        key = 'key=' + key + '&'
        query = 'shapeFormat=raw&latLngCollection='
        latlongs = []
        obj = json.loads(string_json)
        for i in obj['route']['locations']:
            x = i['latLng']['lat']
            y = i['latLng']['lng']

            latlongs.append(url + key + query + '{},{}'.format(str(x),str(y)))

        return latlongs
    except KeyError:
        return None
def get_elev_json(url: list) -> json:
    '''from url, gets elevation json'''
    try:
        jsons = []
        for i in url:

            response = urllib.request.urlopen(i)

            data = response.read()
            response.close()

            text = data.decode(encoding='utf-8')

            jsons.append(text)
        return jsons
    except TypeError:
        return None


