import serial

# Setup UART Serial Port on the Pi
GPSSerial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

while True:
    # Read data from GPS serial port
    GPSData = GPSSerial.readline().decode('ascii', errors='ignore').strip()  # Decodes byte string to ASCII and removes extra whitespace

    # Find the index where RMC data starts and ends
    startIndex = GPSData.find("$GPRMC,")
    endIndex = GPSData.find("$GPVTG")

    if startIndex != -1 and endIndex != -1:
        # Create substring for RMC data
        RMCData = GPSData[startIndex + len("$GPRMC,"):endIndex]
        
        # Split RMC data into components
        DataList = RMCData.split(",")
        
        # Display the parsed data list
        print(DataList)

        # Extract GPS information if data format is complete
        if len(DataList) >= 9:  # Ensure there are enough elements
            GPSTime = DataList[0]
            GPSLatitude = DataList[2]
            GPSLongitude = DataList[4]
            GPSDate = DataList[8]

            # Display extracted information
            print("Time:", GPSTime)
            print("Latitude:", GPSLatitude)
            print("Longitude:", GPSLongitude)
            print("Date:", GPSDate)
    else:
        print("Incomplete GPS data or missing markers.")

    # Display raw GPS data for debugging
    print("Raw GPS Data:", GPSData)
