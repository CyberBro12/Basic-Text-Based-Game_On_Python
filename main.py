from dank import Dank
import time
import sqlite3
from FunctionsByRS import Func
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()
run = True
versionoffile = 0.3
#database
c.execute("""CREATE TABLE IF NOT EXISTS dank (
          name text,
          money integer,
          moneyinbank integer
)""")
conn.commit()

def update():
    import requests
    import hashlib
    from threading import Thread

    def calculate_file_hash(filename):
        with open(filename, "rb") as f:
            # Read the contents of the file in binary mode
            file_contents = f.read()
            # Calculate the MD5 hash of the file contents
            file_hash = hashlib.md5(file_contents).hexdigest()
            return file_hash
    
    def download_file(url, filename, expected_hash):
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Calculate the hash of the file content
            file_content = response.content
            actual_hash = hashlib.md5(file_content).hexdigest()

            # Verify the hash
            if actual_hash == expected_hash:
                print("File is up-to-date")
            else:
                with open(filename, 'wb') as f:
                    f.write(file_content)
                print(f"File Updated! successfully")
                print("Pls Restart the program to take effect!")
        else:
            print("Failed to Update file")

    def download_thread(url, filename, expected_hash):
        thread = Thread(target=download_file, args=(url, filename, expected_hash))
        thread.start()

    def main():
        f1 = calculate_file_hash("main.py")
        f2 = calculate_file_hash("dank.py")
        # List of files to download with their URLs and expected hashes
        files = [
            ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/main/main.py", "main.py", f1),
            ("https://raw.githubusercontent.com/CyberBro12/Dank_In_Python/blob/main/dank.py", "dank.py", f2)
        ]

        # Start a thread for each file download
        for url, filename, expected_hash in files:
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
st =  input("> ")
print("")

if st == "1":
    name = input("enter your name: ")
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
    print("type help for more information\nOr Exit to exit the game\n")
    while run:
        cd = input(f"{name}> ").lower()
        if cd == "help":
                print(f"Current Commands: ", end="")
                print(Dank.Availablecommands(Dank))
        elif cd == "exit":
            exit()
        elif cd == "/bal":
            Dank().bal(name)
        elif cd == "/dig":
            Dank().dig(name)
        elif cd == "/beg":
            Dank().beg(name)
elif st == "2":
    name = input("enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        while run:
            cd = input(f"{name}> ").lower()
            if cd == "help":
                print(f"Current Commands: ", end="")
                print(Dank.Availablecommands(Dank))
            elif cd == "exit":
                exit()
            elif cd == "/bal":
                Dank().bal(name)
            elif cd == "/dig":
                Dank().dig(name)
            elif cd == "/beg":
                Dank().beg(name)
            elif cd == "/update":
                update()
    else:
        print("name not found")
elif st == "3":
    print("This game is still in progress")
    time.sleep(1)
    print("So pls Expect bugs or errors")
    time.sleep(1)
    print("If you ever found errors or bug send me picture of it so i can fix it in the next version")
    time.sleep(1)
    print(f"Version-{versionoffile}")
    time.sleep(10)
elif st == "4":
    print("        Update Logs")
    print("     1.Added new command '/update'\n     2.Added Update Logs Feature")
elif st == "5":
    exit()
else:
    print("Are you stupid or something?\n")
