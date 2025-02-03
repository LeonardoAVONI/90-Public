import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder):
    """
    Extracts each page of the PDF as an image and saves it as i.jpg, where i is the page number.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_folder (str): Path to the folder where images will be saved.
    """
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Iterate over each page in the PDF
        for page_number in range(len(pdf_document)):
            # Get the page
            page = pdf_document[page_number]

            # Render page to a pixmap (image)
            pix = page.get_pixmap()

            # Generate the output file name
            output_file = f"{output_folder}/{page_number + 1}.jpg"

            # Save the image as JPEG
            pix.save(output_file)

            print(f"Page {page_number + 1} saved as {output_file}")

        # Close the PDF document
        pdf_document.close()
        print("All pages have been converted to images.")

    except Exception as e:
        print(f"An error occurred: {e}")

"""
The next lines take the pdf file called "images.pdf" located in 00_pptx
and creates all the images needed to generate the screensaver screens later
The images are then savec in the "01_description_images" folder
"""
current_path = os.getcwd()
source_pdf_path = os.path.join(current_path,"00_pptx","images.pdf")
description_images_path = os.path.join(current_path,"01_description_images")
pdf_to_images(source_pdf_path, description_images_path)