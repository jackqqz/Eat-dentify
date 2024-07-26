import streamlit as st
from login import init_connection, get_cursor, update_user, make_hashes

def sign_out():
  st.session_state.logged_in = False
  st.session_state.username = None
  st.session_state.user_remarks = None
  # st.session_state.should_update_tab1 = True
  # st.session_state.should_update_tab2 = True

def display_profile():
  if st.session_state.logged_in:
    old_username = st.session_state.username
    new_username = st.text_input("New username:", st.session_state.username)
    new_password = st.text_input("New password:",
                                 st.session_state.password,
                                 type='password')
    new_remarks = st.text_area("New remarks:", st.session_state.user_remarks)

    st.write("---")
    # if st.button("Update Profile"):
    #     st.session_state.remarks = new_remarks
    #     st.session_state.username = new_username
    #     st.session_state.password = new_password

    #     update_user(old_username)
    #     st.success("Profile updated successfully!")

    # if st.button("Sign Out"):
    #     sign_out()
    #     st.switch_page("login.py")

    if st.button("Update Profile"):
      st.session_state.remarks = new_remarks
      st.session_state.username = new_username
      st.session_state.password = new_password

      update_user(old_username)
      conn = init_connection()
      c = get_cursor()
      
      # Update password separately if it has changed
      if new_password != st.session_state.password:
        c = get_cursor()
        c.execute("UPDATE users SET password = ? WHERE username = ?",
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
