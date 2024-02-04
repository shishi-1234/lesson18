class Person:
    def say(self, message):
        print(message)
    def say_hello(self):
        self.say('hello work')
tom = Person()
tom.say_hello()