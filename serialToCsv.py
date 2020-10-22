'''
Author: Jesus Minjares
Date: 10/21/2020
App:
    The application will store serial data into a .csv file.It will use 
    serial module.
Note:
    Using PyCharm, in order to run the following code the modules must be
    installed.
    Steps to install modules:
        Go to file
            Setting/Preferences
                Project
                    Python Interpreter
                        '+', top right for Windows, bottom left for MacOS
                            search for the module
                                install package/s
                                    enter ok
Terminate code:
    Windows:
        CTRL + C
    MacOS:
        COMMAND + D
'''
# import modules
import csv
import serial 
# set variables to 0
sample, adcRaw, volt = 0, 0, 0
# set the filed names
fieldnames = ["sample", "adcRaw", "volt"]
'''
Note: If using PyCharm with Windows:
        set serial port to 'COMX', X being the com port number 
      elif Using PyCharm with MacOs:
        set serial port as /dev/tty*
      else:
        set serial port as /dev/ttySx, x being the number of your com port i.e. com3 -> /dev/ttyS3
'''
SERIAL_PORT = '/dev/ttyS3' # using WSL, setting COM3
SERIAL_RATE = 9600  # set baudrate

# create headers for the .csv file 
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

#   initialize serial 
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

# infinite loop 
while True:
    with open('data.csv', 'a') as csv_file:  # open file as appened
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
        reading = ser.readline().decode('utf-8');  # store serial reading as utf-8 into reading variable
        reading.replace('\r\n','')  # remove \r\n
        data = reading.split(' ')  # split the data with spaces 
        adcRaw = int(data[0])  # store data[0] as an integer 
        volt = float(data[1])  # store data[1] as a float  
        # create a dictionary to store the serial data 
        info = {
            "sample": sample,
            "adcRaw": adcRaw,
            "volt": volt
        }
        csv_writer.writerow(info) # write dictionary to the file 
        print(info)  # display dictionary 
        sample += 1  # increment the sample 
