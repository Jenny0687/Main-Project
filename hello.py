import cv2 
import os 
image_path = r'C:\Users\elist\OneDrive\Desktop\foto\images.jpg'
directory = r'C:\Users\elist\OneDrive\Desktop\foto\imagen'
img = cv2.imread(image_path) 
os.chdir(directory) 
print("Before saving image:")   
print(os.listdir(directory))   
filename = 'savedImage.jpg'
cv2.imwrite(filename, img) 
print("After saving image:")   
print(os.listdir(directory)) 
print('Successfully saved')