import streamlit as st
import sqlite3
import hashlib

# Initialize connection to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''DROP TABLE users''')
# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, remarks TEXT)''')


def make_hashes(password):
  return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
  if make_hashes(password) == hashed_text:
    return hashed_text
  return False


def add_user(username, password, remarks):
  c.execute('INSERT INTO users (username, password, remarks) VALUES (?,?,?)',
            (username, make_hashes(password), remarks))
  conn.commit()

def display_db(username):
  c.execute('SELECT * FROM users WHERE username =?', (username,))
  data = c.fetchone()
  return data[0] if data else None  

def get_remarks(username):
  c.execute('SELECT remarks FROM users WHERE username =?', (username,))
  data = c.fetchone()
  return data[0] if data else None  

def login_user(username, password):
  c.execute('SELECT * FROM users WHERE username =?', (username, ))
  data = c.fetchone()
  if data:
    return check_hashes(password, data[1])
  return False

@st.experimental_dialog(title="Sign Up Now")
def sign_up_page():
  st.subheader("Create New Account")
  new_user = st.text_input("Username", key='signup_username')
  new_password = st.text_input("Password",
                               type='password',
                               key='signup_password')
  user_remarks = st.text_area("Remark: \n\n *What's your eating habits?*")

  if st.button("Signup"):
    try:
      add_user(new_user, new_password, user_remarks)
      st.success("You have successfully created an account")
      st.info("Go to Login Menu to login")
    except sqlite3.IntegrityError:
      st.warning("Username already exists. Please choose a different one.")


def sign_in_page():
  st.write("## Sign In")
  st.subheader("Login Section")

  username = st.text_input("User Name", key='signin_username')
  password = st.text_input("Password", type='password', key='signin_password')
  if st.button("Login", key='signin_button',use_container_width=True):
    if login_user(username, password):
      st.session_state.logged_in = True
      st.session_state.username = username
      st.session_state.user_remarks = get_remarks(username)
      st.success(f"Logged In as {username}")
      st.write(display_db(username))
    else:
      st.warning("Incorrect Username/Password")

  if st.button("Sign Up", key='signup_button', use_container_width=True):
    sign_up_page()

def sign_out():
  st.session_state.logged_in = False
  st.session_state.username = None
  st.session_state.user_remarks = None
  # st.session_state.should_update_tab1 = True
  # st.session_state.should_update_tab2 = True

