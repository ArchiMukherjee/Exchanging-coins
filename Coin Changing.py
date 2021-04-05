# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:24:47 2021

@author: Archi
"""

#Coin values are saved in a list called dict_
dict_=[.01,.05,.10,.25,.50,1.00,2.00, 5.00,10.00,20.00,50.00,100.00]
#Taking inputs as PP=Purchase Price CH=Cash payed by customer
PP, CH = [float(x) for x in input().split()]
print(PP,";",CH)


#amount=change value
amount = (CH-PP)
 
 
def findMin(amount):
     N=len(dict_)
     
     #initialize result
     lis_=[]
            
     # Traverse through dict_
     i=N-1
     while(i >=0):
         
         while(amount >= dict_[i]):
             amount-= dict_[i]
             lis_.append(dict_[i])
         
         i-=1
     #print result
     for i in range(len(lis_)):
         for j in range(len(lis_)):
                 if lis_[j] == 100.0:
                    lis_[j]=("HUNDRED")
                 elif lis_[j] == 50.0:
                    lis_[j]=("FIFTY")
                 elif lis_[j] == 20.0:
                    lis_[j]=("TWENTY")
                 elif lis_[j] == 10.0:
                    lis_[j]=("TEN")
                 elif lis_[j] == 5.0:
                    lis_[j]=("FIVE")
                 elif lis_[j] == 2.0:
                    lis_[j]=("TWO")
                 elif lis_[j] == 1.0:
                    lis_[j]=("ONE")
                 elif lis_[j] == .50:
                    lis_[j]=("HALF DOLLAR")
                 elif lis_[j] == .25:
                     lis_[j]=("QUARTER")
                 elif lis_[j] == .10:
                    lis_[j]=("DIME")
                 elif lis_[j] == .05:
                    lis_[j]=("NICKEL")
                 elif lis_[j] == .01:
                    lis_[j]=("PENNY") 
                    print(lis_[j])
     
         print(lis_[i],",",end="")
 
if (CH<PP):
     print("ERROR")
elif (CH == PP):
     print("ZERO")
else:
     findMin(amount)