import sqlite3
import time
import random
from FunctionsByRS import * 
rd = random

#database
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()

class Crimegenerator:
    def __init__(self):
        self.xyz = random.randint(1, 5000)
        self.abc = random.randint(1, 500)
        self.yza = random.randint(1, 50000)
        self.zab = random.randint(1, 15000)
        self.fake_crimes_to_commit = {
            "Hacking": [f"You hacked into Dank Memer and gave yourself {self.xyz}\u20b9. Evil!", "You hacked into your own router and found out the ISP does not actually care about you.", 'You got caught hacking into Dank Memer and Badosz "Thanos Snapped" you'],
            "Bank_robbing": [f"You robbed a bank irl and found {self.yza}\u20b9. Cute!", "You tried to rob a bank but got scared, lol", "You robbed a bank and the little old lady was packing heat, you did NOT make it out"],
            "Trespassing": [f"You walked straight into someone else's yard and found {self.zab}\u20b9. Free real estate!", "You got confused about what trespassing was and walked into your own back yard.", "You tried trespassing onto the property of someone with a gun f*tish and it did NOT go well"],
            "Shoplifting": [f"You managed to steal {self.xyz}\u20b9. Money Heist!", "You tried to steal something, but the shop was closed!", "You stole an unknown drink and drank it. It turned out to be poison and you died. RIP"],
            "cyber_bullying": [f"You bullied a kid and he sent you {self.abc}\u20b9 to stop! I hope that kid grows up richer than you.", "You tried to bully a kid, but quickly got banned by mods. LOL, seeya idiot.", "You laughed at a kid so much, you choked to death. Who is laughing now? Imagine being a bully."],
            "Murder": [f"You murdered a random stranger in a dark alley. There was {self.xyz}\u20b9 in his wallet! Was it worth it?", "You tried to murder a random stranger, but he got away! You can't even murder properly.","You were holding the gun upside down and killed yourself! Imagine being this stupid!"],
            "Piracy": [f'You ripped off your favorite movies and also found {self.abc}\u20b9',"You tried to pirate an adult film and got distracted on the free websites instead", 'The FBI found out about that copy of your Air Bud DVD you made and "took you out"'],
            "Treason": [f"You successfully overthrew the government with your treason and in the halls of congress found {self.abc}\u20b9.", "You failed to host an insurrection, everyone is laughing at you.", "You were caught and the punishment for treason is death."],
            "Vandalism": [f'You wrote "Dank Memer" on a wall and the developers sent you {self.xyz}\u20b9. Nice!', "You tried to write something on a wall, but ran out of spray. LOL", "While writing on the wall you fell from the 10th floor and died."]
        }
    
    def Hacking(self, name):
        d = self.fake_crimes_to_commit["Hacking"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.xyz
            print(hehe)
            c.execute("UPDATE set money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE set money = money - ? WHERE name = ?", (100000, name))
            conn.commit()
    def Bank_robbing(self, name):
        d = self.fake_crimes_to_commit["Bank_robbing"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.yza
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (100000, name))
            conn.commit()
    def Trespassing(self, name):
        d = self.fake_crimes_to_commit["Trespassing"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.zab
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE set money = money - ? WHERE name = ?", (100000, name))
            conn.commit()
    def Shoplifting(self, name):
        d = self.fake_crimes_to_commit["Shoplifting"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.xyz
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE set money = money - ? WHERE name = ?", (100000, name))
            conn.commit()
    def cyber_bullying(self, name):
        d = self.fake_crimes_to_commit["cyber_bullying"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.abc
            print(hehe)
            c.execute("UPDATE set money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE set money = money - ? WHERE name = ?", (100000, name))
            conn.commit()
    def Murder(self, name):
        d = self.fake_crimes_to_commit["Murder"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.xyz
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (100000, name))
            conn.commit()
    def Piracy(self, name):
        d = self.fake_crimes_to_commit["Piracy"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.abc
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (100000, name))
            conn.commit()
    def Treason(self, name):
        d = self.fake_crimes_to_commit["Treason"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.abc
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (100000, name))
            conn.commit()
    def Vandalism(self, name):
        d = self.fake_crimes_to_commit["Vandalism"]
        chances = [10, 50, 40]
        hehe = random.choices(d, chances, k=1)[0]
        if hehe == d[0]:
            money = self.xyz
            print(hehe)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (money, name))
            conn.commit()
        elif hehe == d[1]:
            print(hehe)
        else:
            print(hehe)
            time.sleep(1)
            print("Dank> You lost 100000\u20b9 because you died")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (100000, name))
            conn.commit()
    def crime(self, username):
        random3crime = random.sample(list(self.fake_crimes_to_commit.keys()), k=3)
    
        print("Dank> Which Crime you want to commit?")
        for i, crime in enumerate(random3crime, 1):
            print(f"{i}. {crime}")

        choosecrimetocommit = int(input(f"{username}> "))  # Convert input to integer
        
        chosen_crime = random3crime[choosecrimetocommit - 1]

        if chosen_crime in self.fake_crimes_to_commit:
            crime_gen = Crimegenerator()
            getattr(crime_gen, chosen_crime)(name=username)
        else:
            print("Error in crimegenerator. Please inform the developer")
class Dank:

    @staticmethod
    def question():
        dankquestions = {
            "question1": {
                "question": "Who is prime minister of India currently in 2024?",
                "answer": "narendra modi"
            },
            "question2": {
                "question": "What is 2 + 2 - 3 * 4 + 232 + 24 * 3 - 2432 - 32 + 4 - 32 = ?",
                "answer": "-2196"
            },
            "question3": {
                "question": "What is the value of π (pi) to two decimal places?",
                "answer": "3.14"
            },
            "question4": {
                "question": "Who is often credited with the discovery of the Pythagorean theorem?",
                "answer": "pythagoras"
            },
            "question5": {
                "question": "What is the capital of Australia?",
                "answer": "canberra"
            },
            "question6": {
                "question": "In which year did the Apollo 11 mission successfully land humans on the moon?",
                "answer": "1969"
            },
            "question7": {
                "question": "How many sides does a heptagon have?",
                "answer": "7"
            },
            "question8": {
                "question": "Who wrote famous play 'Romeo and Juliet'?",
                "answer": "william shakespeare"
            },
            "question9": {
                "question": "What is the chemical symbol for gold?",
                "answer": "Au"
            },
            "question10": {
                "question": "What is the largest planet in our solar system?",
                "answer": "jupiter"
            },
            "question11": {
                "question": "What is the square root of 144?",
                "answer": "12"
            },
            "question12": {
                "question": "Who painted the famous artwork 'Starry Night'?",
                "answer": "vincent van gogh"
            }
        }
        return dankquestions
    
    @staticmethod
    def askQuestionandgiveanswer():
        q = Dank.question()
        r = random.choice(list(q.values()))
        return r

    def Availablecommands(self):
        return "< /bal >, < /dig >, < /beg >, < /update >, < /crime > more comming soon baby!!!!!!!"
        
    def bal(self, name):
        c.execute("SELECT money FROM dank WHERE name=?", (name,))
        balance = c.fetchone()
        c.execute("SELECT moneyinbank FROM dank WHERE name=?", (name,))
        balanceinbank = c.fetchone()
        if balance:
            print(f"User: {name}")
            print(f"Balance: {balance[0]}\u20b9")
            print(f"Bank Balance: {balanceinbank[0]}\u20b9")
        else:
            print(f"User {name} not found.")
    def dig(self, name):
        chanc = rd.randint(1, 10)
        
        if chanc == 1:
            soldgold = rd.randint(1, 10000)
            print(f"You strike gold, {name}! You got some gold and sold it for {soldgold}\u20b9.")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (soldgold, name))
            conn.commit()
        elif chanc == 2:
            print(f"You dug down and found nothing! lololololol!")
        elif chanc == 3:
            worth = rd.randint(1, 100)
            print(f"You dug down and found some coins worth {worth}\u20b9")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (worth, name))
            conn.commit()
        elif chanc == 4:
            print(f"You dug down and found buried dog poop XD")
        elif chanc == 5:
            piggybankmoney = rd.randint(1,150)
            print(f"You Digged down and found kid's piggybank, you found {piggybankmoney}\u20b9 ")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (piggybankmoney, name))
            conn.commit()
        elif chanc == 6:
            print(f"You Digged down and Fell into lava pool")
            time.sleep(2)
            deathmessage = f"{name} tries to swim in lava."
            for i in deathmessage:
                print(i, end="")
                time.sleep(0.2)
            print(":|\n")
        elif chanc == 7:
            notez = rd.randint(0,50)
            if notez >= 3:
                l = rd.randint(6083, 56951)
                print(f"You found a single gold coin worth {l}\u20b9 ")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (l, name))
                conn.commit()
            else:
                oo = rd.randint(80000,10000000)
                print(f"You Digged down and found a diamond worth {oo}")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (oo, name))
                conn.commit()
        elif chanc == 8:
            print("You Digged down and found a diamond but then creeper came and blowed you up!\n")
        elif chanc == 9:
            print(f"you digged and found cockroaches!!!!!!!\n")
        elif chanc == 10:
            print(f"Unfortunate turn of events! {name}, your digging attracts unwanted attention from bandits, who demand a share of your findings. Better luck next time.\n")
    def beg(self, name):
        chance = rd.randint(1, 5)
        if chance == 1:
            lm = rd.randint(1, 150)
            print(f"Dank> Ohh you poor~~ soul! here take some {lm}\u20b9")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lm, name))
            conn.commit()
        elif chance == 2:
            lesgo = rd.randint(1, 50)
            print("Dank> ", end="")
            animate_text(text="Bruh! i don't have cash", delay=0.1)
            time.sleep(1)
            print(f"{name}> ", end="")
            animate_text(text="Here's my PayPal qr code scan and give online :D",delay=0.1)
            print(f"Dank> ", end="")
            animate_text(text=f"Are You Serious Right now Bruh?, nvm here's {lesgo}\u20b9", delay=0.1)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lesgo, name))
            conn.commit()
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
            ht = "Head", "Tails"
            dk = rd.choices(ht)
            print("Dank> ", end="")
            animate_text(text="Imma flip coin if it's a head you will give me money\n if it's a tail then i will take money", delay=0.1)
            time.sleep(3.5)
            animate_text("Coin Flips!!!!", 0.1)
            time.sleep(0.5)
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
                dk = rd.choices(ht)
                time.sleep(2.5)
                if dk == "Head":
                    d = "150"
                    animate_text("Head", 0.1)
                    print("Dank> ", end="")
                    animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    animate_text("Aw Man!!!!!!", 0.1)
                    c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                    conn.commit()
                else:
                    animate_text("Tails", 0.1)
                    print("Dank> ", end="")
                    animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    animate_text("wait.... what!!!!!! you fooled me!!!!!!!!", 0.1)
                    c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                    conn.commit()
            else:
                d = "150"
                animate_text("Tails", 0.1)
                print("Dank> ", end="")
                animate_text("I am Still getting the money", 0.1)
                print(f"{name}> ", end="")
                animate_text("How?, wait.... wth!!!!!!!!", 0.1)
                c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                conn.commit()
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
                prize = rd.randint(0, 500)
                print("Dank> Correct answer")
                print(f"Dank> Here is your {prize}")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (prize, name))
                conn.commit()
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
        try:
            guesshiddennumber = input(f"{username}> ")
        except:
            print("")
            print("Enter a number dude....")
            print("")
        if guesshiddennumber.lower() == "lower":
            if hiddennumber > hint:
                print("You guessed it correctly!")
                randomprize = random.randint(1, 500)
                c.execute("UPDATE dank SET money = money + ?  WHERE name = ?", (guesshiddennumber, username))
                conn.commit()
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        elif guesshiddennumber.lower() == "jackpot":
            if hiddennumber == hint:
                print("You guessed it correctly!")
                randomprize = random.randint(1, 500)
                c.execute("UPDATE dank SET money = money + ?  WHERE name = ?", (guesshiddennumber, username))
                conn.commit()
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        elif guesshiddennumber.lower() == "higher":
            if hiddennumber < hint:
                print("You guessed it correctly!")
                randomprize = random.randint(1, 500)
                c.execute("UPDATE dank SET money = money + ?  WHERE name = ?", (guesshiddennumber, username))
                conn.commit()
                print(f"Dank> Here is your {randomprize}")
            else:
                print("Dank> You guessed it wrong!")
                time.sleep(rt)
                print(f"Dank> The secret number was {hiddennumber}")
        
