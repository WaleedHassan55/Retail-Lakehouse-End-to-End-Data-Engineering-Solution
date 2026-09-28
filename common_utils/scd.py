# create a common function in scd type 1
    #parametter, soruce, target and condition
from delta.tables import DeltaTable
from pyspark.sql import SparkSession

def scd_type1(spark,source,target_table,condition):
    if spark.catalog.tableExists(target_table):
        print("table Already Exists")
        #load_data
        target= DeltaTable.forName(spark,target_table)
        #SCD type 1
        #Macth in source and target--> key exist in target
        (
            target.alias("target")
            .merge(
                source.alias("source"),
                condition
            )
            .whenMatchedUpdateAll()

            .whenNotMatchedInsertAll()

            .execute()

        )
    else:
        spark.sql("""CREATE SCHEMA IF NOT EXISTS retail_data_platform_silver""")
        source.write.format("delta").mode("overwrite").saveAsTable(target_table)




    
