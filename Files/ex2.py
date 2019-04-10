#Exercise 2 - Reading from a file
with open("accounts.txt", "r") as accounts:
    print(f"{'Account':<10}{'Name':<10}{'Balance': >10}")
    for record in accounts:
        #the split method splits the one line into a list
        #The list is then unpacked into three variables
        account, name, balance = record.split()
        #displays the variables in columns using field wdths
        print(f"{account:<10}{name:<10}{balance:>10}")
