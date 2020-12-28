import PIL.Image
import PIL.ImageDraw
import cv2
import face_recognition as fr

img = fr.load_image_file('Images/modi.jpg')

detect = fr.face_locations(img)
pil_img = PIL.Image.fromarray(img)

for location in detect:
    top, right, bottom, left = location
    draw = PIL.ImageDraw.Draw(pil_img)
    draw.rectangle([left, top, right, bottom], outline='red')


pil_img.show()