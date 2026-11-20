
from pyspark.sql import SparkSession

# A local spark session
spark = (
    SparkSession.builder
    .appName("MovieReviewsSetupTest")
    .master("local[*]")
    .getOrCreate()
)

print("Spark version:", spark.version)

# Loading the imdb dataset
df=spark.read.csv("IMDB_Dataset.csv",header=True, inferSchema=True)


#Display the rows, columns-Testing
df.show(5)
df.printSchema()
# Stop Spark session
spark.stop()

print("\nSpark test successful in reading the IMDB dataset!")
