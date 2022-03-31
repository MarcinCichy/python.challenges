# Challenge: PDF Page Extraction Application
# from RealPython, Python Basics, chapter 18.3
#
import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# 1. Ask the user to select a PDF file to open.
gui.msgbox(msg="Select a PDF file to extract pages...", title="Select a PDF file")
input_path = gui.fileopenbox(
	title="Select a PDF file...",
	default="*.pdf"
)

# 	2. If no PDF file is chosen, then exit the program.
if input_path is None:
	exit()
	
# 3. Ask for a starting page number.
input_start_page = gui.enterbox(
		msg="Set a starting page",
		title="Start page"
)

# 4. If the user doesn't enter a starting page number, then exit the program.
if input_start_page is None:
	exit()

# 5. Valid page numbers are positive integers. If the user enters an invalid page number:
while not input_start_page.isdigit() or not isinstance(int(input_start_page), int) or int(input_start_page) <= 0:
	# - Warn the user that entry is invalid.
	gui.msgbox(msg="Starting page number is invalid!")
	# - Return step 3.
	input_start_page = gui.enterbox(
		msg="Set a starting page",
		title="Start page"
	)
	if input_start_page is None:
		exit()
		
# 	6. Ask for an ending page number.
input_end_page = gui.enterbox(
		msg="Set a ending page",
		title="Ending page"
)

# 7. If the user doesn't enter an ending page number, then exit program.h
if input_end_page is None:
	exit()
	
# 8. If the user enters an invalid page number:
while not input_end_page.isdigit() or not isinstance(int(input_end_page), int) or int(input_end_page) < 0 or int(input_end_page) < int(input_start_page):
	# - Warn the user that the entry is invalid.
	gui.msgbox(msg="Starting page number is invalid!")
	# - Return to step 6.
	input_end_page = gui.enterbox(
		msg="Set a ending page",
		title="Ending page"
	)
	if input_end_page is None:
		exit()
		
# 	9. Ask for the location to save the extracted pages.
save_title = "Save the extracted PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(
	title=save_title,
	default=file_type
)

# 10. If the user  doesn't select a save location, then exit the program.
if output_path is None:
	exit()
	
# 11. If the chosen save location is the same as the input file path:
while input_path == output_path:
	# - Warn the user that they can't overwrite the input file
	gui.msgbox(msg="Cannot overwrite original file!")
	# - Return to step 9
	output_path = gui.filesavebox(
		title=save_title,
		default=file_type
	)
# To check myself:
# print(input_start_page)
# print(input_end_page)
# print(input_path)
# print(output_path)

# 12. Perform the page extraction:
# - Open the input PDF file
input_pdf = PdfFileReader(str(input_path))
pdf_writer = PdfFileWriter()
for n in range(int(input_start_page)-1, int(input_end_page)):
	page = input_pdf.getPage(n)
	pdf_writer.addPage(page)
# - Write a new PDF file containing only the pages in the selected page range.
with Path(output_path).open(mode='wb') as output_file:
	pdf_writer.write(output_file)

