import re
import re
import random

class Client:
    def __init__(self,full_name,date_birth,number_account,number_phone,balance,password,debts):

        self.full_name = full_name
        self.date_birth = date_birth
        self.number_account = number_account
        self.number_phone = number_phone
        self.balance=balance
        self.password=password
        self.debts=debts
    def __str__(self):
       return f"hello {self._full_name} your balance is :{self._balance}"

    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self,name):
        if match:=re.search(r"^\w+ \w+$",name):
            self._full_name=name
        else:
            raise ValueError
    @property
    def date_birth(self):
       return self._date_birth
    @date_birth.setter
    def date_birth(self,date):
       if match:=re.search(r"^(\d{4})/(\d{2})/(\d{2})$",date):
          year,month,day=match.groups()
          if int(year)>2026 or int(year)<1900:
             raise ValueError
          else:
             if int(month)>12 or int(month)<1:
                raise ValueError
             else:
                if int(day)>30 or int(day)<1:
                   raise ValueError
                else:
                   self._date_birth=date
       else:
          raise ValueError

    @property
    def number_account(self):
       return self._number_account
    @number_account.setter
    def number_account(self,num_acc):
       if len(num_acc)!=20:
          raise ValueError
       else:
          self._number_account=num_acc

    @property
    def number_phone(self):
       return self._number_phone
    @number_phone.setter
    def number_phone(self,num_ph):
       if match:=re.search(r"^\+213 (\d){3} (\d){3} (\d){3}$",num_ph):
          self._number_phone=num_ph
       else:
          raise ValueError
    @property
    def balance(self):
       return self._balance
    @balance.setter
    def balance(self,new_balance):
       if new_balance<0:
          raise ValueError
       else:
          self._balance=new_balance
    @property
    def password(self):
       return self._password
    @password.setter
    def password(self,new_pass):
       sdf=new_pass
       if len(sdf)!=6:
          raise ValueError
       else :
          self._password=new_pass
    @property
    def debts(self):
      return self._debts
    @debts.setter
    def debts(self,num_debts):
      if num_debts<0 :
         raise ValueError
      else:
         self._debts=num_debts
    def borrowing(self,num_brrowing):
      if num_brrowing<0:
         raise ValueError
      else:
         self._debts+=num_brrowing


    def deposit(self,num_d):
       if num_d<0:
          raise ValueError
       else:
          self._balance+=num_d
    def withdraw(self,num_w):
       if num_w>self._balance or num_w<0:
          raise ValueError
       else:
          self._balance=self._balance-num_w


def new_client():
  """Creates a new client account, collects basic personal details, and generates
    a unique 20-digit account number and a 6-digit password.

    Returns:
        Client: A new Client object initialized with the provided personal details
        and generated account credentials.
  """
  print("-----first we get information-----")
  while True:
    full_nam=input("name must be like 'f.name' 's.name': ")
    date_birt=input("date of birth ,must be like '2003/04/03': ")
    number_phon=input("number phone must be like'+213 564 432 590': ")
    lis=[]
    for i in range(20):
       sdf=random.randint(1,9)
       sdf=str(sdf)
       lis.append(sdf)
    st=""
    for a in lis:
     st+=a
    number_accoun=st
    print(f"your number account is :{number_accoun}")
    cfg=""
    for t in range(6):
       dfg=random.randint(1,9)
       dfg=str(dfg)
       cfg+=dfg
    passwor=(cfg)
    print(f"your password is :{passwor}\n you must save and enter the password to perfome account transaction")
    balance=0
    debts=0
    try:
       client= Client(full_nam,date_birt,number_accoun,number_phon,balance,passwor,debts)
       break
    except ValueError:
       print("correct your data:")
  return client


