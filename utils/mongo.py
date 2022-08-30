from utils.password import get_password_hash
from schema import User, Data, DB, MONGODB_USER_TABLE, MONGODB_DATA_TABLE

import datetime

# User function
def insert_user(user_info: User):
    if user_info["name"] in " ": 
        print("Delete space in username.")

    elif len(user_info["name"]) < 4:
        print("username larger than length 4")
    else:    
        username_found = DB[MONGODB_USER_TABLE].find_one({"name": user_info["name"]})
        if username_found:
            print(f"'{user_info['name']}' already exists.")
        else:
            print(f"'{user_info['name']}' not exists.")

            user_info["password"] = get_password_hash(user_info["password"])
            DB[MONGODB_USER_TABLE].insert_one(user_info)
    return username_found

def delete_user(user_info: User):
    username_found = DB[MONGODB_USER_TABLE].find_one({"name": user_info["name"]})
    if username_found:
        DB[MONGODB_USER_TABLE].delete_one({"name": user_info["name"]})
        print(f"Delete {user_info['name']}")
    else:
        print(f"'{user_info['name']}' not exists.")
    return username_found

def get_user():
    user_list = []
    for user in DB[MONGODB_USER_TABLE].find({}):
        user_list.append(user)
    return user_list

# For initialize
user_list = get_user()

if "admin" not in user_list:
    insert_user(
                {"name": "admin", 
                "admin": True,
                "password": "1121"}
                )

# Data Function
def insert_data(data_info: Data):
    scheme = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d"),
        "username": data_info["username"],
        "keyword": data_info["keyword"],
        "classname": data_info["classname"],
        "isdone": False,
        "data": [{"filename": filename, "status": "None"} for filename in data_info["data"]]
    }
    
    DB[MONGODB_DATA_TABLE].insert_one(scheme)

def update_data(data_info: Data):
    pass

def delete_data(data_info: Data):
    pass


if __name__ == "__main__":
    # test = {"name": "", 
    #         "admin": False,
    #         "password": "1121"}
    # delete_user(test)

    test = {"name": "admin", 
            "admin": True,
            "password": "1121"}
    insert_user(test)