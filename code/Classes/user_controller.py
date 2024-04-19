import pandas as pd
from .user import User


class UserController:

    def __init__(self):
        self.user_data = pd.read_csv("CECS-343-Project/code/Data/Users.csv")
        self.users = [User(n[0] + ' ' + n[1], n[4]) for n in self.user_data.values]
        # debug
        # for x in self.users:
        #     x.display()

    def new_user(self, d):
        if d[2] not in self.user_data.values:
            temp = User((d[0][0] + ' ' + d[0][1]))
            temp.generate_uuid()
            arr = d
            arr.append(temp.uuid)
            arr = [arr]
            print(arr)

            df = pd.DataFrame.from_records(arr, columns=["First Name", "Last Name", "Username", "Hashed Password", "UUID"])
            self.user_data = pd.concat([self.user_data, df])
            self.user_data.to_csv("CECS-343-Project/code/Data/Users.csv", mode='w', index=False)
            self.users.append(temp)
            return True
        else:
            return False

    def is_valid(self, username, password):
        if username in self.user_data.values:
            for x in self.user_data.values:
                if x[2] == username:
                    if x[3] == password:
                        return True
                    else:
                        return False
        return False

    def find_by_username(self, username):
        for x in self.user_data.values:
            if x[2] == username:
                name = x[0] + ' ' + x[1]
                for y in self.users:
                    if y.get_name() == name:
                        return y
        return False

    def get_user_data(self):
        return self.user_data

    def update_user(self, fname, lname, uname, passwd, uuid):
        user = self.find_by_username(uname)
        if user in self.users:
            self.users[self.users.index(user)].set_name(fname + ' ' + lname)
            self.users[self.users.index(user)].set_uuid(uuid)
        if uname in self.user_data.values:
            idx = self.user_data['Username'].tolist().index(uname)
            print(self.user_data['Username'][idx])
