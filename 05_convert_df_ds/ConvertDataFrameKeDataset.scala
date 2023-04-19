val newDeptDS = deptDF.as[Dept]

newDeptDS.show()

newDeptDS.first()

// mengonversi ke DataFrame kembali
newDeptDS.toDF.first()
