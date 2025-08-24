!pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

spark = SparkSession.builder.appName("NetflixBigDataAnalysis").getOrCreate()

df = spark.read.csv("/content/netflix_titles_nov_2019.csv", header=True, inferSchema=True)

df.printSchema()
df.show(5)
df.groupBy("type").count().show()
df.groupBy("country").count().orderBy(desc("count")).show(10)
df.groupBy("listed_in").count().orderBy(desc("count")).show(10)
df.groupBy("release_year").count().orderBy("release_year").show(20)
import matplotlib.pyplot as plt
import pandas as pd
trend_df = (
    df.filter(col("release_year").isNotNull())       
      .filter(col("release_year").cast("int").isNotNull()) 
      .groupBy("release_year")
      .count()
      .orderBy("release_year")
      .toPandas()
)

trend_df["release_year"] = pd.to_numeric(trend_df["release_year"], errors="coerce")
trend_df = trend_df.dropna().astype({"release_year": "int"})

plt.figure(figsize=(12,6))
plt.plot(trend_df["release_year"], trend_df["count"], marker="o")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.title("Netflix Content Trend Over Years")
plt.show()

df.groupBy("country").count().orderBy(desc("count")).toPandas().to_csv("netflix_country_counts.csv", index=False)