from requests import get
from bs4 import BeautifulSoup
from json import loads, dump

class news:
    """This class is dedicated to storing the values of selected news from the API link response in dict format. """
    def __init__(self):
        self.author                     :str        = None
        self.title                      :str        = None
        self.description                :str        = None
        self.url                        :str        = None
        self.url_to_image               :str        = None
        self.date_time_of_publishing    :str        = None
        self.id                         :str        = None
        self.name                       :str        = None
    
    # setters and getters.
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    
    def get_url(self): return self.url
    def set_url(self, url): self.url = url
    
    def get_url_to_image(self): return self.url_to_image
    def set_url_to_image(self, url_to_image): self.url_to_image = url_to_image
    
    def get_date_time_of_publishing(self): return self.date_time_of_publishing
    def set_date_time_of_publishing(self, date_time_of_publishing): self.date_time_of_publishing = date_time_of_publishing

    def get_id(self, id): return self.id
    def set_id(self, id): self.id = id

    def get_name(self, name): return self.name
    def set_name(self, name): self.name = name

    def assign_attributes(self,i:dict):
        try:
            self.set_id(i["source"]["id"])
        except: 
            pass
        try:
            self.set_name(i["source"]["name"])
        except: 
            pass
        try:
            self.set_author(i["author"])
        except: 
            pass
        try:
            self.set_title(i["title"])
        except: 
            pass
        try:
            self.set_description(i["description"])
        except: 
            pass
        try:
            self.set_url(i["url"])
        except: 
            pass
        try:
            self.set_url_to_image(i["urlToImage"])
        except: 
            pass
        try:
            self.set_date_time_of_publishing(i["publishedAt"])
        except: 
            pass

    def __str__(self):
        return f"author: {self.author}, title: {self.title} \n" + "-"*60



    

