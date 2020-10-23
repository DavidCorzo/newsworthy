import os
from news import News
from requests import get
from json import loads
from flask import Flask, render_template, request
from datetime import date, timedelta

app = Flask(__name__)
app.static_folder = "static"

environment = os.getenv("ENVIRONMENT", "development")

news_list = []
topics_copy = []


def getRequests(arr):
    nested_arr = []

    for i in arr:
        print(i)
        # max_date = date.today()
        # print(max_date)
        url = f"http://newsapi.org/v2/top-headlines?q={i}&from=2020-09-24&sortBy=publishedAt&apiKey=676d572fbac34973aeb551e96828d0e9"

        print(url)

        page = get(url)
        page.encoding = page.apparent_encoding
        json_page = dict(loads(page.text))["articles"]
        news_list = list()

        for i in json_page:
            newNewsObject = News()
            newNewsObject.assign_attributes(i)
            news_list.append(newNewsObject)
        nested_arr.append(news_list)

    # for i in news_list:
    #     print(i)
    return nested_arr


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

            content = getRequests(topics)
            for i in topics:
                topics_copy.append(i)
            for i in content:
                news_list.append(i)
        
        elif "RemoveTopic" in request.form:
            print("yeah")
            delete_val = request.form["deleteTopic"]
            print(delete_val)
            index_del = topics_copy.index(delete_val)
            print(index_del)
            topics_copy.remove(delete_val)
            news_list.pop(index_del)

        else:
            pass
        
    
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
