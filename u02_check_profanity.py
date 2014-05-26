import urllib

def read_text():
    quotes = open("/Users/stellanova/programming/ud036/movie_quotes.txt")
    contents = quotes.read()
    stringified = str(contents)
    #print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+str(text))
    answer = connection.read()
    #print(answer)
    if "true" in answer:
        print("Profanity Alert!!!")
    elif "false" in answer:
        print("No swear words here!")
    else:
        print("Can't be done! Lo siento, baby!")
    connection.close()

read_text()
