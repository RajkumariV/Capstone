# Per Scholas Capstone
#### Final project for the Per Scholas Data Engineering course

## Project requirements:

![Alt text](https://github.com/RajkumariV/Capstone/blob/dev/resources/graphs/Demo_Objective.png)

# Things to Remember before starting this project

#### Data safety 
-refers to the protection of data from accidental or intentional loss, corruption, or unauthorized access. It involves creating backups, implementing disaster recovery plans, and ensuring that data is stored in a secure location.
(To ensure Data Safety Data is Safely BACKUP)
#### Data security 
-refers to the protection of data from unauthorized access, use, disclosure, or destruction. It involves implementing access controls, encryption, and other security measures to prevent data breaches.
(To ensure Data Safety Customers SSN is handled as Masked.)
#### Data validity 
-refers to the degree to which data accurately represents the business rules or definitions. In other words, data must be relevant and representative of the business metrics it describes.
(7 digit phone no in customer table can be a real time scnerio for that data engineer needs to check Area code if area code is concated to 7 digit no valid phone no can be created but in oue project area code was also not given so random no(1111) added to make data valid)

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

An engine is a higher-level object that provides a simplified interface for connecting to a database. It is typically used for executing SQL statements and managing transactions.

A cnx (short for connection) is a lower-level object that represents a connection to a database. It is typically used for executing SQL statements DIRECTLY and managing transactions.

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
After data is loaded into the database, users can make changes from the front end, and they can also view data from the front end. Now, the business analyst team wants to analyze and visualize the data according to the below requirements. Use Python libraries for the below requirements:
#### 3.1) - Find and plot which transaction type has the highest transaction count.
-![Alt text](image-2.png)

#### 3.2) -Show which state has the highest number of customers
-![Alt text](image-3.png)
- .
#### 3.3) -Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.Hint (use CUST_SSN)
-![Alt text](image-4.png)

### Overview of LOAN application Data API
Banks deal in all home loans. They have a presence across all urban, semi-urban, and rural areas. Customers first apply for a home loan; after that, a company will validate the customer's eligibility for a loan.

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
#### 5.1) -Find and plot the percentage of applications approved for self-employed applicants
-
#### 5.2)- Find the percentage of rejection for married male applicants.
-
#### 5.3)-Find and plot the top three months with the largest volume of transaction data.
- 
#### 5.4--Find and plot which branch processed the highest total dollar value of healthcare transactions.

## Technical Challenges

## Skillsets
- Python
- SQL
- Apache Spark
- REST API
- Git
- My SQL
- Pandas library
- Matplotlib library
-Tableau
