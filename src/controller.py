from random import randint

def getID (String):
    listAfterSplit = String.split("/")
    newString = listAfterSplit[-1]
    idField = newString.split(".")
    idSong = idField[-2]

    return idSong

def formatName (name):
    newName = name.replace(" ", "-")
    return newName

def getRecommendList(list):
    tempList = []
    recommendList = []
    for _ in range(5):
        temp = randint(0, 19)
        tempList.append(temp)
        if list[temp] in tempList:
            continue
        else:
            recommendList.append(list[temp])

    return recommendList
