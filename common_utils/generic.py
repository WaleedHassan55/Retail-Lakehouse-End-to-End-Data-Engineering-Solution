import pyspark.sql.functions as f 


def rename_columns(df,rename):
    for old_name, new_name in rename.item():
        df = df.withColumnRenamed(old_name,new_name)
    return df

def drop_columns(df, columns_names):
    df = df.drop(*columns_names)
    return df

def casting(df,column_names):
    for column, type in column_names.items():
        df = df.withColumn("column",f.col("column").cast(type))
    return df

