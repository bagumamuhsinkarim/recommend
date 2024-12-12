import sys

sys.path.append("/home/muhsin/Desktop/recommend")
#print(sys.path)

from recommend import recommendationengine
from recommend import storageengine
from recommend import filteringengine

def main():
    storage = storageengine.StorageEngine("./test/Data/data.json")
    filter = filteringengine.FilteringEngine()

    mydata = storage.returnDataInCategory("movies") + storage.returnDataInCategory("songs") + storage.returnDataInCategory("notifications")

    for value in mydata:
        print(value)



if __name__ == '__main__':
    main()
