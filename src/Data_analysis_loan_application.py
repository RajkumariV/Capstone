import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import secret

# Q Find and plot the percentage of applications approved for self-employed applicants.

def connect_to_database ():
    user= secret.mysql_username
    passw = secret.mysql_password
    engine = create_engine(f'mysql+mysqlconnector://{user}:{passw}@localhost/creditcard_capstone')
    return engine
    

def Persantage_Approved_Self_Employed ():
    engine=connect_to_database ()
    df = pd.read_sql_table('cdw_sapp_loan_application', engine) 
    #Percentage of Applications Approved for Self-Employed Applicants
    self_employed_df = df[df['Self_Employed'] == 'Yes']
    total_applications = len(self_employed_df)
    approved_applications = len(self_employed_df[self_employed_df['Application_Status'] == 'Y'])
    approval_rate = approved_applications / total_applications
    notapproval_rate = 1 - approval_rate  # Disapproval rate is the remainder
            
    plt.figure(figsize=(10, 6))
    explode = (0.05,0.05)
    plt.pie([approval_rate, notapproval_rate], labels=['Approved', 'Not Approved'], 
                    autopct='%1.1f%%', colors=['cyan', 'gold'], startangle=90,explode=explode,textprops={'fontsize': 14})
    plt.title('Percentage of Applications Approved for Self-Employed Applicants',fontsize=16)
    # Add a circle at the center of the pie chart
    centre_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    #The plt.gcf() method gets the current figure, and fig.gca() gets the current axis.

    print(plt.show())

def Persantage_rejected_male_applicant():
    engine=connect_to_database ()
    df = pd.read_sql_table('cdw_sapp_loan_application', engine)  # Load data from database 
    married_male_df = df[(df['Gender'] == 'Male') & (df['Married'] == 'Yes')]
    total_married_male = len(married_male_df)
    rejected_applications = len(married_male_df[married_male_df['Application_Status'] == 'N'])

    rejection_rate = rejected_applications / total_married_male
    rejected_applications = married_male_df[married_male_df['Application_Status'] == 'N']
    total_rejected = len(rejected_applications)
    # print(rejected_applications)
    # input(nav)
    rejection_rate = total_rejected / total_married_male
    accepted_rate = 1 - rejection_rate  
        
    plt.figure(figsize=(10, 6))
    explode = (0.05,0.05)
    plt.pie([rejection_rate, accepted_rate], labels=['Rejected', 'Accepted'],  autopct='%.2f%%',
        colors=['red', 'lightgreen'], startangle=90,explode=explode,textprops={'fontsize': 14})
    plt.title('Percentage of Applications Rejected for Married Male Applicants',fontsize=16)
    # Add a circle at the center of the pie chart
    centre_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    print("\nTotal Married Male: ", total_married_male)
    print("Total Rejections  : ", rejected_applications)
    print("Total Rejections  : ", total_rejected)
    print("Rejected Rate %  : ", rejection_rate*100)
    print(plt.show())

def Top_Three_Months_with_Largest_Transaction_Volume():
    engine=connect_to_database ()
    df = pd.read_sql_table('cdw_sapp_credit_card', engine)
    monthly_data = df.groupby('MONTH')['TRANSACTION_VALUE'].sum()
    # Get the top three months with the largest transaction volume
    top_three = monthly_data.nlargest(3)
    print(top_three)
    # Plot the top three months
    colors = ['green', 'blue', 'orange']
    plt.bar(top_three.index, top_three.values,color=colors)
    plt.xlabel('Month')
    plt.ylabel('Transaction Volume')
    plt.title('Top Three Months with Largest Transaction Volume')
    plt.grid(linestyle='--')
    plt.show()
    
def branch_highest_value_healthcare_transactions():
    engine=connect_to_database ()

    df = pd.read_sql_table('cdw_sapp_credit_card', engine)
    # Filter the data to include only healthcare transactions
    healthcare_data = df[df['TRANSACTION_TYPE'] == 'Healthcare']

    # Group the data by branch code and sum the transaction values
    branch_data = healthcare_data.groupby('BRANCH_CODE')['TRANSACTION_VALUE'].sum()
    branch_data = branch_data.sort_values(ascending=False)


    # Get the branch with the highest total dollar value of healthcare transactions
    highest_branch = branch_data.idxmax()
    #idxmax() method of a pandas DataFrame object to return the index of the maximum value across a specified axis.
    top_branch = branch_data.nlargest(5)
    print(top_branch)

    #plt.plot(branch_data1)
    sizes=[90,70,50,30,10]
    plt.bar(top_branch.index,top_branch,edgecolor='black')
    plt.scatter(top_branch.index,top_branch,s=sizes)
    #plt.bar(top_three.index, top_three.values,color=colors, edgecolor='black')
    plt.xlabel('Branch Code')
    plt.ylabel('Transaction Value')
    plt.xticks(top_branch.index)
    #plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title(f'Healthcare Transactions by Branch (Highest: {highest_branch})')
    plt.show()
        
    

    



    