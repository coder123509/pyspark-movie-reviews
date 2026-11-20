# PySpark IMDb Movie Reviews Analysis- Data and Storytelling course, RVCE 7th Semester 2026

This project (`pyspark-movie-reviews`), is built to process, clean, analyze, and transform the IMDb 50K Movie Reviews dataset using Apache Spark (PySpark).

---

## Assignment Problem Statement

**Objective:** Create a GitHub account and commit basic PySpark code that processes a movie review dataset.

### Setup & Repository Requirements
* Create a public GitHub repository named `pyspark-movie-reviews`
* Download the Movie Review Dataset from Kaggle: [IMDb Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
* Complete the PySpark tasks and push the code to the repository

### Data Processing Tasks
1. **Load the Dataset:** Use PySpark to read the CSV file into a DataFrame.
2. **Explore the Data:**
   * Print the schema of the DataFrame.
   * Display the first 5 rows.
3. **Clean the Data:** Remove any rows with null or empty reviews.
4. **Analyze the Data:**
   * Count the total number of reviews.
   * Count how many reviews are labeled positive and negative.
5. **Transform the Data:**
   * Create a new column that stores the length of each review (number of characters).
   * Filter and display reviews where the review length is greater than 500 characters.
6. **Save Your Results:** Save the cleaned and transformed DataFrame as a new CSV file.

---

## Dataset & Output Files

* **Raw Input Dataset:** `IMDB_Dataset.csv` (from [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews), excluded from Git via `.gitignore` due to file size).
* **Processed Output Dataset (`result_imdb_dataset.csv`):** The final cleaned and transformed CSV file containing the added `review_length` column is hosted on Google Drive:  
**[Download `result_imdb_dataset.csv` (Google Drive)]([https://google.com](https://drive.google.com/file/d/1vw7I39JPaKjajFkjHaysbk8GdRxVi4xD/view?usp=drive_link)**

---

## Repository Contents

* `main.py` — Full PySpark pipeline covering data loading (with `multiLine=True` and `escape='"'` to handle embedded quotes/commas in reviews), null/empty string filtering, sentiment aggregation, character-length calculation, filtering (`> 500` characters), and CSV export.
* `test_pyspark.py` — Initial environment test script verifying Apache Spark (`v4.0.1`) setup, CSV ingestion, and schema inference.
* `images/` — Screenshots of terminal execution and query outputs.
* `.gitignore` — Excludes large `.csv` files, `.venv/`, and `__pycache__/`.

---

## Key Results Summary

* **Schema:** `review` (`string`, nullable) and `sentiment` (`string`, nullable)
* **Total Valid Reviews:** `50,000`
* **Sentiment Breakdown:**
  * `positive`: `25,000`
  * `negative`: `25,000`
* **Transformation & Filtering:** Computed character length per review (`review_length`) and filtered reviews exceeding `500` characters.

---

## How to Run Locally

1. **Clone the repository** and place `IMDB_Dataset.csv` inside the project root folder:
   ```bash
   git clone https://github.com/coder123509/pyspark-movie-reviews.git
   cd pyspark-movie-reviews
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   ```
   * **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install pyspark "pandas>=2.0" pyarrow
   ```

4. **Run the PySpark analysis script:**
   ```bash
   python main.py
   ```

## Output
After running the script, the terminal displays the DataFrame schema, sample rows, total valid review counts, sentiment breakdown (`positive` vs. `negative`), and reviews exceeding 500 characters. The cleaned and transformed dataset is exported to `result_imdb_dataset.csv` in the project directory.

## Execution Screenshots

1. Initial Setup & Schema Check (test_pyspark.py)
2. Full Pipeline Execution & Results (main.py)
