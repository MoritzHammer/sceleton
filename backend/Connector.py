import requests

class Connection:
    def __init__(self, ipAdress):
        self.url = None
        self.ip = ipAdress

    def requestProcess(self, metaDataInfo, deviceAlias=""):
        endpoint, isBalluffApi, method = self.endpointConstructor(metaDataInfo, deviceAlias)
        self.urlManager(endpoint, isBalluffApi)
        return self.requestManager(method)

    def endpointConstructor(self, metaDataInfo, deviceAlias="") -> (str, bool, str):
        endpointInfos = ()
        if metaDataInfo == "deviceId":
            # endpointDeviceIdentification
            isBalluffApi = True
            endpointInfos = ("/devices/identification", isBalluffApi, "get")
        elif metaDataInfo == "deviceInfo":
            # endpointDeviceInformation
            isBalluffApi = False
            endpointInfos = (f"/devices/{deviceAlias}/identification", isBalluffApi, "get")
        elif metaDataInfo == "masterId":
            # endpointIdentification
            isBalluffApi = True
            endpointInfos = ("/identification", isBalluffApi, "get")
        elif metaDataInfo == "masterInfo":
            # endpointSystemInfo
            isBalluffApi = True
            endpointInfos = ("/", isBalluffApi, "get")
        elif metaDataInfo == "diagnostics":
            # endpointSystemInfo
            isBalluffApi = True
            endpointInfos = ("/diagnostics/leds", isBalluffApi, "get")
        return endpointInfos

    def urlManager(self, endpoint, isBalluffApi):
        if isBalluffApi:
            self.url = f"http://{self.ip}/api/balluff/v1{endpoint}"
        elif not isBalluffApi:
            self.url = f"http://{self.ip}/iolink/v1/devices{endpoint}"

    def requestManager(self, requestMethod):
        return requests.request(method=requestMethod, url=self.url).json()

