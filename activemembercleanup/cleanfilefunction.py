'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
        #TODO: Open the exMem file in a+ mode

        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.

        #TODO: iterate through the members and create a new list of the innactive members

        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem

        with open(currentMem,'r+') as writeFile: 
            with open(exMem,'a+') as appendFile:
                #get the data
                writeFile.seek(0)
                members = writeFile.readlines()
                #remove header
                header = members[0]
                members.pop(0)
                    
                inactive = [member for member in members if ('no' in member)]
                '''
                The above is the same as 

                for member in members:
                if 'no' in member:
                    inactive.append(member)
                '''
                #go to the beginning of the write file
                writeFile.seek(0) 
                writeFile.write(header)
                for member in members:
                    if (member in inactive):
                        appendFile.write(member)
                    else:
                        writeFile.write(member)      
                writeFile.truncate()
                    
        memReg = 'members.txt'
        exReg = 'inactive.txt'
        cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
    


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

def testMsg(passed):
    if passed:
        return 'Test Passed'
    else :
        return 'Test Failed'

testWrite = "/testWrite.txt"
testAppend = "/testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    

                