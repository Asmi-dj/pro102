import os
import shutil 

from_dir = dir("c:/Users/msreddy3105/Pictures/Screenshots")
to_dir = dir("c:/Users/msreddy3105/Desktop/document_files")

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for filename in list_of_files:
    name,ext = os.path.splitext(filename)

    if ext == '':
        continue 
    if ext in['.txt', '.doc', '.docx', '.pdf', '.png']:
        path1 = from_dir + '/' + filename 
        path2 = to_dir + '/' + "document_files" 
        path3 = to_dir + '/' + "document_files" + '/' + filename 

    if os.path.exists(path2):
        print("moving" + filename + '...')
        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("moving" + filename + "...")
        shutil.move(path1,path3)

