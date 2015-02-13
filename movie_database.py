from urllib.request import urlopen
import json

class Movie:

  def find_highest_rated(filename):
    with open(filename, encoding='utf-8') as f:
      winning_movie_data = None
      highest_rating = 0
      for line in f:
        movie_data = line.split(",")
        rating = float(movie_data[3])
        if rating > highest_rating:
          highest_rating = rating
          winning_movie_data = movie_data

    best_movie = Movie()
    best_movie.id = winning_movie_data[0]
    best_movie.title = winning_movie_data[1]
    best_movie.director = winning_movie_data[2]
    best_movie.imdb_rating = float(winning_movie_data[3])
    return best_movie

  def plot(self):
    webservice_url = "http://www.omdbapi.com/?i=" + self.id + "&plot=short&r=json"
    data = urlopen(webservice_url).read().decode('utf-8')
    result = json.loads(data)
    return result["Plot"]

