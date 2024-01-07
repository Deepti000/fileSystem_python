import os
import datetime





def file_list(dir):
    files = os.listdir(dir)
    print(f"Listing files in given path :  {dir}")
    i = 1
    fa = {}
    for f in files:
        if os.path.isfile(dir + '/' + f):
           filestat = os.stat(f'{dir}/{f}')
           mtime = filestat.st_mtime 
           timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')        
           print(f"{i}   {f}   {filestat.st_size} bytes  {filestat.st_uid} user  {timestamp_str} \n")
           fa[i] = f
           i = i+1
    return fa
    


option = 1
while(True):
     dir = input("Enter absolute path for files what you want to delete - ")
     fa = file_list(dir)
     print("choose option \n\t\t1)\tDeletion of file\n\t\t2)\tExit\n")
     option = input("Enter option : ")
     if(option == "1"):
          
             no = input("Enter no. of file which you want to delete - ")
             if int(no) in fa:
                 print(f"{fa[int(no)]} is deleted successfull")  
                 os.remove(f"{dir}/{fa[int(no)]}")
                   
             else:
                   print(f"file related to this {no}, doesn't exist. pls enter right no. \n\n")       
     elif(option == "2"):
             break               

     else:
          print("Enter correct option \n\n")

                   
