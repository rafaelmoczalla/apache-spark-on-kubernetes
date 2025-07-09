from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    # Beispiel-Input
    data = ["Hello world", "Hello Kubernetes", "Hello Spark"]

    # RDD erzeugen
    rdd = spark.sparkContext.parallelize(data)

    # WordCount-Logik
    words = rdd.flatMap(lambda line: line.split(" "))
    word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    # Ausgabe in Log
    for word, count in word_counts.collect():
        print(f"{word}: {count}")

    spark.stop()

