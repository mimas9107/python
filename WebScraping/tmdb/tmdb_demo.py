import streamlit as st
import requests
import random
import os
import pandas as pd

TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZGZiNjA1OWVkMTJjMzkxOWZmNGZhZThhMjgxZTM4NSIsIm5iZiI6MTczNzM1MTAzMS42MTQsInN1YiI6IjY3OGRkZjc3NDJmMjdjNzU0YzY1M2M1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jmou5ZXXYR5plGIjjXLZrvFTHgM94SUDIg4qPfL9EaQ'
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"

# Function to fetch movie genres
def fetch_movie_genres():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }
    url = "https://api.themoviedb.org/3/genre/movie/list"
    response = requests.get(url, headers=headers)

    data = response.json()
    genres = {genre['name']: genre['id'] for genre in data['genres']}
    return genres

def fetch_top_popular_movies_by_genre_year(genre_id, year):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }
    url = "https://api.themoviedb.org/3/discover/movie"
    http_params = {
        'include_adult': False,
        'include_video': False,
        'language': 'en-US',
        'page': 1,
        'sort_by': 'popularity.desc',
        'with_genres': genre_id,
        'year': year
    }

    response = requests.get(url, params=http_params, headers=headers)
    data = response.json()

    return data['results']

# Function to fetch all movies by genre and year
def fetch_all_movies_by_genre_year(genre_id, year):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }
    url = "https://api.themoviedb.org/3/discover/movie"
    http_params = {
        'include_adult': False,
        'include_video': False,
        'language': 'en-US',
        'page': 1,
        'sort_by': 'popularity.desc',
        'with_genres': genre_id,
        'year': year
    }

    response = requests.get(url, params=http_params, headers=headers)
    data = response.json()
    total_pages = data['total_pages']
    total_results = data['total_results']

    movie_list = []
    for i in range(1, total_pages+1):
        http_params['page'] = i
        response = requests.get(url, params=http_params, headers=headers)
        data = response.json()
        movie_list = movie_list + data['results']
        print('page', i, '/', total_pages, 'fetched successfully')

    if len(movie_list) == total_results:
        print('All movies fetched successfully')
    else:
        print('Failed to fetch all movies')
    return movie_list

def download_movie_image(poster_path, save_path):
    if not poster_path:
        return
    response = requests.get(TMDB_IMAGE_BASE_URL + poster_path, stream=True)
    if response.status_code == 200:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, poster_path.split('/')[-1]), 'wb') as f:
            f.write(response.content)

# Main function
def main_by_streamlit():
    st.title("Movie Genre Explorer")
    
    # Fetch movie genres
    genres = fetch_movie_genres()
    
    # Let user select genre
    selected_genre = st.selectbox("Select a genre", list(genres.keys()))

    # Let user select year
    years = {f'{year}': year for year in range(2024, 1980, -1)}
    selected_year = st.selectbox("Select an year", list(years.keys()))
    
    # Fetch and display movies for the selected genre
    if st.button("Show Movies"):
        genre_id = genres[selected_genre]
        year = years[selected_year]
        movies = fetch_top_popular_movies_by_genre_year(genre_id, year)
        st.write(f"Movies in {selected_genre} in year {year}:")
        for movie in movies:
            title = movie['title']
            poster_path = movie['poster_path']
            if poster_path != None:
                st.image(TMDB_IMAGE_BASE_URL + poster_path, caption=title)
            st.write('Release Date: ', movie['release_date'])
            st.write('Overview: ',  movie['overview'])

def main():
    # Fetch movie genres
    genres = fetch_movie_genres()
    selected_genre = random.choice(list(genres.keys()))

    # Let user select year
    years = {f'{year}': year for year in range(2024, 1980, -1)}
    selected_year = random.choice(list(years.keys()))

    print('Feathing movies of', selected_genre, 'in the year', selected_year, '...')

    # Fetch and display movies for the selected genre
    genre_id = genres[selected_genre]
    year = years[selected_year]
    movies = fetch_all_movies_by_genre_year(genre_id, year)

    df = pd.DataFrame(movies)
    df.to_csv(f'movies_{selected_year}_{selected_genre}.csv', index=False)

if __name__ == "__main__":
    main_by_streamlit()
    # main()
