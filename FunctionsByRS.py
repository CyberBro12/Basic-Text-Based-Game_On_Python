import time
import os
import socket

def animate_text(text, delay=0.05, end_char='\n'):
    """Prints text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end_char, flush=True)

def create(file_path):
    """Creates an empty file if it doesn't exist."""
    with open(file_path, "a"):
        pass

def clear_cmd():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip():
    """Prints the hostname and IPv4 address of the machine."""
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = 'Unavailable'
    print(f"Hostname: {hostname}")
    print(f"IPv4 Address: {ip_address}")

def read_file(file_path):
    """Reads and returns the entire content of a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def write_file(file_path, content):
    """Writes content to a file, overwriting existing content."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def append_file(file_path, content):
    """Appends content to a file."""
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False

def count_words(text):
    """Counts the number of words in a string."""
    return len(text.split())

def reverse_text(text):
    """Returns the reversed version of the input text."""
    return text[::-1]

def cap_first_letter(text):
    """Capitalizes the first letter of the input text."""
    return text[:1].upper() + text[1:] if text else text
