from creditcard_and_loan_application_etl import *
from Creditcard_transaction_and_Data_analysis import *
from Data_analysis_loan_application import *
print("WELCOME TO THE CAPSTONE DEMO PROGRAM")
print("Objective of this Demo")
img = Image.open('../resources/graphs/Demo_objective.png')
# Show the image
plt.imshow(img)
plt.show()
print("Three Major Areas to cover -Data Safety(Backup),Data Security(Handle confidencial Data),Data Validity")


while True:  
    print("\nMAIN MENU")  
    print("1. Credit card data operations")  
    print("2. Load Data API operations")  
    print("3. Exit")  
    mainchoice = int(input("Enter the Choice:"))  
  
    if mainchoice == 1:
        while True:  
            print("\n Select the credit card data operation you want to perform")  
            print("1. ETL Customer Data File")  
            print("2. ETL Credit Card File")  
            print("3. ETL Branch Data File")
            print("4. View Transaction Data")
            print("5. Update Customer Data")
            print("6. Analyze and Visualize credit card data")
            print("7. Go back to main menu")              
            choice2 = int(input("Enter the Choice:"))  
    
            if choice2 == 1:  
                etl_credit_card_customer_data()               
                
            elif choice2 == 2:  
                etl_credit_card_card_data()
                
            elif choice2 == 3:  
                etl_credit_card_branch_data()

            elif choice2 == 4:
                while True:  
                    print("\n Select the credit card data operation you want to perform")  
                    print("1. Customer transaction given zipcode,Month,Year Order by day in Descending")  
                    print("2. Display the number and total values of transactions for a given type.")  
                    print("3. display the total number and total values of transactions for branches in a given state.")
                    print("4. Go back to previous menu")              
                    SelectQ = int(input("Select Question:"))

                    if SelectQ == 1:  
                        customer_transaction_given_zip_code()      
                    
                    elif SelectQ == 2: 
                        number_value_of_transaction_for_given_type()
                    
                    elif SelectQ == 3:  
                        number_value_transaction_for_branches_givenstate()

                    elif SelectQ == 4:  
                        break  
                    
                    else:  
                        print("Oops! Incorrect Choice.") 

            elif choice2 == 5:
                while True:  
                    print("\n Select the credit card data operation you want to perform")  
                    print("1. Get Customer Details")  
                    print("2. Modify existing account details-Phone No")
                    print("3. Modify existing account details-Address") 
                    print("4. Modify existing account details-Email Id") 
                    print("5. Generate monthly bill for customer")
                    print("6. transaction by customer between two dates")
                    print("7. Go back to previous menu")              
                    SelectQ = int(input("Select Question:"))

                    if SelectQ == 1:  
                        customer_account_details()             
                    
                    elif SelectQ == 2:
                        Modify_cust_phone() 
                        
                    elif SelectQ == 3:  
                        Modify_Cust_Address()

                    elif SelectQ == 4:  
                        Modify_cust_email_ID()

                    elif SelectQ == 5:  
                        generate_monthly_bill() 

                    elif SelectQ == 6:  
                        transaction_by_customer_between_two_dates()
                    
                    elif SelectQ == 7:  
                        break

                    else:  
                        print("Oops! Incorrect Choice.") 
            
            elif choice2 == 6:
                while True:  
                    print("\n Select the data analysis operation you want to perform")  
                    print("1. Find and plot which transaction type has the highest transaction count")  
                    print("2. Find and plot which state has a high number of customers." )

                    print("3. top 10 customers, and which customer has the highest transaction amount.")  
                    
                    print("4. Go back to previous menu")              
                    SelectQ = int(input("Select Question:"))
                        
                    if SelectQ == 1:
                        Transaction_type_highest_transaction_counts()  
                      

                    elif SelectQ == 2:  
                        state_high_customer() 

                    elif SelectQ == 3:  
                        top_customers()
                    
                    elif SelectQ == 4:  
                        break

                    else:  
                        print("Oops! Incorrect Choice.") 

       
            elif choice2 == 7:  
                break  
                
            else:  
                print("Oops! Incorrect Choice.")        
                            
    elif mainchoice == 2:
        while True:  
            print("\nSelect the load application data operation you want to perform")  
            print("1. ETL the Load application data from the API")  
            print("2. Data Analysis and Visualization for LOAN Application")
            print("3. Go back to the main menu")                
            choice3 = int(input("Enter the Choice:"))  
    
            if choice3 == 1:
                etl_loan_application_data()  
                
                
            elif choice3 == 2:  
                while True:  
                    print("\n Select Loan application analysis you want to perform")  
                    print("1.Percentage of Applications Approved for Self-Employed Applicants")  
                    print("2.percentage of rejection for married male applicants ")
                    print("3.Top Three Months with Largest Transaction Volume ")  
                    print("4.branch processed the highest total dollar value of healthcare transactions. ")
                 
                    print("5. Go back to previous menu")              
                    SelectQ = int(input("Select Question:"))

                    if SelectQ == 1: 
                        Persantage_Approved_Self_Employed() 
                        

                    elif SelectQ == 2:  
                        Persantage_rejected_male_applicant() 

                    elif SelectQ == 3:  
                        Top_Three_Months_with_Largest_Transaction_Volume()

                    elif SelectQ == 4:  
                        branch_highest_value_healthcare_transactions()  
                    
                    elif SelectQ == 5:  
                        break

                    else:  
                        print("Oops! Incorrect Choice.") 
            
            elif choice3 == 3:
                break
                                     
            else:  
                print("Oops! Incorrect Choice.")        
                     
                    
    elif mainchoice == 3:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")            
                            
   
    

            
    
            
      
    
      
    