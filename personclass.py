class Person:
    def __init__(self, name, email, phone, friends):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = friends

    def greet(self, other_person):
         return('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_contact_info(self):
        return "{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone)



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", [])
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [])

jordan.friends.append("sonny")
sonny.friends.append("jordan")

# print(sonny.greet(jordan))
# print (jordan.greet(sonny))


# jordcont = jordan.email, jordan.phone
# print(jordcont)

# sonnycont = sonny.email, sonny.phone
# print(sonnycont)
# print (sonny.phone, sonny.email)

# print(sonny.print_contact_info())

print(sonny.friends)
