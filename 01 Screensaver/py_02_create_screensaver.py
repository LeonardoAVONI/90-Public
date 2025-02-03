from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import os

def split_string(input_string, max_length):
    words = input_string.split()
    lines = []
    current_line = ""
    
    for word in words:
        # Check if adding the word to the current line would exceed max_length
        if len(current_line) + len(word) + (1 if current_line else 0) <= max_length:
            # If not, add the word to the current line
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            # If yes, push the current line to the lines list and start a new line with the word
            lines.append(current_line)
            current_line = word
    
    # Add the last line to the list
    if current_line:
        lines.append(current_line)
    
    # Join the lines with newline characters
    return '\n'.join(lines)

def create_loading_screen(text_file, images_folder, background_image, output_folder):
    """Main function to generate loading screens with text and images."""
    
    # reading all the lines for the tips
    with open(text_file, 'r') as f:
        lines = f.readlines()


    with Image(filename=background_image) as background:


        # Loop through each line in the text file
        for idx, line in enumerate(lines):
            with background.clone() as new_image:
                line = line.strip()  # Remove any extra whitespace

                # separate the content from the category
                text = line.split("&")
                category = text[0]
                content = text[1]
                content = split_string(content, max_length=50)

                # Corresponding image based on line number
                image_filename = f"{idx + 1}.jpg"  # Assuming image filenames are 1.jpg, 2.jpg, etc.
                
                # select the correct image filename to open
                img_path = os.path.join(images_folder, image_filename)

                try:
                    # Open the overlay image using Wand
                    with Image(filename=img_path) as overlay_image:
                        # Resize overlay image to match the desired size
                        overlay_image.resize(967+9, 1466+2)

                        # Composite the overlay image onto the background
                        new_image.composite(overlay_image, left=440, top=569-120) #for background_3.jpg
                        #new_image.composite(overlay_image, left=440, top=569-2) #for background.jpg

                        
                        # Add text to the image
                        with Drawing() as draw1: #needs to be capital letters #Neue Helvetica 77 Condensed Bold
                            draw1.font = 'Helvetica-Bold'  # Set your font path if needed
                            draw1.font_size = 90
                            draw1.font_weight = 500
                            draw1.fill_color = Color("#E4DA81")
                            
                            # Draw the category and content text
                            #draw1.text(1540, 770, category.upper()) #background.jpg
                            draw1.text(1540, 770-120, category.upper()) 
                            
                            # Draw the text on the background
                            draw1(new_image)

                        with Drawing() as draw2: #needs to be non capital
                            draw2.font = 'Helvetica-Bold'  # Set your font path if needed
                            draw2.font_size = 80
                            draw2.fill_color = Color('white')
                            
                            # Draw the category and content text                            
                            #draw2.text(1540, 1050, content)
                            draw2.text(1540, 1050-120, content) 
                            
                            # Draw the text on the background
                            draw2(new_image)

                        # Apply sepia tone filter
                        #new_image.sepia_tone(threshold=1)

                        # Save the new image
                        output_filename = os.path.join(output_folder, f"loading_screen_{idx + 1}.jpg")
                        new_image.save(filename=output_filename)

                        print(f"Created: {output_filename}")
                        
                        del new_image

                except Exception as e:
                    print(f"Error processing image {image_filename}: {e}")

"""
This code takes the text located in "hints.txt"
It also takes the background image called background.jpg
And for all lines in the text document, it generates the corresponding screensaver
screen using the line and the corresponding description image
"""
text_file = 'hints.txt'
images_folder = '01_description_images'
background_image = 'background.jpg'
output_folder = '02_output_screensaver_images'

create_loading_screen(text_file, images_folder, background_image,output_folder)