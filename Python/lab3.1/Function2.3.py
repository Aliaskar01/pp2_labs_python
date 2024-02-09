from movie import movie

movies = movie()

def category(category):
    has = False
    for movie in movies:
        if movie["category"] == category:
            has = True
            print(movie)
    if not has:
        print()

name = input()
category(name)