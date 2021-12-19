
def getEmployeeData():
    employeeID = 0
    employeeName = ""
    employeeEMail = ""
    employeeAddress = ""
    employeeSalary = 0.0

    tempDict = {"Employee ID": 0, "Employee Name": "", "Employee E-Mail": "", "Employee Address": "", "Employee Salary": 0.0}

    #Get employee ID
    employeeID = int(input("Enter employee ID: "))
    while(employeeID > 9999999):
        print("Employee ID was too large. It must be 7 digits or fewer. Please try again.")
        employeeID = int(input("Enter employee ID: "))
    tempDict["Employee ID"] = employeeID
    #Get employee Name
    validName = False
    while(validName == False):
        employeeName = input("Enter employee Name: ")
        validName = True
        for letter in employeeName:
            if(not(letter == " " or letter == "'" or letter == "-" or letter.isalpha())):
                validName = False
                break
        if(validName == False):
            print("Invalid Name. Name must containt only letters, spaces, or the characters ' or - \nPlease try again.")
    tempDict["Employee Name"] = employeeName
    #Get EMail address
    validEmail = False
    while(validEmail == False):
        employeeEMail = input("Enter employee E-Mail address: ")
        validEmail = True
        for char in employeeEMail:
            if(not(char.isalnum() or char == "@" or char == ".")):
                validEmail = False
                break
        if(validEmail == False):
            print("Invalid E-Mail address. E-Mail can not contain the following characters: ! \" ' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \ )")
            print("Please try again.")

    tempDict["Employee E-Mail"] = employeeEMail
    #Get Address
    enterAddress = ""
    while(enterAddress != "yes" or enterAddress != "no"):
        enterAddress = input("Does the employee have an address to enter?: ").lower()
        if(enterAddress != "yes" and enterAddress != "no"):
            print("Invalid response. Enter 'yes' or 'no'")
        else:
            break
    if(enterAddress == "no"):
        tempDict["Employee Address"] = "N/A"
    else:
        validAddress = False
        while(validAddress == False):
            employeeAddress = input("Enter employee's address: ")
            validAddress = True
            for char in employeeAddress:
                if(not(char.isalnum() or char == "." or char == " ")):
                    validAddress = False
                    break
            if(validAddress == False):
                print("Invalid address. Address can not contain the following characters:  ! \" ' @ $ % ^ & * _  = + < >  ? ; : [ ] { } ")
                print("Please try again.")
        tempDict["Employee Address"] = employeeAddress
    #Get Salary
    employeeSalary = float(input("Enter employee salary: $"))
    while(employeeSalary < 18 or employeeSalary > 27):
        if(employeeSalary < 18):
            print("Salary must be above 18.00. Please try again.")
        elif(employeeSalary > 27):
            print("Salary must be under $27.00. Please try again.")
        employeeSalary = float(input("Enter employee salary: $"))
    tempDict["Employee Salary"] = employeeSalary
        


    return tempDict






def inputData():
    listOfDicts = []
    moreEntries = "yes"

    while (moreEntries != "no"):
        if(moreEntries == "no"):
            break
        elif(moreEntries == "yes"):
           listOfDicts.append(getEmployeeData())
        else:
            print("Invalid response; Please try again.")
        moreEntries = input("Would you like to input more employee data? Enter 'yes' or 'no': ").lower()
    
    return listOfDicts



def main():
    listOfData = []
    #getEmployeeData()
    listOfData = inputData()
    for i in listOfData:
        i["Employee Name"] = i["Employee Name"] + " IT Department"
        i["Employee Salary"] = round(i["Employee Salary"] * 1.3, 2)

    for i in listOfData:
        print(i)


main()