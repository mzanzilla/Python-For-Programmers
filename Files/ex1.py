#Exercise 1 - writing to a text file
#With statements ensures resources as effectively used. In this case
#that files closed after being accessed

#accounts is an object variable
with open("accounts.txt", "w") as accounts:
    accounts.write("100 Jones    24.98\n")
    accounts.write("101 Doe      14.98\n")
    accounts.write("102 Mensah   20.98\n")
    accounts.write("300 White 0.00\n")
    accounts.write("103 Adole    20.98\n")
    #Using a print statement and providing a file argument will write to the file
    #and automatically insert a \n
    print("104 Asiedu   20.00", file=accounts)
