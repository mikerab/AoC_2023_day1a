# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

masterCalibration = 0
numberOfLines = 0

# Open a document
doc = open('input.txt', 'rt')

for line in doc:
    # Read a line
    # This is wrong, line has already been read // currLine = doc.readline()
    numberOfLines = numberOfLines + 1
    print(line)

    firstNumber = 0
    calibrationNumber = 0

    # Start reading each character in order and if it's a number, multiply by 10, store it and stop
    for char in line:
        if char.isnumeric():
            firstNumber = int(char) * 10
            print(f'firstNumber is {firstNumber}')
            break

    if firstNumber == 0:
        print('ERROR!!!! firstNumber is still zero')

    # Now start from the end of the line and reverse order and find that number.
    for char in reversed(line):
        if char.isnumeric():
            calibrationNumber = firstNumber + int(char)
            print(f'calibrationNumber is {calibrationNumber}')
            break

    # Add the calibration number to the master number
    masterCalibration = masterCalibration + calibrationNumber
    print(f'masterCalibration is {masterCalibration}')
    # Read the next line and repeat until end of document

# Close the document
doc.close()

# print the master number
print(f'Master Calibration Number is {masterCalibration} based on {numberOfLines} lines')

