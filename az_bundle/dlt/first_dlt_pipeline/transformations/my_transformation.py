import dlt
from pyspark.sql.functions import *

@dlt.table(name="orders_bronze")
def orders_bronze():
    return spark.read.table("ap_databricks_ws.default.orders_raw")

@dlt.expect("valid_order_id", "amount > 200")
@dlt.table(name="orders_silver")
def orders_silver():
    return spark.read.table("ap_databricks_ws.default.orders_bronze")
 