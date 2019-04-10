#Updating records in a text file
#We want to update the name for record number 300 - change name from White to Williams
#Updating textfiles can affect formattting because texts may have varrying length.
#To address this a temporary file will be created
import os
tempFile = open("tempFile.txt", "w")
accounts = open("accounts.txt", "r")
#The 'with' statement manages two resource objects
with accounts, tempFile:
    #Loop through each line or record in the text file
    for record in accounts:
        #I split and unpack each line into variables
        account, name, balance = record.split()
        #If the account number is not equal to the record number 300, I want to put that record (or line)
        #in a temporary text file else I want to join the existing record with the name "Williams" to create
        #a new record
        if account != "300":
            tempFile.write(record)
        else:
            newRecord = ' '.join([account, "Williams", balance])
            tempFile.write(newRecord + "\n")

#delete the accounts text file
#remove should be used with caution as it does not warn you about deleting a file
os.remove("accounts.txt")

#rename tempFile to accounts.txt

os.rename("tempFile.txt", "accounts.txt")
