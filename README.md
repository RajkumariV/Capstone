# Per Scholas Capstone
#### Final project for the Per Scholas Data Engineering course

## Project requirements:

![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Demo_Objective.png)

# Things to considered before starting this project

#### Data safety 
-refers to the protection of data from accidental or intentional loss, corruption, or unauthorized access. It involves creating backups, implementing disaster recovery plans, and ensuring that data is stored in a secure location.
(To ensure Data Safety Data is Safely BACKUP)
#### Data security 
-refers to the protection of data from unauthorized access, use, disclosure, or destruction. It involves implementing access controls, encryption, and other security measures to prevent data breaches.
(To ensure Data Safety Customers SSN is handled as Masked.)
#### Data validity 
-refers to the degree to which data accurately represents the business rules or definitions. In other words, data must be relevant and representative of the business metrics it describes.
(7 digit phone no in customer table can be a real time scnerio for that data engineer needs to check Area code if area code is concated to 7 digit number valid phone number can be created but in oue project area code was also not given so random no(111) added to make data valid)


### Project Instructions
#Local
if you want to run this project in your local download raw files and while connecting to database use your user and password and mark # aws connection code as below for all 3 files.
-#file_json_data = get_json_file_data_aws_s3_bucket("capstone.creditcard.loan","cdw_sapp_branch.json")    
-#Branch_df=spark.read.json(spark.sparkContext.parallelize([file_json_data]))
#AWS
for connecting to cloud AWS create a S3 bucket in AWS account upload raw files ,create key id and key password use it for AWS connection mark #  file connection code as below for all 3 files
-#branch_df=spark.read.json("C:\Capstone Project\CDW_SAPP_BRANCH.JSON")

### 1. Load Credit Card Database (SQL)
#### 1.1) Data Extraction and Transformation with Python and PySpark
For “Credit Card System,” create a Python and PySpark SQL program to read/extract the following JSON files according to the specifications found in the mapping document.
- CDW_SAPP_BRANCH.JSON
- CDW_SAPP_CREDITCARD.JSON
- CDW_SAPP_CUSTOMER.JSON

#### 1.2) Data Loading Into Database
Once PySpark reads data from JSON files, and then utilizes Python, PySpark, and Python modules to load data into RDBMS(SQL), perform the following:
- Create a Database in My SQL, named “creditcard_capstone.”
- Create a Python and Pyspark Program to load/write the “Credit Card System Data” into RDBMS(creditcard_capstone)
	- Tables should be created by the following names in RDBMS:
		- CDW_SAPP_BRANCH
		- CDW_SAPP_CREDIT_CARD
		- CDW_SAPP_CUSTOMER

## Database Connection- I have used different methods in different section to connect to database
A cnx (short for connection) is a lower-level object that represents a connection to a database. It is typically used for executing SQL statements DIRECTLY and managing transactions.
(Query was done in database through python so cnx worked)

An engine is a higher-level object that provides a simplified interface for connecting to a database. It is typically used for executing SQL statements and managing transactions.
(engine is needed to get full table in dataframe )

### 2. Application Front-End

Once data is loaded into the database, we need a front-end (console) to see/display data. For that, create a console-based Python program to satisfy System Requirements 2 (2.1 and 2.2).
#### 2.1) Transaction Details Module
- Used to display the transactions made by customers living in a given zip code for a given month and year. Order by day in descending order.
- Used to display the number and total values of transactions for a given type
- Used to display the total number and total values of transactions for branches in a given state.
#### 2.2) Customer Details Module
- Check the existing account details of a customer.
- Modify the existing account details of a customer.
- Generate a monthly bill for a credit card number for a given month and year.
- Display the transactions made by a customer between two dates. Order by year, month, and day in descending order.

### 3. Credit Card Data Analysis and Visualization

## Tableau
For this section I have used Tableau so query was done in database and then saved it in csv file and loaded in Tableau to make plots,and these be used in Power BI, however Tableau desktop gives us option to connect to my sql database and query inside tableau.

#### 3.1) Find and plot which transaction type has the highest transaction count.
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Transaction_Types_with_Transaction_count.png)

#### 3.2) Show which state has the highest number of customers
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Customers_State.png)

#### 3.3) Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.Hint (use CUST_SSN)
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Top_Customers.png)

### Overview of LOAN application Data API
Banks want to automate the loan eligibility process (in real-time) based on customer details provided while filling out the online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History, and others. To automate this process, they have the task of identifying the customer segments to those who are eligible for loan amounts so that they can specifically target these customers. Here they have provided a partial dataset.

#### API Endpoint: [https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json](https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json)

The above URL allows you to access information about loan application information. This dataset has all of the required fields for a loan application. You can access data from a REST API by sending an HTTP request and processing the response.

### 4. LOAN Application Dataset

#### 4.1) Access API Endpoint
- Create a Python program to GET (consume) data from the above API endpoint for the loan application dataset.
#### 4.2) Access Status Code
- Find the status code of the above API endpoint.
#### 4.3) Load Into Database
- Once Python reads data from the API, utilize PySpark to load data into RDBMS(SQL). The table name should be "CDW-SAPP_loan_application" in the database. Use the “creditcard_capstone” database.

### 5. Loan Data Analysis and Visualization

#### 5.1)Find and plot the percentage of applications approved for self-employed applicants
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Approved_self_employed.png)

#### 5.2)Find the percentage of rejection for married male applicants.
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Rejected_married_male_applicant.png)

#### 5.3)Find and plot the top three months with the largest volume of transaction data.
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Top3_months_Largest_transaction.png)

#### 5.4Find and plot which branch processed the highest total dollar value of healthcare transactions.
![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Helthcare_transaction_by%20_Branch.png)

## Technical Challenges

### Modifying Customer Account Details

Project requirement in section 2.2 is having the option to modify a customer's account details. This includes every part of a customer's account excluding a few parameters ('SSN' and 'LAST_UPDATED' columns). Even 'FULL_STREET_ADDRESS' was included as well.So did some research on that and found that if we ask bank to change our appartment no. or strret no. or state or county ,Bank will ask full address proof for security purpose and full address is verified along with small apt change so (APT_NO,STREET_NAME,RESIDENCE,CITY,STATE,ZIP,COUNTRY )cosidered as one part and CUST_PHONE and CUST_EMAIL is cosidered seprate. Although this portion of the project took the longest to implement, writing the code this way did shorten the time it took to complete it.

### Tableau vs Matplotlib

Tableau is a business intelligence tool that allows you to connect to almost any database, drag and drop to create visualizations, and share with a click. It provides a user-friendly system that allows you to create attractive visualizations with ease.
Matplotlib, on the other hand, is a Python plotting library that produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. It offers a variety of free data visualization libraries to data scientists such as Seaborn, Plotly, and more. With Matplotlib, you can visualize any data and their available documentation offers a better user experience.
In summary, if you’re looking for a tool that provides attractive visualizations with ease of use, Tableau might be the right choice for you. If you’re looking for a more flexible and customizable tool that allows you to create publication-quality figures, Matplotlib might be the better option.
So for section Three I used Tableau and for section 5 I used matplotlib.

## Skillsets
- Python
- SQL
- Apache Spark
- REST API
- Github
- My SQL
- Pandas library
- Matplotlib library
- Tableau
