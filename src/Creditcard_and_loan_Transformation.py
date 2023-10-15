import pyspark
import secret
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import col,date_format,lit,concat
from pyspark.sql.types import StringType, IntegerType, StructType, StructField
from pyspark.sql.functions import concat_ws, to_date

# Define the transformation functions
# Format phone numbers in the phone_number column as (xxx) xxx-xxxx
def format_phone_number(phone_number):
    if phone_number is None:
        return None
    else:
        return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

# convert date,month,year to format dd-mm-yyy
#def convert_to_date(DAY,MONTH,YEAR):
   #return to_date(concat_ws('-', DAY, MONTH, YEAR), 'dd-MM-yyyy')

def load_dataframe_in_db(data_frame,full_table_name):
    user= secret.mysql_username
    passw = secret.mysql_password
    data_frame.write.format("jdbc") \
    .mode("overwrite") \
    .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
    .option("dbtable", full_table_name) \
    .option("user",user ) \
    .option("password", passw) \
    .save()

def etl_credit_card_branch_data():
    spark= SparkSession.builder.appName('Capstone').getOrCreate()
    df=spark.read.json("CDW_SAPP_BRANCH.JSON")
    df = df.fillna({"BRANCH_ZIP": 99999})
    format_phone_number_udf = F.udf(format_phone_number, StringType())
    df = df.withColumn("BRANCH_PHONE", format_phone_number_udf(col("BRANCH_PHONE")))
    load_dataframe_in_db(df,"creditcard_capstone.CDW_SAPP_BRANCH")
    print("Credit card branch data extracted , transformed and loaded successfully in table creditcard_capstone.CDW_SAPP_BRANCH")


credit_df=spark.read.json("CDW_SAPP_CREDIT.JSON")
#format_date_udf = F.udf(convert_to_date, StringType())
#credit1_df= credit_df.withColumn("timeid", format_date_udf(col("DAY"),col("MONTH"),col("YEAR")))
credit_df= credit_df.withColumn("date", to_date(credit_df["YEAR"]*10000 + credit_df["MONTH"]*100 + credit_df["DAY"], "yyyyMMdd"))
credit_df.show()

from pyspark.sql.functions import initcap
customer_df=spark.read.json("CDW_SAPP_CUSTMER.JSON")
customer_df.show()
customer_df=customer_df.withColumn("FIRST_NAME", initcap("FIRST_NAME"))
#customer_df.show()

from pyspark.sql.functions import lower
customer_df = customer_df.withColumn("MIDDLE_NAME", lower("MIDDLE_NAME"))
#customer_df.show()

from pyspark.sql.functions import initcap
customer_df=customer_df.withColumn("LAST_NAME", initcap("LAST_NAME"))
#customer_df.show()

customer_df = customer_df.withColumn("Residence", concat("STREET_NAME", lit(", "), "APT_NO"))
#customer_df.show()

customer_df = customer_df.withColumn('CUST_PHONE', concat('CUST_PHONE',lit('111')))
customer_df.show()

format_phone_number_udf = F.udf(format_phone_number, StringType())
customer_df = customer_df.withColumn("CUST_PHONE", format_phone_number_udf(col("CUST_PHONE")))
customer_df.printSchema()
customer_df.show()
















