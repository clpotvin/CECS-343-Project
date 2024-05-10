import pandas as pd
import os
from .user import User

users_f = os.getcwd() + '/CECS-343-Project/code/Data/Users.csv'


class UserController:
    """Class that contains all User accounts.

        Attributes:
            user_data (DataFrame): A pandas dataframe containing user account info (from csv)
            users (list): A list containing User objects
    """

    def __init__(self):
        """Initialize all class data members."""
        self.user_data = pd.read_csv(users_f)
        self.users = [User(n[0] + ' ' + n[1], n[4]) for n in self.user_data.values]
        self.current_user = None

    def new_user(self, d):
        """Create a new user account."""
        if d[2] not in self.user_data.values:
            temp = User((d[0][0] + ' ' + d[0][1]))
            temp.generate_uuid()
            arr = d
            arr.append(temp.uuid)
            arr = [arr]

            df = pd.DataFrame.from_records(arr, columns=["First Name", "Last Name", "Username", "Hashed Password", "UUID"])
            self.user_data = pd.concat([self.user_data, df])
            self.user_data.to_csv(users_f, mode='w', index=False)
            self.users.append(temp)
            return True
        else:
            return False

    def is_valid(self, username, password):
        """Check if login credentials are valid.
        Returns:
            bool: True if valid, False if not valid.
        """
        if username in self.user_data.values:
            for x in self.user_data.values:
                if x[2] == username:
                    if x[3] == password:
                        self.current_user = self.find_by_username(username)
                        return True
                    else:
                        return False
        return False

    def find_by_username(self, username):
        """Find and return a User object by username
        Returns:
            User/bool: Returns a User object if the User exists, else return False.
        """
        for x in self.user_data.values:
            if x[2] == username:
                name = x[0] + ' ' + x[1]
                for y in self.users:
                    if y.get_name() == name:
                        return y
        return False

    def get_user_data(self):
        """Returns the user_data dataframe."""
        return self.user_data

    def update_user(self, fname, lname, uname, passwd, uuid, old_uname):
        """Update a user account."""
        user = self.find_by_username(old_uname)
        if user in self.users:
            self.users[self.users.index(user)].set_name(fname + ' ' + lname)
            self.users[self.users.index(user)].set_uuid(int(uuid))
        if old_uname in self.user_data.values:
            idx = self.user_data['Username'].tolist().index(old_uname)
            self.user_data.loc[idx, 'First Name'] = fname
            self.user_data.loc[idx, 'Last Name'] = lname
            self.user_data.loc[idx, 'Username'] = uname
            self.user_data.loc[idx, 'Hashed Password'] = passwd
            self.user_data.loc[idx, 'UUID'] = int(uuid)
            self.user_data.to_csv(users_f, mode='w', index=False)

    def delete_user(self, username):
        """Delete a user from the database and remove it from the User object list."""
        user = self.find_by_username(username)
        if not user:
            return

        idx = self.users.index(user)
        df = self.user_data
        df = df.drop(idx)
        self.user_data = df
        self.user_data.to_csv("CECS-343-Project/code/Data/Users.csv", mode='w', index=False)
        self.users.pop(idx)

