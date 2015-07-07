__author__ = 'DeysMachine'

import re
import logging


# log = logging.log()
notes_dict = {}

# class Notes:
# 	book_title = ""
# 	location = ""
# 	note = ""


def extract_notes():
	"""

	"""
	book_title = ""
	location = ""
	note = ""

	# to determine if the title is read or not
	read_title = False
	# creating a list for storing notes
	notes_list = []

	# starting the loop for reading all the lines
	for line in file.readlines(file("My Clippings.txt")):
		line = line.lstrip()
		if line.startswith("===="):
			'''It marks the end of a note'''
			arrange_notes(book_title, location, note)		# add the note in the notes_list
			read_title = False				# reset read_tile back to False
			book_title = ""
			location = ""
			note = ""
		elif line.startswith("- "):
			''' these lines contains the marker/notes location and time info'''
			read_title = True				# set the read_title to True
			location = int(re.search(r'\d+', line).group())
		else:
			if read_title:
				''' if the title are already read then treat the lines as notes'''
				# TODO: analyze cases when the note comes as multiple lines
				note = line		# assumes that the note will only be of one line
			else:
				# if the title contains more lines then only store one line as the title
				if book_title == "":
					book_title = line.rstrip()
					read_title = True

	# list of objects
	return notes_list


def arrange_notes(title, location, note):

	if len(title) > 15:
		''' Truncate the title to 15 chars'''
		title = title[:15]

	if title not in notes_dict:
		''' if the book title is not stored then create a new entry'''
		book = dict()
		book[location] = note			# store the note indexed with the location

	else:
		''' the case when we are adding notes to an existing book'''
		book = notes_dict.get(title)	# fetch the book

		''' we will store notes indexed with the page location
		and if there is a duplicate location then fetch the note
		and append the new note to it
		'''
		if location not in book:
			book[location] = note
		else:
			old_note = book.get(location)
			note = old_note + "\n" + note
			book[location] = note

	notes_dict[title] = book		# store the book into the notes_dict


def print_notes():
	output_file = open("Arranged.txt", 'w+')
	for book, notes in notes_dict.items():
		output_file.write(book.upper() + "\n")
		output_file.write("----------------------" + "\n")
		for loc, note in sorted(notes.items()):
			# output_file.write(str(loc) + ": " + note + "\n")
			output_file.write(note + "\n")
	output_file.close()

# calling the extract_notes fn
extract_notes()
print_notes()
