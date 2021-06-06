#import pymongo
import pymongo
from pymongo import *

#connect python to mongo
client = MongoClient()

#connect to a new or existing Data Base
Data_Base = client.database
#Data_Base is the name python will use to refer to the database
#DB is the name of the database in mongo(or the oone that will e created)

#Then connect t a collection in the data base
User = Data_Base.collection
# User is the name python uses and collection is the name of the collection in mongo

#My approach was to first create a document with available info then later edit that document 
# To create a document create a dictionary then insert into mongo using a .insert() function
profile = {"Name" : "Eric"}
# This is where you use the .get() for the value of the keys
# eg. age = age_entry.get() ...so this has to be in a funtion that comes after actually getting the data from the entrys
		#Then add it to mongo
User.insert_one(profile)

# Now you can edit the document using a special feature like name as a query
	# If your using same script just use the .update_one() which first takes the query dictionary , then the updated one and the word $set
User.update_one({"Name" : "Eric"} , {"$set" :{"BMI" : "323"}}) #The name and bmi should be replaced with the name of the varriables you have for them

# Or you could create a list of documents in the collection then arrange them in descending order
# Set a limit to only find one which will be the last created document
List = list(User.find({},sort = [( '_id', pymongo.DESCENDING )]).limit(1))  #print List to see the format ..currently idk what that means so..
data = dict(List[0]) # this makes it a dictionary of the first item that we can with
		# get the info you need to make a query
id = data["_id"]  # can be anything else


		# Then you can edit it
User.update_one({"_id" : id}, {"$set" : {"BMI" : "40"}})