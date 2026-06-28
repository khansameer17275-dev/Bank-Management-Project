🏦 Bank Management System (Python)
A simple console-based banking application that stores account data persistently using a local JSON file.

📋 How It Works — Step by Step
1. Data Loading on Startup
When the program starts, it checks if data.json exists. If it does, all existing account records are loaded into memory. If not, it starts fresh.
2. Account Creation (Createaccount)

Collects user details: name, age, email, and a 4-digit PIN
Validates that the user is 18 or older and the PIN is exactly 4 digits
Generates a unique account number (mix of letters, digits, and special characters)
Saves the new account to data.json

3. Deposit Money (depositmoney)

Authenticates the user via account number + PIN
Accepts a deposit amount between ₹0 and ₹10,000
Updates the balance and saves to file

4. Withdraw Money (withdrawmoney)

Authenticates the user via account number + PIN
Checks if sufficient balance is available before deducting
Updates the balance and saves to file

5. Show Account Details (showdetails)

Authenticates the user via account number + PIN
Displays all stored account information

6. Update Details (updatedetails)

Authenticates the user via account number + PIN
Allows updating name, email, and PIN only
Fields left blank are kept unchanged
Balance, age, and account number cannot be changed

7. Delete Account (Delete)

Authenticates the user via account number + PIN
Asks for confirmation before permanently removing the account from data.json


🗂️ File Structure
├── bank.py        # Main application file
└── data.json      # Auto-generated database file

▶️ How to Run
bashpython bank.py
Then follow the on-screen menu to choose an action (1–6).

⚠️ Known Limitations

No loop — the program exits after one action per run
if userdata == False should be if not userdata for correct empty-list checking
The updatedetails method has a bug: uses == instead of = when keeping old values


Feel free to ask if you'd like a badge, installation section, or anything else added!You said: much more explain not enoughmuch more explain not enough12:38 AMClaude responded: Here's a much more detailed README:Here's a much more detailed README:

🏦 Bank Management System (Python)
A beginner-friendly, console-based banking application built in Python. It simulates core banking operations and stores all data locally in a JSON file — no database setup required. Perfect for learning Object-Oriented Programming (OOP) concepts in Python.

📌 Table of Contents

Overview
Features
How It Works
Code Breakdown
File Structure
How to Run
Limitations & Bugs
Future Improvements


🧾 Overview
This project is a Bank Management System written in pure Python using Object-Oriented Programming (OOP). It uses a single class Bank that handles everything — from creating accounts to deleting them. All data is saved and loaded from a data.json file, which acts as the application's database.

✨ Features
FeatureDescription✅ Create AccountRegister a new bank account with personal details✅ Deposit MoneyAdd money to your account (up to ₹10,000 per transaction)✅ Withdraw MoneyTake out money if balance is sufficient✅ Show DetailsView all your account information✅ Update DetailsChange your name, email, or PIN✅ Delete AccountPermanently remove your account✅ Persistent StorageAll data is saved in data.json automatically

⚙️ How It Works
🔷 Step 1 — Program Starts & Data Loads
pythonif Path(database).exists():
    with open(database) as fs:
        data = json.loads(fs.read())
The very first thing the program does when it starts is check whether a file called data.json already exists on your system.

If YES → It opens the file and loads all previously saved account records into the data list in memory
If NO → It prints a message and starts with an empty list
This means your data is never lost between sessions — every time you run the program, it picks up right where it left off
Any errors during file reading are caught by a try/except block to prevent crashes


🔷 Step 2 — Menu is Displayed to the User
press 1 for creating an account
press 2 for depositing money in the bank
press 3 for withdrawing the money
press 4 for details
press 5 for updating the details
press 6 for deleting your account
After loading the data, the program shows a simple numbered menu. The user types a number (1–6) and the corresponding function is called. Each option maps directly to a method inside the Bank class.

🔷 Step 3 — Account Creation (Createaccount)
pythondef Createaccount(self):
    info = {
        "name": input("Tell your name :- "),
        "age" : int(input("tell your age :- ")),
        "email": input("tell your email :- "),
        "pin": int(input("tell your pin :- ")),
        "accountNo.": Bank.__accountgenerate(),
        "balance" : 0
    }
This method collects all the information needed to open a new bank account:

