import PIL.Image as img
import PIL.ImageDraw as dr
import face_recognition as fr

images = fr.load_image_file('Images/APJ.jpg')
feature_list = fr.face_landmarks(images)

pil_img = img.fromarray(images)
draw = dr.Draw(pil_img)

for landmarks in feature_list:
    for name, list_points in landmarks.items():
        print("The {} in this face has following points: {}".format(name, list_points))
        draw.line(list_points, fill='red', width=1)

pil_img.show()