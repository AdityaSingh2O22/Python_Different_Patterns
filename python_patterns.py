# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:08:58 2022

@author: Aditya Singh
 

"""
(1)

* 
* * 
* * * 
* * * * 
* * * * *

"""   
# for c in range (6):
#     for r in range(c+1):
#         print("#",end=" ")
#     print("\n")     

# def pattern(n,sign):
#     for i in range(n):
#         for j in range(i+1):
#             print(sign,end=" ")
#         print("\n")
#     print()    
# n=int(input("Enter the value of the N: "))    
# sign=input("Enter the sign of the pattern: ")

# pattern(n,sign)

"""
(2)

# # # # # 

# # # # 

# # # 

# # 

# 
   
"""
# n=int(input("Enter the vaulue of N: "))
# for i in range(n):
#     for j in range(n-i):
#         print("#",end=(" "))
#     print("\n")    
    
 
# def pattern(n,sign):
#     for i in range(n+1,0,-1):
#         for j in range(i-1):
#             print(sign,end=" ")
#         print("\n")

# n=int(input("Enter the value of N: "))
# sign=input("Enter the symbol: ")        
# pattern(n,sign)

"""
(3)

        # 

      # # # 

    # # # # # 

  # # # # # # # 
  
"""
# n=int(input("Enter the value of N: "))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")    

"""
(4)

            # 

          # # # # 

        # # # # # # # 

      # # # # # # # # # # 

    # # # # # # # # # # # # # 

  # # # # # # # # # # # # # # # # 
         
"""
# n=int(input("Enter the value of N: "))
# for i in range (n):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(3*i-2):
#         print("#",end=(" "))
#     print("\n")    

"""
(5)

# # # # # # # # # 

  # # # # # # # 

    # # # # # 

      # # # 

        # 
           
"""
# n=int(input("Enter the value of N: "))
# for i in range (n,0,-1):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")


"""
(6)

        # 

      # # # 

    # # # # # 

  # # # # # # # 

# # # # # # # # # 

  # # # # # # # 

    # # # # # 

      # # # 

        #
        
"""
# n=int(input("Enter the value of N: "))
# for i in range (n):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")
# for i in range (n,0,-1):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")

"""
(7)

# 

# # 

# # # 

# # # # 

# # # # # 

# # # # 

# # # 

# # 

#
 
"""
# n=int(input("Enter the value of N: "))
# for i in range (n):
#     for j in range(i+1):
#         print("#",end=(" "))
#     print("\n")
# for i in range (n,0,-1):
#     for j in range(i-1):
#         print("#",end=(" "))
#     print("\n")
    
"""
(8)

# # # # # # # # # 

  # # # # # # # 

    # # # # # 

      # # # 

        # 

          

        # 

      # # # 

    # # # # # 

  # # # # # # # 

# # # # # # # # # 

"""
# n=int(input("Enter the value of the N: "))
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ",end=(" "))
#     for k in range(2*i-1):
#         print("#",end=(" "))
#     print("\n")    

"""
(9)

  # 

    # # 

      # # # 

        # # # # 

          # # # # # 

            # # # # # # 

              # # # # # # # 

            # # # # # # 

          # # # # # 

        # # # # 

      # # # 

    # # 

  # 

"""

# for i in range(6):
#     for k in range(i+1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("#",end=(" "))
#     print("\n")    
# for i in range(6,-1,-1):
#     for k in range(i+1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("#",end=(" "))
#     print("\n")       
"""
(10)

              # # # # # # # 

            # # # # # # 

          # # # # # 

        # # # # 

      # # # 

    # # 

  # 

    # # 

      # # # 

        # # # # 

          # # # # # 

            # # # # # # 

              # # # # # # # 

"""    

# for i in range(6,-1,-1):
#     for k in range(i+1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("#",end=(" "))
#     print("\n")    
# for i in range(1,6+1):
#     for k in range(i+1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("#",end=(" "))
#     print("\n") 

"""
(11)

  #                                         # 

    # #                                 # # 

      # # #                         # # # 

        # # # #                 # # # # 

          # # # # #         # # # # # 

            # # # # # # # # # # # # 

            # # # # # # # # # # # # 

          # # # # #         # # # # # 

        # # # #                 # # # # 

      # # #                         # # # 

    # #                                 # # 

  #                                         # 

"""
# for i in range(6):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("#",end=(" "))
#     for l in range(6-i*2+4):
#         print(" ",end=(" "))    
#     for m in range(6-i*2+4):
#         print(" ",end=(" "))
#     for n in range(i+1):
#         print("#",end=(" "))        
#     print("\n") 

# for i in range(5,-1,-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("#",end=(" "))
#     for l in range(6-i*2+4):
#         print(" ",end=(" "))    
#     for m in range(6-i*2+4):
#         print(" ",end=(" "))
#     for n in range(i+1):
#         print("#",end=(" "))        
#     print("\n")     
    

