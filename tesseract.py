import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

s = pytesseract.image_to_string(r'images stuff\3.png')
d = pytesseract.image_to_string(r'images stuff\4.png')
print(s)
print(d)

with open('modern tools/tesseract2.txt', 'w') as f:
    f.write(s)
    f.write(d)

# it works but quality is so shit that its like im reading heiroglyphs
# ok its working much better now 