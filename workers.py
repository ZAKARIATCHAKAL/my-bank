import re
import random
import sys

class Workers:
    def __init__(self,full_name,cart_ID,salary,number_phone,job,password):
        self.full_name=full_name
        self.cart_ID=cart_ID
        self.number_phone=number_phone
        self.job=job
        self.password=password
        self.salary=salary

    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self,n_name):
        if match:=re.search(r"^(\w)+ (\w)+$",n_name):
            self._full_name=n_name
        else:
            raise ValueError

    @property
    def cart_ID(self):
        return self._cart_ID
    @cart_ID.setter
    def cart_ID(self,car_id):
        if len(str(car_id)) !=8 :
            raise ValueError
        else:
            self._cart_ID=car_id

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,change_salary):
        if change_salary<0 or change_salary>100000 :
            raise ValueError
        else:
            self._salary=change_salary
    @property
    def number_phone(self):
        return self._number_phone
    @number_phone.setter
    def number_phone(self,num_ph):
        if mutch:=re.search(r"^\+213 (\d){3} (\d){3} (\d){3}$",num_ph) :
            self._number_phone=num_ph
        else:
            raise ValueError

    @property
    def job(self):
        return self._job
    @job.setter
    def job(self,jo):
        if jo not in ["manager","cashier","accountant","security"]:
            raise ValueError
        else:
            self._job=jo

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,pas_wor):
        lis_pass=[{"job":"manager","passord":"112134"},{"job":"accountant","passord":"123496"},{"job":"cashier","passord":"987356"},{"job":"security","passord":"321478"}]
        dam=False
        for i in lis_pass:
            if pas_wor==i["passord"] :
                dam=True
                self._password=pas_wor
        if dam==False:
           raise ValueError



def new_worker():
 """Authenticates manager access to register a new bank employee.

    Prompts for the manager's password, generates a unique 8-digit cart_ID,
    assigns job roles and default security passwords, collects salary/contact
    information, and constructs a new worker record.

    Returns:
        Workers: A newly initialized Workers object containing the registered employee details.
 """
 while True:
        frg=False
        ctrl=False
        check_password=input("Enter the password of the manager to check: ")
        for i in range(3):
           if check_password=="112134":
             ctrl=True
             nam=input("name: ")
             car_ID=""
             for g in range(8):
               cvb=random.randint(1,9)
               cvb=str(cvb)
               car_ID+=cvb
             lis_pass=[{"job":"manager","passord":"112134"},{"job":"accountant","passord":"123496"},{"job":"cashier","passord":"987356"},{"job":"security","passord":"321478"}]
             print(f"your cart_ID is: {car_ID}")
             dfg=False
             while True:
                 try:
                    cvb=False
                    jb=input("your job :")
                    for i in lis_pass:
                       if jb==i["job"]:
                          ps=i["passord"]
                          print(f"your password is : {i['passord']}")
                          dfg=True
                          cvb=True
                          break
                    if dfg==False:
                       raise ValueError
                    else:
                       break
                 except ValueError:
                   jb=input("correct your job: ")
             while True:
                 try:
                   salar=int(input("your salary: "))
                   num_ph=input("your number phone: ")
                   break
                 except ValueError:
                    salar=int(input("the salary or the number phone is false\nEnter salary:"))
                    num_ph=input("Enter number phone")
             try:
                return Workers(nam,car_ID,salar,num_ph,jb,ps)
             except ValueError :
                print("correct your information")
           else:
               check_password=input("your password is false!!\nEnter again: ")
           if ctrl==True:
              break

def Accountant_work(ls_work,ls,name,car_id):
    """Provides accounting reports regarding aggregate bank balances or total active customer debts.

    Authenticates the accountant using their name, cart_ID, and password before calculating
    and displaying total financial metrics across all registered client accounts.

    Args:
        ls_work (list): List of registered Workers objects.
        ls (list): List of registered Client objects.
        name (str): Full name of the accountant.
        car_id (str): Cart ID number of the accountant.
    """
    for work in ls_work:
     python=False
     if name==work.full_name and car_id==work.cart_ID:
        python=True
        for i in range(5):
           sdf=False
           check_password=input("Enter password: ")
           if check_password==work.password:
             question=input("what are you need:\n1)number the balance in the bank\n2)number the debts in the bank\nEnter your choise: ")
             while True:
               if question=="number the balance in the bank":
                   num_bal_bank=0
                   for client in ls:
                       num_bal_bank+=client.balance
                   print(f"the number of balance in the bank: {num_bal_bank}")
                   sdf=True
                   break
               elif question=="number the debts in the bank":
                   num_deb_bank=0
                   for client in ls :
                       num_deb_bank+=client.debts
                   print(f"the number debts in the bank is: {num_deb_bank}")
                   sdf=True
                   break
               else:
                   question=input("---your request is incorrect or unavailable---")
           if sdf==True:
               break
    if python==False:
        print("no worker with this name and cart_ID")

