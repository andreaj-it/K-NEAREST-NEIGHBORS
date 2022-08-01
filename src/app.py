import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import ast
import shutil

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

filename = "../assets/tmdb_5000_credits.zip"
extract_dir = "../data/raw"
archive_format = "zip"
 
# Unpack the archive file
shutil.unpack_archive(filename, extract_dir, archive_format)

movies = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv')
credits = pd.read_csv('../data/raw/tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')

movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#movies.isnull().sum()

movies.dropna(inplace = True)
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)

movies['overview'] = movies['overview'].apply(lambda x : x.split())

movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

movies['tags'] = movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']

new_df = movies[['movie_id','title','tags']]

new_df['tags'] = new_df['tags'].apply(lambda x :" ".join(x))

cv = CountVectorizer(max_features=5000 ,stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

cosine_similarity(vectors).shape
similarity = cosine_similarity(vectors)

recommend('Avatar')
