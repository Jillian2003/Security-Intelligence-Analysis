'''
Firepower:
Pull Logs for Security Intelligence and Activity
 
Umbrella:
Pull Logs for Users Site access

Observe correlation of Security threats between them and make a table of all the threats and their CVE's
'''

#-------------> Convert the pdf file into csv and load info of dataframes <---------------------
import tabula
import pandas as pd

tabula.convert_into("firepower.pdf", "output.csv", output_format="csv", pages='all')

firepower = pd.read_csv("output.csv")
umbrella = pd.read_csv("Logs (UTC).csv")

umbrella.info()
firepower.info()

#------------> Sort the data by saving the columns of the users who are blocked and drop null coloumns<----------------


umbrella_block = umbrella[umbrella["Action"] == "Blocked"]
umbrella_block.dropna(axis=1, how='all', inplace=True)
umbrella_block.info()
umbrella_block.to_csv("umbrella_logs.csv")

firepower_block = firepower [(firepower["Action"]== "Block")]
firepower_block.dropna(how='all', axis=1, inplace=True) 
firepower_block.head()
firepower_block.to_csv("firepower_logs.csv")
print("done")  

#------------> Merge the Firepower and Umbrella logs using the Responder IP in the Firepower Logs <----------------

firepower_logs = pd.read_csv("firepower_logs.csv")
umbrella_logs = pd.read_csv("umbrella_logs_csv")

# Merge the two DataFrames based on the "Responder IP" column in Firepower logs
merged_logs = pd.merge(firepower_logs, umbrella_logs, left_on="Initiator IP", right_on="Resolved IP", how="inner")

# Save the merged DataFrame to a new CSV file
merged_logs.to_csv("merged_logs.csv", index=False)

#--------------> Sort the data and pull columns that list the applications that were blocked and list them <---------------

df = merged_logs[[ "Categories","Blocked Categories", "Application", "Application Category", "Resolved IP"]]
print(df)
column_data = merged_logs['Application']

# Find unique values
unique_values = column_data.unique()
print(unique_values)

#-------------> Research possible CVE's for these applications and map them to the Applications column <----------------

possible_cves= {'Microsoft Account': 'CVE-20XX-XXXX', etc. }

# Map CVEs to the 'Applications' column
merged_logs['CVEs'] =merged_logs['Application'].map(possible_cves)
merged_logs.to_csv("CVE_LIST.csv")
print("done")
















