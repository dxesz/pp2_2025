# Directories

# # 1
# import os
# path=os.getcwd()
# os.chdir('\\Users\\Сырым\\OneDrive\\Desktop\\Lab 5')
# l=os.listdir()
# for i in l:
#     if os.path.isfile(i): # isdir for directories
#         print(i)


# # 2
# import os
# #path=os.getcwd()
# path='\\Users\\Сырым\\OneDrive\\Desktop\\Lab 5'
# l=os.listdir()
# def f(path):
#     if not os.path.exists(path):
#         print(f"{path} does not exist")
#         return
    
#     if os.access(path, os.R_OK):
#         print(f"{path} is readable")
#     else:
#         print(f"{path} is not readable")


#     if os.access(path, os.W_OK):
#         print(f"{path} is writable")
#     else:
#         print(f"{path} is not writable")
    

#     if os.access(path, os.X_OK):
#         print(f"{path} is executable")
#     else:
#         print(f"{path} is not executable")

# f(path)


# # 3
# import os
# path='\\Users\\Сырым\\OneDrive\\Desktop\\Lab 5'
# def f(path):
#     if os.path.exists(path):
#         print(f"{path} exists")

#         d=os.path.dirname(path)
#         print(f"{d} is a directory portion")

#         f_n=os.path.basename(path)
#         print(f"{f_n} is a filename")
#     else:
#         print("The file does not exists")

# f(path)


# # 4
# with open('ex2.txt','r') as f:
#     l=f.readlines()
#     print(len(l))


# # 5
# l=["red","blue","green","black"]
# with open('ex.txt','w') as f:
#     for i in l:
#         f.write(str(i)+"\n")


# # 6
# for i in range(26):
#     name=chr(65+i)+'.txt'
    
#     with open(name,'w') as f:
#         f.write(f"This is a file named {name}")


# # 7
# with open ('ex.txt','r') as f:
#     l=f.readlines()
# with open('ex2.txt','a') as f:
#     for i in l:
#         f.write(i)


# # 8
# import os
# path='\\Users\\Сырым\\OneDrive\\Desktop\\Lab 6\\examples'
# def f(path):
#     if os.path.exists(path):
#         l=os.listdir(path)
#         for i in l:
#             fullName=os.path.join(path,i)
#             if os.path.isfile(fullName): # isdir for directories
#                 os.remove(fullName)
#     else:
#         print("The file does not exists")

# f(path)