Name — the customer's full name
Age — must be 18 or above, otherwise the account is rejected
Email — contact email address
PIN — a 4-digit security PIN (must be exactly 4 digits)
Account Number — automatically generated (user doesn't choose this)
Balance — starts at 0 by default

🔐 Account Number Generation (__accountgenerate)
pythonalpha = random.choices(string.ascii_letters, k=3)
num = random.choices(string.digits, k=3)
spchar = random.choices("!@#$%^&*", k=1)
id = alpha + num + spchar
random.shuffle(id)
return "".join(id)
A unique account number is created using Python's random and string modules:

3 random letters (uppercase or lowercase)
3 random digits (0–9)
1 random special character from !@#$%^&*
All 7 characters are then shuffled randomly and joined into one string
This ensures every account gets a different, unpredictable ID

✅ Validation Rules

Age must be ≥ 18
PIN must be exactly 4 digits
If either rule fails → account is not created
If both pass → account is saved and user is told to note down their account number

💾 Saving the Data
pythonBank.data.append(info)
Bank.__update()
The new account dictionary is added to the data list and then __update() writes the entire list back to data.json.

🔷 Step 4 — Deposit Money (depositmoney)
pythonuserdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
Authentication: The user must enter their account number AND PIN. The program searches through all accounts and finds the one that matches both — this is a basic but effective login check.
Deposit Rules:

Amount must be greater than 0
Amount must be less than or equal to ₹10,000 per transaction
If the amount is invalid → deposit is rejected with a message
If valid → the balance is increased and saved immediately

pythonuserdata[0]['balance'] += amount
Bank.__update()
Since userdata[0] is a reference to the actual dictionary inside Bank.data, updating it directly also updates the master list — no need to search again.

🔷 Step 5 — Withdraw Money (withdrawmoney)
Similar to deposit, but works in reverse:
Authentication: Same account number + PIN check
Withdrawal Rules:

The user enters how much they want to withdraw
Program checks: if userdata[0]['balance'] < amount → if the user doesn't have enough money, the transaction is blocked
If sufficient balance exists → amount is deducted and saved

pythonuserdata[0]['balance'] -= amount
Bank.__update()
This prevents accounts from going into negative balance.

🔷 Step 6 — Show Account Details (showdetails)
pythonfor i in userdata[0]:
    print(f"{i} : {userdata[0][i]}")
After authenticating via account number + PIN, this method loops through every key-value pair in the user's account dictionary and prints it line by line. The user can see their full profile including name, age, email, account number, PIN, and current balance.

🔷 Step 7 — Update Account Details (updatedetails)
This method allows partial updates — the user can change only what they want and skip the rest:
pythonnewdata = {
    "name": input("please tell new name or press enter : "),
    "email": input("please tell your new Email or press enter to skip :"),
    "pin": input("enter new Pin or press enter to skip: "),
}
What CAN be changed:

Name
Email
PIN

What CANNOT be changed:

Age
Account Number
Balance

If the user presses Enter without typing anything, the field is supposed to keep the old value. The final comparison loop:
pythonfor i in newdata:
    if newdata[i] == userdata[0][i]:
        continue
    else:
        userdata[0][i] = newdata[i]
This goes through each field — if the new value is the same as the old one, it skips it. If it's different, it updates it. Then __update() saves everything to the JSON file.

🔷 Step 8 — Delete Account (Delete)
pythoncheck = input("press y if you actually want to delete the account or press n ")
if check == 'n' or check == "N":
    print("bypassed")
else:
    index = Bank.data.index(userdata[0])
    Bank.data.pop(index)
    Bank.__update()
After authentication, the user is asked to confirm deletion. This is a safety step to prevent accidental deletion.

If user presses n or N → deletion is cancelled
If user presses anything else (including y) → account is found by index, removed from the list using .pop(), and the updated list is saved to data.json


🔷 Step 9 — Saving Data (__update)
python@classmethod
def __update(cls):
    with open(cls.database, 'w') as fs:
        fs.write(json.dumps(Bank.data))
This is a private class method (indicated by the double underscore __). It is called internally every time data changes. It:

Opens data.json in write mode (overwrites the file completely)
Converts the entire Bank.data list to a JSON string using json.dumps()
Writes it to the file

This ensures the file always has the latest, most up-to-date information.

🗂️ File Structure
bank-management-system/
│
├── bank.py          # Main Python file — all code lives here
└── data.json        # Auto-created file — stores all account records
data.json example after creating one account:
json[
  {
    "name": "Rahul Sharma",
    "age": 22,
    "email": "rahul@gmail.com",
    "pin": 1234,
    "accountNo.": "a3!Kd9z",
    "balance": 0
  }
]

▶️ How to Run
Requirements

Python 3.x installed on your system
No external libraries needed (only built-in modules: json, random, string, pathlib)

Steps
bash# 1. Clone or download the project
git clone https://github.com/your-username/bank-management-system.git

# 2. Navigate into the folder
cd bank-management-system

# 3. Run the program
python bank.py

🐛 Known Limitations & Bugs
IssueLocationExplanation❌ Wrong empty checkdepositmoney, withdrawmoney, Deleteif userdata == False should be if not userdata — an empty list is falsy but == False doesn't work correctly❌ Assignment bug in updateupdatedetailsnewdata["name"] == userdata[0]['name'] uses == (comparison) instead of = (assignment), so old values are never actually kept❌ No loopEntire programThe program exits after one operation — user has to re-run it every time❌ PIN stored as plain integerAll methodsPINs are not encrypted or hashed — anyone who opens data.json can see all PINs❌ No duplicate email checkCreateaccountTwo accounts can be created with the same email

🚀 Future Improvements

 Add a loop so the user can perform multiple operations in one session
 Hash the PIN using hashlib for security
 Add input validation to prevent crashes from wrong data types
 Add a transaction history feature
 Add a transfer money feature between accounts
 Build a simple GUI using tkinter
 Replace JSON file with a proper SQLite database


👨‍💻 Author
Built as a Python learning project to practice OOP, file handling, and JSON data management.
