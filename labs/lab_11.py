import csv

def read_csv_as_dict(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return {row['Title']: row for row in reader}

def highest_grossing_movie(movie_data):
    return max(
        movie_data, 
        key=lambda movie: float(movie_data[movie]['World Wide Sales (in $)']) 
        if movie_data[movie]['World Wide Sales (in $)'].replace('.', '', 1).isdigit() 
        else 0
    )

def highest_grossing_movie_for_year(movie_data, year):
    movies_of_year = {movie: data for movie, data in movie_data.items() if data['Year'] == str(year)}
    return highest_grossing_movie(movies_of_year) if movies_of_year else None

movie_data = read_csv_as_dict('movie_data_shuffled.csv')
print(highest_grossing_movie(movie_data))
print(highest_grossing_movie_for_year(movie_data, 1999))
print(highest_grossing_movie_for_year(movie_data, 1984))
print(highest_grossing_movie_for_year(movie_data, 1973))

def top_grossing_movies(movie_data, top=10):
    return sorted(
        movie_data.items(), 
        key=lambda movie: float(movie[1]['World Wide Sales (in $)']) 
        if movie[1]['World Wide Sales (in $)'].replace('.', '', 1).isdigit() 
        else 0,
        reverse=True
    )[:top]

for i, (title, data) in enumerate(top_grossing_movies(movie_data), start=1):
    sales = "{:,}".format(float(data['World Wide Sales (in $)']))
    print(f"{i}. {title} ({data['Year']}): ${sales}")



