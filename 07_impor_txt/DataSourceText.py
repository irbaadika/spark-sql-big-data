# To load text files, we use �text� method which will return a single column with column name as �value� and type as string.

df_txt = spark.read.text("file:///home/cloudera/spark-2.0.0-bin-hadoop2.7/examples/src/main/resources/people.txt")
df_txt.show()
df_txt
# DataFrame[value: string]
