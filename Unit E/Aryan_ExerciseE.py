'''
Aryan Singhal
CIS 41A   Winter 2024
Unit E, Exercise E
'''

scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]

movie_name = input("Enter the name of a movie: ")

if movie_name in scifi:
    print(f"{movie_name} is a Sci-Fi movie.")
elif movie_name in comedy:
    print(f"{movie_name} is a Comedy movie.")
else:
    print(f"Sorry, I don't know what kind of movie {movie_name} is.")

for i in range(10, -1, -2):
    print(i)

movies = {
    "The Wizard of Oz": 1939,
    "The Godfather": 1972,
    "Lawrence of Arabia": 1962,
    "Raging Bull": 1980
}
for movie in sorted(movies):
    print(f"{movie} was made in {movies[movie]}")


'''
Execution results:

Enter the name of a movie: Moon
Moon is a Sci-Fi movie.
Enter the name of a movie: Superbad
Superbad is a Comedy movie.
Enter the name of a movie: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.

10
8
6
4
2
0

Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939
'''