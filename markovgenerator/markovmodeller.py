import nltk

from chatbot.markovgenerator.mmodel.markovmodel import MarkovModel

separator = " "


def build_markov_model_from_list_of_sentences(listlist):
    model = MarkovModel()
    for sentence in listlist:
        old_token = None
        for token in sentence:
            token = token.lower()
            model.add_node_if_not_present(token)
            model.connect(old_token, token)
            old_token = token

    return model


def build_markov_model_from_string(text):
    sentences = nltk.sent_tokenize(text)
    model = MarkovModel()

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)

        old_token = None
        for token in tokens:
            token = token.lower()
            model.add_node_if_not_present(token)
            model.connect(old_token, token)
            old_token = token

    return model


def get_max_walk(model: MarkovModel):
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
        # print(destination_node)
        node = destination_node

    return return_string.lstrip()


def get_walk(model: MarkovModel):
    start_node = model.get_start_node()
    return_string = ""
    end_node_found = False
    node = start_node
    while not end_node_found:
        connection = node.get_connection_next_connection_weighted()
        # connection = node.get_strongest_connection()
        if connection is None:
            break
        destination_node = connection.destination_node
        return_string += separator + destination_node.word
        # print(destination_node)
        node = destination_node

    return return_string.lstrip()


def get_next_word(self, word):
    print("get_next_word for word " + str(word))
