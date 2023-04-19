case class Dept(dept_id: Int, dept_name: String)

val deptRDD = sc.makeRDD(Seq(Dept(1,"Sales"),Dept(2,"HR")))

val deptDS = spark.createDataset(deptRDD)

val deptDF = spark.createDataFrame(deptRDD)

deptDS.rdd

//res12: org.apache.spark.rdd.RDD[Dept] = MapPartitionsRDD[5] at rdd at 
//<console>:31

deptDF.rdd

//res13: org.apache.spark.rdd.RDD[org.apache.spark.sql.Row] = //MapPartitionsRDD[8] at rdd at <console>:31

deptDS.filter(x => x.dept_location > 1).show()
