from chatbot.chatbot import ChatBot

quitTerms = ["quit", "q", "exit", "finish"]

def main():

    lets_chat = True

    # name = input("Hi! Please select a name for the chatbot\n")
    name = "Paul"

    youPrompt = "YOU: "
    botPrompt = str( name) + ": "

    chatbot = ChatBot(name)

    print("you are now chatting with " + chatbot.name)
    # firstInput = input("you are now chatting with " + chatbot.name + ", why don't you say something?\n" + youPrompt)
    #
    # chatbot.receive(firstInput)
    # print(chatbot.respond())

    while(lets_chat):
        usrInput = input(youPrompt)

        if usrInput.lower() in quitTerms:
            break

        chatbot.receive(usrInput)

        print(botPrompt + chatbot.respond())

    print("Thanks for a nice chat, see you soon!")

if __name__ == "__main__":
    main()