

def superficial_design():
    print("---------hello in zaki bank---------")
    print("1)Customer Use\n2)Employee Use\n3)The rules and notes\n--In every input request don't enter the number and the symbol-- ")
    first_choise=input("Enter your choise:")
    ls=["Customer Use","Employee Use","The rules and notes"]
    for tyu in range(5):
     if first_choise not in ls:
        print("you must take one of the three choise:")
        first_choise=input("1)Customer Use\n2)Employee Use\n3)The rules and notes\nEnter your choise: ")
    return first_choise
def intermediate_design_client():
    print("----How we can help you----")
    second_choise_client=input("1)Deposit money\n2)Withdraw money\n3)Transfar money\n4)Open new account\n5)Borrowing money\n6)Take a look at our services\n7)Paying off debts\n8)See your account\n9)Change information\nEnter you choise: ")
    ls=["Deposit money","Withdraw money","Transfar money","Open new account","Borrowing money","Take a look at our services","Paying off debts","See your account","Change information"]
    for st in range(5):
       if second_choise_client not in ls:
        second_choise_client=input("you must take choise from those choises:\n1)Deposit money\n2)Withdraw money\n3)Transfar money\n4)Open new account\n5)Brrowing money\n6)Take a look at our services\n7)Paying off debts\n8)See your account\n9)Change information\nEnter you choise: ")
    return second_choise_client

def View_services():
    print("Hello in zaki Bank we provide for you a lot of services:\n--You can deposit money or withdraw from you account\n--You can without interest\n--You can transfer money to another account\n--We provide multiple layers of protection for your account and data\n--This bank is supported by the state ta assist vulnerable groups seeking an oppotunity to lanch projects and bring their ideas to life")
def the_rules():
    print("1) Please note: when entering data, do not include the number and the symbol following it—specifically the '(' character\n2) This bank employs very high security standards; entering the wrong password more than three times will cause the process to fail You will then need to visit the manager's office to recover or change the password after verifying your identity\n3) The manager is the only person authorized to modify the system code; please consult them regarding any issues.")

def workers_design():
     request=input("1)Accounting Department\n2)New Worker\n3)Managment Office\nEnter yuor choise: ")
     list_work=["Accounting Departement","New Worker","Managment Office"]
     for dfg in range(5):
       if request not in list_work:
        request=input("You must take choise from the three choise\n1)Accounting Department\n2)New Worker\n3)Managment Office")
     return request
