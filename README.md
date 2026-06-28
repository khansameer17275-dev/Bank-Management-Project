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


Feel free to ask if you'd like a badge, installation section, or anything else added!
