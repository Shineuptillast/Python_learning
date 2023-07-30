import argparse
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *



def main(data_source, save_source):
    
    spark = SparkSession.builder.appName('EmrApp').getOrCreate()
    df = spark.read.format('csv').option('header',True).option('inferschema',True).load(data_source)
    df.show()
    df.printSchema()
    df.count()
    df1 = df.groupBy('Ship_Mode').sum('Sales')
    df1.show()
    df1.write.format('csv').mode('overwrite').save(save_source)

    spark.stop()



if __name__ == "__main__":
    parse=argparse.ArgumentParser()
    parse.add_argument('--data_source')
    parse.add_argument('--save_source')
    args=parse.parse_args()
    main(args.data_source, args.save_source)


