class user:
    active_user=0
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
        user.active_user+=1

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]} {self.last[0]}"
    
    def is_senior(self):
        return self.age <=65

    

user1= user("shivam", "goel", 19)
user2= user("sidhant","goyal", 22)


print(user.active_user)
print(user1.full_name(),user2.full_name())
print(user1.initials(),user2.initials())
print(user2.is_senior(),user1.is_senior())
print(user.active_user)
        

