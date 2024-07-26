import streamlit as st
import sqlite3
import hashlib

# st.session_state.sidebar_state = 'collapsed'
# if 'layout' not in st.session_state:
# st.session_state.layout = 'centered'
st.set_page_config(page_title="Login Page 🔑",
                   layout="centered",
                   initial_sidebar_state='collapsed')

# st.write(st.session_state.sidebar_state)

st.markdown(
    """
<style>
  [data-testid="collapsedControl"] {
      display: none
  }
</style>
""",
    unsafe_allow_html=True,
)

DB_FILE = 'users.db'


@st.cache_resource
def init_connection():
  return sqlite3.connect(DB_FILE, check_same_thread=False)


def get_cursor():
  return init_connection().cursor()


conn = init_connection()
c = get_cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, remarks TEXT)''')
conn.commit()

@st.experimental_dialog(title="Sign Up Now")
def sign_up_page():
  st.subheader("Create New Account")
  new_user = st.text_input("Username", key='signup_username')
  new_password = st.text_input("Password",
                               type='password',
                               key='signup_password')
  user_remarks = st.text_area("Remark: \n\n *What's your eating habits?*")

  if st.button("Sign Up"):
    if new_user == "" or new_password == "":
      st.warning("Please enter both username and password")
    else:
      try:
        add_user(new_user, new_password, user_remarks)
        st.success("You have successfully created an account")
        st.info("Go to Login Menu to login")
        # c.execute('SELECT * FROM users')
      except sqlite3.IntegrityError:
        st.warning("Username already exists. Please choose a different one.",
                   icon="⚠️")


def sign_in_page():
  with st.container(border=True):
    warning_message = None

    st.write("# Sign In To Eat-dentify")
    st.write(":gray[Login Section]")

    username = st.text_input("Username", key='signin_username')
    password = st.text_input("Password",
                             type='password',
                             key='signin_password')

    st.write("###")
    col1, col2 = st.columns(2)

    with col1:
      if st.button("Login", key='signin_button', use_container_width=True):
        if username == "" and password == "":
          warning_message = "Please enter both username and password"
        else:
          if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.user_remarks = get_remarks(username)
            st.success(f"Logged In as {username}")
            st.switch_page("pages/eatdentify.py")
          else:
            warning_message = "Incorrect Username/Password"

    if warning_message:
      st.warning(warning_message, icon="⚠️")

    with col2:
      if st.button("Sign Up", key='signup_button', use_container_width=True):
        sign_up_page()

    if st.button("Continue as Guest",
                 key='guest_account',
                 use_container_width=True,
                 type="primary"):
      st.toast("Logging in as Guest")
      st.switch_page("pages/eatdentify.py")

def make_hashes(password):
  return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
  if make_hashes(password) == hashed_text:
    return True
  return False


def update_user(username):
  c = get_cursor()
  c.execute("UPDATE users SET remarks = ? WHERE username = ?",
            (st.session_state.remarks, username))
  c.execute("UPDATE users SET username = ? WHERE username = ?",
            (st.session_state.username, username))
  c.execute("UPDATE users SET password = ? WHERE username = ?",
            (make_hashes(st.session_state.password), username))
  conn.commit()


def add_user(username, password, remarks):
  c = get_cursor()
  c.execute('INSERT INTO users (username, password, remarks) VALUES (?,?,?)',
            (username, make_hashes(password), remarks))
  conn.commit()


def display_db(username):
  c = get_cursor()
  c.execute('SELECT * FROM users WHERE username =?', (username, ))
  data = c.fetchone()
  return data[0] if data else None


def get_remarks(username):
  c = get_cursor()
  c.execute('SELECT remarks FROM users WHERE username =?', (username, ))
  data = c.fetchone()
  try:
    return data[0]
  except Exception as e:
    return ""


def login_user(username, password):
  c = get_cursor()
  c.execute('SELECT * FROM users WHERE username =?', (username, ))
  data = c.fetchone()
  # print(f"New Username {username}")
  # print(f"New Password {password}")
  # print(f"Stored Password {data[1]}")
  if data:
    return check_hashes(password, data[1])
  return False

def main():
  sign_in_page()


if __name__ == '__main__':
  main()