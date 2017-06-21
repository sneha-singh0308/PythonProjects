from declaration import*
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#defining function enabling the display of chat history.
def read_old_chat():

    read_conversation = choose_friend()
    for chat in friends[read_conversation]['chats']:
        if chat['sent_by_me']:

            print colored("[%s]:","blue") %(chat['time'].strftime("%d,%B,%Y")), colored("You said", "red")
            print chat['message']

        else:

            #adding multiple colours to out text.
            print colored("[%s]:","blue") %(chat['time'].strftime("%d,%B,%Y")),\
                colored(friends[read_conversation]['name'] +" said","red" )
            print chat['message']

#defining function that would enable the user to send a secret message to other spy.
def send_secret_message():
    send_friend_choice = choose_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("what is the secret text you want to convey?")

    Steganography.encode(original_image, output_path, text)

    #creating new dictionary for the new chat to be appended in the main chat between two spies.
    new_chat = {
        'message' : text,
        'time' : datetime.now(),
        'sent_by_me' : True
    }

    friends[send_friend_choice]['chats'].append(new_chat)
    print "Your message is ready to be saved"

#defining function that helps the user to read secret message sent by another spy.
def read_secret_message():
    read_friend_choice = choose_friend()

    output_path = raw_input("what is the path of the image?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        'message': secret_text,
        'time': datetime.now(),
        'sent_by_me': False
    }

    #appending/adding the new chat to the previous chats done by the user.
    friends[read_friend_choice]['chats'].append(new_chat)
    print "Your message has been saved"

#defining class for choosing a friend from the list of friends.
def choose_friend():
    item_number = 1

    for friend in friends:
        print "%d.%s aged %d of spy rating %.2f is online" %(item_number, friend['name'], friend['age'], friend['rating'])
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends.")
    friend_choice_position = int(friend_choice)-1

    return friend_choice_position

#defining a function enabling the option of adding new friends to the list.
def add_friend():
    new_friend = {
        'name' : "",
        'salutation' : "",
        'age' : 0,
        'rating' : 0.0,
        'chats' : []
    }

    new_friend['name'] = raw_input("Please add your friend's name")
    new_friend['salutation'] = raw_input("Mention their gender(Mr or Ms)?")
    new_friend['name'] = new_friend['salutation'] +"." +new_friend['name']
    new_friend['age'] = int(raw_input("What is your friend's age?"))
    new_friend['rating'] = float(raw_input("What is their rating?"))

    #providing condition that needs to be fulfilled in order to add new friend.
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and  new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print "New Friend has been added!!"

    else:
        print "Sorry!!We cannot add this friend for the chat"

    return len(friends)

#defining another function for adding status message.
def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print "Your status is %s \n " %(current_status_message)

    else:
        print "You don't have any status message currently"

    default = raw_input("Do you want to select from previous?(Y/N)")
    if default.upper() == "N":
        new_status_message = raw_input("What status you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(new_status_message)

    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) +"."  +message
            item_position = item_position + 1

        message_selection = int(raw_input("choose status from above mentioned ones"))
        if len(STATUS_MESSAGES) > message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection-1]

    return updated_status_message

#defining function that would start the chat when called.
def start_chat(spy):

    current_status_message = None
    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:
        print "Authentication done!!Welcome "  + spy['name']  +" of age "  +str(spy['age'])\
               + " of spy rating " + str(spy['rating']) + "."

        #if authentication completes, only then show the menu to the user.
        show_menu = True

        while show_menu:

            menu_choices = "what you want to do? \n 1) Add status update \n 2) Add Friend \n 3) Select a friend " \
                       "\n 4) Send a secret message \n 5) Read a secret message \n 6) Read the chat " \
                       "\n 7) Close Application"

            menu_choice = int(raw_input(menu_choices))

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)

            elif menu_choice == 2:
                number_of_friends = add_friend()
                print "you have %d friends" %(number_of_friends)

            elif menu_choice == 3:
                index = choose_friend()
                print index

            elif menu_choice == 4:
                 send_secret_message()

            elif menu_choice == 5:
                 read_secret_message()

            elif menu_choice == 6:
                 read_old_chat()

            else:
                show_menu = False

    else:
        print "You are not of appropriate age"

#if the user wants to continue as a default user, then immediately calls the start_chat function.
if existing == "Y":

    start_chat(spy)

#if no, then ask the user to fill in his/her credentials in order to start the chat.
else:

    spy = {
        'name' : '',
        'salutation' : '',
        'age' : 0,
        'rating' : 0.0,
        'is_online' : False
    }

    spy['name'] = raw_input("What's your name?")
        #asks the user to specify his/her name. user directly enters the name in console.

    if len(spy['name']) > 0:

        print "Welcome " +spy['name'] +"." +"We're glad to have you here."
            #prints welcome message for the user.

        spy['salutation'] = raw_input("So " +spy['name'] +"," +"How you want to be greeted(Mr or Ms)?")
            #asks the user to specify his/her gender

        #spy['name'] = spy['salutation'] +"." +spy['name']
            #concatenates salutation in front of the spy's name.

        print(spy['name'] +"," +"we wish you have a great time with us.")

        spy['age'] = int(raw_input("What is your age?"))


        spy['rating'] = float(raw_input("What is your spy rating"))

        if spy['rating'] > 4.5:
            print "Great ace!"

        elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
            print "You are one of the good ones."

        elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
            print "You can always do better"

        else:
            print "We can always use somebody to help in the office."

        spy['is_online'] = True

        start_chat(spy)

    else:
        print "Spy needs to have a valid name.TRY AGAIN!!"



