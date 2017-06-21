spy = {
    'name' : 'Rohan',
    'salutation' : 'Dr',
    'age' : 24,
    'rating' : 4.7,
    'is_online' : True
}

STATUS_MESSAGES = ["Available" , "busy", "At Movie", "At Gym"]

friends = [
    {
        'name' : 'Raj' ,
        'salutation' : 'Mr.' ,
        'age' : 39,
        'rating' : 4.9,
        'chats' : []
     },

    {
        'name': 'Rohit',
        'salutation': 'Mr.',
        'age': 24,
        'rating': 4.8,
        'chats': []
    },
    {
        'name': 'Priya',
        'salutation': 'Ms.',
        'age': 34,
        'rating': 4.8,
        'chats': []
    }
]

print "Hello!! Let's get started."
#This will simply print a message "Hello!! Let's get started."

question = "Do you want to continue as " +spy['salutation'] +" " +spy['name'] +".(Y/N)"
existing = raw_input(question)