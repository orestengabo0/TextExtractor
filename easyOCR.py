import easyocr

# Create an EasyOCR Reader instance
reader = easyocr.Reader(['en'])  # You can add more languages like ['en', 'fr'] if needed

# Path to the image file
image_path = 'images/image.png'

# Use easyOCR to extract text
result = reader.readtext(image_path)

# Print the extracted text
for detection in result:
    print(f"Detected text: {detection[1]}")
