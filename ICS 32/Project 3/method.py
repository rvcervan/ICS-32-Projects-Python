class map:
    def __init__(self, latlong: dict, directions: list, time: int, distance: float, elevations: list):
        self._L = latlong
        self._Steps = directions
        self._T = time
        self._Dist = distance
        self._Elev = elevations


    def latlong(self):
        try:
            x = ''
            x += 'LATLONGS\n'
            for i in self._L:
                x += i + '\n'

            x = x[:-1]

            return x
        except TypeError:
            return

    def steps(self):
        try:
            x = ''
            x += 'DIRECTIONS\n'
            for i in self._Steps:
                x += i + '\n'

            x = x[:-1]

            return x
        except TypeError:
            return
    def totaltime(self):
        try:
            return 'TOTAL TIME: {} minutes'.format(round(self._T/60))
        except TypeError:
            return
    def totaldistance(self):
        try:
            return 'TOTAL DISTANCE: {} miles'.format(round(self._Dist))
        except TypeError:
            return
    def elevation(self):
        try:
            x = ''
            x += 'ELEVATIONS\n'
            for i in self._Elev:
                x += i + '\n'

            x = x[:-1]

            return x
        except TypeError:
            return