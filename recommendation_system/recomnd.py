import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# A more diverse sample dataset: User-Item ratings matrix with Movie Titles and Genres
data = {
    'user_id': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7],
    'movie_id': [1, 2, 3, 4, 1, 2, 3, 5, 2, 3, 4, 1, 3, 4, 5, 2, 3, 4, 5, 1, 3, 5, 2, 4],
    'rating': [5, 3, 4, 2, 4, 2, 5, 1, 5, 4, 3, 3, 4, 5, 2, 4, 3, 5, 1, 5, 4, 2, 4, 3]
}

movies = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'Toy Story', 'Jaws', 'Star Wars', 'The Godfather'],
    'genre': ['Sci-Fi', 'Animation', 'Thriller', 'Sci-Fi', 'Crime']
}

df = pd.DataFrame(data)
movies_df = pd.DataFrame(movies)

# Merging movie data with ratings
df = pd.merge(df, movies_df, on='movie_id')

# Creating the user-item matrix
user_item_matrix = df.pivot(index='user_id', columns='title', values='rating').fillna(0)

# Compute the cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Debug: Print the user-item matrix and similarity matrix
print("User-Item Matrix:")
print(user_item_matrix)
print("\nUser Similarity Matrix:")
print(user_similarity_df)

# Function to recommend items to a user
def recommend_items(user_id, user_item_matrix, user_similarity_df, n_recommendations=3):
    user_ratings = user_item_matrix.loc[user_id]
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)

    # Debug: Print the ratings of the user
    print(f"\nRatings for User {user_id}:")
    print(user_ratings)

    recommendations = pd.Series(dtype='float64')
    for similar_user, similarity in similar_users.items():
        if similar_user == user_id:
            continue
        user_recommendations = user_item_matrix.loc[similar_user]

        # Debug: Print the similarity and ratings from a similar user
        print(f"\nSimilar User {similar_user} with similarity {similarity}:")
        print(user_recommendations)

        weighted_recommendations = user_recommendations[user_ratings == 0] * similarity

        # Debug: Print the weighted recommendations
        print(f"Weighted Recommendations from User {similar_user}:")
        print(weighted_recommendations)

        recommendations = recommendations.add(weighted_recommendations, fill_value=0)

    recommendations = recommendations.sort_values(ascending=False).head(n_recommendations)

    return recommendations.index.tolist()

# Recommend items to a user
user_id = 8  # Change this ID to get recommendations for different users
recommended_items = recommend_items(user_id, user_item_matrix, user_similarity_df, n_recommendations=3)
print(f"\nRecommended movies for user {user_id}: {recommended_items}")
