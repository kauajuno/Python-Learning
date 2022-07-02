class User:

    def __init__(self, username):
        self.name = username
        self.followers = 0
        self.following = 0

    def mutual(self, user):
        self.followers += 1
        self.following += 1


user1 = User(input("What's the username"))
user2 = User(input("What's the username"))

