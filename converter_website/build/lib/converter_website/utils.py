import pickle


def get_users():
    users_file = open("users_file", "rb")
    try:
        users = pickle.load(users_file)
    except:
        import pdb;pdb.set_trace()
    username_table = {u.username: u for u in users}
    return username_table


class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}
