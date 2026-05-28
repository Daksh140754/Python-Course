class Reverse:
    def __init__(self , s):
        self.s=s

    def reversestr(self):
        reversed_str=""
        for char in self.s:
            reversed_str=char + reversed_str
        return reversed_str
        
user_input=str(input("Ente ryour string:"))

e=Reverse(user_input)
print(e.reversestr())