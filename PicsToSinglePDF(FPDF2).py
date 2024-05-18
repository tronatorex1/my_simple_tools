# This tool allows to compile and convert Pic files into a single PDF.
#   All found pic files are gathered and converted into a single PDF that holds the folder's name
#   It uses fpdf2 library (more reliable than img2pdf)

from fpdf import FPDF # install "pip install fpdf2"; not fpdf which is deprecated already
from PIL import Image # this is used to extract the images' dimensions
import os, time

dpi = 120 # note for calcs below that "pt" units are 1/72th of an inch
pdf = FPDF(unit="pt") # does not use Letter/A4 or any pre-format; uses pt dinamically based on Pics' sizes
pdf.set_margins(0, 0, 0) # sets the basic margins
ext = "jpg|jpeg|png|gif"

print("\n\n-----------------------------------------------------------------------")
print("* PICs to single PDF file converter (batch)\n")

# -- Real sorter -----------------------------------------------------------------
# taken from stackoverflow
import re
def sorted_alphanumeric(data): # this function allows to alphabetically sort the file names (real sorting)
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
# -- Real sorter -----------------------------------------------------------------

def page_size(image): # this function allows to determine the pic's dimensions, so the new pdf page = pic's dimensions
    with open(image, "rb") as f:
        dim = Image.open(f)
        page_size = dim.size[0]/dpi*72, dim.size[1]/dpi*72 # the dpi*72 is a formula taken thanks to (Exanmple #2): https://www.programcreek.com/python/example/97320/fpdf.FPDF#:~:text=%2C%20size)-,Example%20%232,-Source%20File%3A
    return page_size # returns a tuple with the pic's dimensions

dirs = "c:\\tmp\cbr"
for root, subdirs, file in os.walk(dirs):
    if (file): # asking for the existence of a files allows to determine if reached the end of path and where pics reside
        pdf = FPDF()
        output_file = root # it collects the paths' (not file's) name to use it as pdf output name 
        sorted_1 = sorted_alphanumeric(file) # this allows to real sort the pics' file names
        sorted_2 = [os.path.join(root , i) for i in sorted_1] # this allows to concat the root + the pics' file names 
        print(f"  * File: [{output_file}] = INSERTING!------------------------------")
        for i in sorted_2: # sorted_2 holds the whole paths + pics' file names
            if(re.findall(ext, i)): 
                try:
                    size = page_size(i) # this allows to read the pic's dimensions, so each pdf page's dimension = pic dimension
                except:
                    size = (720, 1200) # default pic size if page_size errors out!
                try:
                    pdf.add_page(format = size) # creates a new pdf page with the pic's dimensions (size = tuple)
                    pdf.image(i, 0, 0, size[0], size[1]) # set the pic's image to the desired size = add_page size (line above)
                    print(f"    * Image: [{i}] inserted = OK!!!")
                except Exception as e:
                    print(f"[X] Error: msg = [{e}]... Jumping to the next available set of PIC files...")
        # pdf.output(f"{output_file}___.pdf", "F") # syntax for FPDF (v1)
        pdf.output(f"{output_file}___.pdf") # syntax for FPDF2 (current)
        print(f"  * File: [{output_file}] = DONE!" + "\n\n")
        time.sleep(2)