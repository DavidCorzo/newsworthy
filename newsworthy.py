from flask import Flask, render_template, request
import requests
import sys
import json
from card import *

app = Flask(__name__)

# def getRequests(some array []):
#    news_request = "https://idk_which_news_website.com"
#    try:
#        news_content = requests.get(news_request).text
#    except:
#        print(f"unable to get {news_request}")
#        sys.exit(1)
#    news_cards = json.loads(news_content)
#    return news_cards

news_content = []

@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
def View():
    # cards.append(1)
    # cards.append(2)

    if request.method == "POST":
        if "AddFilters" in request.form:
            topics = request.form["exampleInputEmail1"]
            # content = getRequests(topics)
            # news_content.copy(content) # metodo copiar content a news_content no me recuerdo como era.
            
            for i in news_content:
                print(i)
        else:
            pass
    return render_template(
        "index.html",
        news_array = news_content
    )

if __name__ == "__main__":
    debug = True
    app.run(debug=debug)
