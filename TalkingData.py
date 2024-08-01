#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "50 First Dates"
print("My favorite movie is: " + favMovie)

#Part 3 Investigate the data

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
favMovieData = movieData.loc[favMovieBooleanList]
favMovieRating= favMovieData.iloc[0]["audience_rating"]

print("My faorite movie : " + favMovie)
print ("Audience rating is: " + str(favMovieRating))

print("\n\n")

#Create a new variable to store a new data set with a certain genre

comedyMovieBooleanList = movieData["genres"].str.contains("Comedy")
comedyMovieData = movieData.loc[comedyMovieBooleanList]


numOfMovies = comedyMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Comedy in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Comedy.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = comedyMovieData["audience_rating"].min()
difference = favMovieRating - min
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(difference) + " points higher than the lowest rated movie.")
print()

#find max
max = comedyMovieData["audience_rating"].max()
difference = max - favMovieRating
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(difference) + " points lower than the highest rated movie.")
print()

#find mean
mean = comedyMovieData["audience_rating"].mean()
if favMovieRating > mean:
      compare = "higher than"
elif favMovieRating < mean:
      compare = "lesser than"
else:
      compare = "same as"
      


print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is " + compare + " the mean movie rating.")

#find median
median = comedyMovieData["audience_rating"].median()
if favMovieRating > median:
      compare = "higher than"
elif favMovieRating < median:
      compare = "lesser than"
else:
      compare = "same as"
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is " + compare + " the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(comedyMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Comedy Movies Histogram")
plt.xlabel("Audiene Ratings")
plt.ylabel("Num of Comedy Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, ..."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = comedyMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, ..."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
