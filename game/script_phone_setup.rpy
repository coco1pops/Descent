#Be sure to make all the three(3) entries for the images to work.

#avatars
image makiA = "/images/phone/m avatar.png"
image noimage = "/images/phone/blank.png"#this is needed do not delete or remove the .png file

#phone face
image phone0 = "images/phone/phone0.png"
image phone1 = "images/phone/phone1.png"

#pointers
image send_pointer = "images/phone/pointer-tip-send.png"
image receive_pointer = "images/phone/pointer-tip-receive.png"

#message bubble
image bubble_send = "images/phone/bubble-send.png"
image bubble_receive = "images/phone/bubble-receive.png"

#define main image for full screen image
#image img0 = ("images/phone images/phone image 0.jpg")
#image img1 = ("images/phone images/phone image 1.jpg")
#image img2 = ("images/phone images/phone image 0.jpg") #BadMustard being lazy
#add more here as needed increasing the numbers

#define small image to be shown on phone screen
#image thumb0 = ("images/phone images/thumbs/phone image 0.jpg")
#image thumb1 = ("images/phone images/thumbs/phone image 1.jpg")
#image thumb2 = ("images/phone images/thumbs/phone image 0.jpg") #BadMustard being lazy
#add more here as needed increasing the numbers

#put everything in a python list
init python:
    closeup_page = 0
    class phoneItem:
        def __init__(self, images, thumb):
            self.images = images
            self.thumb = thumb

    phone_images = []
#    phone_images.append (phoneItem(["img0"], "thumb0"))
#    phone_images.append (phoneItem(["img1"], "thumb1"))
#    phone_images.append (phoneItem(["img2"], "thumb2"))
    #add more here as needed increasing the numbers
