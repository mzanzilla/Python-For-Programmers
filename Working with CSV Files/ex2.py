#Reading from a csv file
import csv
#With statement to handle file objects and ensure it is properly closed after execution
with open("accounts.csv", "r") as accounts:
    #print formatting
    print(f"{'account':<10}{'Name':<10}{'Balance':>10}")
    #Reader function returns an object that reads csv-format data from specified file object
    reader = csv.reader(accounts)
    #returns each record as a list of values which is unpacked into variables - account, name, and balance
    for record in reader:
        account, name, balance = record
        print(f"{account:<10}{name:<10}{balance:>10}")