def client_deposit(ls,nam,number_A,depos):
   """Handles depositing money into a client's account following password authentication.

    Args:
        ls (list): The list of registered Client objects in the bank.
        nam (str): Full name of the client receiving the deposit.
        number_A (str): Account number of the target client.
        depos (int or float): The initial amount to deposit into the account.
    """
   stope_3=False
   for clie in ls :
      if clie.full_name==nam and clie.number_account==number_A :
         stope_3=True
         i=0
         while i<3:
            password=input("Enter password(you have three attempts to ensure security): ")
            if password==clie.password:
               while True:
                 try:
                   clie.deposit(depos)
                   print("------the operation end------")
                   Question=input(f"do you want see your balance(yes/no):")
                   break
                 except ValueError:
                    print("--You entered the wrong balance!!")
                    depos=int(input("Enter the balance: "))
               if Question=="yes":
                  print(f"your balance is {clie.balance}")
               break
            i+=1
         if i==3:
            print("--------------you can't enter-------------")
            print("go to problem Office to reset your password ")
      if stope_3==True:
         break
   if stope_3==False:
      print("there is no one in the bank with this data")


def withdraw_client(ls,nam,number_A,withd):
   """Executes a fund withdrawal from a client's account after security verification.

    Args:
        ls (list): The list of registered Client objects.
        nam (str): Full name of the client making the withdrawal.
        number_A (str): Account number of the client.
        withd (int or float): The amount to withdraw.
   """
   wt=False
   for clie in ls :
      if clie.full_name==nam and clie.number_account==number_A:
         wt=True
         i=0
         while i<3:
            check_password=input("Enter password(you have three attempts to ensure security): ")
            i+=1
            if check_password==clie.password:
                try:
                  clie.withdraw(withd)
                  print("------the operation end------")
                  Question=input("do you want see your balance(yes/no):")
                  if Question=="yes":
                   print(f"your balance: {clie.balance}")
                   break
                except ValueError :
                   v=0
                   while v<2:
                     v+=1
                     try:
                       new_withd=int(input("--You entered the wrong balance!!\n Enter the balance again"))
                       clie.withdraw(new_withd)
                       break
                     except ValueError:
                        pass
         if i==3 :
            print("--------------you can't enter-------------")
            print("go to problem Office to reset your password")

      if wt==True:
        break

   if wt==False:
      print("no one in the bank with this data!!")

def transfer_client(ls,name_tran,number_account_tr,name_received,number_account_received,number_balance):
   """Transfers funds between two valid bank accounts after authenticating the sender.

    Args:
        ls (list): The list of registered Client objects.
        name_tran (str): Full name of the sender.
        number_account_tr (str): Account number of the sender.
        name_received (str): Full name of the recipient.
        number_account_received (str): Account number of the recipient.
        number_balance (int or float): The amount to transfer.
    """
   stope_4=False
   for search in ls :
      if search.full_name == name_tran and number_account_tr== search.number_account :
         for search_2 in ls :
            if search_2.full_name== name_received and search_2.number_account == number_account_received :
                stope_4=True
                n=0
                for i in range(3):
                     stop=False
                     check_password=input("Enter password(you have three attempts to ensure security): ")
                     if check_password== search.password:
                       while n<3:
                        n+=1
                        try:
                           stop=False
                           search.withdraw(number_balance)
                           search_2.deposit(number_balance)
                           print("------the operation end------")
                           Question=input("do you want see your balance(yes/no):")
                           stop=True
                           break
                        except ValueError:
                           number_balance=int(input("----The balance you entered is false----\nBalance: "))
                       if Question=="yes":
                            print(f"your balance: {search.balance}")
                     if stop==True :
                        break
   if stope_4==False:
      print(" there is data is wrong check the information and enter again")



