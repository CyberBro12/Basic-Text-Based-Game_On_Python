import sqlite3
import time
import random
from FunctionsByRS import animate_text

# Database setup
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()

class Crimegenerator:
    def __init__(self):
        self.values = {
            "xyz": random.randint(1, 5000),
            "abc": random.randint(1, 500),
            "yza": random.randint(1, 50000),
            "zab": random.randint(1, 15000)
        }
        self.fake_crimes_to_commit = {
            "Hacking": [f"You hacked into Dank Memer and gave yourself {self.values['xyz']}\u20b9. Evil!", 
                        "You hacked into your own router and found out the ISP does not actually care about you.", 
                        'You got caught hacking into Dank Memer and Badosz "Thanos Snapped" you'],
            "Bank_robbing": [f"You robbed a bank irl and found {self.values['yza']}\u20b9. Cute!", 
                             "You tried to rob a bank but got scared, lol", 
                             "You robbed a bank and the little old lady was packing heat, you did NOT make it out"],
            "Trespassing": [f"You walked straight into someone else's yard and found {self.values['zab']}\u20b9. Free real estate!", 
                            "You got confused about what trespassing was and walked into your own back yard.", 
                            "You tried trespassing onto the property of someone with a gun f*tish and it did NOT go well"],
            "Shoplifting": [f"You managed to steal {self.values['xyz']}\u20b9. Money Heist!", 
                            "You tried to steal something, but the shop was closed!", 
                            "You stole an unknown drink and drank it. It turned out to be poison and you died. RIP"],
            "cyber_bullying": [f"You bullied a kid and he sent you {self.values['abc']}\u20b9 to stop! I hope that kid grows up richer than you.", 
                               "You tried to bully a kid, but quickly got banned by mods. LOL, seeya idiot.", 
                               "You laughed at a kid so much, you choked to death. Who is laughing now? Imagine being a bully."],
            "Murder": [f"You murdered a random stranger in a dark alley. There was {self.values['xyz']}\u20b9 in his wallet! Was it worth it?", 
                       "You tried to murder a random stranger, but he got away! You can't even murder properly.",
                       "You were holding the gun upside down and killed yourself! Imagine being this stupid!"],
            "Piracy": [f'You ripped off your favorite movies and also found {self.values["abc"]}\u20b9',
                       "You tried to pirate an adult film and got distracted on the free websites instead", 
                       'The FBI found out about that copy of your Air Bud DVD you made and "took you out"'],
            "Treason": [f"You successfully overthrew the government with your treason and in the halls of congress found {self.values['abc']}\u20b9.", 
                        "You failed to host an insurrection, everyone is laughing at you.", 
                        "You were caught and the punishment for treason is death."],
            "Vandalism": [f'You wrote "Dank Memer" on a wall and the developers sent you {self.values["xyz"]}\u20b9. Nice!', 
                          "You tried to write something on a wall, but ran out of spray. LOL", 
                          "While writing on the wall you fell from the 10th floor and died."]
        }
        self.chances = [10, 50, 40]

    def commit_crime(self, crime, name):
        d = self.fake_crimes_to_commit[crime]
        result = random.choices(d, self.chances, k=1)[0]
        print(result)
        if result == d[0]:
            # Success, add money
            money_key = next((k for k in self.values if str(self.values[k]) in result), "xyz")
            money = self.values[money_key]
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
        elif result == d[2]:
            # Death, lose money
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            with conn:
                c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (100000, name))

    def crime(self, username):
        crimes = list(self.fake_crimes_to_commit.keys())
        random3crime = random.sample(crimes, k=3)
        print("Dank> Which Crime you want to commit?")
        for i, crime in enumerate(random3crime, 1):
            print(f"{i}. {crime}")
        try:
            choice = int(input(f"{username}> "))
            if 1 <= choice <= 3:
                self.commit_crime(random3crime[choice - 1], username)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

