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
    """
    Generate a SHA-256 hash of the given password.
    
    Args:
        password (str): Plain text password to hash
        
    Returns:
        str: Hexadecimal representation of the SHA-256 hash
        
    Used for secure password storage by converting plain text passwords
    into irreversible hash values before database storage.
    """
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    """
    Verify if a plain text password matches a stored hash.
    
    Args:
        password (str): Plain text password to verify
        hashed_text (str): Stored hash to compare against
        
    Returns:
        str or False: Returns the hash if passwords match, False otherwise
        
    Used during login to authenticate users by comparing the hash of
    their input password with the stored hash in the database.
    """
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


def add_user(username, password, remarks):
    """
    Add a new user to the database with hashed password.
    
    Args:
        username (str): Unique username for the new user
        password (str): Plain text password (will be hashed)
        remarks (str): User's eating habits and preferences
    
    Raises sqlite3.IntegrityError if username already exists.
    """
    c.execute('INSERT INTO users (username, password, remarks) VALUES (?,?,?)',
              (username, make_hashes(password), remarks))
    conn.commit()

def display_db(username):
    """
    Retrieve and display user data from the database.
    
    Args:
        username (str): Username to look up
        
    Returns:
        str or None: Username if found, None if user doesn't exist
        
    Queries the database for user information and returns the username
    for display purposes after successful login.
    """
    c.execute('SELECT * FROM users WHERE username =?', (username,))
    data = c.fetchone()
    return data[0] if data else None  

def get_remarks(username):
    """
    Retrieve user's personal remarks from the database.
    
    Args:
        username (str): Username to look up
        
    Returns:
        str or None: User's remarks if found, None if user doesn't exist
        
    Fetches the user's eating habits and preferences stored during registration
    for use in personalized restaurant recommendations.
    """
    c.execute('SELECT remarks FROM users WHERE username =?', (username,))
    data = c.fetchone()
    return data[0] if data else None  

def login_user(username, password):
    """
    Authenticate user login credentials against the database.
    
    Args:
        username (str): Username to authenticate
        password (str): Plain text password to verify
        
    Returns:
        str or False: Returns hashed password if authentication succeeds, False otherwise
        
    Looks up the user in the database and verifies the password hash
    to determine if login credentials are valid.
    """
    c.execute('SELECT * FROM users WHERE username =?', (username, ))
    data = c.fetchone()
    if data:
        return check_hashes(password, data[1])
    return False

@st.experimental_dialog(title="Sign Up Now")
def sign_up_page():
    """    
    Creates a modal dialog with registration form and handles user registration with validation and feedback
    """
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
    """    
    Creates the main login page and handles user authentication:
    """
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
    """
    Sign out the current user and clear session state.    
    Called when users choose to sign out or when switching to login page.
    """
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.user_remarks = None

