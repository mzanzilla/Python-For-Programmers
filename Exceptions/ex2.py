#Combining with statements and try except statements
try:
    with open("sometext.txt", "r") as accounts:
        print(f"{'id':<3}{'name':<7}{'grade'}")
        for record in accounts:
            studentId, name, grade = record.split()
            print(f"{studentId:<3}{name:<7}{grade}")
except FileNotFoundError:
    print("The file Name you specified does not exist")
