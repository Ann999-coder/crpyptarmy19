import os
from PIL import Image

entries = os.listdir(os.getcwd() + "\\" + "8129432735" + "\\" + "recieve" + "\\" + "9847531780")


file_count=0
for x in entries:
    file_count= file_count+1
    print(x)
print("file count:",file_count)




fname=str(file_count)

if file_count==0:
    fname=str(1)
else:
    pk=(file_count//2) +1
    fname=str(pk)

print("F Name......:",fname)
text_file=os.getcwd() + "\\" + "8129432735" + "\\" + "recieve" + "\\" + "9847531780"+ "\\"+ str(fname)+".txt"
image_file=os.getcwd() + "\\" + "9847531780" + "\\" + "send" + "\\" + "8129432735" + "\\" + str(fname) + ".png"
rec_file=os.getcwd() + "\\" + "8129432735" + "\\" + "recieve" + "\\" + "9847531780"+ "\\"+ str(fname)+ ".png"

f= open(text_file,"w+")
#f1= open(rec_file,"w+")

img = Image.new('RGB', (60, 30), color='red')
img.save(image_file)
img.save(rec_file)