'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members

    This function should remove all rows from currentMem containing 'no'
    in the 'Active' column and appends them to exMem.
    '''
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
