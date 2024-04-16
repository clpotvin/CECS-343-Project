import pandas as pd
from user import User
import os

current_path = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(current_path, "../Data/Users.csv")

class UserController:

    def __init__(self):
        self.user_data = pd.read_csv(file)
        self.users = [User(n[0] + ' ' + n[1]) for n in self.user_data.values]

    def new_user(self, d):
        temp = User((d[0][0] + ' ' + d[0][1]))
        temp.generate_uuid()
        arr = d
        arr.append(temp.uuid)
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["First Name", "Last Name", "Username", "Hashed Password", "UUID"])
        self.user_data = pd.concat([self.user_data, df])
        self.user_data.to_csv(file, mode='w', index=False)
        self.users.append(temp)

    def is_valid(self, username, password):
        ud = self.user_data.values
        if username in self.user_data.values:
            for x in ud:
                if x[2] == username:
                    if x[3] == password:
                        return True
                    else:
                        return False
        return False
