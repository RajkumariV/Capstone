import mysql.connector
import secret

def connect_database():
    user= secret.mysql_username
    passw = secret.mysql_password
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password= 'password',
                            database='creditcard_capstone')
    
    return cnx

#1
def customer_transaction_given_zip_code ():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    zip_code = input("Enter zip code: ")
    month = input("Enter month: ")
    year = input("Enter year: ")
    # Define the query
    query = """
            select transaction_value,transaction_type,year,month,day
    from cdw_sapp_credit_card as card
    join  cdw_sapp_customer as customer
    on card.credit_card_no=customer.credit_card_no
    where cust_zip = %s and month=%s and year=%s
    order by day DESC"""

    params = (zip_code, month, year)
    cursor.execute(query,params)    
    print("Customer transactions for the given input are displayed below:")
    for row in cursor:
        print(row)   
    cnx.close()

#2
def number_value_of_transaction_for_given_type():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    transaction_type= input("Enter the Transaction Type:")
    # Define another query
    query = ("""
            select TRANSACTION_TYPE,sum(TRANSACTION_VALUE),count(TRANSACTION_VALUE) from cdw_sapp_credit_card
    WHERE TRANSACTION_TYPE = %s
            """)
    params = (transaction_type,)
    cursor.execute(query,params)

    print("Sum and transaction count for the input transaction type below:")
    for row in cursor:
        print(row)
    cnx.close()
#3
def number_value_transaction_for_branches_givenstate():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    BRANCH_STATE= input("ENTER BRANCH STATE:")
    # Define another query
    query = ("""
            select branch.BRANCH_CODE,count(card.TRANSACTION_ID),sum(card.TRANSACTION_VALUE)
            from cdw_sapp_credit_card as card
            join  cdw_sapp_branch as branch
            on card.branch_code=branch.branch_code
            where branch.BRANCH_STATE=%s
            group by card.BRANCH_CODE
            """)
    params = (BRANCH_STATE,)
    cursor.execute(query,params)
    print("Branch transaction details for the given state are displayed below:")
    for row in cursor:
        print(row) 
    cnx.close()       
    

# customer details

#1)Used to check the existing account details of a customer.

def customer_account_details():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    CC_SSN= input("Enter Credit Card No or SSN Number of the customer:")
    # Define another query
    query = ("""
            SELECT  FIRST_NAME,MIDDLE_NAME,LAST_NAME,CUST_EMAIL,CUST_PHONE,Residence,CUST_CITY,CUST_STATE,concat('XXXXXXXXX',right(ssn,4)) as ssn_masked 
            FROM cdw_sapp_customer where CREDIT_CARD_NO = %s or SSN =%s
            """)
    params = (CC_SSN,CC_SSN)
    cursor.execute(query,params)
    # Print the results
    print("Customer found are displayed below:")
    for row in cursor:
        print(row)
    cnx.close()    

# 2) Used to modify the existing account details of a customer.
# A.modify cust_phone
def Modify_cust_phone():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
   # Get user input
    CC_SSN= input("Enter Credit Card No or SSN Number of the customer:")
    CUST_PHONE=input("Enter New Phone Number in this format (XXX) XXX-XXXX:")
    # Define another query
    query = ("""update cdw_sapp_customer
            set CUST_PHONE = %s
            where CREDIT_CARD_NO = %s or SSN =%s""")
    params = (CUST_PHONE,CC_SSN,CC_SSN)
    cursor.execute(query,params)
    cnx.commit()
    # Print the results
    print("Customer Phone number has been updated" )
    cnx.close()

# B.modify customer address
def Modify_Cust_Address():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
   # Get user input
    CC_SSN= input("Enter Credit Card No or SSN Number of the customer:")
    APT_NO=input("Enter New Apt No:")
    STREET_NAME=input("Enter New Street Name:")
    CITY=input("Enter New City:")
    STATE=input("Enter New State:")
    ZIP=input("Enter New Zip:")
    COUNTRY=input("Enter New Country:")
    RESIDENCE = STREET_NAME +","+ APT_NO
    # Define another query
    query = ("""update cdw_sapp_customer
             set APT_NO = %s,STREET_NAME = %s,RESIDENCE = %s,CUST_CITY = %s,CUST_STATE = %s,CUST_ZIP = %s,CUST_COUNTRY = %s
            where CREDIT_CARD_NO = %s or SSN =%s""")
    params = (APT_NO,STREET_NAME,RESIDENCE,CITY,STATE,ZIP,COUNTRY,CC_SSN,CC_SSN)
    cursor.execute(query,params)
    cnx.commit()
    # Print the results
    print("Customer Address has been updated" )
    cnx.close()

#3) Used to generate a monthly bill for a credit card number for a given month and year.
def generate_monthly_bill():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    CREDIT_CARD_NO=input("Enter Credit Card No:")
    MONTH= input("ENTER Month:")
    YEAR= input("ENTER Year:")

    # Define another query
    query = ("""select sum(transaction_value),TRANSACTION_TYPE,month,YEAR 
            from cdw_sapp_credit_card
            where CREDIT_CARD_NO= %s and MONTH=%s and year=%s
            group by TRANSACTION_TYPE""")

    params = (CREDIT_CARD_NO,MONTH,YEAR)
    cursor.execute(query,params)
    # Print the results
    print("credit card bill for the customer is displayed below")
    for row in cursor:
        print(row)
    cnx.close()

# 4) Used to display the transactions made by a customer between two dates. Order by year, month, and day in descending order.

def transaction_by_customer_between_two_dates():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Get user input
    CREDIT_CARD_NO=input("Enter Credit Card No:")
    START_DATE= input("Enter Start Date in YYYY-MM-DD format:")
    END_DATE= input("Enter End Date in YYYY-MM-DD format:")

    # Define another query
    query = ("""select * 
            from cdw_sapp_credit_card
            where CREDIT_CARD_NO= %s and
            date between %s and %s order by date desc
             """)

    params = (CREDIT_CARD_NO,START_DATE,END_DATE)
    cursor.execute(query,params)
    # Print the results
    print("Customer transactions for the given date ranges are displayed below:")
    for row in cursor:
        print(row)
    cnx.close()


# Data Analysis

#Find and plot which transaction type has the highest transaction count.
def transaction_by_customer_between_two_dates():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""select transaction_type,count(transaction_id) as Transaction_count from cdw_sapp_credit_card
            group by TRANSACTION_TYPE""")
    cursor.execute(query)
    # Print the results
    print("C:\Capstone Project\credit_resources\Transaction Types with Transaction count.png")
    for row in cursor:
        print(row)
    cnx.close()

#Find and plot which state has a high number of customers.

def state_high_customer():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""select cust_state ,count(credit_card_no) 
            from cdw_sapp_customer
            group by cust_state""")

    cursor.execute(query)
    # Print the results
    print("C:\Capstone Project\credit_resources\High Number of customer state.png")
    for row in cursor:
        print(row)
    cnx.close()

# Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.
# Hint (use CUST_SSN). 

def top_customers():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""select sum(transaction_value),cust_ssn
            from cdw_sapp_credit_card as card
            join  cdw_sapp_customer as customer
            on card.credit_card_no=customer.credit_card_no
            group by CUST_SSN
            limit 10""")
    cursor.execute(query)
    # Print the results
    print("C:\Capstone Project\credit_resources\Top 10 Customers1.png")
    for row in cursor:
        print(row)
    cnx.close()



    