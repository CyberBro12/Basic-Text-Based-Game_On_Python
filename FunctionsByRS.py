import time

def animate_text(text, delay, end_char='\n'):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end_char, flush=True)


def create(y):
    open(y, "a")

def clear_cmd():
    import os
    os.system('cls')

def getip():
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("Hostname: ", hostname)
    print("IPv4 Address: ", ip_address)

def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        content = ''.join(lines)
        return content

def write_file(file_name, content):
    with open(file_name, "w") as f:
        w = f.write(content)
        return w

def append_file(file_name, content):
    with open(file_name, "a") as f:
        a = f.write(content)
        return a

def count_words(text):
    words = text.split()
    return len(words)

def reverse_text(text):
    rev = text[::-1]
    return rev

def cap_first_letter(text):
    return text.capitalize()
