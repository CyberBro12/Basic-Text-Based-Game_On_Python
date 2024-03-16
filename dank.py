from dank import Dank, Crimegenerator
import time
import sqlite3
from threading import Thread
import requests
import hashlib

conn = sqlite3.connect("dankdata.db")
c = conn.cursor()
run = True
versionoffile = 0.4

# Create table if not exists
c.execute("""CREATE TABLE IF NOT EXISTS dank (
          name text,
          money integer,
          moneyinbank integer
)""")
conn.commit()

# Function to update files from GitHub
def update():
    def calculate_file_hash(filename):
        with open(filename, "rb") as f:
            file_contents = f.read()
            file_hash = hashlib.md5(file_contents).hexdigest()
            return file_hash

    def download_file(url, filename, expected_hash):
        response = requests.get(url)
        if response.status_code == 200:
            file_content = response.content
            actual_hash = hashlib.md5(file_content).hexdigest()
            if actual_hash == expected_hash:
                print("File is up-to-date")
            else:
                with open(filename, 'wb') as f:
                    f.write(file_content)
                print("File updated successfully")
                print("Please restart the program to take effect!")
        else:
            print("Failed to update file")

    def download_thread(url, filename, expected_hash):
        thread = Thread(target=download_file, args=(url, filename, expected_hash))
        thread.start()

    def main():
        files = [
            ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/main.py", "main.py"),
            ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/dank.py", "dank.py"), 
            ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/FunctionsByRS.py", "FunctionsByRS.py")
        ]

        for url, filename in files:
            expected_hash = calculate_file_hash(filename)
            download_thread(url, filename, expected_hash)

    if __name__ == "__main__":
        main()

print("Welcome to the meme game >:)")
print("Playing for the first time?")
print("1.New Game")
print("2.Continue")
print("3.About the game")
print("4.Update Logs")
print("5.Exit")
print("")

st = input("> ")
print("")

cooldowns = {
    "/bal": 10,   # Cooldown time for /bal command in seconds
    "/dig": 20,   # Cooldown time for /dig command in seconds
    "/beg": 15,   # Cooldown time for /beg command in seconds
    "/crime": 30,  # Cooldown time for /crime command in seconds
    "/highlow": 20
}

last_command_usage = {}  # Dictionary to store the last time each command was used

if st == "1":
    name = input("Enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        print("This user already exists! Continuing with the game.")
    else:
        pass
    starter = [name, 0, 0]
    time.sleep(1)
    c.execute(f"INSERT INTO dank VALUES (?, ?, ?)", starter)
    conn.commit()
    print(f"Hello, {name}\n")
    print("Type 'help' for more information\nOr 'exit' to exit the game\n")
    
    while run:
        cd = input(f"{name}> ").lower()
        current_time = time.time()
        
        if cd == "help":
            print(f"Current Commands: ", end="")
            print(Dank.Availablecommands(Dank))
        elif cd == "exit":
            exit()
        elif cd in cooldowns:
            if cd not in last_command_usage or current_time - last_command_usage[cd] >= cooldowns[cd]:
                if cd == "/bal":
                    Dank().bal(name)
                elif cd == "/dig":
                    Dank().dig(name)
                elif cd == "/beg":
                    Dank().beg(name)
                elif cd == "/crime":
                    user = Crimegenerator()
                    user.crime(username=name)
                elif cd == "/highlow":
                    Dank().highlow(username=name)
                last_command_usage[cd] = current_time  # Update last command usage time
            else:
                print(f"Command is on cooldown. Please wait {cd}Seconds before using it again.")
        elif cd == "/update":
            update()
        else:
            print("Command not found!")

elif st == "2":
    name = input("Enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        while run:
            cd = input(f"{name}> ").lower()
            current_time = time.time()
            
            if cd == "help":
                print(f"Current Commands: ", end="")
                print(Dank.Availablecommands(Dank))
            elif cd == "exit":
                exit()
            elif cd in cooldowns:
                if cd not in last_command_usage or current_time - last_command_usage[cd] >= cooldowns[cd]:
                    if cd == "/bal":
                        Dank().bal(name)
                    elif cd == "/dig":
                        Dank().dig(name)
                    elif cd == "/beg":
                        Dank().beg(name)
                    elif cd == "/crime":
                        user = Crimegenerator()
                        user.crime(username=name)
                    elif cd == "/highlow":
                        user = Dank()
                        user.highlow(username=name)
                    last_command_usage[cd] = current_time  # Update last command usage time
                else:
                    print("Command is on cooldown. Please wait before using it again.")
            elif cd == "/update":
                update()
            else:
                print("Command not found!")
    else:
        print("Name not found")

elif st == "3":
    print("This game is still in progress")
    time.sleep(1)
    print("So please expect bugs or errors")
    time.sleep(1)
    print("If you ever found errors or bugs, send me a picture of it so I can fix it in the next version")
    time.sleep(1)
    print(f"Version-{versionoffile}")
    time.sleep(10)

elif st == "4":
    print("        Update Logs")
    print("      *Updates*\n")
    print(f"     1. Added new command < /highlow >\n\n\n  Version-{versionoffile}")

elif st == "5":
    exit()

else:
    print("Are you stupid or something?\n")
