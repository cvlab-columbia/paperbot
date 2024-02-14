import os
from tqdm import tqdm
from pdf2image import convert_from_path

# Ensure this script is run in the directory containing your PDF files

# Get all PDF files in the current directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Set DPI for high quality. This still affects the output resolution but doesn't add margins.
dpi_setting = 300  # Adjust this value as needed

# tqdm
pdf_files = tqdm(pdf_files, desc="Converting PDFs")
for pdf_file in pdf_files:
    # Convert each PDF to a list of images
    # Use 'size' parameter only if you want to force a particular size.
    # Omitting 'size' to keep the original aspect ratio without forcing dimensions.
    images = convert_from_path(pdf_file, dpi=dpi_setting)
    
    # Save each page as an image
    for i, image in enumerate(images):
        # Constructing image file name based on PDF file name and page number
        image_file_name = f"{os.path.splitext(pdf_file)[0]}.jpg"
        image.save(image_file_name, 'JPEG', quality=100)

print("Conversion completed.")
