*This is an assignment from IBM course Python for data science...*

## Question: ##
Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
Given the file **currentMem**, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the **exMem** file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

## Step 1: Generate the currentMem and exMem files ##
First step is to generate the files for membership using random functions.

```Python
#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

## add this part to test the files
with open(memReg, 'r') as currentMem:
    list_cMem = currentMem.read()

with open(exReg, 'r') as exMem:
    list_exMem = exMem.read()

print("Current Members:")
print(list_cMem)
print("Ex Members:")
print(list_exMem)

```

**String Format Syntax**

Here in this file we notice that the lines are generate in a particular format. To realise this the **format syntax** are used.

```Python
data = "{:^13}  {:<11}  {:<6}\n"
```
data is a string and it has three brackets {}. This is called placeholder. Within the place holder is the format of the content. **:^13** means 13 characters long and center aligns. **:<** means left aligns. When writing the text to the file, **data.format()** is used. The input arguments of **format()** should match the placeholder in the data, in our case means three input arguments.

## Step 2: Clean the members.txt ##
In this step we will read the **members.txt** file and move the inactive members to the **inactive.txt** file.

### My answer to the question ##
Here is my answer to the question. Different from the recommended answer, we create a list of active members. The inactive members will be append to the **inactive.txt** directly.

```Python
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem, 'r+') as cMemFile:
        #TODO: Open the exMem file in a+ mode
        with open(exMem, 'a+') as exMemFile:
            # first line is the header, we need to write it to the file again
            header = cMemFile.readline()

            # create a list for the active members
            # the inactive members will be append to the file directly
            list_activeMem = []
            for line in cMemFile:
                memStatus = line.split()
                is_active = memStatus[2]
                if is_active == 'yes':
                    list_activeMem.append(line)
                else:
                    exMemFile.write(line)


            # Go to the beginning of the currentMem file
            # write the header back to the members.txt
            # then go through the active member list to write the active members back to the file
            # finally truncate the unoverwritten part
            cMemFile.seek(0,0)
            cMemFile.write(header)
            for mem in list_activeMem:
                cMemFile.write(mem)
            cMemFile.truncate()



# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

```
### Recommended answer ###

Different from my answer, this solution use **readlines()** to directly read all the lines from the **members.txt** into a list. Header line is the first element in the list and use **pop(0)** to delete it from the list.

Then it use the list comprehension to generate a list of inactive members. Notice that in the list there are no names in it, so "'no' in member" works. If the there are names in the list, this may cause some unexpected results.

```Python
def cleanFiles(currentMem,exMem):
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

```
