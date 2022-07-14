import datetime
import os

print(os.environ["USERPROFILE"])
e = datetime.datetime.now()
print(e.strftime("%b %d, %Y @ %I:%M:%S\n"))


def forUserInput(username, week):
    numstu = int(input("Enter the number of students: "))
    contract = open("studentFile.txt","w")
    for amount in range(numstu):
        studentname = input("Enter the name of the student: ")
        pts = int(input("Enter student's contract point: "))
        contract.write(f"Name: {studentname}\t\tContract Points: \t{pts}\n")
    contract.close()
    print(f"\n{username}, there are the Contract Points for Week: {week}\n")
    return

# main
username = input("Enter your name: ")
week = int(input("Enter week number: "))
forUserInput(username, week)
print(f"Contract points\n-------------------------------------------------")
contract = open("studentFile.txt","r")
print(contract.read())

"""
DECLARE week<-int(input("Enterweeknumber:")) : INTEGER
DECLARE username<-input("Enteryourname:") : STRING
DECLARE pts<-int(input("Enterstudent'scontactpoint:")) : INTEGER
DECLARE studentname<-input("Enterthenameofthestudent:") : STRING
DECLARE numstu<-int(input("Enterthenumberofstudents:")) : INTEGER
import datetime
import os

OUTPUT os.environ["USERPROFILE"]
e<-datetime.datetime.now()
OUTPUT e.strftime("%b %d, %Y @ %I:%M:%S\n"


FUNCTION  forUserInput(username, week):
RETURNS // What gets sent back?
ENDFUNCTION
INPUT numstu<-int(input("Enterthenumberofstudents:"))
    contract<-open("studentFile.txt","w")
    FOR amount in range(numstu):
INPUT studentname<-input("Enterthenameofthestudent:")
INPUT pts<-int(input("Enterstudent'scontactpoint:"))
        contract.write(f"Name: {studentname}\t\tContract Points: \t{pts}\n")
    contract.close()
    OUTPUT f"\n{username}, there are the Contract Points FOR Week: {week}\n"  //Pseudocode can't handle this
    return

// main
INPUT username<-input("Enteryourname:")
INPUT week<-int(input("Enterweeknumber:"))
forUserInput(username, week)
OUTPUT f"Contract points\n-------------------------------------------------"
contract<-open("studentFile.txt","r")
OUTPUT contract.read(
"""