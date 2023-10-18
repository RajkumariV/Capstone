import pyspark
import secret
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import col,date_format,lit,concat,concat_ws, to_date,initcap,lower
from pyspark.sql.types import StringType, IntegerType, StructType, StructField
import requests
import json
import boto3

# Define the transformation functions
# Format phone numbers in the phone_number column as (xxx) xxx-xxxx
def format_phone_number(phone_number):
    if phone_number is None:
        return None
    else:
        return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

def get_json_file_data_aws_s3_bucket(bucket_name,file_name ):
    s3 = boto3.resource('s3', aws_access_key_id=secret.aws_access_key_id, aws_secret_access_key=secret.aws_secret_access_key)
    obj = s3.Object(bucket_name, file_name)    
    data = obj.get()['Body'].read().decode('utf-8')    
    json_data = [json.loads(jline) for jline in data.splitlines()]    
    return json_data

#Go To Mysql Workbench Write query
#create schema creditcard_capstone; 
#and its created

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

def get_spark_session():
    spark= SparkSession.builder.appName('Capstone').getOrCreate()
    return spark

def etl_credit_card_branch_data():
    spark= get_spark_session()
    file_json_data = get_json_file_data_aws_s3_bucket("capstone.creditcard.loan","cdw_sapp_branch.json")    
    Branch_df=spark.read.json(spark.sparkContext.parallelize([file_json_data]))
    #Uncomment below line if you want to use the raw files from the resource folder and comment out the above two lines for S3
    #Branch_df=spark.read.json("../resources/data-files/CDW_SAPP_BRANCH.JSON")  
    Branch_df = Branch_df.fillna({"BRANCH_ZIP": 99999})
    format_phone_number_udf = F.udf(format_phone_number, StringType())
    Branch_df = Branch_df.withColumn("BRANCH_PHONE", format_phone_number_udf(col("BRANCH_PHONE")))
    load_dataframe_in_db(Branch_df,"creditcard_capstone.CDW_SAPP_BRANCH")
    spark.stop()
    print("Credit card branch data extracted , transformed and loaded successfully in table creditcard_capstone.CDW_SAPP_BRANCH")

def etl_credit_card_card_data():
    spark= get_spark_session()
    file_json_data = get_json_file_data_aws_s3_bucket("capstone.creditcard.loan","cdw_sapp_credit.json")    
    credit_df=spark.read.json(spark.sparkContext.parallelize([file_json_data]))
    #Uncomment below line if you want to use the raw files from the resource folder and comment out the above two lines for S3
    #credit_df=spark.read.json("C:\Capstone Project\CDW_SAPP_CREDIT.JSON")
    credit_df= credit_df.withColumn("date", to_date(credit_df["YEAR"]*10000 + credit_df["MONTH"]*100 + credit_df["DAY"], "yyyyMMdd"))
    load_dataframe_in_db(credit_df,"creditcard_capstone.CDW_SAPP_CREDIT_CARD")
    spark.stop()
    print("Credit card Card data extracted , transformed and loaded successfully in table creditcard_capstone.CDW_SAPP_CREDIT_CARD")

def etl_credit_card_customer_data():
    spark= get_spark_session()
    file_json_data = get_json_file_data_aws_s3_bucket("capstone.creditcard.loan","cdw_sapp_custmer.json")    
    customer_df=spark.read.json(spark.sparkContext.parallelize([file_json_data]))
    #Uncomment below line if you want to use the raw files from the resource folder and comment out the above two lines for S3
    #customer_df=spark.read.json("C:\Capstone Project\CDW_SAPP_CUSTMER.JSON")
    customer_df=customer_df.withColumn("FIRST_NAME", initcap("FIRST_NAME"))
    customer_df = customer_df.withColumn("MIDDLE_NAME", lower("MIDDLE_NAME"))
    customer_df=customer_df.withColumn("LAST_NAME", initcap("LAST_NAME"))
    customer_df = customer_df.withColumn("Residence", concat("STREET_NAME", lit(", "), "APT_NO"))
    customer_df = customer_df.withColumn('CUST_PHONE', concat('CUST_PHONE',lit('111')))
    format_phone_number_udf = F.udf(format_phone_number, StringType())
    customer_df = customer_df.withColumn("CUST_PHONE", format_phone_number_udf(col("CUST_PHONE")))
    load_dataframe_in_db(customer_df,"creditcard_capstone.CDW_SAPP_CUSTOMER ")
    spark.stop()
    print("Credit card Customer data extracted , transformed and loaded successfully in table creditcard_capstone.CDW_SAPP_CUSTOMER")


# etl  loan application data from the API endpoint
def etl_loan_application_data():
    url= "https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json"
    response=requests.get(url)
    data=response.json()
    print("Response Status Code received is-"+ str(response.status_code))
    spark= get_spark_session()
    # Convert the JSON data to a PySpark DataFrame
    loan_df = spark.read.json(spark.sparkContext.parallelize([data]))
    load_dataframe_in_db(loan_df,"creditcard_capstone.CDW_SAPP_loan_application")
    spark.stop()
    print("Loan application data extracted from API endpoint, transformed and loaded successfully in table creditcard_capstone.CDW_SAPP_loan_application")















