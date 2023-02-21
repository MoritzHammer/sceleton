from flask import Flask
from Connector import Connection

app = Flask(__name__)
TestIpAddress = "192.168.95.181"
metaDataInfos = ["deviceId", "deviceInfo", "masterId", "masterInfo", "diagnostics"]


@app.route('/MasterId')
def get_masterId():
    connection = Connection(TestIpAddress)
    response = connection.requestProcess(metaDataInfos[2])
    return response


@app.route('/MasterInfo')
def get_masterInfo():
    connection = Connection(TestIpAddress)
    response = connection.requestProcess(metaDataInfos[3])
    return response


@app.route('/DevicesId')
def get_devices():
    connection = Connection(TestIpAddress)
    response = connection.requestProcess(metaDataInfos[0])
    return response


@app.route('/DevicesInfo')
def get_deviceinfo():
    connection = Connection(TestIpAddress)
    response = connection.requestProcess(metaDataInfos[0])
    deviceInfos = {}
    for device in response:
        deviceName = device['deviceAlias']
        deviceInfos[deviceName] = connection.requestProcess(metaDataInfos[1], deviceName)
    return deviceInfos


@app.route('/Diagnostics')
def get_diagnostics():
    connection = Connection(TestIpAddress)
    response = connection.requestProcess(metaDataInfos[4])
    return response


if __name__ == "__main__":
    app.run(debug=True)
