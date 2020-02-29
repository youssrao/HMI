from PIL import Image, ImageDraw
import face_recognition

# Load image file
image = face_recognition.load_image_file("klas.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

pil_image = Image.fromarray(image)

draw = ImageDraw.Draw(pil_image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print location of each face
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    #Draw a rectangle around each face
    face_image = image[top:bottom, left:right]
    draw.rectangle(((left, top), (right, bottom)), width=8, outline=(255, 0, 0))

del draw

pil_image.show()