from PIL import Image
import sys

# General Algorithm converting an image to ASCII art:
# - Resize the image to the desired width, maintaining the original image aspect ration.
# - Convert the image to gray-scale.
# - Convert every pixel to an ASCII character with a similar intensity. 
# - With each pixel converted to an ASCII character we can then construct the new ASCII art piece.  
# - We will use Python Image Library (PIL) which we will import at the top of the program.
# 
# To run: 
#  ```bash
#  $ python script.py
#  ```
# 
# Use the JPG file in the folder `1748613858636.jpg` as input.

# ASCII character used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to new width
def resize_image(image, new_width = 100):
   width, height = image.size
   ratio = height / width
   new_height = int(new_width * ratio)
   resized_image = image.resize((new_width, new_height))
   return(resized_image)

# Convert each pixel to grayscale
def grayify(image):
   grayscale_image = image.convert("L")
   return(grayscale_image)

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
   pixels = image.getdata()
   characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
   return(characters)

def main(new_width=100):
   # Attempt to open image from user input
   image_path = input("Enter a valid pathname to an image:\n")
   try:
      with Image.open(image_path) as img:
         # Image successfully opened
         print(f"image opened successfully. Format: {img.format}, width: {img.width}, height: {img.height}")

         # Convert image to ASCII
         resized_image = resize_image(img)
         new_image_data =  pixels_to_ascii(grayify(resized_image))
         
         # Format
         pixel_count = len(new_image_data)
         ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
         
         # Save result to "ascii_image.txt"
         with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)

         # Print the result
         print(ascii_image)
         
         sys.exit(1)
         
   except FileNotFoundError:
      # if the pathname is not valid
      print(f"******* ERROR: The file '{image_path}' is not a valid pathname to an image.")
      sys.exit(1)
   except Exception as e:
      print(f"******* GENERAL ERROR: An unexpected error occurred: {e}")
      sys.exit(1)


main()
