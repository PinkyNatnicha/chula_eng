Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import tkinter as tk
... import random
... 
... # Thai consonant dictionary (Symbol : Pronunciation)
... thai_consonants = {
...     "ก": "gor gai (ก ไก่)",
...     "ข": "khor khai (ข ไข่)",
...     "ฃ": "khor khuad (ฃ ขวด)",
...     "ค": "khor khwai (ค ควาย)",
...     "ฅ": "khor khon (ฅ คน)",
...     "ฆ": "khor rakhang (ฆ ระฆัง)",
...     "ง": "ngor ngu (ง งู)",
...     "จ": "jor jaan (จ จาน)",
...     "ฉ": "chor ching (ฉ ฉิ่ง)",
...     "ช": "chor chang (ช ช้าง)"
... }
... 
... # Initialize the main application window
... root = tk.Tk()
... root.title("Thai Consonant Flashcards")
... root.geometry("400x300")
... 
... # Function to show a new consonant
... def show_new_consonant():
...     global current_consonant
...     current_consonant = random.choice(list(thai_consonants.keys()))
...     consonant_label.config(text=current_consonant)
...     flip_button.config(state=tk.NORMAL)
...     meaning_label.config(text="")
... 
... # Function to flip the card and reveal the pronunciation
... def flip_card():
...     meaning_label.config(text=thai_consonants[current_consonant])
...     flip_button.config(state=tk.DISABLED)
... 
... # UI Elements
consonant_label = tk.Label(root, text="", font=("Arial", 50))
consonant_label.pack(pady=20)

flip_button = tk.Button(root, text="Flip", command=flip_card, font=("Arial", 14))
flip_button.pack()

meaning_label = tk.Label(root, text="", font=("Arial", 16))
meaning_label.pack(pady=10)

next_button = tk.Button(root, text="Next", command=show_new_consonant, font=("Arial", 14))
next_button.pack()

# Show the first consonant
show_new_consonant()

# Start the application loop
