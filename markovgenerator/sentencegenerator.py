from nltk.corpus import gutenberg
from nltk.text import Text

from chatbot.markovgenerator import markovmodeller

if __name__ == "__main__":
    my_essay = True
    if my_essay:
        txt = ""
        with open('res/ans.txt') as text:
            for line in text:
                txt += line

        model = markovmodeller.build_markov_model_from_string(txt)

    else:
        list_sentences = Text(gutenberg.sents('austen-sense.txt'))
        model = markovmodeller.build_markov_model_from_list_of_sentences(list_sentences)

    while (True):
        walk_string = markovmodeller.get_walk(model)
        print(walk_string)
        x = input("--- type X to stop")
        if x == "X":
            break
