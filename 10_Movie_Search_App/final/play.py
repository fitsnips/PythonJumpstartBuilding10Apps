import requests
import collections

MoveResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration,director, year, rating, imdb_score, keywords, genres'
)

search = input("Search string: ")
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)


resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

#print(type(movie_data), movie_data)
#print(type(movies_list), movies_list)


movies = []
for md in movies_list:
    m = MoveResult(**md)
    movies.append(m)

print("Found {} movies for search {}".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))