def borrowing_client(ls,name,number_account,balance_brrowing):
   """Processes an interest-free loan request, updating debt and account balance.

    Args:
        ls (list): The list of registered Client objects.
        name (str): Full name of the borrowing client.
        number_account (str): Account number of the borrower.
        balance_brrowing (int or float): The requested loan amount.
    """
   for client in ls :
      if client.full_name == name and client.number_account==number_account :
         for i in range(3):
            stop=False
            check_password=input("Enter passsword:(you have three attempts to ensure security)")
            if check_password==client.password:
               cse=0
               for s in range(3):
                  try:
                     client.borrowing(balance_brrowing)
                     client.deposit(balance_brrowing)
                     print("------the operation end------")
                     Question=input("do you want see your balance(yes/no):")
                     if Question=="yes":
                        print(f"your balance: {client.balance}")
                     stop=True
                     break
                  except ValueError:
                    balance_brrowing=int(input("----The balance you entered is false----\nBalance: "))
            if stop==True:
                  break
def change_information(ls,name,number_account):
    """Allows authenticated clients to update profile attributes like name, DOB, phone, or password.

    Args:
        ls (list): The list of registered Client objects.
        name (str): Current full name of the client.
        number_account (str): Account number of the client.
    """
    for client in ls:
       if client.full_name==name and client.number_account==number_account :
           for i in range(3):
              check_password=input("Enter password(you have three attempts to ensure security): ")
              if check_password==client.password :
                 list_change=["full_name","date_birth","number_phone","password"]
                 for dfg in range(4):
                    Question=input("what wloud you change: \n1)full_name\n2)date_birth\n3)number_phone\n4)password\nEnter your choise: ")
                    change_data=input("Enter the new information:")
                    for sdf in range(3):
                         stop_1=False
                         if Question not in list_change:
                            Question=input("this change request is unavaible or invalid!!\nEnter your choise again:")
                         else:
                            if Question=="full_name":
                              for we in range(3):
                                 try:
                                    client.full_name=change_data
                                    stop_1=True
                                    break
                                 except ValueError:
                                    print("the name you entered false!!")
                            if stop_1==True:
                              break
                            if Question=="date_birth":
                               stop_1=False
                               for tyu in range(3):
                                  try:
                                      client.date_birth=change_data
                                      stop_1=True
                                      break
                                  except ValueError:
                                     print("the date_birth you entered to change is  false")
                                     change_data=input("Enter date_birth again: ")
                            if stop_1==True:
                             break
                            if Question =="number_phone":
                              for iop in range(3):
                                try:
                                   client.number_phone=change_data
                                   stop_1=True
                                   break
                                except ValueError:
                                     print("the number_phone you entered to change is false")
                                     change_data=input("Enter number_phone again: ")
                            if stop_1==True:
                              break
                            if Question=="password":
                               stop_1=False
                               for asd in range(3):
                                  try:
                                     client.password=change_data
                                     stop_1=True
                                     break
                                  except ValueError:
                                     print("the password  you entered to change is false")
                                     change_data=input("Enter password again: ")
                            if stop_1==True:
                               break

def paying_of_debts(ls,name,num_acc,pay):
   for client in ls:
      if client.full_name==name and client.number_account==num_acc:
         for i in range(3):
            stop=False
            check_password=input("Enter password(you have three attempts to ensure security): ")
            if check_password==client.password:
               if pay>client.debts:
                  answer=input("the balance you enter great then your debts wloud you Top up the remaining balance in your account(yes/no)?: ")
                  if answer=="yes":
                     pay_debts=client.debts-pay
                     client.debts=0
                     pay_debts*=-1
                     client.deposit(pay_debts)
                     stop=True
                     break
                  else:
                     pay=int(input(f"your debts is {client.debts} enter the balance wloud you pay:"))
                     client_debts=client.debts-pay
                     stop=True
                     break
               else:
                  client.debts-=pay
                  print("----the operation end----")
                  stop==True
                  break
            if stop==True:
               break

def see_account(ls,account_number):
   for client in ls :
      if client.number_account==account_number:
         for i in range(3):
             check_password=input("Enter password: ")
             if client.password==check_password:
                print(client)
                break
             else:
                print("--------the password is false--------")





















