from pyspark.sql.functions import col

def apply_transformations(employees_df, department_df):
    # Extract the dept_id from the department struct in employees_df
    employees_df = employees_df.withColumn("dept_id", col("department.dept_id"))

    # Filter employees older than 30
    filtered_employees_df = employees_df.filter(col("age") > 30)

    # Join the filtered employees DataFrame with the department DataFrame on dept_id
    joined_df = filtered_employees_df.join(department_df, on="dept_id", how="inner")

    return joined_df