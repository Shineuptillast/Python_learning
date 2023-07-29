from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType

def spark_session():
    spark = SparkSession.builder.appName('EmrApp2').getOrCreate()
    return spark


def main():
    
    spark=spark_session()
    data = [(1,'Naman',25,'Graduated',['Hadoop','Kafka','Spark']), (2,'Tejal',27,'Post-Graduated',['PhotoShop','Illustrator']), (3,'Nirjara',20,'Student',['SQL','Bio-Tech']), (4,'Siddharth',16,'Student',['Gaming','CS'])]
    schema = StructType([StructField('Id', IntegerType()), StructField('Name',StringType()), StructField('Age',IntegerType()),StructField('Status',StringType()),StructField('Skills',ArrayType(StringType())) ])
    df = spark.createDataFrame(data,schema)
    df.show()
    df.printSchema()
    df.count()
    df.columns
    df.schema
    df.dtypes
    df1 = df.filter(col('Age')<25)
    df1.show()
    df1.write.format('json').mode('overwrite').save(path='/data')

    spark.stop()



if __name__ == "__main__":
    main()


