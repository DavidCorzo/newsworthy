from flask import Flask, render_template, request
from requests import get
from json import loads
from news import news
import jinja2


#http://newsapi.org/v2/everything?q=bitcoin&from=2020-09-22&sortBy=publishedAt&apiKey=58e9f79801054ad698f961de67f7c258
page = get("http://newsapi.org/v2/top-headlines?country=us&apiKey=58e9f79801054ad698f961de67f7c258") 
page.encoding = page.apparent_encoding
json_page = dict(loads(page.text))["articles"]
news_list = list()
for i in json_page:
    newNewsObject = news()
    newNewsObject.assign_attributes(i)
    news_list.append(newNewsObject)
# for i in news_list:
#     print(i)

# start the api app.
app = Flask(__name__)
app.static_folder = "static"

@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
def run():
    return render_template("index.html",news_list=news_list) 
    
if __name__ == "__main__":
    
    app.run(debug=True)



# ian's trash
# def getRequests(some array []):
#    news_request = "https://idk_which_news_website.com"
#    try:
#        news_content = requests.get(news_request).text
#    except:
#        print(f"unable to get {news_request}")
#        sys.exit(1)
#    news_cards = json.loads(news_content)
#    return news_cards


# if request.method == "POST":
#     if "AddFilters" in request.form:
#         topics = request.form["exampleInputEmail1"]
#         # content = getRequests(topics)
#         # news_content.copy(content) # metodo copiar content a news_content no me recuerdo como era.
        
#         for i in news_content:
#             print(i)
#     else:
#         pass
# elif request.method == "DELETE":
#     if "RemoveCard" in request.form:
#         pass # hacer algo para quitar carta de news_content
# return render_template(
#     "index.html",
#     news_array = news_content
# )
