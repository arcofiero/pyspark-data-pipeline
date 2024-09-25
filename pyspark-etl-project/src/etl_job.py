from pyspark.sql import SparkSession
from io_operations import read_data
from transformations import apply_transformations
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col

def main():
    # Initialize Spark Session
    spark = SparkSession.builder.appName("ETL Job").getOrCreate()
    
    # Define paths
    RAW_DATA_PATH = "file:///Users/architraj/Google Drive/Project/pyspark-data-pipeline/pyspark-etl-project/data/raw/"
    
    # Define employee schema
    employee_schema = StructType([
        StructField("employee_id", IntegerType(), True),
        StructField("first_name", StringType(), True),
        StructField("last_name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("department", StructType([
            StructField("dept_id", IntegerType(), True),
            StructField("dept_name", StringType(), True)
        ]), True),
        StructField("address", StructType([
            StructField("street", StringType(), True),
            StructField("city", StringType(), True),
            StructField("state", StringType(), True),
            StructField("zip", StringType(), True)
        ]), True),
        StructField("skills", StringType(), True)
    ])

    # Define department schema
    department_schema = StructType([
        StructField("dept_id", IntegerType(), True),
        StructField("budget", IntegerType(), True),
        StructField("manager", StringType(), True)
    ])

    # Read the employee and department JSON data
    employees_df = read_data(spark, RAW_DATA_PATH, employee_schema)
    department_df = read_data(spark, RAW_DATA_PATH, department_schema)

    # Display the schema to ensure it is read correctly
    employees_df.printSchema()
    employees_df.show(truncate=False)
    
    department_df.printSchema()
    department_df.show(truncate=False)

    # Apply transformations and join the data
    transformed_df = apply_transformations(employees_df, department_df)

    # Show the transformed DataFrame
    transformed_df.show(truncate=False)

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()