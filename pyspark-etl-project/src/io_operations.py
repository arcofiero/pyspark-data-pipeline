import os

def read_data(spark, path, schema):
    # Convert Spark path to local path for os.listdir
    local_path = path.replace("file://", "")
    
    # List all files in the raw directory
    files = [f for f in os.listdir(local_path) if os.path.isfile(os.path.join(local_path, f))]
    
    # Filter files by their extension
    json_files = [f for f in files if f.endswith(".json")]
    
    # Read JSON files
    if json_files:
        print(f"Reading JSON files from {path}")
        # Use file:/// for Spark to read the files (notice the triple slashes for the correct file system)
        df = spark.read.option("multiLine", "true").schema(schema).json([f"file:///{os.path.join(local_path, f)}" for f in json_files])
    else:
        raise ValueError(f"No JSON files found in {local_path}")
    
    return df