import re

mainmenu = """
Welcome to BookBot
------------------
1. Open a book
2. Exit
------------------
"""

def __main__():
    while True:
        print(mainmenu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            open_book()
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_book_text(name):
    try:
        with open(f"books/{name}.txt") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The book '{name.capitalize()}' was not found.\nReturning to main menu...")
        return None

def get_word_count(text):
    return len(text.split())
    
def get_char_dict(text):
    char_counter = {}
    letters = re.sub(r'[^a-z]', '', text)
    for c in letters:
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1
    return char_counter

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list      

def open_book():
    title = input("Enter the name of the book: ").strip().lower()
    text = get_book_text(title)

    if text is None:
        return
    
    num_words = get_word_count(text)
    if num_words == 0:
        print(f"{title.capitalize()} contains no words or readable content.\nReturning to main menu...")
        return

    chars_dict = get_char_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    bookmenu = f"""
What would you like to do with {title.capitalize()}?
------------------
1. Read the book
2. Generate report
------------------
"""
    while True:
        print(bookmenu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(text)
            break
        elif choice == "2":
            print(f"--- Begin report of {title.capitalize()} ---")
            print(f"{num_words} words found in {title.capitalize()}.\n")

            for item in chars_sorted_list:
                print(f"The '{item['char']}' character appears {item['num']} times.")
            print(f"\n--- End report of {title.capitalize()} ---")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
__main__()