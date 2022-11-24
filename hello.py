# lobj='lisa'
# if lobj == 'lisa':
#      print(lobj)

# ed = {'bet': 'betania de canela', 'beta': 'otherrrr'}
# print(ed['bet'])

# acceso = {'userName': 'betania31', 'password': 'cane123', 'telephone': '22334455'}
# print(acceso['userName'])
# print(acceso['password'])
# print(acceso['telephone'])

# table = 2
# for num in range(1, 11):
#     print(str(table)+ 'x' + str(num) + '=' + str(table * num))

# # acceso = {0 : 'userName', 1: 'password', 2: 'numberId'}
# datos = []
# for dat in range(2, 12, 2):
#     datos.append(dat)
# print(datos)

# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    """ An abstract bank class

    [IMPLEMENT ME]
        1. This class must derive from class ABC
        2. Write a basicinfo() function that prints out "This is a generic bank" and
           returns the string "Generic bank: 0" 
        3. Define a second function called withdraw and keep it empty by
           adding the `pass` keyword under it. Make this function abstract by
           adding an '@abstractmethod' tag right above the function declaration.
    """
    ### YOUR CODE HERE
    def basicinfo(self):
        print('This is generic bank')
        return 'Generic bank: 0'

    @abstractmethod    
    def withdraw(self):
        pass
# Class Swiss
class Swiss(Bank):
    """ A specific type of bank than derives from class Bank

    [IMPLEMENT ME]
        1. This class must derive from class Bank
        2. Create a constructor for this class that initializes a class
           variable `bal` to 1000
        3. Implement the basicinfo() function so that it prints "This is the 
           Swiss Bank" and returns a string with "Swiss Bank: " (don't forget
           the space after the colon) followed by the current bank balance.

           For example, if self.bal = 80, then it would return "Swiss Bank: 80"

        4. Implement withdraw so that it takes one argument (in addition to
           self) that is an integer which represents the amount to be withdrawn
           from the bank. Deduct the withdrawn amount from the bank bal, print 
           the withdrawn amount ("Withdrawn amount: {amount}"), print the new
           balance ("New Balance: {self.bal}"), and return the new balance.

           Note: Make sure to verify that there is enough money to withdraw!  
                 If amount is greater than balance, then do not deduct any 
                 money from the class variable `bal`. Instead, print a 
                 statement saying `"Insufficient funds"`, and return the 
                 original account balance instead.
    """
    ### YOUR CODE HERE
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print('this is bank')
        return 'Swiss bakn:' + str(self.bal)

    def withdraw(self, amount):
        if amount > self.bal:
            print('insuficient funds')
            print('balance:', {self.bal})
        else:   
            self.bal -= amount
            print('withdraw amount:', { amount})
            print('New Balance:', {self.bal})
        return self.bal
# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()