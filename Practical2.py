from PIL import Image, ImageDraw, ImageFont 
import random 
import string 

captcha_text = ''.join( 
    random.choices(string.ascii_uppercase + string.digits, k=6) 
    ) 
img = Image.new("RGB", (300, 100), color="white") 

draw = ImageDraw.Draw(img) 
draw.text((50, 25), captcha_text, fill="black") 
img.save("captcha.png") 
print("CAPTCHA image generated successfully!") 

img.show()
user_input = input("Enter CAPTCHA shown in image: ") 
if user_input.upper() == captcha_text: 
    print("CAPTCHA Verified") 
else: 
    print("Wrong CAPTCHA") 