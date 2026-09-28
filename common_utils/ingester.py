from pymongo import MongoClient
from bson import json_util


def read_sql_jdbc(spark,url,dbtable,user,password,driver= "com.microsoft.sqlserver.jdbc.SQLServerDriver"):
   
 """
 url     : as in the sql we need the sql server link to get the data inshort connection url from source
 dbtable : table you want to ingest from the source
 user    : username of relatonal databse
 password: password of relational database
 driver  : driver form source for example here we are using the jdbc driver to process the SQL server data
 """

 df = spark.read.format("jdbc")\
       .option("url", url)\
       .option("dbtable", dbtable)\
       .option("user",user)\
       .option("password",password)\
       .option("driver",driver)\
       .load()
       
 return df


def read_cosmosdb_json( spark, connection_string , database_name , collection_name):
    """
    connectionString : connection string of cosmosdb which our soruce
    database_name    : database name is cosmosdb
    connection_name  : collection name is cosmosdb which comes after database there are many connection in the database 
    here for the cosmos we need to make the MongoClient to import the data in form of documents which we later convert into json using json_utils.dump() func and after that we will make spark dataframe from it
    """
    client = MongoClient(connection_string) # here im connecting to mongodb
    db = client[database_name]   # here im getting the database I want to collect data from
    collection = db[collection_name]  # here im getting the collection I want to collect data from
    documents = list(collection.find({}))
    json_rows = [] # creating an empty tuple to store the data later
    for document in documents:
        json_string = json_util.dumps(document)
        json_rows.append((json_string,))
    
    df = spark.createDataFrame(json_rows, ['json_data'])

    return df


def read_s3_parquet(spark , aws_access_key_id,aws_secret_access_key,path):
    """
    aws_access_key_id : aws access key id
    aws_secret_access_key : aws secret access key
    path : path of the s3 bucket
    """

    source_path = (
          f"s3a://{aws_access_key_id}:{aws_secret_access_key}"
         f"@{path}"
    )
    df = spark.read.parquet(source_path)
    return df

def write_raw(df, target_path, mode, file_format, options=None):
    """
    df : dataframe which we want to write
    target_path : path where we want to write the data
    mode : mode of writing the data
    file_format : format of the file which we want to write
    options : options for the writer
    """

    writer = df.write.mode(mode).format(file_format)

    for key, value in (options or {}).items():
        writer = writer.option(key, value)

    writer.save(target_path)

    return target_path
