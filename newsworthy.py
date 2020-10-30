from flask import Flask, render_template, request
from requests import get
from json import loads
from news import news
import jinja2

# david's trash
# #http://newsapi.org/v2/everything?q=bitcoin&from=2020-09-22&sortBy=publishedAt&apiKey=58e9f79801054ad698f961de67f7c258
# page = get("http://newsapi.org/v2/top-headlines?country=us&apiKey=58e9f79801054ad698f961de67f7c258")
# page.encoding = page.apparent_encoding
# json_page = dict(loads(page.text))["articles"]
# news_list = list()
# for i in json_page:
#     newNewsObject = news()
#     newNewsObject.assign_attributes(i)
#     news_list.append(newNewsObject)
# # for i in news_list:
# #     print(i)

# start the api app.
app = Flask(__name__)
app.static_folder = "static"

# ian's trash


def getRequests(arr):
    nested_arr = []
    for i in arr:
        print(i)
        url = "http://newsapi.org/v2/top-headlines?q=%s&from=2020-09-24&sortBy=publishedAt&apiKey=537a36338c1e4d119f54dfec8f08ba9b" % i
        print(url)
        page = get(url)
        page.encoding = page.apparent_encoding
        json_page = dict(loads(page.text))["articles"]
        news_list = list()
        for i in json_page:
            newNewsObject = news()
            newNewsObject.assign_attributes(i)
            news_list.append(newNewsObject)
        nested_arr.append(news_list)
    return nested_arr


news_list = []
topics_copy = []


@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
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
        "index.html",
        news_list=news_list,
        topics_list=topics_copy
    )


if __name__ == "__main__":
    app.run(debug=True)
