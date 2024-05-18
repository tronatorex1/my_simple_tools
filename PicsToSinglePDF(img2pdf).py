# This tools allows to compile and ovnert from PIC files into a single PDF. All found pic files are gathered and converted into a single PDF that holds the folder's name
#   It uses img2pdf library (https://pypi.org/project/img2pdf/); not the most elegant solution... img2pdf errors a lot!!!

import img2pdf
import os, time

print("\n\n-----------------------------------------------------------------------")
print("* PICs to single PDF file converter (batch)")
dirs = "c:\\tmp\cbr" # set the root starting path to detect PICS to convert to PDF

# -- Real sorter -----------------------------------------------------------------
# taken from stackoverflow
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
# -- Real sorter -----------------------------------------------------------------

for root, subdirs, file in os.walk(dirs):
    if (file):
        output_file = root
        sorted_1 = sorted_alphanumeric(file) # 
        sorted_2 = [os.path.join(root , i) for i in sorted_1] # 
        
        print("  * Writing the [" + output_file + "] pdf file... ", end = "")
        
        try:
            f = open(output_file + ".pdf", "wb")
            f.write(img2pdf.convert(sorted_2))
            f.close()
            print("OK!!!")
        except Exception as e:
            print("\n" + f"[X] Error: msg = [{e}]... Jumping to the next available set of PIC files...")
        
        time.sleep(2)