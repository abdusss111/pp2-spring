# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def is_high_imdb(movie):
    return movie['imdb'] > 5.5


#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def get_movies_above_5_5(movies):
    high_imdb_movies = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            high_imdb_movies.append(movie)
    return high_imdb_movies

#Write a function that takes a category name and returns just those movies under that category.

def get_movie_by_category(movies, category):
    category_movies = []
    for movie in movies:
        if movie['category'] == category:
            category_movies.append(movie)
    return category_movies

def get_movie_by_category(movies, category):
    category_movies = list(filter(lambda movie: movie['category'] == category, movies))
    return category_movies

#Write a function that takes a list of movies and computes the average IMDB score.

def avrg(movies):
    sum = 0
    cnt = 0
    for movie in movies:
        sum += int(movie['imdb'])
        cnt += 1
    return sum/cnt

#Write a function that takes a category and computes the average IMDB score.

def get_movie_by_category(movies, category):
    sum = 0
    cnt = 0
    for movie in movies:
        if movie['category'] == category:
            sum += int(movie['imdb'])
            cnt += 1
