from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

file_path = "/content/wordcount.txt" 
text_file = spark.read.text(file_path).rdd.map(lambda r: r[0])

# Split the lines into words and count them
word_counts = text_file.flatMap(lambda line: line.split(" ")).count()

# Print the word count
print("Number of words in the file:", word_counts)

# Stop the SparkSession
spark.stop()