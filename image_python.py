from PIL import Image

mac = Image.open("E:/SIDDU/Personal/PLACEMENT/siddu's photo.jpg")
print(type(mac))

#print(mac.show())
print(mac.size)
print(mac.format_description)

resize_img = mac.resize((150,250))
resize_img.show()

x = 0
y = 0
w = 200
h = 231
mac_crop = mac.crop((x,y,w,h))
mac_crop.show()

mac.paste(im=mac_crop,box=(20,30))
mac.show()


