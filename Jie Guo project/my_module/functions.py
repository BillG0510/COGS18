"""A collection of function for doing my project."""
import random
import string
#get guess range
def generate_range(low, high):
    assert low <= high, 'range does not exit'
    return random.randint(low, high)

#start game function
def start_game():
    print('The Guess Game begin ! (๑‵●‿●‵๑)')
    # Get a Low Range Input from the user
    low_str = input('Low Range Input :\t')
    # Get a High Range Input from the user
    high_str = input('High Range Input :\t')
    low_num = int(low_str)
    high_num = int(high_str)
    target = generate_range(low_num, high_num)
    input_str = input('Your guess :\t')
    # Quit game
    if input_str == "Quit_Game":
        print("Game Over, see you next time!")
        return
    outcome = int(input_str)
    # Count number of attempts
    count = 1;
    while outcome != target:
        count += 1
        if outcome < target:
            print("Answer shall be bigger")
        else:
            print("Answer shall be smaller")
        input_str = input('Your guess :\t')
        if input_str == "Quit_Game":
            print("Game Over, see you next time!")
            return
        outcome = int(input_str)
    print('Great! The answer is: ', outcome)
    print('Number of attempts: ', count)
    print("Game Over, see you next time!")

# Calculate string expresssion
def calculate():
    s = input('Calculate Expression:\t')
    print('The answer is: ', helper(s))
# help to calculate string expresssion
def helper(s):
    num, stack, sign = 0, [], "+"
    s += ' '
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == '(':
            num, skip = helper(s[i+1:])
            i += skip
        elif s[i] in '+-*/)' or i == len(s)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))

            if s[i] == ')':
                return sum(stack), i + 1
            num = 0
            sign = s[i]
        i += 1
    return sum(stack)

## Functions below are mainly got from homework 3
## but some of the functions are modified

# Check if the input is a question
def is_question(input_string):
    if '?' in input_string:
        return True
    else:
        return False
# get rid of all punctuation
def remove_punctuation(input_string):
    out_string = ''
    for x in input_string:
        if x not in string.punctuation:
            out_string += x
    return out_string
#  prepare the text inputs for processing.
def prepare_text(input_string):
    temp_string = input_string.lower();
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split(" ")
    return out_list
# return a string that has been repeated a specified number of times, with a given separator
def respond_echo(input_string, number_of_echoes, spacer):
    if input_string is not None:
        echo_temp = input_string+spacer
        echo_output = echo_temp*number_of_echoes
    else:
        echo_output = None
    return echo_output
# select an output for the chatbot, based on the input it got
def selector(input_list, check_list, return_list):
    output = None
    for x in input_list:
        if x in check_list:
            output = random.choice(return_list)
            break
    return output
# concatenate two strings, combining them with a specified separator.
def string_concatenator(string1, string2, separator):
    if string1 == None or string2 == None or separator == None:
        output = None
    else:
        output = string1 + separator + string2
    return output
def list_to_string(input_list, separator):
    output  = input_list[0]
    for i in range(1, len(input_list)):
        output = string_concatenator(output, input_list[i], separator)
    return output
def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None
def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False
# end the chat
def end_chat(input_list):
    if 'quit' in input_list:
        return True
    else:
        return False

# start chat
def have_a_chat():
    """Main function to run our chatbot."""
    GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
    GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

    COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
    COMP_OUT = ["Python is what I'm made of.", \
                "Did you know I'm made of code!?", \
                "Computers are so magical", \
                "Do you think I'll pass the Turing test?"]

    PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
    PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
    PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

    JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
    JOKES_OUT = ['ha', 'haha', 'lol'] 

    NONO_IN = ['matlab', 'java', 'C++']
    NONO_OUT = ["I'm sorry, I don't want to talk about"]

    UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']

    GUESS = ['guess']
    CALCULATE = ['calculate']

    QUESTION = "I'm too shy to answer questions. What do you want to talk about?"
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)

        # Start the guess game
        if(is_in_list(msg, GUESS)):
            print('Let\'s start guess game')
            start_game()
        # Start the calculator
        if(is_in_list(msg, CALCULATE)):
            print('Let me help you to calculate ヽ(^o^)ノ❀ヅ❤♫')
            calculate()
       
