import requests

apikey = "a26b0a0256b9ce48bb14c97059c9d85646a41991"
url = "http://comicvine.gamespot.com/api"

from simyan.comicvine import Comicvine
from simyan.sqlite_cache import SQLiteCache

session = Comicvine(api_key=apikey, cache=SQLiteCache())

# Search for Publisher
results = session.list_characters(params={"filter": "name:Emma Frost"})

print(results[0].date_last_updated)