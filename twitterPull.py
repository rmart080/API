import tweepy
import tkinter
import json
from tkinter import messagebox

access_token = "937081695538483201-1eFDKVZzsuAGUHkWHfkrTIyt1LFVLY3"
access_token_secret = "d9GE6sI8Armj5QfDCwL36KPIH6TxKvSSQx8zfrZD6Afyt"
consumer_key = "GJPM7u5Dk9EwlqOFu5NcJ2jh2"
consumer_secret = "CVahv7fMA1ldUPbpnHNPkGGk1KjCgPLlUh7cgUCnOgI5yhopQv"

def runSearch(userName):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    if not userName:
            messagebox.showinfo("Error", "You left the box blank huh?")
    else:
            userPrep = api.get_user(userName)
           
            
    userTweets = api.user_timeline(userPrep.id)

    for tweets in userTweets:
            print(tweets.text)
    

            






def upDate(inValue):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    if not inValue:
            messagebox.showinfo("Error", "You left the box blank huh?")
    else:
            api.update_status(inValue)

top = tkinter.Tk()
e = tkinter.Entry(top)
e.pack()
button = tkinter.Button(top, text="Search", bg="blue", fg="white", command= lambda: runSearch(e.get()))
buttonTwo = tkinter.Button(top, text="Update Status", command= lambda: upDate(e.get()))
buttonTwo.pack()
button.pack()

if __name__ == '__main__': 
  
    
    top.mainloop()

