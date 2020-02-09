import nltk

from chatbot.markovchatbot.mmodel.markovmodel import MarkovModel

separator = " "


def build_markov_model(text):
    # print("building mm")
    tokens = nltk.word_tokenize(text)
    print(tokens)

    model = MarkovModel()
    old_token = None
    for token in tokens:
        model.add_node_if_not_present(token.lower())
        model.connect(old_token, token.lower())
        old_token = token

    return model


def get_totally_random_walk(model: MarkovModel):
    start_node = model.get_start_node()
    return_string = ""
    end_node_found = False
    node = start_node
    while not end_node_found:
        connection = node.get_strongest_connection()
        if connection is None:
            break
        destination_node = connection.destination_node
        return_string += separator + destination_node.word
        print(destination_node)
        node = destination_node

    return return_string.lstrip()


def get_walk(self, last_word, total_string=""):
    print("walking")
    total_string = total_string + last_word

    if len(total_string) > 5:
        return total_string

    return self.get_walk(self.get_next_word(last_word), total_string)


def get_next_word(self, word):
    print("get_next_word for word " + str(word))
