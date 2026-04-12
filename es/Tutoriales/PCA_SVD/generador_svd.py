import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import json
import os

def build_svd_data():
    cwd = os.getcwd()
    print(f"Working in {cwd}")

    # 1. Read u.data
    data_cols = ['user_id', 'item_id', 'rating', 'timestamp']
    ratings_df = pd.read_csv('u.data', sep='\t', names=data_cols)

    # 2. Read u.item
    genre_names = ['unknown', 'Action', 'Adventure', 'Animation', "Children", 'Comedy', 
                   'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
                   'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    item_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + genre_names
    movies_df = pd.read_csv('u.item', sep='|', names=item_cols, encoding='latin-1')
    
    def get_genres(row):
        g = []
        for genre in genre_names:
            if row[genre] == 1:
                g.append(genre)
        return g
    
    movies_df['genres'] = movies_df.apply(get_genres, axis=1)

    all_movies = {}
    for _, row in movies_df.iterrows():
        all_movies[str(row['movie_id'])] = {
            "title": row['title'],
            "genres": row['genres']
        }

    # 3. Pivot ratings (Crear matriz usuario-item con NaNs reales)
    R_df = ratings_df.pivot(index='user_id', columns='item_id', values='rating')
    col_ids = R_df.columns.tolist()

    # 4. Centrar por usuario (restar su media)
    user_means = R_df.mean(axis=1)
    R_centered = R_df.sub(user_means, axis=0)
    
    # Rellenar NaNs restantes con 0
    R_filled = R_centered.fillna(0)

    # 5. Aplicar TruncatedSVD (como en el notebook de clase)
    k = 20
    svd = TruncatedSVD(n_components=k, random_state=42)
    
    # fit_transform equivaldría a X_reduced = X · VT. 
    svd.fit(R_filled)
    
    # Extraemos solo V^T (los componentes).
    # En JS haremos fit_transform manualmente (u = c · V^T) y luego inverse_transform (r = u · V)
    VT = svd.components_.tolist()  # shape (20, n_movies)

    # 6. Top movies to rate
    movie_stats = ratings_df.groupby('item_id').agg(
        num_ratings=('rating', 'count'),
        avg_rating=('rating', 'mean')
    ).reset_index()
    
    top_movies = movie_stats.sort_values('num_ratings', ascending=False).head(200)
    
    movies_to_rate = []
    for _, row in top_movies.iterrows():
        mid = int(row['item_id'])
        m_info = all_movies.get(str(mid), {})
        if m_info:
            movies_to_rate.append([
                mid,
                m_info.get('title', ''),
                m_info.get('genres', []),
                float(row['avg_rating']),
                int(row['num_ratings'])
            ])

    global_mean = float(ratings_df['rating'].mean())

    # Build output (SIN Sigma, exacto al notebook)
    out_data = {
        "movies_to_rate": movies_to_rate,
        "all_movies": all_movies,
        "VT": VT,
        "column_ids": col_ids,
        "global_mean": global_mean
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False)

    print("Success! data.json created, notebook-compatible.")

if __name__ == '__main__':
    build_svd_data()
