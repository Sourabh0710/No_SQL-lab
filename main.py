import streamlit as st
from crud import add_user, get_users, update_user, delete_user

def main():
    st.title("User Management App")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Add User")
        username = st.text_input("Username")
        email = st.text_input("Email")
        if st.button("Add"):
            add_user(username, email)
            st.success("User added successfully!")

    elif choice == "Read":
        st.subheader("View Users")
        users = get_users()
        for user in users:
            st.write(f"Username: {user['username']}, Email: {user['email']}")

    elif choice == "Update":
        st.subheader("Update User")
        users = get_users()
        selected_user = st.selectbox("Select a user", [user["username"] for user in users])
        new_username = st.text_input("New Username")
        new_email = st.text_input("New Email")
        if st.button("Update"):
            update_user(selected_user, new_username, new_email)
            st.success("User updated successfully!")

    elif choice == "Delete":
        st.subheader("Delete User")
        users = get_users()
        selected_user = st.selectbox("Select a user", [user["username"] for user in users])
        if st.button("Delete"):
            delete_user(selected_user)
            st.success("User deleted successfully!")

if __name__ == "_main_":
    main()