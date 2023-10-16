import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import secret

# Q Find and plot the percentage of applications approved for self-employed applicants.

def connect_to_database ():
    user= secret.mysql_username
    passw = secret.mysql_password
    engine = create_engine(f'mysql+mysqlconnector://{secret.mysql_username}:{secret.mysql_password}@localhost/creditcard_capstone')
    return engine
    

def Persantage_Approved_Self_Employed ():
    engine=connect_to_database ()
    df = pd.read_sql_table('cdw_sapp_loan_application', engine) 
    #Percentage of Applications Approved for Self-Employed Applicants
    self_employed_df = df[df['Self_Employed'] == 'Yes']
    total_applications = len(self_employed_df)
    approved_applications = len(self_employed_df[self_employed_df['Application_Status'] == 'Y'])
    approval_rate = approved_applications / total_applications
    notapproval_rate=1-approval_rate
    approval_per=approval_rate*100
    print(approval_per)
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
    plt.legend(labels=['Approved', 'Not Approved'],loc='upper left',bbox_to_anchor=(1,1))
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
    plt.legend(labels=['Rejected', 'Accepted'],loc='upper left',bbox_to_anchor=(1,1))
    print(plt.show())

def Top_Three_Months_with_Largest_Transaction_Volume():
    engine=connect_to_database ()
    
    df = pd.read_sql_table('cdw_sapp_credit_card', engine)
    top_month = df.groupby('MONTH')['TRANSACTION_VALUE'].sum()
    top_month = top_month.sort_values(ascending=False).head(3)
    print(top_month)
    colors = ['peru',  'burlywood','bisque']
    ax = top_month.plot.bar(rot='horizontal',color=colors)

    ax.set_title(' Top three months with the largest volume of transaction data.')
    ax.set_xlabel('Months')
    ax.set_ylabel('Transaction Amount')
    ax.set_ylim(200000, 203000)
    ax.bar_label(ax.containers[0])
    """ax.bar_label(ax.containers[0]) is a method call in Matplotlib that adds labels to the bars in a bar plot. The ax parameter is the Axes object that represents the plot, and the containers[0] parameter is the BarContainer object that contains the bars in the plot.

The bar_label() method adds labels to the bars in the given BarContainer. You may need to adjust the axis limits to fit the labels. The fmt parameter specifies the format string for the labels, and the label_type parameter specifies whether to label the edge or center of each bar. The padding parameter specifies the padding between the label and the bar.

Here’s an example of how to use ax.bar_label(ax.containers[0]):"""

    plt.show()
    
def branch_highest_value_healthcare_transactions():
    engine=connect_to_database ()
    df = pd.read_sql_table('cdw_sapp_credit_card', engine)
    # Filter the data to include only healthcare transactions
    healthcare_data = df[df['TRANSACTION_TYPE'] == 'Healthcare']
    # Group the data by branch code and sum the transaction values
    healthcare_data = healthcare_data.groupby('BRANCH_CODE')['TRANSACTION_VALUE'].sum()
    healthcare_data = healthcare_data.sort_values(ascending=False)
    top_branch=healthcare_data.head(1)
    ax = top_branch.plot.bar(rot='horizontal',color='palegreen',width=0.2)
    ax.set_title('Top Branch in Healthcare Transactions')
    ax.set_xlabel('Top Branch Code')
    ax.set_ylabel('Transaction Amount')
    ax.bar_label(ax.containers[0],color='red')
    
    plt.show()
        
    

    



    