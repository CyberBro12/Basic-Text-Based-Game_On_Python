import time
import sqlite3
import requests
import hashlib
from dank import Dank, Crimegenerator

DB_PATH = "dankdata.db"
VERSION = 0.5
FILES_TO_UPDATE = [
    ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/main.py", "main.py"),
    ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/dank.py", "dank.py"),
    ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/FunctionsByRS.py", "FunctionsByRS.py")
]

COOLDOWNS = {
    "/bal": 10,
    "/dig": 20,
    "/beg": 15,
    "/crime": 30,
    "/highlow": 20
}

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS dank (
            name TEXT PRIMARY KEY,
            money INTEGER,
            moneyinbank INTEGER
        )""")
        conn.commit()

def get_names():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM dank")
        return [row[0] for row in c.fetchall()]

def add_user(name):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO dank VALUES (?, ?, ?)", (name, 0, 0))
        conn.commit()

def calculate_file_hash(filename):
    try:
        with open(filename, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        return None

def update_files():
    for url, filename in FILES_TO_UPDATE:
        expected_hash = calculate_file_hash(filename)
        response = requests.get(url)
        if response.status_code == 200:
            actual_hash = hashlib.md5(response.content).hexdigest()
            if actual_hash != expected_hash:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"{filename} updated. Please restart the program.")
            else:
                print(f"{filename} is up-to-date.")
        else:
            print(f"Failed to update {filename}.")

def game_loop(name):
    last_command_usage = {}
    print(f"Hello, {name}\nType 'help' for more information\nOr 'exit' to exit the game\n")
    while True:
        cmd = input(f"{name}> ").lower().strip()
        current_time = time.time()
        if cmd == "help":
            print("Current Commands:", Dank.Availablecommands(Dank))
        elif cmd == "exit":
            print("Goodbye!")
            break
        elif cmd in COOLDOWNS:
            cooldown = COOLDOWNS[cmd]
            last_used = last_command_usage.get(cmd, 0)
            if current_time - last_used >= cooldown:
                if cmd == "/bal":
                    Dank().bal(name)
                elif cmd == "/dig":
                    Dank().dig(name)
                elif cmd == "/beg":
                    Dank().beg(name)
                elif cmd == "/crime":
                    Crimegenerator().crime(username=name)
                elif cmd == "/highlow":
                    Dank().highlow(username=name)
                last_command_usage[cmd] = current_time
            else:
                print(f"Command is on cooldown. Please wait {int(cooldown - (current_time - last_used))} seconds.")
        elif cmd == "/update":
            update_files()
        else:
            print("Command not found!")

def main():
    init_db()
    print("Welcome to the meme game >:)")
    print("Playing for the first time?")
    print("1.New Game\n2.Continue\n3.About the game\n4.Update Logs\n5.Exit\n")
    choice = input("> ").strip()
    print("")

    if choice == "1":
        name = input("Enter your name: ").strip()
        names = get_names()
        if name in names:
            print("This user already exists! Continuing with the game.")
        else:
            add_user(name)
        game_loop(name)
    elif choice == "2":
        name = input("Enter your name: ").strip()
        if name in get_names():
            game_loop(name)
        else:
            print("Name not found.")
    elif choice == "3":
        print("This game is still in progress\nExpect bugs or errors.\nSend bug reports for fixes.\nVersion-", VERSION)
        time.sleep(2)
    elif choice == "4":
        print("Update Logs\n*Updates*\n1.No new commands in this version\n2.Fixed a lot of Bugs\nVersion-", VERSION)
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid selection. Please enter a valid option.")

if __name__ == "__main__":
    main()
