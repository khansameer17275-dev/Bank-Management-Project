import json
import random
import string
from pathlib import Path

DATABASE = "data.json"


def _load() -> list:
    path = Path(DATABASE)
    if path.exists():
        try:
            with open(path) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def _save(data: list) -> None:
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=2)


def _generate_acc_no() -> str:
    parts = (
        random.choices(string.ascii_uppercase, k=3)
        + random.choices(string.digits, k=4)
    )
    random.shuffle(parts)
    return "".join(parts)


class Bank:

    @staticmethod
    def find_user(acc_no: str, pin: int):
        """Return matching user dict or None."""
        data = _load()
        matches = [u for u in data if u["accountNo."] == acc_no and u["pin"] == pin]
        return matches[0] if matches else None

    @staticmethod
    def create_account(name: str, age: int, email: str, pin: int):
        """Create a new account. Returns (user_dict, message)."""
        if age < 18:
            return None, "You must be at least 18 years old."
        if not name or not email:
            return None, "Name and email are required."

        data = _load()
        acc_no = _generate_acc_no()
        new_user = {
            "name":      name.strip(),
            "age":       age,
            "email":     email.strip().lower(),
            "pin":       pin,
            "accountNo.": acc_no,
            "balance":   0,
        }
        data.append(new_user)
        _save(data)
        return new_user, f"Account created! Your account number is: {acc_no}"

    @staticmethod
    def deposit(acc_no: str, pin: int, amount: int):
        """Deposit money. Returns (success: bool, message: str)."""
        data = _load()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                user["balance"] += amount
                _save(data)
                return True, f"₹{amount:,} deposited. New balance: ₹{user['balance']:,}"
        return False, "Invalid account number or PIN."

    @staticmethod
    def withdraw(acc_no: str, pin: int, amount: int):
        """Withdraw money. Returns (success: bool, message: str)."""
        data = _load()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if amount > user["balance"]:
                    return False, f"Insufficient balance. Available: ₹{user['balance']:,}"
                user["balance"] -= amount
                _save(data)
                return True, f"₹{amount:,} withdrawn. Remaining: ₹{user['balance']:,}"
        return False, "Invalid account number or PIN."

    @staticmethod
    def update_user(acc_no: str, pin: int, name: str = "", email: str = "", new_pin: str = ""):
        """Update user details. Returns (success: bool, message: str)."""
        data = _load()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if name.strip():
                    user["name"] = name.strip()
                if email.strip():
                    user["email"] = email.strip().lower()
                if new_pin.strip():
                    if len(new_pin) == 4 and new_pin.isdigit():
                        user["pin"] = int(new_pin)
                    else:
                        return False, "New PIN must be exactly 4 digits."
                _save(data)
                return True, "Details updated successfully!"
        return False, "Invalid account number or PIN."

    @staticmethod
    def delete_user(acc_no: str, pin: int):
        """Delete account. Returns (success: bool, message: str)."""
        data = _load()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                data.remove(user)
                _save(data)
                return True, "Account permanently deleted."
        return False, "Invalid account number or PIN."