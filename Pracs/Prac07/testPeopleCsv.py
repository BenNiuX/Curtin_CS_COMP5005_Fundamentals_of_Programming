from people import Address, Person, Staff, Student, Postgrad, Undergrad, DodInvalid

CSV_COL_TYPE = 0
CSV_COL_NAME = 1
CSV_COL_DOB = 2
CSV_COL_ADDR = 3
CSV_COL_ID = 4
CSV_COL_MAX = 5
CSV_ADDR_NUM_STREET = 0 # Num and street split by space
CSV_ADDR_SUB = 1
CSV_ADDR_POST = 2
CSV_ADDR_MAX = 3

peoples = []
classes = [Staff, Postgrad, Undergrad]
print('#### People Test Program ###')
input_files = ['not_exist.csv', 'people.csv', 'people_error.csv']
with open('errorLog.txt', 'w') as errLog:
    for input_file in input_files:
        try:
            with open(input_file, 'r') as csvFile:
                for line in csvFile.readlines():
                    lineSplit = line.strip().split(':')
                    if len(lineSplit) == CSV_COL_MAX:
                        addrStr = lineSplit[CSV_COL_ADDR]
                        addrSplit = addrStr.strip().split(',')
                        if len(addrSplit) == CSV_ADDR_MAX:
                            streetSplit = addrSplit[CSV_ADDR_NUM_STREET].strip().split(' ', 1)
                            if len(streetSplit) == 2:
                                addr = Address(streetSplit[0].strip(), streetSplit[1].strip(),
                                        addrSplit[CSV_ADDR_SUB].strip(), addrSplit[CSV_ADDR_POST].strip())
                                for type_class in classes:
                                    csv_type = lineSplit[CSV_COL_TYPE].strip()
                                    if csv_type == type_class.myclass:
                                        try:
                                            peoples.append(type_class(lineSplit[CSV_COL_NAME], lineSplit[CSV_COL_DOB],
                                                        addr, lineSplit[CSV_COL_ID]))
                                        except DodInvalid as err:
                                            print(err)
                                            errLog.write(str(err) + '\n')
                            else:
                                print("Street can't recornised, skip:", addrSplit[CSV_ADDR_NUM_STREET])
                        else:
                            print("Addr can't recornised, skip:", addrStr)
                    else:
                        print("Line can't recornised, ignore:", line)
        except OSError as err:
            print('Error with file open: ', err)
            errLog.write(str(err) + '\n')
        except Exception as err:
            print('Unexpected error: ', err)
            errLog.write(str(err) + '\n')
        finally:
            print('Handled file: ', input_file)

for people in peoples:
    people.displayPerson()
    print()
