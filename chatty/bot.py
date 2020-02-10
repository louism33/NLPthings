

class ChatBot:
    def __init__(self, name):
        self.name = name

    def receive(self, string):
        print("received: " + str(string))

    def respond(self):
        return "this is my response: hi."

    def markov_walk(self, first_word="hello"):
        walk = self.get_walk(first_word)
        return "this is my walk:\n"

    def get_walk(self, last_word, total_string =""):
        print("walking")
        total_string = total_string + last_word

        if len(total_string) > 5:
            return total_string

        return self.get_walk(self.get_next_word(last_word), total_string)


    def get_next_word(self, word):
        print("get_next_word for word " + str(word))


