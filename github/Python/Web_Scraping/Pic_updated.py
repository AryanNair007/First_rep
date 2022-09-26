import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
import urllib.request
from time import gmtime, sleep, strftime
from PIL import Image

"""
1. cheak if the pics are same 
    a) if they are same filename doesn't change prints file alredy downloaded 
    b) if not same filename change new pic downloads 
"""

def New_Download(index,times):
    if times!=0:
        filename= "{}. {}({})".format(index,todays_date,times)
        cloud_write("{} {} {} {}".format(index,todays_date,current_hour,times))
    else:
        filename= "{}. {}".format(index,todays_date)
        cloud_write("{} {} {} {}".format(index,todays_date,current_hour,0))

    res=requests.get('https://bing.wallpaper.pics/')
    soup=BeautifulSoup(res.text, 'html.parser')
    image_box=soup.find('a', {'class' : 'cursor_zoom'})
    image= image_box.find('img')
    link=image['src']

    print(filename)
    urllib.request.urlretrieve(link, f'{filename}.jpg')
    print("till now")
    move_file(source,destination,filename,filetype)

def delete_file(filename,filetype):
    file_exe="{}.{}".format(filename,filetype)
    if os.path.exists('{}'.format(file_exe)):
        os.remove("{}".format(file_exe))
        print("deleted")
    else: print("file not found")

def move_file(source,destination,filename,filetype):
    try:
        print(source + filename + filetype ,destination + filename + filetype)
        os.rename(source + filename + filetype ,destination + filename + filetype)
    except:
        print("File Not Found")

def image_show(destination,filename,filetype):
    im=Image.open("{}{}{}".format(destination,filename,filetype))

def cloud_write(filename):
    cloud_write=open("test.txt","w")
    cloud_write.write(filename)
    cloud_write.close()

#returns inti_values
def cloud_read():
    cloud_read=open("test.txt","r")
    initial_name=cloud_read.readline()
    inti_values=initial_name.split(" ")
    cloud_read.close()
    return inti_values



source ='C:\\Users\\ashna\\OneDrive\\Desktop\\PYTHON\\programs files\\pic_of _day\\demo\\'
destination ='C:\\Users\\ashna\\OneDrive\\Desktop\\image of the day\\'
filetype ='.jpg'

down_data=cloud_read()
Sr_no,last_date,inti_hour,NTD=int(down_data[0].split(".")[0]),down_data[1],int(down_data[2]),int(down_data[3])
todays_date,current_hour= dt.now().strftime('%d-%m-%y'),dt.now().strftime("%H")
x=(True if todays_date== last_date  else False )


if x==True:
    print("press y to continue the pic download last downloaded {} hrs ago".format(current_hour))
    conformation=input("Do you want download th pic(y/n):").lower()
    cloud_write("{}. {} {} {}".format(Sr_no,todays_date,inti_hour,NTD+1))
    dummy= New_Download(Sr_no,NTD+1) if conformation=="y" else exit()
else:
    final_name="{}. {} {} {}".format(Sr_no+1,todays_date,inti_hour,0)
    cloud_write(final_name)
    New_Download(Sr_no+1,0)

print('exit')
print('Pic is downloded')
sleep(1)



 


