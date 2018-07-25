import os
import cv2
from PIL import Image
import pytesseract
import argparse
import webbrowser

os.system("adb shell screencap -p | sed 's/\r$//' > loco2.PNG")   #uncomment this to start taking screenshot!
image = cv2.imread("loco2.PNG")
print (image.shape)


cropped = image[467:633, 78:642]
ans1 = image[658:741, 111:610]
ans2 = image[794:878, 111:610]
ans3 = image[930:1015, 111:610]

cv2.imshow("ans1", ans1)

#cv2.imshow("cropped", cropped)
#cv2.waitKey(0)


# write the cropped image to disk in PNG format
cv2.imwrite("q.png", cropped)

cv2.imwrite("ans1.png", ans1)
cv2.imwrite("ans2.png", ans2)
cv2.imwrite("ans3.png", ans3)


q = pytesseract.image_to_string(Image.open("q.png"))

a1 = pytesseract.image_to_string(Image.open("ans1.png"))
a2 = pytesseract.image_to_string(Image.open("ans2.png"))
a3 = pytesseract.image_to_string(Image.open("ans3.png"))

#print(q)

#print(a1)
#print(a2)
#print(a3)

q=q.encode('ISO-8859-1', 'ignore')

a1=a1.encode('ISO-8859-1', 'ignore')
a2=a2.encode('ISO-8859-1', 'ignore')
a3=a3.encode('ISO-8859-1', 'ignore')


o1 = q+"  "+a1
o2 = q+"  "+a2
o3 = q+"  "+a3

#print(type(q))
print(type(o1))
#print(o1,o2,o3)

search_terms = [o1,o2,o3]

for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)


