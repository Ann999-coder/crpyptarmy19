import os
Rec_Id='7510625756'
User_iD='8129432735'


fs=os.listdir(os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD)
print(fs)

for x in fs:
    print(x)