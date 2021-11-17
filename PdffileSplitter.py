# Challenge: PdfFileSplitter Class
# from RealPython, Python Basics, chapter 14.3
#

import tempfile
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfFileSplitter:
	writer1 = PdfFileWriter()
	writer2 = PdfFileWriter()
	
	def __init__(self, file_name):
		self.file_name = file_name
		
		pdf_path = Path.cwd() / self.file_name
		self.pdf_reader = PdfFileReader(str(pdf_path))
		self.num_pages = self.pdf_reader.getNumPages()
		# self.pdf_writer = PdfFileWriter()
		
	def split(self):
		break_page_num = input("Podaj numer strony rozdzielającej plik pdf: ")
		while not break_page_num.isdigit() and break_page_num != "":
			break_page_num = input("Podaj jeszcze raz numer strony rozdzielającej plik pdf: ")
		if break_page_num == "":
			break_page_num = int(self.num_pages/2)
		print("Wybrałeś numer strony rozdzielającej: "+str(break_page_num))
		for page in self.pdf_reader.pages[:int(break_page_num)-1]:
			PdfFileSplitter.writer1.addPage(page)
		for page in self.pdf_reader.pages[int(break_page_num)-1:]:
			PdfFileSplitter.writer2.addPage(page)
		
	def write(self, new_file_name):
		with Path(new_file_name+"_1.pdf").open(mode='wb') as output_file:
			PdfFileSplitter.writer1.write(output_file)
		with Path(new_file_name+"_2.pdf").open(mode='wb') as output_file:
			PdfFileSplitter.writer2.write(output_file)


pdf_splitter = PdfFileSplitter("Pride_and_Prejudice.pdf")
pdf_splitter.split()
pdf_splitter.write("test_pdf_split.pdf")
