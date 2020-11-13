import unittest
import requests
from app import *
from news import News

class testMethods(unittest.TestCase): 
    # Environment Variables
    global newNewsObject
    newNewsObject = News()
    json_v = {
    "source":{"id":"breitbart-news","name":"Breitbart News"},
    "author":"Kyle Olson",
    "title":"Pelosi Undermines Claim Trump Lawsuits Will Hamper Biden 'Transition'",
    "description":"House Speaker Nancy Pelosi seemed to undermine on Thursday a claim that legal challenges will hamper a Joe Biden \"transition.\" | Politics",
    "url":"http://www.breitbart.com/politics/2020/11/12/nancy-pelosi-undermines-claim-donald-trump-lawsuits-will-hamper-joe-biden-transition/",
    "urlToImage":"https://media.breitbart.com/media/2020/11/Nancy-Pelosi-Joe-Biden-Hand-in-Hand-640x335.jpg",
    "publishedAt":"2020-11-12T23:01:49Z"
    }
    newNewsObject.assign_attributes(json_v)


    # Object Methods
    def test1(self): # author
        self.assertEqual(newNewsObject.author, "Kyle Olson")
    
    def test2(self): # title
        self.assertEqual(newNewsObject.title, "Pelosi Undermines Claim Trump Lawsuits Will Hamper Biden 'Transition'")

    def test3(self): # description
        self.assertEqual(newNewsObject.description, "House Speaker Nancy Pelosi seemed to undermine on Thursday a claim that legal challenges will hamper a Joe Biden \"transition.\" | Politics")
    
    def test4(self): # url
        self.assertEqual(newNewsObject.url, "http://www.breitbart.com/politics/2020/11/12/nancy-pelosi-undermines-claim-donald-trump-lawsuits-will-hamper-joe-biden-transition/")
    
    def test5(self): # urlToImage
        self.assertEqual(newNewsObject.url_to_image, "https://media.breitbart.com/media/2020/11/Nancy-Pelosi-Joe-Biden-Hand-in-Hand-640x335.jpg")
    
    def test6(self): # publishedAt
        self.assertEqual(newNewsObject.date_time_of_publishing, "2020-11-12T23:01:49Z")

    # App Methods
    def test7(self): # printMDB
        self.assertEqual(printMDB(), "Successful")
    
    def test8(self): # delMDB_Collections
        self.assertEqual(delMDB_Collections(), "Successful")

    def test9(self): # createCols
        testTopics = ["test1", "test2"]
        self.assertEqual(createCols(testTopics), "Successful")

    def test10(self): # getRequests, assertTrue ya que retorna un nested array
        testGetRequests = ["test"]
        global requests
        requests = getRequests(testGetRequests)
        self.assertTrue(requests)
    
    def test11(self): # addRequests, assertTrue ya que retorna un nested array
        global listRequests 
        listRequests = addRequests(requests)
        self.assertTrue(listRequests)
    
    def test12(self): # postDB
        self.assertEqual(postDB(listRequests), "Successful")
    
    def test13(self): # getDB
        self.assertTrue(getDB())
    
    def test14(self): # getTopics
        global topic_list
        topic_list = getTopics()
        self.assertTrue(topic_list)

    def test15(self): # delDB
        self.assertEqual(delDB("test"), "Successful")

    def test16(self): # delTfromList
        self.assertEqual(delTfromList(topic_list, "test"), "Successful")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
