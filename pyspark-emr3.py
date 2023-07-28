import sys
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType

def spark_session():
    spark = SparkSession.builder.appName('EmrApp2').getOrCreate()
    return spark


def main():
    
    spark=spark_session()
    schema = StructType([StructField('Id', IntegerType()), StructField('Name',StringType()), StructField('Age',IntegerType()),StructField('Status',StringType()),StructField('Skills',ArrayType(StringType())) ])

    df = spark.read.option('header',True).schema(schema).csv(path=sys.argv[1])
    df.show()
    df.printSchema()
    df.count()
    df.columns
    df.schema
    df.dtypes
    df1 = df.filter(col('Age')<=25)
    df1.show()
    df1.write.format('csv').mode('overwrite').save(path=sys.argv[2])

    spark.stop()



if __name__ == "__main__":
    main()


