import os
import shutil
Photos="Task3(Task Automation with Python Scripts)/Move jpg files/Photos"
Images="Task3(Task Automation with Python Scripts)/Move jpg files/Images"
if not os.path.exists(Images):
    os.makedirs(Images)

files = os.listdir(Photos)
for file in files:
    if file.endswith(".jpg"):
        source = os.path.join(Photos, file)
        destination = os.path.join(Images, file)
        shutil.move(source, destination)
    print(f"{file} is moves successfully")
print("All JPG files are move from the folder successfully ")
