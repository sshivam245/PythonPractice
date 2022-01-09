class human:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

    def __repr__(self):
        return f" human named {self.first} {self.last}"

    def __len__(self):
        return self.age
    
s=human("shivam", "goel", 19)
print(s, len(s))