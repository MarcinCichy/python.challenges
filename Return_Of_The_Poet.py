# Challenge: Return of the Poet
# from RealPython, Python Basics, chapter 18.10
#

from tkinter import *
from tkinter.filedialog import asksaveasfilename
import random


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.some_text = ('Write at least three words in each category.\n Click the [Generate] button to generate poem.')
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		# create the frames to organize GUI
		frm_info = Frame(self)  # , bg="green"
		frm_info.grid_rowconfigure(0, weight=1)
		frm_info.grid_columnconfigure(0, weight=1)
		frm_upper = Frame(self)  # , bg="blue"
		frm_button = Frame(self)
		frm_button.grid_rowconfigure(0, weight=1)
		frm_button.grid_columnconfigure(0, weight=1)
		frm_downer = Frame(self)  # , bg="red"
		frm_downer.grid_rowconfigure([0,1,2,3,4,5], weight=1)
		frm_downer.grid_columnconfigure(0, weight=1)
		frm_downer['relief'] = "groove"
		frm_downer['borderwidth'] = "5"
		frm_info.grid(row=0, column=0, sticky="ew")
		frm_upper.grid(row=1, column=0, sticky="ew")
		frm_downer.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
		frm_button.grid(row=2, column=0, stick="ew")

		
		# create labels
		self.lbl_upper_information = Label(frm_info)
		self.lbl_upper_information['text'] = "Enter your favorite words, separated by commas."
		self.lbl_upper_information.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
		
		self.lbl_Nouns = Label(frm_upper)
		self.lbl_Nouns['text'] = "Nouns:"
		self.lbl_Nouns.grid(row=0, column=0, padx=5, pady=2, sticky="e")
		self.lbl_Verbs = Label(frm_upper)
		self.lbl_Verbs['text'] = "Verbs:"
		self.lbl_Verbs.grid(row=1, column=0, padx=5, pady=2, sticky="e")
		self.lbl_Adj = Label(frm_upper)
		self.lbl_Adj['text'] = "Adjectives:"
		self.lbl_Adj.grid(row=2, column=0, padx=5, pady=2, sticky="e")
		self.lbl_Preps = Label(frm_upper)
		self.lbl_Preps['text'] = "Prepositions:"
		self.lbl_Preps.grid(row=3, column=0, padx=5, pady=2, sticky="e")
		self.lbl_Adverb = Label(frm_upper)
		self.lbl_Adverb['text'] = "Adverbs:"
		self.lbl_Adverb.grid(row=4, column=0, padx=5, pady=2, sticky="e")

		# create entries
		self.ent_Nouns = Entry(frm_upper, width=80)
		self.ent_Nouns.grid(row=0, column=1, padx=5, pady=2, sticky="e")
		self.ent_Verbs = Entry(frm_upper, width=80)
		self.ent_Verbs.grid(row=1, column=1, padx=5, pady=2, sticky="e")
		self.ent_Adj = Entry(frm_upper, width=80)
		self.ent_Adj.grid(row=2, column=1, padx=5, pady=2, sticky="e")
		self.ent_Preps = Entry(frm_upper, width=80)
		self.ent_Preps.grid(row=3, column=1, padx=5, pady=2, sticky="e")
		self.ent_Adverb = Entry(frm_upper, width=80)
		self.ent_Adverb.grid(row=4, column=1, padx=5, pady=2, sticky="e")
		
		# create label with Poem or announcement
		self.lbl_Poem_Info = Label(frm_downer)
		self.lbl_Poem_Info['text'] = "Your Poem: "
		self.lbl_Poem = Label(frm_downer)
		self.lbl_Poem['text'] = self.some_text
		self.lbl_Poem_Info.grid(row=0, column=0)
		self.lbl_Poem.grid_columnconfigure(0, weight=1)
		self.lbl_Poem.grid(row=2, column=0, padx=10, pady=10, sticky="ewns")
		
		# create buttons
		# create button to generate poem
		self.btn_generate = Button(frm_button)
		self.btn_generate['text'] = "Generate"
		self.btn_generate['command'] = self.but_gen_action
		self.btn_generate.grid(row=0, column=0, padx=15, pady=15)
		# create button to save poem
		self.btn_save = Button(frm_downer)
		self.btn_save['text'] = "Save to file"
		self.btn_save['command'] = self.save_poem
		self.btn_save.grid(row=5, column=0, pady=10)
		
	def but_gen_action(self):
		poem_ingredients = []
		self.lbl_Poem['text'] = ""
		nouns = self.ent_Nouns.get()
		list_nouns = self.format_entries(nouns)
		poem_ingredients.append(list_nouns)
		verbs = self.ent_Verbs.get()
		list_verbs = self.format_entries(verbs)
		poem_ingredients.append(list_verbs)
		adj = self.ent_Adj.get()
		list_adj = self.format_entries(adj)
		poem_ingredients.append(list_adj)
		preps = self.ent_Preps.get()
		list_preps = self.format_entries(preps)
		poem_ingredients.append(list_preps)
		adverb = self.ent_Adverb.get()
		list_adverb = self.format_entries(adverb)
		poem_ingredients.append(list_adverb)
		
		if None in poem_ingredients:
			pass
		else:
			self.gen_poem(poem_ingredients)
		
	def format_entries(self, ent):
		list_ent = []
		ent = ent.replace(" ", "")
		list_ent = ent.split(",")
		for word in list_ent:
			if word == '':
				list_ent.remove(word)
		length = self.check_correct_entries_length(list_ent)
		only = self.check_only_one(list_ent)
		if length == "error" or only == "error":
			return
		else:
			return list_ent
	
	def check_correct_entries_length(self, list_ent):
		if len(list_ent) < 3:
			self.lbl_Poem['foreground'] = 'red'
			self.lbl_Poem['text'] = "You need more words. Correct it."
			return "error"
		
	def check_only_one(self, list_ent):
		for x in list_ent:
			count = list_ent.count(x)
			if count > 1:
				self.lbl_Poem['foreground'] = 'red'
				self.lbl_Poem['text'] = "Words are duplicated. Correct it."
				return "error"
			
	def save_poem(self):
		""" Save the current file as a new file"""
		filepath = asksaveasfilename(
			defaultextension="txt",
			filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
		)
		if not filepath:
			return
		with open(filepath, "w") as output_file:
			text_poem = self.lbl_Poem['text']
			output_file.write(text_poem)
		# window.title(f"Return Of The Poet - {filepath}")

	def gen_poem(self, words_list):
		""" The code below was taken (with small changes) from
			Challenge: Wax Poetic
			from RealPython, Python Basics, chapter 9.5"""
		def drawn_words(words_list):
			""" The function randomly selects words from the list.
				Depending on the part of the sentence (nouns, verbs, adjectives, prepositions, adverbs),
				it selects the required number of words and returns it in one list. """
			
			words = []
			for i in range(0, len(words_list)):
				if words_list.index(words_list[i]) < 3:  # lists from 0 to 2 (nouns, verbs, adjectives) needs 3 words
					for j in range(0, 3):
						word = random.choice(words_list[i])
						words.append(word)
				elif words_list.index(words_list[i]) == 3:  # list 3 (prepositions) need 2 words
					for j in range(0, 2):
						word = random.choice(words_list[i])
						words.append(word)
				else:
					for j in range(0, 1):  # list 4 (adverbs) need 1 word
						word = random.choice(words_list[i])
						words.append(word)
			return words
		
		new_list = drawn_words(words_list)
		
		""" Little help to write poem, what index is what a part of sentence ;)
			noun1 - new_list[0]
			noun2 - new_list[1]
			noun3 - new_list[2]
			verb1 - new_list[3]
			verb2 - new_list[4]
			verb3 - new_list[5]
			adj1 - new_list[6]
			adj2 - new_list[7]
			adj3 - new_list[8]
			prep1 - new_list[9]
			prep2 - new_list[10]
			adverb1 - new_list[11] """
		
		# indefinite article - which one to use
		if new_list[6][0] in "ieaou":
			start_letter = "An"
		else:
			start_letter = "A"
		
		# write a poem :))))
		self.lbl_Poem['foreground'] = 'black'
		self.lbl_Poem['text'] = \
			(f'{start_letter} {new_list[6]} {new_list[0]}.\n'

			f'{start_letter} {new_list[6]} {new_list[0]} {new_list[3]} {new_list[9]} the {new_list[7]} {new_list[1]}\n'
			f'{new_list[11]}, the {new_list[0]} {new_list[4]}\n'
			f'the {new_list[1]} {new_list[5]} {new_list[10]} a {new_list[8]} {new_list[2]}.\n'
			f'   Your Computer\n'
			f'	  Inspired by Clifford Pickover\n')

		
root = Tk()
app = Application(root)
root.title('Return of the Poet')
root.mainloop()
