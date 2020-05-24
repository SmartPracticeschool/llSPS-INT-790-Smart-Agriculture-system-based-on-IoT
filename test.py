import sys
import ibmiotf.device

organization = "awijzh"
deviceType = "Data"
deviceId = "12345"
authMethod = "token"
authToken = "123456789"


def commandHandler(cmd):
    print("Command received: %s" % cmd.data)

    for key in cmd.data.keys():
        if key == 'motor':
            if cmd.data['motor'] == 'ON':
                print("MOTOR is turned ON")

            elif cmd.data['motor'] == 'OFF':
                print("MOTOR is turned OFF")


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:

    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:
    deviceCli.commandCallback = commandHandler
