#Writing to a csv file
import csv
with open("accounts.csv", "w", newline="") as accounts:
    #the csv module's writer function returns an object that writes csv data to specified file object
    writer = csv.writer(accounts)
    #Each call to the writer’s writerow method receives an iterable to store in the file
    writer.writerow([100, "Jones", 24.98])
    writer.writerow([200, "Doe", 340.98])
    writer.writerow([300, "White", 0.00])
    writer.writerow([400, "Stone", -42.16])
    writer.writerow([500, "Rich", 224.62])
