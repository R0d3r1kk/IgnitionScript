# library for reading csv
import json

import pandas
import os
import Result as Models

os.chdir("/Users/rodrigo.hernandez/Desktop")

# read csv data
data = pandas.read_csv("ENEL_F13A  C01 N01 BMS01 (Core 19) data points.csv", usecols={
    "pointLocator/configurationDescription": str,
    "pointLocator/modbusDataType": str,
    "pointLocator/offset": str,
    "pointLocator/bit": str,
    "name": str
})

# creating device & device Tag
deviceName = "PAC_TEST"
deviceId = "1"
device = Models.Device(deviceName, "Folder", [])
deviceTag = Models.DeviceTag("ONE_TAG", "Folder", [])


def checkDataType(dataTye, dataBit, offset):
    if dataTye == "TWO_BYTE_INT_UNSIGNED":
        return "HRUS"
    if dataTye == "TWO_BYTE_INT_SIGNED":
        return "HR"
    if dataTye == "BINARY":
        return "HR" + str(offset) + "." + str(dataBit)
    if dataTye == "EIGHT_BYTE_INT_UNSIGNED":
        return "HRUI_64"
    if dataTye == "EIGHT_BYTE_INT_SIGNED":
        return "HRI_64"


def replaceDataType(dataTye):
    if dataTye == "TWO_BYTE_INT_UNSIGNED":
        return "Int4"
    if dataTye == "TWO_BYTE_INT_SIGNED":
        return "Int2"
    if dataTye == "BINARY":
        return "Boolean"
    if dataTye == "EIGHT_BYTE_INT_UNSIGNED":
        return "Int8"
    if dataTye == "EIGHT_BYTE_INT_SIGNED":
        return "Int8"


# cycle csv array rows
for i in range(len(data)):
    tag = Models.Tag(valueSource="opc",
                     opcItemPath="ns\u003d1;s\u003d[" + deviceName + "]" + deviceId + "." + checkDataType(
                         data.values[i][1], data.values[i][3], data.values[i][2]),
                     dataType=replaceDataType(data.values[i][1]),
                     name=data.values[i][4],
                     tagType="AtomicTag",
                     opcServer="Ignition OPC UA Server")
    deviceTag.tags.append(tag)

device.tags.append(deviceTag)

#save data to json file a print it
print(device.toJSON())
