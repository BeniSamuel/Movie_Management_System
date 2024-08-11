import handlers


movies=[]

def main():

    while True:

        print("\nWelcome to movie management\n1. Add Movie\n2. Display Movie\n3. Delete Movie\n4. Search Movie\n5. Update Movie\n6. Exist")
        choice=int(input("Enter choice: "))

        match choice:
            case 1:
                handlers.addMovies(movies)
            case 2:
                handlers.displayMovies(movies)
            case 3:
                handlers.deleteMovies(movies)
            case 4:
                handlers.searchMovies(movies)
            case 5:
                handlers.updateMovies(movies)
            case 6:
                print("Existing Byee!!")
                break
            case _:
                print("Invalid Choice")





main()