class myClass:
    __privatevar = 27

    def __privmeth(self):
        print("I'm inside myclass")

    def hello(self):
        print("Private Variable values:" , myClass. __privatevar)



foo = myClass()
foo.hello()
foo.__privatevar