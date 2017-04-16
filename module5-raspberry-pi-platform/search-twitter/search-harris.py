from twython import TwythonStreamer

tCount = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global tCount
        if 'text' in data:
            print (data['text'].encode('utf-8'))
            tCount += 1

        if tCount >= 3:
            print ("Ian G. Harris is popular!")
            self.disconnect()

    def on_error(self, status_code, data):
        print (status_code, data)

# Requires Authentication as of Twitter API v1.1
APP_KEY = 'C9KnhAClYN9Q4mOulZwUmMOSJ'
APP_SECRET = 'gzmfnsRAPAjZvzeB8oJrigmgZEv58R9ZfNqhbpkrGr8KQzcrv4'
OAUTH_TOKEN = '23097932-SrplsgTsw86ipFxpuC3DlFbmlrsAkWnIDa2glvvrU'
OAUTH_TOKEN_SECRET = 'lZG5NeN5J8B66SVSuk6xIFW6tWgYsk7eThLacdCWqZA6r'

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='Ian G. Harris')
