class User:

    def __init__(self, userid: int, username):
        self.id = userid
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, 'waqas')
user_2 = User(2, 'saad')
print(user_1.name, user_2.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

