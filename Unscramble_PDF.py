# Challenge: Unscramble a PDF
# from RealPython, Python Basics, chapter 14.7
#
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path.cwd() / "scrambled.pdf"
pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

dict_of_pages = {}
for page in pdf_reader.pages:
	text = page.extractText()
	if page["/Rotate"] != 0:
		page.rotateCounterClockwise(page["/Rotate"])
	dict_of_pages[int(text[0])] = page

for key in sorted(dict_of_pages):
	pdf_writer.addPage(dict_of_pages[key])

with Path("Unscrambled.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)
