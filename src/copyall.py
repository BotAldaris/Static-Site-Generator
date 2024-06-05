import os
import shutil
def copy_all():
    if(os.path.exists("./public")):
        shutil.rmtree("./public")
    if not os.path.exists("static"):
        return
    copy("./static")

def copy(path:str):
    dir_name = path[:].replace("static","public")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    items = os.listdir(path)
    for item in items:
        path_item = path+"/"+item
        if os.path.isfile(path_item):
            shutil.copy(path_item,path_item[:].replace("static","public"))
        else:
            copy(path_item)

copy_all()