# Convert to image
from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
)

from PIL import Image, ImageOps

import img2pdf

import os

images = convert_from_path('input.pdf')


idx_counter = []
for idx, i in enumerate(images):
    idx_counter.append('output'+str(idx)+".jpeg")
    i = ImageOps.invert(i)
    i.save('output'+ str(idx) +'.jpeg')

with open("output.pdf","wb") as f:
    f.write(img2pdf.convert(idx_counter))
    
for i in idx_counter:
    os.remove(i)

#



