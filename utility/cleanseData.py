def cleanseData(data):
    data = removeSpaces(data)
    data = setStringSize(data)
    return data

def removeSpaces(data):
    return data.strip().replace("\n", "")

def setStringSize(string, size=2000):
    if len(string) > size:
        return string[:size]
    return string