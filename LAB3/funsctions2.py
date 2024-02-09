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
}]

#ex1


def above_5_5(movie):
    return movie["imdb"] > 5.5

def check_movies(movies_list):
    for movie in movies_list:
        if above_5_5(movie):
            print(f"{movie['name']}: True")
        else:
            print(f"{movie['name']}: False")

check_movies(movies)

#ex2


def movies_above_5_5(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]

result = movies_above_5_5(movies)
for movie in result:
    print(movie["name"])

#ex3
    
def movies_by_category(category_name, movies_list):
    return [movie for movie in movies_list if movie["category"] == category_name]


category_name = input("Which category do you prefer? ")
result = movies_by_category(category_name, movies)

if result:
    print(f"These movies can be suitable for you: '{category_name}':")
    for movie in result:
        print(movie["name"])
else:
    print(f"Error'{category_name}'.")

#ex4

def average_score(movies_list):
    if not movies_list:
        return 0  
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)


avg_score = average_score(movies)
print(avg_score)

#ex5

def average_category(category_name, movies_list):
    category_movies = [movie for movie in movies_list if movie["category"] == category_name]
    if category_movies:
        return sum(movie["imdb"] for movie in category_movies) / len(category_movies)
    return 0

category_name = input("Which category do you prefer: ")
avg_score = average_category(category_name, movies)
print(avg_score)