class Dank:
    @staticmethod
    def question():
        return {
            "question1": {"question": "Who is prime minister of India currently in 2024?", "answer": "narendra modi"},
            "question2": {"question": "What is 2 + 2 - 3 * 4 + 232 + 24 * 3 - 2432 - 32 + 4 - 32 = ?", "answer": "-2196"},
            "question3": {"question": "What is the value of π (pi) to two decimal places?", "answer": "3.14"},
            "question4": {"question": "Who is often credited with the discovery of the Pythagorean theorem?", "answer": "pythagoras"},
            "question5": {"question": "What is the capital of Australia?", "answer": "canberra"},
            "question6": {"question": "In which year did the Apollo 11 mission successfully land humans on the moon?", "answer": "1969"},
            "question7": {"question": "How many sides does a heptagon have?", "answer": "7"},
            "question8": {"question": "Who wrote famous play 'Romeo and Juliet'?", "answer": "william shakespeare"},
            "question9": {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            "question10": {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
            "question11": {"question": "What is the square root of 144?", "answer": "12"},
            "question12": {"question": "Who painted the famous artwork 'Starry Night'?", "answer": "vincent van gogh"}
        }

    @staticmethod
    def askQuestionandgiveanswer():
        q = Dank.question()
        return random.choice(list(q.values()))

    def Availablecommands(self):
        return "< /dig >, < /beg >, < /crime >, </highlow> < /update >, < /bal >, more coming soon!"

    def bal(self, name):
        c.execute("SELECT money, moneyinbank FROM dank WHERE name=?", (name,))
        result = c.fetchone()
        if result:
            print(f"User: {name}")
            print(f"Balance: {result[0]}\u20b9")
            print(f"Bank Balance: {result[1]}\u20b9")
        else:
            print(f"User {name} not found.")

    def dig(self, name):
        chanc = random.randint(1, 10)
        if chanc == 1:
            soldgold = random.randint(1, 10000)
            print(f"You strike gold, {name}! You got some gold and sold it for {soldgold}\u20b9.")
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (soldgold, name))
        elif chanc == 2:
            print("You dug down and found nothing! lololololol!")
        elif chanc == 3:
            worth = random.randint(1, 100)
            print(f"You dug down and found some coins worth {worth}\u20b9")
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (worth, name))
        elif chanc == 4:
            print("You dug down and found buried dog poop XD")
        elif chanc == 5:
            piggybankmoney = random.randint(1, 150)
            print(f"You Digged down and found kid's piggybank, you found {piggybankmoney}\u20b9 ")
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (piggybankmoney, name))
        elif chanc == 6:
            print("You Digged down and Fell into lava pool")
            time.sleep(2)
            deathmessage = f"{name} tries to swim in lava."
            for i in deathmessage:
                print(i, end="")
                time.sleep(0.2)
            print(":|\n")
        elif chanc == 7:
            notez = random.randint(0, 50)
            if notez >= 3:
                l = random.randint(6083, 56951)
                print(f"You found a single gold coin worth {l}\u20b9 ")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (l, name))
            else:
                oo = random.randint(80000, 10000000)
                print(f"You Digged down and found a diamond worth {oo}")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (oo, name))
        elif chanc == 8:
            print("You Digged down and found a diamond but then creeper came and blowed you up!\n")
        elif chanc == 9:
            print("you digged and found cockroaches!!!!!!!\n")
        elif chanc == 10:
            print(f"Unfortunate turn of events! {name}, your digging attracts unwanted attention from bandits, who demand a share of your findings. Better luck next time.\n")

    def beg(self, name):
        chance = random.randint(1, 5)
        if chance == 1:
            lm = random.randint(1, 150)
            print(f"Dank> Ohh you poor~~ soul! here take some {lm}\u20b9")
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lm, name))
        elif chance == 2:
            lesgo = random.randint(1, 50)
            print("Dank> ", end="")
            animate_text(text="Bruh! i don't have cash", delay=0.1)
            time.sleep(1)
            print(f"{name}> ", end="")
            animate_text(text="Here's my PayPal qr code scan and give online :D", delay=0.1)
            print("Dank> ", end="")
            animate_text(text=f"Are You Serious Right now Bruh?, nvm here's {lesgo}\u20b9", delay=0.1)
            with conn:
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lesgo, name))
        elif chance == 3:
            print("Dank> ", end="")
            animate_text(text="Why?", delay=0.1)
            time.sleep(1)
            print(f"{name}> ", end="")
            animate_text(text="Because i am poor?", delay=0.1)
            time.sleep(2.5)
            print("Dank> ", end="")
            animate_text(text="Then give me money i am poor", delay=0.1)
            time.sleep(2.5)
            print(f"{name}> ", end="")
            animate_text(text=":|, Nvm..", delay=0.1)
        elif chance == 4:
            ht = ("Head", "Tails")
            dk = random.choice(ht)
            print("Dank> ", end="")
            animate_text(text="Imma flip coin if it's a head you will give me money\n if it's a tail then i will take money", delay=0.1)
            time.sleep(3.5)
            animate_text("Coin Flips!!!!", 0.1)
            time.sleep(0.5)
            d = 150
            if dk == "Head":
                animate_text("Head", 0.1)
                print("Dank> ", end="")
                animate_text("It's a head i won money!!", 0.1)
                time.sleep(2.5)
                print(f"{name}> ", end="")
                animate_text("Wait wai wait!!!!!!!!!, again pls :-c", 0.1)
                time.sleep(2.5)
                print("Dank> ", end="")
                animate_text("Fine", 0.1)
                dk = random.choice(ht)
                time.sleep(2.5)
                if dk == "Head":
                    animate_text("Head", 0.1)
                    print("Dank> ", end="")
                    animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    animate_text("Aw Man!!!!!!", 0.1)
                    with conn:
                        c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                else:
                    animate_text("Tails", 0.1)
                    print("Dank> ", end="")
                    animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    animate_text("wait.... what!!!!!! you fooled me!!!!!!!!", 0.1)
                    with conn:
                        c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
            else:
                animate_text("Tails", 0.1)
                print("Dank> ", end="")
                animate_text("I am Still getting the money", 0.1)
                print(f"{name}> ", end="")
                animate_text("How?, wait.... wth!!!!!!!!", 0.1)
                with conn:
                    c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                print(f"{d}\u20b9 Deducted from the pocket")
        else:
            print("Dank> Ok only if you answer my question correctly")
            time.sleep(2.5)
            print(f"{name}> Ok!")
            time.sleep(1)
            question_data = Dank.askQuestionandgiveanswer()
            question = question_data['question']
            correct_answer = question_data['answer']
            print(f"Dank> {question}")
            user_answer = input(f"{name}> ")
            if user_answer.lower() == correct_answer.lower():
                prize = random.randint(0, 500)
                print("Dank> Correct answer")
                print(f"Dank> Here is your {prize}")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (prize, name))
            else:
                print("Dank> Wrong Answer!!!!")

    def highlow(self, username):
        rt = random.randint(1, 5)
        hiddennumber = random.randint(1, 100)
        hint = random.randint(1, 100)
        print("Dank> I just chose a secret number between 1 and 100.")
        time.sleep(rt)
        print(f"Dank> Is the secret number higher or lower than {hint}?")
        time.sleep(rt)
        print(f"Dank> | Lower -> if the number is lower than {hint}.")
        print(f"Dank> | Jackpot -> If the number is same as {hint}.")
        print(f"Dank> | Higher -> If the number is higher than {hint}.")
        print("      [Lower] [Jackpot!] [Higher]")
        time.sleep(rt)
        guesshiddennumber = input(f"{username}> ").lower()
        randomprize = random.randint(1, 500)
        if guesshiddennumber == "lower":
            if hiddennumber < hint:
                print("You guessed it correctly!")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (randomprize, username))
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        elif guesshiddennumber == "jackpot":
            if hiddennumber == hint:
                print("You guessed it correctly!")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (randomprize, username))
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        elif guesshiddennumber == "higher":
            if hiddennumber > hint:
                print("You guessed it correctly!")
                with conn:
                    c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (randomprize, username))
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        else:
            print("Invalid input. Please choose 'Lower', 'Jackpot', or 'Higher'.")

# Don't forget to close the connection when done
# conn.close()
