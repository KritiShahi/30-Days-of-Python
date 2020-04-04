"""1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name,
the release year of the movie, and the movie’s budget."""
movies = [('The Intern', 'Nancy Meyers', '2015', '$35 million')]

"""2. Use the input function to gather information about another movie. You need a title, director’s name, 
release year, and budget."""
title = input("Enter the name of movie ")
director_name = input("Enter the name of director ")
release_year = input("Enter the release year ")
budget = input("Enter the budget ")

"""3. Create a new tuple from the values you gathered using input. Make sure they’re in the 
same order as the tuple you wrote in the movies list."""
movie = title, director_name, release_year, budget

# 4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{movie[0]} movie released in year {movie[2]}")

# 5. Add the new movie tuple to the movies collection using append.
movies.append(movie)

# 6. Print both movies in the movies collection.
print(f"{movies[0]} and {movies[1]}")

# 7. Remove the first movie from movies. Use any method you like.
movies.pop(0)
