from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

# 1. Initialize SparkSession
spark = (
    SparkSession.builder.appName("IMDbMovieReviewsAnalysis")
    .master("local[*]")
    .getOrCreate()
)

# Optional: Reduce verbose Spark INFO logs so your output is easier to read
spark.sparkContext.setLogLevel("ERROR")

# ---------------------------------------------------------
# TASK 1: Load the Dataset
# ---------------------------------------------------------
# escape='"' and multiLine=True are used for the IMDb dataset
# because movie reviews often contain commas, quotes, and line breaks.

file_path = "IMDB_Dataset.csv"
df = spark.read.csv(
    file_path, header=True, inferSchema=True, escape='"', multiLine=True
)

# ---------------------------------------------------------
# TASK 2: Exploring the Data(checking schema and contents of the dataset)
# ---------------------------------------------------------
print("--- DataFrame Schema ---")
df.printSchema()

print("--- First 5 Rows ---")
df.show(5, truncate=50)

# ---------------------------------------------------------
# TASK 3: Clean the Data
# ---------------------------------------------------------
# We Remove rows where the 'review' column is null or completely empty, as they donot contribute to the analysis
df_clean = df.filter(col("review").isNotNull() & (trim(col("review")) != ""))

# ---------------------------------------------------------
# TASK 4: Analyzing the Data: a) Number of valid reviews b)Sentiment analysis/breakdown
# ---------------------------------------------------------
total_reviews = df_clean.count()
print(f"Total number of valid reviews: {total_reviews}\n")

print("--- Sentiment Breakdown (Positive vs Negative) ---")
df_clean.groupBy("sentiment").count().show()

# ---------------------------------------------------------
# TASK 5: Transforming the Data
# ---------------------------------------------------------
# Create a new column storing the character count of each review
df_transformed = df_clean.withColumn("review_length", length(col("review")))

print("--- Reviews Longer Than 500 Characters ---")
df_long_reviews = df_transformed.filter(col("review_length") > 500)
df_long_reviews.show(5, truncate=50)

# ---------------------------------------------------------
# TASK 6: Saving the Results
# Converting PySpark DataFrame to pandas df for easy saving process
# ---------------------------------------------------------

output_file = "result_imdb_dataset.csv"
df_transformed.toPandas().to_csv(output_file, index=False)

print(f"Processing complete! Results saved to '{output_file}'")




# Stop the SparkSession
spark.stop()
