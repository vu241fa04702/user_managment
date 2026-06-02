"""
class UserManagement:
    def __init__(self, user_name=None, user_email=None, address=None, phone=None, gender=None):
        self.__user_name = user_name
        self.__user_email = user_email
        self.address = address
        self.phone = phone
        self.gender = gender

    def get_user_name(self):
        return self.__user_name
    def set_user_name(self, name):
        self.__user_name = name
    def get_user_email(self):
        return self.__user_email
    def set_user_email(self,mail):
        self.__user_email = mail
    def get_user_address(self):
        return self.address
    def set_user_address(self, address):
        self.address = address
    def get_user_phone(self):
        return self.phone
    def set_user_phone(self,phone):
        self.phone=phone


# Creating objects correctly
user_management = UserManagement("ram","ram@gmail.com","guntur","9087")
user_management1 = UserManagement("amit","amit@gmail.com","vijaywada","09876")

print(user_management.get_user_name())
print(user_management1.get_user_email())
print(user_management1.get_user_address())
print(user_management1.get_user_phone())
"""
class UserManagement:
    def __init__(self, user_name=None, user_email=None, address=None, phone=None, gender=None):
        self.__user_name = user_name
        self.__user_email = user_email
        self.address = address
        self.phone = phone
        self.gender = gender

    def get_user_name(self):
        return self.__user_name
    def set_user_name(self, name):
        self.__user_name = name

    def get_user_email(self):
        return self.__user_email

    def set_user_email(self, mail):
        self.__user_email = mail

    def get_user_address(self):
        return self.address

    def set_user_address(self, address):
        self.address = address

    def get_user_phone(self):
        return self.phone

    def set_user_phone(self, phone):
        self.phone = phone
    def add_user(self):

        """
        take all atributes
        """

        user_name=input("enter your name:  ")
        user_email = input("enter your email:  ")
        address = input("enter your address:  ")
        phone = input("enter your phone:  ")
        user_obj=UserManagement(user_name,user_email,address,phone)
        user_data.append(user_obj)
        print("user added successfully:::")
       # print(user_data[0].get_user_name())

    def view_all_users(self):
        """
        this function displays the data
        :return:
        """
        print("user data :::\n\n\n")
        for i in user_data:
            print("user name: ",i.get_user_name(),"\n"
            "user email: ", i.get_user_email() ,"\n"
            "user address: ", i.get_user_address(),"\n"
            "user phone: ", i.get_user_phone())

    def update_user(self):
        user_email = input("enter your email: ")

        for i in user_data:
            if i.get_user_email() == user_email:
                print("please enter new details")

                i.set_user_name(input("enter new user name: "))
                i.set_user_email(input("enter new email: "))
                i.set_user_address(input("enter new address: "))
                i.set_user_phone(input("enter new phone: "))

                print("user updated successfully")
                break
        else:
            print("user not found")

    def delete_user(self):
        user_email = input("enter user email to delete: ")

        for i in user_data:
            if i.get_user_email() == user_email:
                user_data.remove(i)
                print("user deleted successfully")
                break
        else:
            print("user not found")


if __name__ == "__main__":
    print("welcome")
    user_data=list()
    user_management=UserManagement()
    while True :
        print("1. add users \n"
             "2. view all users\n"
             "3. add users \n"
             "4. view all users\n"
             "5. Exit")

        option=int(input("please select: "))
        if option==1:
              user_management.add_user()
        elif option==2:
              user_management.view_all_users()
        elif option==3:
            user_management.update_user()
        elif option==4:
            user_management.delete_user()
        elif option==5:
            pass
        else:
            print("please select a valid option")
