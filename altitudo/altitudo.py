# -*- coding: utf-8 -*-

"""Main module."""

import requests
import warnings
from altitudo import __version__


def altitudo(lat, lon, feet=False, session=None, timeout=30):
    """
    Fetch the elevation at the given geo coordinate

    Parameters
        lat: float/iterable - of floats  Latitude
        lon: float/iterable - of floats  Longitude
        feet: bool - To return the elevation in feet instead of meters.
        session: requests.Session() - object if special session is needed. (proxies, ect)
        timeout: int - 
    Returns:
        float/list of floats
    """
    
    session = requests.Session() if session is None else session
    session.headers.update({'ALTITUDO_VERSION': __version__})

    try:
        lat, lon = iter(lat), iter(lon)
        single = False
    except TypeError:
        single = True
        lat, lon = [lat], [lon]

    elevations = []

    points = ''
    current_count = 0
    for latitude, longitude in zip(lat, lon):

        points += '({},{})'.format(latitude, longitude)
        current_count += 1

        if current_count == 50:
            elevations.extend(_get_elevations(points, session, timeout))
            points = ''
            current_count = 0

    if points:
        elevations.extend(_get_elevations(points, session, timeout))

    # Return a list of dicts containing points and associated elevation
    # if more than one coordinate is given, otherwise return the elevation 
    # value itself, as user already knows the coordinates
    if feet:
        [elevation.update({'elevation': _convert_to_feet(elevation['elevation'])}) 
        for elevation in elevations]
    return elevations if not single else elevations[0]['elevation']


def _convert_to_feet(meters):
    return meters * 3.28084


def _get_elevations(points, sess, timeout):
    """
    points: string of tuples, representing lat and lons. ie. '(1.23,2.34),(1.2,4.5)'
    sess: request.Session() to make the requests

    Returns:
        list of the points and the elevations given
    """

    url = 'https://elevation-api.io/api/elevation?points={}'.format(points)
    resp = sess.get(url, timeout=timeout)
    if resp.ok:
        json = resp.json()
        msg = json.get('message')
        if msg:
            warnings.warn(msg, category=UserWarning)
        return json.get('elevations', [])
    else:
        raise IOError(
            'Unable to fetch elevation(s)! Got error code {} from server w/ content: {}'
            .format(resp.status_code, resp.content)
        )
    
