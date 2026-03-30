# 🎬 Movie Recommendation System

This project is a **Movie Recommendation System** built using **Python**. It suggests movies to users based on their previous ratings and preferences. The system uses **Collaborative Filtering** to find movies similar to the ones a user likes and provides personalized recommendations.

This is similar to how platforms like Netflix or Amazon Prime recommend movies to users.

---

## Features

* Recommend movies based on your favorite choices
* Uses **Collaborative Filtering** and **Cosine Similarity**
* Interactive interface with **Streamlit**
* Shows top recommended movies instantly
* Visualizes user ratings and popular movies

---

## Dataset

The system uses two datasets:

1️. **Movies dataset** – contains movie IDs, titles, and genres
2️ .**Ratings dataset** – contains user IDs, movie IDs, and ratings

These datasets are standard movie recommendation datasets (like the MovieLens dataset).

---

## How it Works

1. Load movies and ratings datasets
2. Preprocess the data (clean, remove missing values, merge datasets)
3. Create a **movie-user matrix**
4. Calculate **similarity between movies** using Cosine Similarity
5. Recommend movies based on similarity
6. Display recommendations on a **Streamlit app**

---

## Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit (for the interactive web app)
* Matplotlib / Seaborn (for visualizations)

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the URL provided by Streamlit in your browser and start using the app.

---

## Example Output

If a user selects **Toy Story**, the system might recommend:

* Toy Story 2
* Monsters Inc
* Finding Nemo
* The Incredibles
* Up

You can also explore ratings and popular movies through simple visualizations.

---

## Advantages

* Personalized movie suggestions
* Saves users time
* Easy to understand and use
* Shows practical ML implementation

---

## Limitations

* Cannot recommend for completely new users (cold start problem)
* Limited data may reduce accuracy
* New movies without ratings may not appear in recommendations

---

## Future Improvements

* Add **deep learning-based recommendation models**
* Implement a **hybrid system** combining content-based and collaborative filtering
* Real-time recommendations based on user behavior
* Deploy the app online for public use

---

## Author

**Ambika Sidgiddi**
B.Tech CSE (AI & Data Science)

---


