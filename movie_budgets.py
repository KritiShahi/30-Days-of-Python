"""Dataset of movies is given where each item in the list is a tuple containing a movie name and movie budget.
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
For this project, program should do the following:
1. Calculate the average budget of all movies in the data set.
2. Print out every movie that has a budget higher than the average you calculated.
You should also print out how much higher than the average the movie's budget was.
3. Print out how many movies spent more than the average you calculated.
4. Allow users to add more movies to the data set before running the calculations.

You can do this by asking the user how many movies they want to add, which will allow you to use a for loop and
range to repeat some code a given number of times. Inside the for loop, you can write some code that takes in
some user input and appends a movie tuple containing the collected data to the movie list."""
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
n_movies = int(input("Enter the number of movies you want to add in movies dataset"))
for num in range(n_movies):
    movie_name = input("Enter the movie name ")
    movie_budget = int(input("Enter the budget of the movie "))
    movie = (movie_name, movie_budget)
    movies.append(movie)

total_budget = 0
for movie in movies:
    total_budget += movie[1]
avg_budget = int(total_budget / len(movies))

count = 0
for movie in movies:
    if movie[1] > avg_budget:
        print(f"{movie[0]} has ${movie[1] - avg_budget:,} budget higher than average budget ${avg_budget:,}")
        count += 1
print(f"Number of movies that spent more budget than average are {count}")
