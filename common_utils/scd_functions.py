# create a common function in scd type 1
    #parametter, soruce, target and condition
from delta.tables import DeltaTable
from pyspark.sql import SparkSession
from common_utils.logging import get_logger
logger = get_logger("scd_functions")

def scd_type1(spark,source,target_table,key_columns):
    """
    Perform SCD type 1
    Existing records are updated
    New records are inserted

    Parameters:
    spark:sparksession
    source: source dataframe
    target_table: ste fully qualified delta table
    condition: conditon for merging the soruce and target tables
    """
    logger.info("Starting SCD type 1 for %s",target_table)
    logger.info("SCD type 1 keys %s",key_columns)

    # --------------------------------------------------------
    # Validate key columns
    # --------------------------------------------------------
    # here im going to validate key columns if they exists
    missing_keys = [k for k in key_columns if k not in source.columns]
    # here it will check if the key_columns exists in source datafrmae, if they not exist they will be stored in the missing key
    #missing_keys = [] # empty array , the following function is equavalent to the upper functions which is consice
    #for k in key_columns:
    #    if k not in source.columnns:
    #       missing_columns.append(k) 
    if missing_keys:
        raise ValueError(
            f"Missing key col) SCD type 1 merge condition:"
            f"{missing_keys}"

        )
    # --------------------------------------------------------
    # check the target tab;e
    # --------------------------------------------------------

    if not spark.catalog.tableExists(target_table):
       logger.info("Target_table %s does not exist", target_table)
       return False
    # if the target_table does not exist it will return false as for scd types we need a target_table to update, merge and insert and it will bypass as table not exist so it will activate the command to create schema


    
    # --------------------------------------------------------
    # Get Delta target
    # --------------------------------------------------------

    target= DeltaTable.forName(spark,target_table)

    
    # --------------------------------------------------------
    # Building Merge conditions
    # --------------------------------------------------------

    merge_conditions = " AND ".join([f"target.{k}=source.{k}"for k in key_columns])
    logger.info(
        "SCD Type 1 merge condition: %s",
        merge_conditions
    )
    #merge_condition = []
    #condition = []
    #for k in key_columns:
    # condition.append(f"targer.{k}=source.{k}")
    #merge_condition="AND.join(condition)
    # --------------------------------------------------------
    # Execution of merge conditions
    # --------------------------------------------------------
    (
        target.alias("target")
        .merge(
        source.alias("source"),
        merge_conditions
        )
        .whenMatchedUpdateAll()

        .whenNotMatchedInsertAll()

        .execute()

     )
    logger.info("SCD type 1 completed for %s",target_table)
    return True




    