def managment(ls_work,ls_client):
    """Executes managerial administrative operations and high-level banking control.

    Allows authenticated management to generate system reports (client statistics,
    staffing/payroll breakdowns), update existing employee records, or safely terminate the program.

    Args:
        ls_work (list): List of registered Workers objects.
        ls_client (list): List of registered Client objects.
    """
    while True:
      check_password=input("Enter password:")
      if check_password=="112134":
         request=input("---How can we help you sir---\n1)see report about client\n2)see report about workers\n3)change data of workers\n4)end the programe\nEnter:")
         if request=="see report about client":
            number_client=0
            number_balance_client=0
            number_debts_client=0
            for client in ls_client:
               number_client+=1
               number_balance_client+=client.balance
               number_debts_client+=client.debts
            print(f"----------------------------------------------------\nthe number of the client in the bank:{number_client}\nthe balance in all the bank:{number_balance_client}\nthe number of debts in all the bank:{number_debts_client}\n------------------------------------------------------")
            break
         elif request=="see report about workers":
            number_workers=0
            all_salary=0
            number_work_security=0
            number_work_accountant=0
            number_work_cashier=0
            for work in ls_work:
               number_workers+=1
               all_salary+=work.salary
               if work.job=="security":
                  number_work_security+=1
               elif work.job=="cashier":
                  number_work_cashier+=1
               elif work.job=="accountant":
                  number_work_accountant+=1
            print(f"-------------------------------------------------------------------------\nthe number of workers: {number_workers}\nthe salary of all workers: {all_salary}\nthe number of works in security: {number_work_security}\nthe number of works in Accounting:{number_work_accountant}\nthe number cashiers:{number_work_cashier}------------------------------------------------------------------------ ")
            break
         elif request=="change data of workers":
            print("Enter this information: ")
            name_work=input ("Enter the name of worker: ")
            num_account=input("Enter cart_ID number: ")
            for w in ls_work:
               stope_5=False
               if w.full_name==name_work and num_account==w.cart_ID :
                  change_data=input("what wloud yu change:\n1)name\n2)cart_ID number\n3)number_phone\n4)password\n5)salary")
                  if change_data=="name":
                     while True:
                        try:
                           w.full_name=input("enter the new name: ")
                           stope_5=True
                           break
                        except ValueError:
                           print("the name is false!!!")
                  elif change_data=="cart_ID number":
                     while True:
                        try:
                           w.cart_ID=input("enter the new cart_ID number: ")
                           stope_5=True
                           break
                        except ValueError:
                           print("the cart_ID number you entered false!!")
                  elif change_data=="number_phone":
                     while True:
                       try:
                           w.number_phone=input("enter the new number phone: ")
                           stope_5=True
                           break
                       except ValueError:
                          print("this number_phone is false!!!")
                  elif change_data=="password":
                     while True:
                       check_2=input("this is very sensitive so for that enter the password again: ")
                       stt=False
                       if check_2=="112134":
                         while True:
                           try:
                              w.password=input("Enter the new password: ")
                              stt=True
                              stope_5=True
                              break
                           except ValueError:
                              print("this password not available!!")
                       if stt==True :
                           break
                  elif change_data=="salary":
                     while True:
                        try:
                           w.salary=int(input("Enter the new salary: "))
                           stope_5=True
                           break
                        except ValueError:
                           print("this salary is false: ")
               if stope_5==True :
                  break
         elif request=="end the programe":
            while True:
              check_ps=input("Enter the password for security:")
              if check_ps=="112134":
                 sys.exit("the programe End")
              else:
                 print("the password is false!!")

















