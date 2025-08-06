import streamlit as st
from login import init_connection, get_cursor, update_user, make_hashes

def sign_out():
    """
    Sign out the current user and clear session state.
    
    Resets the user authentication state by:
    - Setting logged_in status to False
    - Clearing username from session state
    - Clearing user_remarks from session state
    
    This function is called when users choose to sign out or when
    redirecting to login page for authentication.
    """
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.user_remarks = None

def display_profile():
    """
    Display the user profile management interface.
    
    Provides different interfaces based on authentication status:
    
    For logged-in users:
    - Shows current username (read-only)
    - Allows password updates with secure input field
    - Allows editing of user remarks/preferences
    - Provides "Update Profile" button to save changes to database
    - Includes "Sign Out" button to end session
    - Updates both session state and database when profile is modified
    
    For guest users:
    - Shows informational message about guest mode
    - Provides "Sign In Now" button to redirect to login page
    
    Handles password hashing and database updates securely when changes are saved.
    """
    if st.session_state.logged_in:
        st.write("Your username:")
        st.markdown(f"**{st.session_state.username}**")
        new_password = st.text_input("New password:",
                                     st.session_state.password,
                                     type='password')
        new_remarks = st.text_area("New remarks:", st.session_state.user_remarks)

        st.write("---")

        if st.button("Update Profile"):
          st.session_state.remarks = new_remarks
          st.session_state.password = new_password

          update_user(st.session_state.username)
          conn = init_connection()
          
          # Update password separately if it has changed
          if new_password != st.session_state.password:
            with conn.session as s:
              s.execute("UPDATE users SET password = ? WHERE username = ?",
                      (make_hashes(new_password), st.session_state.username))
            conn.commit()

          st.session_state.password = new_password  # Update session state after hashing
          
          st.success("Profile updated successfully!")

        if st.button("Sign Out"):
          sign_out()
          st.switch_page("login.py")

    else:
      st.info("You are currently in guest mode!")
      if st.button("Sign In Now"):
        sign_out()
        st.switch_page("login.py")
