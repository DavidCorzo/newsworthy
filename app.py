import os
from news import News
from requests import get
from json import loads
from flask import Flask, render_template, request
from datetime import date, timedelta
import pymongo
from operator import itemgetter

app = Flask(__name__)
app.static_folder = "static"

environment = os.getenv("ENVIRONMENT", "development")

# Usando mongoDB y tests con algunos valores sacados de internet
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsflash_db"]

# Methods -------------------------------------------------------------
def printMDB():
    print(mydb.list_collection_names())
    return "Successful"

def delMDB_Collections():
    for item in mydb.list_collection_names():
        mycol = mydb.get_collection(item)
        mycol.drop()
    return "Successful"

def getRequests(arr):
    nested_arr = []
    for i in arr:
        print(i)
        # max_date = date.today()
        # print(max_date)
        url = f"http://newsapi.org/v2/top-headlines?q={i}&from=2020-10-12&sortBy=publishedAt&apiKey=537a36338c1e4d119f54dfec8f08ba9b"
        print(url)

        page = get(url)
        page.encoding = page.apparent_encoding
        json_page = dict(loads(page.text))["articles"]
        request_list = list()

        for j in json_page:
            newNewsObject = News()
            newNewsObject.assign_attributes(j)
            request_list.append(newNewsObject)
        nested_arr.append(request_list)
    return nested_arr

def createCols(topics):
    for item in topics:
        col = mydb[f"{item}"]
        x = col.insert_one({ "name":"test"})
        z = col.delete_many({})
    for item in mydb.list_collection_names():
        print(item)

mylist = []
def addRequests(content):
    for item in content:
        nestedlist = []
        for news in item:
            list_item = { 
                "author": f"{news.author}", 
                "title": f"{news.title}",
                "description": f"{news.description}",
                "url": f"{news.url}",
                "url_to_image": f"{news.url_to_image}",
                "date_time_of_publishing": f"{news.date_time_of_publishing}",
                "id": f"{news.id}",
                "name": f"{news.name}",
                }
            nestedlist.append(list_item)
        mylist.append(nestedlist)
    return mylist

temp = []
def postDB(mylist): # Aqui esta el error, agrega la misma lista a cada uno
    for item in mydb.list_collection_names():
        mycol = mydb.get_collection(item)
        temp.append(mycol)
    n = 0
    for i in mylist:
        for j in i:
            try:
                x = temp[n].insert_one(j) # mycol.insert_one() for only one value
            except:
                pass
        n+=1

def getDB():
    news_list = []
    for i in mydb.list_collection_names():
        mycol = mydb.get_collection(i)
        nested_news_list = []
        for item in mycol.find():
            newNewsObject = News()
            newNewsObject.author = itemgetter("author")(item)
            newNewsObject.title = itemgetter("title")(item)
            newNewsObject.description = itemgetter("description")(item)
            newNewsObject.url = itemgetter("url")(item)
            newNewsObject.url_to_image = itemgetter("url_to_image")(item)
            newNewsObject.date_time_of_publishing = itemgetter("date_time_of_publishing")(item)
            newNewsObject.id = itemgetter("id")(item)
            newNewsObject.name = itemgetter("name")(item)
            nested_news_list.append(newNewsObject)
        news_list.append(nested_news_list)
    return news_list

def getTopics():
    topics_copy = []
    for item in mydb.list_collection_names():
        topics_copy.append(item)
    return topics_copy

def delDB():
    pass


# Calling Methods -----------------------------------------------------
printMDB()
# delMDB_Collections()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/news", methods=["GET", "POST", "DELETE"])  # main card view page
def run():
    if request.method == "POST":
        if "AddFilters" in request.form:
            first = request.form["firstTopic"]
            second = request.form["secondTopic"]
            third = request.form["thirdTopic"]
            fourth = request.form["fourthTopic"]
            fifth = request.form["fifthTopic"]
            topics = [first, second, third, fourth, fifth]
            createCols(topics)

            # try:
            content = getRequests(topics)
            list = addRequests(content)
            # print(list)
            postDB(list)
            
        
        elif "RemoveTopic" in request.form:
            delete_val = request.form["deleteTopic"]
            mydb.get_collection(delete_val).drop()
            topics_copy = getTopics()
            index = 0
            for topic in topics_copy:
                if topic == delete_val:
                    break
                index+=1
            
            mylist.pop(index)
            printMDB()

        else:
            pass
    
    news_list = getDB()
    topics_copy = getTopics()

    return render_template(
        "news.html",
        news_list=news_list,
        topics_list=topics_copy
        ) 


if __name__ == "__main__":

    debug = False

    if environment == "development" or environment == "local":
        debug = True

    app.run(host="127.0.0.1", debug=debug)
