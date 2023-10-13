from credit_file_etl import *
from functional import *
print("WELCOME TO THE CAPSTONE DEMO PROGRAM")

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
            print("5. View/Update Customer Data")
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
                    print("1. customer_transaction_given_zip_code")  
                    print("2. number_value_of_transaction_for_given_ty")  
                    print("3. number_value_transaction_for_branches_givenstate")
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
                    print("2. Modify Customer Phone No")
                    print("3. Modify Customer Address")  
                    print("4. Generate monthly bill for customer")
                    print("5. transaction_by_customer_between_two_dates")
                    print("6. Go back to previous menu")              
                    SelectQ = int(input("Select Question:"))

                    if SelectQ == 1:  
                        customer_account_details()             
                    
                    elif SelectQ == 2:
                        Modify_cust_phone() 
                        
                    elif SelectQ == 3:  
                        Modify_Cust_Address()

                    elif SelectQ == 4:  
                        generate_monthly_bill() 

                    elif SelectQ == 5:  
                        transaction_by_customer_between_two_dates()
                    
                    elif SelectQ == 6:  
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
                Data_analysis()
                
            elif choice3 == 7:  
                break                                
                    
                    
            else:  
                print("Oops! Incorrect Choice.")          
                    
    elif mainchoice == 3:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")            
                            
   
    

            
    
            
      
    
      
    