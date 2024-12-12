import sys

sys.path.append("/home/muhsin/Desktop/recommend")

from recommend.user import User
from recommend.history import History
from recommend.location import Location

#creating a user
my_user = User("001")

#adding to the user's history
my_user.addToHistory(["notifications", "NOT001"])
my_user.addToHistory(["notifications", "NOT004"])
my_user.addToHistory(["notifications", "NOT003"])
my_user.addToHistory(["notifications", "NOT002"])
print(my_user.getHistory().viewHistory())

#removing history of a user
my_user.deleteFromHistory("NOT004")
print(my_user.getHistory().viewHistory())

#search for a particular feature instane id in history
exists = my_user.searchInHistory("NOT002")

if exists == False:
    print("Not in user history")

else:
    print("Present in user's history")
