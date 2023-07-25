import shutil
import os
def sort_files():
 #This takes the directory the user wants to organize as input
 directory = input("Folder you want to organize, Input the full path please: ")

 targets = [os.path.join(directory,"pdfs"), os.path.join(directory,"Pictures"), os.path.join(directory,"worddocs"), os.path.join(directory,"zipfiles"), os.path.join(directory,"txtfiles"), os.path.join(directory,"data"),os.path.join(directory,"misc")]

 #This function is just to recude code duplication and it moves <filename> to the target directory using the shutil module 
 def move():
    shutil.move(os.path.join(directory, filename), os.path.join(target, filename))

 #The loop that checks that the folders that <filename> will be sorted into exist
 for paths in targets:
    if not os.path.isdir(paths):
        os.mkdir(paths)

 #The actual loop that sorts the files
 for filename in os.listdir(directory):

    if filename.endswith(".pdf"):
        target = targets[0]
        move()

    if filename.endswith(".png"):
        target = targets[1]
        move()
    
    if filename.endswith(".jpeg"):
        target = targets[1]
        move()

    if filename.endswith(".docx"):
        target = targets[2]
        move()

    if filename.endswith(".zip"):
        target = targets[3]
        move()
            
        
    if filename.endswith(".txt"):
        target = targets[4]
        move()
    
    if (filename.endswith(".xlsx") or filename.endswith(".csv") or filename.endswith(".json")):
        target = targets[5]
        move()
        
