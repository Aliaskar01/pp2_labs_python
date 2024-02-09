from movie import movie

movies = movie()

def avarage(takes):
    sum = 0
    devide = 0
    for take in takes:
        has = False
        for movie in movies:
            if take == movie["name"]:
                has = True
                sum += movie["imdb"]
                devide += 1
    if devide == 0:
        devide = 1
    return sum / devide

takes = input()
takes = takes.split(", ")
print(avarage(takes))