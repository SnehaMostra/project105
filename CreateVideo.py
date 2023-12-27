import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame= cv2.imread(images[80])
#cv2.imshow("output",frame)
#cv2.waitKey(3000)
height,width,channels=frame.shape
sunset= cv2.VideoWriter("sunset.avi",cv2.VideoWriter_fourcc(*'MPEG'),15,(width,height))
for i in range(count-1,0,-1):
    img=cv2.imread(images[i])
    sunset.write(img)
print("done")
sunset.release()    