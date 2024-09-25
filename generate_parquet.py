from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
import random

# Initialize a Spark session with the correct local file system configuration
spark = SparkSession.builder \
    .appName("Generate Parquet File") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .getOrCreate()

# Define schema for employee data
schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("department", StructType([
        StructField("dept_id", IntegerType(), True),
        StructField("dept_name", StringType(), True)
    ])),
    StructField("address", StructType([
        StructField("street", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True),
        StructField("zip", StringType(), True)
    ])),
    StructField("skills", ArrayType(StringType()), True)
])

# Generate sample employee data
def generate_employee_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        employee = (
            i,
            f"FirstName{i}",
            f"LastName{i}",
            random.randint(22, 60),
            {
                "dept_id": random.randint(101, 120),
                "dept_name": f"Dept{random.randint(1, 20)}"
            },
            {
                "street": f"{random.randint(1000, 9999)} Some St",
                "city": random.choice(["San Francisco", "New York", "Chicago", "Los Angeles", "Seattle"]),
                "state": random.choice(["CA", "NY", "IL", "WA", "TX"]),
                "zip": f"{random.randint(10000, 99999)}"
            },
            random.sample(["Python", "Spark", "AWS", "Scala", "Kafka", "SEO", "Google Analytics"], 3)
        )
        data.append(employee)
    return data

# Create DataFrame with employee data without Pandas
employee_data = generate_employee_data(100)
df = spark.createDataFrame(employee_data, schema)

# Show a sample of the DataFrame
df.show(5, truncate=False)

# Write DataFrame to Parquet file
df.write.mode('overwrite').parquet("data/raw/sample_employees.parquet")

# Stop the Spark session
spark.stop()