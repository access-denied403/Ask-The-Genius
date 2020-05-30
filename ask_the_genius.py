import argparse
import wikipedia
from win10toast import ToastNotifier

def ask_genius(question):
    answer = wikipedia.summary(question).split(".")[0]
    toast = ToastNotifier()
    toast.show_toast("The Genius:", answer, duration=50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("question", 
            help="What do you want to ask the genius?")
    args = parser.parse_args()
    ask_genius(args.question)

