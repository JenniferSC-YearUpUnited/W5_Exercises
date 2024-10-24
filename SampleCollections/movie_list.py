fav_movies = ['La Bamba', 'Selena', 'The Equalizer', 'Spiderman into the verse']
length = len(fav_movies)
print(length)
print(" The list", fav_movies, "includes my top", len(fav_movies), "favorite movies.")
sorted_fav_movies = sorted(fav_movies)
print(sorted_fav_movies)
print(fav_movies)
# When I compare the two outputs I see that sorted () function will list my items in alphabetical order but when I remove the function it returns them back to the order I initally had the items in.
fav_movies.sort()
print(fav_movies)
# When I compare the two outputs I see that it sorted my items alphabetically without having to create a new variable. 
fav_movies.append("A Million Miles Away")
print("The list", fav_movies, "not only does it include my top", len(fav_movies), "favorite movies but it also includes an inspirational biopic.")

