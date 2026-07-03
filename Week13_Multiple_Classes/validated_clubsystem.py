class ClassMembership:
    membership_counter = 1000

    def __init__(self, student_ID_number, student_last_name, student_programmme):
        self.student_ID_number = student_ID_number
        self.student_last_name = student_last_name
        self.student_programmme = student_programmme

        self.membership_number = ClassMembership.membership_counter
        ClassMembership.membership_counter += 1


class ClubSystem:
    def __init__(self):
        self.members = []

    def register_student(self):
        print("=registration=")
        while True:
            student_ID_number = input("Enter student ID number: ")
            if student_ID_number.isdigit():
                if len(student_ID_number)==4:
                    if student_ID_number.strip()!='':
                        for member in self.members:
                            if student_ID_number == member.student_ID_number:
                                print("Student ID already exists")
                                break
                        student_last_name = input("Enter student last name: ")
                        student_programmme = input("Enter student programme: ")

                        member_info = ClassMembership(student_ID_number, student_last_name, student_programmme)
                        self.members.append(member_info)
                    else:
                        print("Student ID number cannot be empty")
                else:
                    print("Student ID number should be 4 digits")
            elif not student_ID_number.isdigit():
                print("Student ID Number Should Be Numeric")
            else:
                print("Invalid Input")


            print("Student", student_ID_number, "has been added with membership ID", member_info.membership_number)

    def withdraw_student(self):
        print("=withdraw=")
        membership_number = int(input("Enter membership number: "))
        student_last_name = input("Enter student last name: ")

        for member in self.members:
            if member.membership_number == membership_number and member.student_last_name == student_last_name:
                self.members.remove(member)
                print("Member removed successfully")
                return

        print("Membership number not found")

    def display_members(self):
        number_of_diploma = 0
        number_of_bachelors = 0

        print("Current membership counter:", ClassMembership.membership_counter)
        print("Total students registered:", len(self.members))

        for member in self.members:
            print("ID number:", member.student_ID_number)
            print("Last name:", member.student_last_name)
            print("Student programme:", member.student_programmme)
            print("Membership number:", member.membership_number)
            print()

            if member.student_programmme.lower() == "diploma":
                number_of_diploma += 1
            elif member.student_programmme.lower() == "bachelor":
                number_of_bachelors += 1

        print("Diploma:", number_of_diploma)
        print("Bachelor:", number_of_bachelors)



club = ClubSystem()

club.register_student()
club.register_student()

club.display_members()

club.withdraw_student()

club.display_members()