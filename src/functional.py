import mysql.connector
import secret
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import re




def connect_database():
    user= secret.mysql_username
    passw = secret.mysql_password
    # Connect to the database
    cnx = mysql.connector.connect(user=user, password= passw,
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
    

#### customer details

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
    CUST_PHONE=input("Enter New 10 digit valid phone number :")
    pattern = r'^\d{10}$'
    if CUST_PHONE and re.match(pattern,CUST_PHONE):
        CUST_PHONE_FMT= f"({CUST_PHONE[:3]}) {CUST_PHONE[3:6]}-{CUST_PHONE[6:]}"    
    # Define another query
        query = ("""update cdw_sapp_customer
                set CUST_PHONE = %s
                where CREDIT_CARD_NO = %s or SSN =%s""")
        params = (CUST_PHONE_FMT,CC_SSN,CC_SSN)
        cursor.execute(query,params)
        cnx.commit()
        # Print the results
        print("Customer Phone number has been updated" )
    else:
        print("Please enter a non empty valid 10 digit phone number and retry.")  
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
    # Check if all input fields are filled
    if APT_NO and STREET_NAME and CITY and STATE and ZIP and COUNTRY:
    # Define another query
        query = ("""update cdw_sapp_customer
                set APT_NO = %s,STREET_NAME = %s,RESIDENCE = %s,CUST_CITY = %s,CUST_STATE = %s,CUST_ZIP = %s,CUST_COUNTRY = %s
                where CREDIT_CARD_NO = %s or SSN =%s""")
        params = (APT_NO,STREET_NAME,RESIDENCE,CITY,STATE,ZIP,COUNTRY,CC_SSN,CC_SSN)
        cursor.execute(query,params)
        cnx.commit()
        # Print the results
        print("Customer Address has been updated" )
    else:
        print("Please provide all address fields.")    
    cnx.close()

def Modify_cust_email_ID():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
   # Get user input
    CC_SSN= input("Enter Credit Card No or SSN Number of the customer:")
    CUST_EMAIL=input("Enter new valid email Id :")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if CUST_EMAIL and (re.fullmatch(regex, CUST_EMAIL)):
    # Define another query
        query = ("""update cdw_sapp_customer
                set CUST_EMAIL = %s
                where CREDIT_CARD_NO = %s or SSN =%s""")
        params = (CUST_EMAIL,CC_SSN,CC_SSN)
        cursor.execute(query,params)
        cnx.commit()
        # Print the results
        print("Customer Email Id has been updated" )
    else:
        print("Please enter valid email address and retry.")  
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


## Data Analysis

#Find and plot which transaction type has the highest transaction count.
def Transaction_type_highest_transaction_counts():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""select transaction_type,count(transaction_id) as Transaction_count from cdw_sapp_credit_card
            group by TRANSACTION_TYPE
            order by Transaction_count DESC
             Limit 1""")
    cursor.execute(query)
    # Print the results
    for row in cursor:
        print(row)
        # Open the image file
    img = Image.open('Transaction_Types_with_Transaction_count.png')
    # Show the image
    plt.imshow(img)
    plt.show()
    cnx.close()
   

#Find and plot which state has a high number of customers.

def state_high_customer():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""select cust_state ,count(credit_card_no) as customer
            from cdw_sapp_customer
            group by cust_state
             order by customer DESC 
             limit 1""")
    cursor.execute(query)
    # Print the results
    for row in cursor:
        print(row)
        # Open the image file
    img = Image.open('Customers_state.png')
    # Show the image
    plt.imshow(img)
    plt.show()
    cnx.close()
  
    

# Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.
# Hint (use CUST_SSN). 

def top_customers():
    cnx = connect_database()
    # Create a cursor object
    cursor = cnx.cursor()
    # Define another query
    query = ("""SELECT REPLACE(cust_ssn, LEFT(cust_ssn, 5), 'XXXXX') AS masked_ssn, SUM(transaction_value)
            FROM cdw_sapp_credit_card AS card
            JOIN cdw_sapp_customer AS customer ON card.credit_card_no = customer.credit_card_no
            GROUP BY cust_ssn
            LIMIT 10""")
    cursor.execute(query)
    # Print the results
    #print("C:\Capstone Project\credit_resources\Top 10 Customers1.png")
    for row in cursor:
        print(row)
    # Open the image file
    img = Image.open('../resources/graphs/Top_Customers.png')
    # Show the image
    plt.imshow(img)
    plt.show()
    cnx.close()
    
    



    