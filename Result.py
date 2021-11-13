import json


class Device:
    name = ""
    tagType = ""
    tags = []

    def __init__(self, name, tagType, tags):
        self.name = name
        self.tagType = tagType
        self.tags = tags

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DeviceTag:
    name = ""
    tagType = ""
    tags = []

    def __init__(self, name, tagType, tags):
        self.name = name
        self.tagType = tagType
        self.tags = tags

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Tag:
    valueSource = ""
    opcItemPath = ""
    dataType = ""
    name = ""
    tagType = ""
    opcServer = ""

    def __init__(self, valueSource, opcItemPath, dataType, name, tagType, opcServer):
        self.valueSource = valueSource
        self.opcItemPath = opcItemPath
        self.dataType = dataType
        self.name = name
        self.tagType = tagType
        self.opcServer = opcServer

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
