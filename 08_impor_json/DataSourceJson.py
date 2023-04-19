# Copy input dataset(people.json) to HDFS and then get into PySpark Shell. To read json file, use format to specify the type of datasource. 

df_json = spark.read.load("file:///home/cloudera/spark-2.0.0-bin-hadoop2.7/people.json", format="json")
df_json = spark.read.json("file:///home/cloudera/spark-2.0.0-bin-hadoop2.7/people.json")
df_json.printSchema()

df_json.show()

# To write data to another JSON file, use below command.

df_json.write.json("newjson_dir")
df_json.write.format("json").save("newjson_dir2")

# To write data to any other format, just mention format you want to save. Below example saves df_json DataFrame in Parquet format. 

df_json.write.parquet("parquet_dir")
df_json.write.format("parquet").save("parquet_dir2")
