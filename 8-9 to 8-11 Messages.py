my_msg_list = ["Hi, How are you?", "Good Day ! It's nice to see you.", "Hey there! Welcome back."]
my_sent_msg_list = []

# Only for Exercise 8-9 -->
'''
def show_msg(msg_list):
    for msg in msg_list:
        print(msg)

show_msg(my_msg_list)
'''

def send_msg(msg_list, sent_msg_list):
    """Sends messages to the people in list and prints out once done. """

    if  my_msg_list != sent_msg_list:
        for msg in msg_list:
            msg_list[:].pop()
            print(f" Sending Message: {msg}:")
            sent_msg_list.append(msg)
        print(f"\nOriginal Message List: {msg_list}")
        print(f"Sent Message List: {sent_msg_list}")


send_msg(my_msg_list, my_sent_msg_list)

