def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	character_count = count_characters(text)
	sorted_chars = sort_characters(character_count)
	write_report(book_path, num_words, sorted_chars)

def get_num_words(text):
	words = text.split()
	return len(words)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_characters(text):
	chars = {}
	for char in text:
		lowerCase = char.lower()
		if lowerCase in chars:
			chars[lowerCase] += 1
		else:
			chars[lowerCase] = 1
	return chars

def sort_on(dict):
	return dict["count"]

def sort_characters(dict):
	characters = []
	for key, value in dict.items():
		if key.isalpha():
			characters.append({"char": key, "count":value})

	return sorted(characters, key=lambda c: c['count'], reverse=True)

def write_report(path, words, list):
	print(f"--- Begin report of :{path} ---")
	print(f"{words} words found in the document\n")
	for dic in list:
		print(f"The \'{dic['char']}\' character was found {dic['count']} times")
	print("--- End report ---")

main()
