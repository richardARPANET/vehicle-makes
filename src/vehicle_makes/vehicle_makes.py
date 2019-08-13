import logging

import requests
from requests_futures.sessions import FuturesSession

logger = logging.getLogger(__name__)
_BASE_URI = 'https://www.autotrader.co.uk'


def _get_makes():
    url = f'{_BASE_URI}/json/search/options?advertising-location=at_cars'
    resp = requests.get(url)
    resp.raise_for_status()
    return (r['displayName'] for r in resp.json()['options']['make'])


def get_makes_and_models():
    logger.info('Getting vehicle makes and models...')
    session = FuturesSession()
    futures = []
    for make in _get_makes():
        url = f'{_BASE_URI}/json/search/options?make={make}'
        futures.append((make, session.get(url)))

    makes_and_models = {}
    responses = ((m, f.result()) for m, f in futures)
    for make, response in responses:
        models = tuple(
            r['displayName'] for r in response.json()['options']['model']
        )
        makes_and_models[make] = models
    return makes_and_models
