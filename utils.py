import streamlit as st

from  passlib.context import CryptContext
from schema import User, DB, MONGODB_USER_TABLE, MONGODB_WORK_TABLE

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def insert_user(user_info: User):
    if user_info["name"] in " ": 
        print("Delete space in username.")

    elif len(user_info["name"]) < 4:
        print("username larger than length 4")
    else:    
        username_found = DB[MONGODB_USER_TABLE].find_one({"name": user_info["name"]})
        if username_found:
            # st.error("This user already exists.")
            print(f"'{user_info['name']}' already exists.")
        else:
            print(f"'{user_info['name']}' not exists.")

            user_info["password"] = get_password_hash(user_info["password"])
            DB[MONGODB_USER_TABLE].insert_one(user_info)

def delete_user(user_info: User):
    username_found = DB[MONGODB_USER_TABLE].find_one({"name": user_info["name"]})
    if username_found:
        # if username_found["admin"]:
        #     st.warning
        DB[MONGODB_USER_TABLE].delete_one({"name": user_info["name"]})
        print(f"Delete {user_info['name']}")
    else:
        print(f"'{user_info['name']}' not exists.")

def get_user():
    user_list = []
    for user in DB[MONGODB_USER_TABLE].find({}):
        user_list.append(user)
    return user_list

if __name__ == "__main__":
    test = {"name": "", 
            "admin": False,
            "password": "1121"}
    delete_user(test)

    # test = {"name": "admin", 
    #         "admin": True,
    #         "password": "1121"}
    # insert_user(test)