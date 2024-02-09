from movie import movie

movies = movie()

def avarage(category):
    sum = 0
    devide = 0
    for movie in movies:
        if category == movie["category"]:
            sum += movie["imdb"]
            devide += 1
    try:
        return str(sum / devide)
    except:
        return "we don't have this category"
    
name = input()
print(avarage(name))