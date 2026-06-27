import streamlit as st
from bank import Bank

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="NeoBank", page_icon="🏦", layout="centered")

# ─── Styling ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0a0f1e; color: #e8eaf0; }
#MainMenu, header, footer { visibility: hidden; }

.neo-header { text-align: center; padding: 2.5rem 0 1.5rem; }
.neo-header h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem; font-weight: 700;
    background: linear-gradient(135deg, #6ee7f7 0%, #a78bfa 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin: 0; letter-spacing: -1px;
}
.neo-header p { color: #6b7280; font-size: 0.95rem; margin-top: 0.4rem; }

.card {
    background: #111827; border: 1px solid #1f2937;
    border-radius: 16px; padding: 1.8rem; margin-bottom: 1.2rem;
}
.balance-big {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem; font-weight: 700; color: #6ee7f7; line-height: 1;
}
.balance-label {
    font-size: 0.78rem; text-transform: uppercase;
    letter-spacing: 2px; color: #6b7280; margin-bottom: 0.3rem;
}
.acc-badge {
    display: inline-block; font-family: 'Space Grotesk', monospace;
    background: #1f2937; border: 1px solid #374151;
    border-radius: 8px; padding: 0.25rem 0.75rem;
    font-size: 1rem; letter-spacing: 2px; color: #6ee7f7;
}
.info-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 0.55rem 0; border-bottom: 1px solid #1f2937; font-size: 0.92rem;
}
.info-row:last-child { border-bottom: none; }
.info-key { color: #6b7280; }
.info-val { color: #e8eaf0; font-weight: 500; }

.stSelectbox > div > div {
    background: #111827 !important; border: 1px solid #374151 !important;
    border-radius: 12px !important; color: #e8eaf0 !important;
}
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: #1f2937 !important; border: 1px solid #374151 !important;
    border-radius: 10px !important; color: #e8eaf0 !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #6ee7f7 !important;
    box-shadow: 0 0 0 2px rgba(110,231,247,0.15) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #6ee7f7, #a78bfa) !important;
    color: #0a0f1e !important; font-weight: 600 !important;
    border: none !important; border-radius: 10px !important;
    padding: 0.6rem 2rem !important; width: 100%;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.88 !important; }
.danger-btn .stButton > button {
    background: linear-gradient(135deg, #f87171, #ef4444) !important;
    color: #fff !important;
}
hr { border-color: #1f2937 !important; }
.stAlert { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="neo-header">
  <h1>🏦 NeoBank</h1>
  <p>Secure · Simple · Modern</p>
</div>
""", unsafe_allow_html=True)

# ─── Menu ─────────────────────────────────────────────────────────────────────
menu = st.selectbox(
    "Action",
    ["🆕 Create Account", "💰 Deposit", "💸 Withdraw",
     "👤 View Details", "✏️ Update Details", "🗑️ Delete Account"],
    label_visibility="collapsed",
)
st.markdown("<hr>", unsafe_allow_html=True)


# ─── Auth Fields Helper ────────────────────────────────────────────────────────
def auth_fields(prefix=""):
    acc = st.text_input("Account Number", key=f"{prefix}_acc", placeholder="e.g. A3B9Z7K")
    pin = st.text_input("PIN", key=f"{prefix}_pin", type="password",
                        placeholder="4-digit PIN", max_chars=4)
    return acc.strip(), pin.strip()


# ═══════════════════════════════════════════════════════════════════════════════
# 1. CREATE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
if menu == "🆕 Create Account":
    st.subheader("Open a New Account")
    with st.form("create_form", clear_on_submit=True):
        name  = st.text_input("Full Name")
        age   = st.number_input("Age", min_value=0, max_value=120, step=1)
        email = st.text_input("Email Address")
        pin   = st.text_input("Choose a 4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if not name or not email or not pin:
            st.error("Name, email, and PIN are required.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            user, msg = Bank.create_account(name, int(age), email, int(pin))
            if user:
                st.success("Account created successfully!")
                st.markdown(f"""
<div class="card">
  <div class="balance-label">Your Account Number</div>
  <div class="acc-badge">{user['accountNo.']}</div>
  <br><br>
  <div class="info-row"><span class="info-key">Name</span><span class="info-val">{user['name']}</span></div>
  <div class="info-row"><span class="info-key">Email</span><span class="info-val">{user['email']}</span></div>
  <div class="info-row"><span class="info-key">Starting Balance</span><span class="info-val">₹ 0</span></div>
</div>
<p style="color:#6b7280;font-size:0.82rem;">⚠️ Save your account number — you'll need it to log in.</p>
""", unsafe_allow_html=True)
            else:
                st.error(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. DEPOSIT
# ═══════════════════════════════════════════════════════════════════════════════
elif menu == "💰 Deposit":
    st.subheader("Deposit Money")
    acc, pin = auth_fields("dep")
    amount = st.number_input("Amount to Deposit (₹)", min_value=1, max_value=10_00_000, step=100)

    if st.button("Deposit"):
        if not acc or not pin:
            st.error("Please enter account number and PIN.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            success, msg = Bank.deposit(acc, int(pin), int(amount))
            if success:
                st.success(msg)
            else:
                st.error(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. WITHDRAW
# ═══════════════════════════════════════════════════════════════════════════════
elif menu == "💸 Withdraw":
    st.subheader("Withdraw Money")
    acc, pin = auth_fields("with")
    amount = st.number_input("Amount to Withdraw (₹)", min_value=1, max_value=10_00_000, step=100)

    if st.button("Withdraw"):
        if not acc or not pin:
            st.error("Please enter account number and PIN.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            success, msg = Bank.withdraw(acc, int(pin), int(amount))
            if success:
                st.success(msg)
            else:
                st.error(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. VIEW DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif menu == "👤 View Details":
    st.subheader("Account Details")
    acc, pin = auth_fields("view")

    if st.button("Show Details"):
        if not acc or not pin:
            st.error("Please enter account number and PIN.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            user = Bank.find_user(acc, int(pin))
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                st.markdown(f"""
<div class="card">
  <div class="balance-label">Balance</div>
  <div class="balance-big">₹ {user['balance']:,}</div>
  <br>
  <div class="info-row"><span class="info-key">Name</span><span class="info-val">{user['name']}</span></div>
  <div class="info-row"><span class="info-key">Age</span><span class="info-val">{user['age']}</span></div>
  <div class="info-row"><span class="info-key">Email</span><span class="info-val">{user['email']}</span></div>
  <div class="info-row"><span class="info-key">Account No.</span>
    <span class="acc-badge">{user['accountNo.']}</span></div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# 5. UPDATE DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif menu == "✏️ Update Details":
    st.subheader("Update Account Details")
    acc, pin = auth_fields("upd")

    if st.button("Load My Details"):
        if not acc or not pin:
            st.error("Please enter account number and PIN.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            user = Bank.find_user(acc, int(pin))
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                st.session_state["edit_acc"] = acc
                st.session_state["edit_pin"] = pin
                st.session_state["edit_user"] = user

    if "edit_user" in st.session_state:
        user = st.session_state["edit_user"]
        st.info("Leave a field blank to keep the current value.")
        with st.form("update_form"):
            new_name  = st.text_input("New Name",  placeholder=user["name"])
            new_email = st.text_input("New Email", placeholder=user["email"])
            new_pin   = st.text_input("New PIN (4 digits)", type="password",
                                      placeholder="••••", max_chars=4)
            save_btn = st.form_submit_button("Save Changes")

        if save_btn:
            success, msg = Bank.update_user(
                st.session_state["edit_acc"],
                int(st.session_state["edit_pin"]),
                new_name, new_email, new_pin
            )
            if success:
                st.success(msg)
                del st.session_state["edit_user"]
            else:
                st.error(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# 6. DELETE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
elif menu == "🗑️ Delete Account":
    st.subheader("Delete Account")
    st.warning("⚠️ This action is **permanent** and cannot be undone.")
    acc, pin = auth_fields("del")
    confirm = st.checkbox("I understand this will permanently delete my account.")

    with st.container():
        st.markdown('<div class="danger-btn">', unsafe_allow_html=True)
        delete_btn = st.button("Delete My Account")
        st.markdown('</div>', unsafe_allow_html=True)

    if delete_btn:
        if not confirm:
            st.error("Please check the confirmation box first.")
        elif not acc or not pin:
            st.error("Please enter account number and PIN.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        else:
            success, msg = Bank.delete_user(acc, int(pin))
            if success:
                st.success(msg)
            else:
                st.error(msg)