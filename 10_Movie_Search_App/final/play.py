import requests
import collections

MoveResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration,director, year, rating, imdb_score, keywords, generes'
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
    m = MoveResult(
        imdb_code=md.get('imdb_code'),
        title=md.get('title'),
        duration=md.get('duration'),
        director=md.get('director'),
        year=md.get('year', 0),
        rating=md.get('rating', 0),
        imdb_score=md.get('imdb_score', 0.0),
        keywords=md.get('keywords'),
        generes=md.get('generes')
    )
    movies.append(m)

print("Found {} movies for search {}".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))