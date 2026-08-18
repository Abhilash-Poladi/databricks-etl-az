import dlt
from pyspark.sql.functions import *

customers_raw_expectations = {
    "custid": "customer_id is not null",
    "customer_name": "customer_name is not null",
    "customer_segment": "customer_segment IN ('VIP', 'STANDARD', 'PREMIUM')",
}


@dlt.expect_all(customers_raw_expectations)
@dlt.table(name="customers_bronze")
def customers_broze():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", 'csv')
        .option("header", True)
        .load("/Volumes/ap_databricks_ws/ecommerce/source/customers/")
    )







