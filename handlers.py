def addMovies(movies):
    name=input("Enter name: ")
    description=input("Enter Description: ")
    rate=float(input("Enter movie rate: "))
    movies.append({"name":name,"description":description,"rate":rate})


def displayMovies(movies):
    for idx,movie in enumerate(movies,1):
        print(f"{idx}. name: {movie["name"]}\ndescription: {movie["description"]}\n rate: {movie["rate"]}")



def deleteMovies(movies):
    name=input("Enter name: ").lower()
    for movie in movies:
        if movie["name"].lower() == name:
            movies.remove(movie)
            print(f"Deleted Successfully! {movie["name"]}")
        else:
            print(f"Movie doesn't Exist!! {name}")



def searchMovies(movies):
    name=input("Enter name: ").lower()
    for movie in movies:
        if movie["name"].lower() == name:
            print(f"Name: {movie["name"]} description: {movie["description"]} rate: {movie["rate"]}")
        else:
            print(f"Movie doesn't Exist!!!")



def updateMovies(movies):
    name=input("Enter a name for movie to update: ").lower()
    newName=input("Enter new name: ")
    description=input("Enter new description: ")
    rate=float(input("Enter new rate: "))
    for movie in movies:
        if movie["name"].lower() == name:
            movie["name"]= newName
            movie["description"]=description
            movie["rate"]= rate
            print(f"Update name: {newName} description: {description} rate: {rate}")
        else:
            print(f"Movie doesn't exist!!!")



