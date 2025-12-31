import os
from pyspark.sql import SparkSession

def init_spark(app_name="CrimeProject", driver_memory="10g"):
    """
    Initialize Apache Spark with Java + Hadoop dependencies.
    This function is reusable across all notebooks.
    """

    # Required for Spark on Windows
    os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
    os.environ["HADOOP_HOME"] = r"C:\hadoop"
    os.environ["PATH"] = (
        r"C:\Program Files\Java\jdk-17\bin;"
        r"C:\hadoop\bin;"
        + os.environ["PATH"]
    )

    # Create Spark Session
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName(app_name)
        .config("spark.driver.memory", driver_memory)
        .config("spark.sql.execution.arrow.enabled", "true")
        .getOrCreate()
    )

    print(f"Spark Initialized: {app_name}")
    return spark
