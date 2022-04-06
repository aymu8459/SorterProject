import os 
import shutil





#Comment: After finding this code, I wanted to make a GUI that would use the file explorer and somehow input a value for path, but could not find solution



path = "" #can be any path you want to set new folders in Ex. /Users/Selasi/Desktop
names = os.listdir(path) # this will show the names of the folders in the selected path
folder_name = ['JPEG','RAW'] # array that will be used to create and name new folders; these will be the new folder names
for x in range(0,2): # producing two folders because array length for folder_name is 2
    if not os.path.exists(path+folder_name[x]): 
        os.makedirs(path+folder_name[x])
        # ^ if the folder doesn't already exist within the path directory, this for loop will create a new folder in the path
for files in names:
    if ".jpeg" in files and not os.path.exists(path+'JPEG/'+files): 
    	shutil.move(path+files, path+'JPEG/'+files) 
        # if .jpeg extension file doesn't exist within the 'JPEG' folder already, it will be moved into that folder; same logic for RAW files in the next two lines
    if ".dcf" in files and not os.path.exists(path+'RAW/'+files):
    	shutil.move(path+files, path+'RAW/'+files)
        #I believe ".dcf" is the extension for RAW files but I'm not sure
