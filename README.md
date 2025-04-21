# 🛡️ Super Secure Data Encryption System

**Muhammad Hammad**  
**GIAIC Student ID Number:** 413850  
**Slot:** Section A (Tuesday Evening)  
**Growth Mindset Challenge Web App Deployed URL:** [Super Secure Data Encryption System](https://project-5-secure-data-encryption-system-12.streamlit.app/)

---

A Streamlit-based secure data storage and retrieval web app that uses advanced encryption and passkey hashing for protecting sensitive user data.

## 🚀 Features

- 🔒 **Advanced Encryption** using `cryptography.fernet`
- 🔑 **Secure Passkey Hashing** with SHA-256 and Salt
- 📂 **Data Storage** in encrypted form with timestamps
- 🔍 **Secure Data Retrieval** through authentication and decryption
- ⏰ **Access Logging** via encryption timestamps
- 👮‍♂️ **Brute Force Prevention** with max 3 failed attempts
- 🔐 **Login System** for blocked users

## 🧱 Tech Stack

- **Frontend:** Streamlit
- **Encryption:** Python `cryptography` package (`Fernet`)
- **Hashing:** `hashlib` with PBKDF2 and Salt
- **State Management:** Streamlit's session state
- **Language:** Python 3.9+

## 📷 Screenshots

| Home Page | Store Data | Retrieve Data | Login Page |
|-----------|------------|----------------|-------------|
| ![Home](screenshots/home.png) | ![Store](screenshots/store.png) | ![Retrieve](screenshots/retrieve.png) | ![Login](screenshots/login.png) |

## 🛠️ How it Works

### 🔐 Storing Data:
1. User enters data and a passkey.
2. The passkey is hashed with salt.
3. Data is encrypted using `Fernet`.
4. Encrypted data is stored in session state with a timestamp.

### 🔍 Retrieving Data:
1. User inputs the encrypted text and the original passkey.
2. If the hash matches the stored hash, data is decrypted.
3. If failed 3 times, user is locked out and redirected to login.

### 🔑 Login:
A simple master password (`admin123`) restores access after failed attempts.

## 🧪 Running the App Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hammadsheikh5/Project-5-Secure-Data-Encryption-System
   cd Project-5-Secure-Data-Encryption-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 📦 Dependencies

- streamlit
- cryptography

You can install all with:

```bash
pip install streamlit cryptography
```

## 🧠 Future Improvements

- Persistent database storage (e.g., SQLite, Firebase)
- Email/OTP-based authentication
- File encryption support
- Role-based access control (RBAC)


## ❤️ Acknowledgments

Built as a learning project to demonstrate secure data handling and encryption using Python & Streamlit.
