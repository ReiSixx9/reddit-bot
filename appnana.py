import praw
import time

def run():
    #Create Bot with login and private key - username - password
    bot = praw.Reddit(user_agent='AppNana Post Scheduler Bot v0.1', client_id='xyNB7BJhkza4hQ', client_secret='fNGdPVgk-WaPUqJvMEEKkauH8YY',
        username='ReiSixx9', password='7893123abc')
    sub_list = ['AppNana', 'AppNanas', 'Appnana_4_everybody']
    while 1:
        for sub in sub_list:
            title = "d25367499"
            message = ''
            bot.subreddit(sub).submit(title, message)                   #Code for submitting new post on Reddit
            time.sleep(600)
        time.sleep(60*100)                                        #Sleep for 2 hours

if __name__ == '__main__':
    run()