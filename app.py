import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import time

# Session state initialization
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authorized" not in st.session_state:
    st.session_state.authorized = True

# Generate key for encryption
if "key" not in st.session_state:
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.key)

# Hashing passkey with salt
def hash_passkey(passkey):
    salt = b'secure_salt'
    return hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000).hex()

# Encrypt data
def encrypt_data(text):
    return st.session_state.cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    for key, value in st.session_state.stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()

    st.session_state.failed_attempts += 1
    return None

# UI Title with Animation
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B; animation: pulse 2s infinite;'>
        🛡️ Super Secure Data Encryption System
    </h1>
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

# Navigation with Icons
menu = ["🏠 Home", "📂 Store Data", "🔍 Retrieve Data", "🔐 Login"]
choice = st.sidebar.selectbox("📁 Navigation", menu)

# Home Page
if choice == "🏠 Home":
    st.subheader("🏠 Welcome")
    st.markdown("""
    ### Features:
    - 🔒 Advanced Encryption
    - 🔑 Secure Password Protection
    - 📊 Data Management
    - ⏰ Timestamp Tracking

    Yeh app aapko **data securely store aur retrieve** karne mein madad karti hai using advanced encryption techniques.
    """)

# Store Data Page
elif choice == "📂 Store Data":
    st.subheader("📂 Store Your Data")
    user_data = st.text_area("Enter your data:", height=150)
    passkey = st.text_input("Enter a passkey:", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt & Store", use_container_width=True):
            if user_data and passkey:
                with st.spinner("Encrypting..."):
                    time.sleep(1)
                    hashed_pass = hash_passkey(passkey)
                    encrypted_text = encrypt_data(user_data)
                    st.session_state.stored_data[encrypted_text] = {
                        "encrypted_text": encrypted_text,
                        "passkey": hashed_pass,
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.success("✅ Data encrypted & stored successfully!")
                    st.code(encrypted_text, language="text")
            else:
                st.error("⚠️ Dono fields zaroori hain!")
    with col2:
        if st.button("Clear Fields", use_container_width=True):
            st.rerun()

# Retrieve Data Page
elif choice == "🔍 Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔒 Unauthorized access! Please login first.")
        st.stop()

    st.subheader("🔍 Retrieve Data")
    encrypted_input = st.text_area("Paste your encrypted text:", height=100)
    passkey = st.text_input("Enter your passkey:", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Decrypt", use_container_width=True):
            if encrypted_input and passkey:
                with st.spinner("Decrypting..."):
                    time.sleep(1)
                    decrypted = decrypt_data(encrypted_input, passkey)
                    if decrypted:
                        st.success("✅ Decrypted Data:")
                        st.code(decrypted, language="text")
                        if encrypted_input in st.session_state.stored_data:
                            st.info(f"🕒 Encrypted on: {st.session_state.stored_data[encrypted_input]['timestamp']}")
                    else:
                        remaining = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Incorrect passkey! Attempts remaining: {remaining}")
                        if st.session_state.failed_attempts >= 3:
                            st.session_state.authorized = False
                            st.warning("🔐 Too many failed attempts! Redirecting to login.")
                            time.sleep(2)
                            st.rerun()
            else:
                st.error("⚠️ Dono fields zaroori hain!")
    with col2:
        if st.button("Clear Fields", use_container_width=True):
            st.rerun()

# Login Page
elif choice == "🔐 Login":
    st.subheader("🔐 Re-Login Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login", use_container_width=True):
        with st.spinner("Authenticating..."):
            time.sleep(1)
            if login_pass == "admin123":
                st.session_state.failed_attempts = 0
                st.session_state.authorized = True
                st.success("✅ Login successful! You can now retry decryption.")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Incorrect master password!")

# Footer
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <p>Made with ❤️ for Security</p>
    </div>
""", unsafe_allow_html=True)
