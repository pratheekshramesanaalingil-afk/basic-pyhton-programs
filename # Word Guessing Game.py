import tkinter as tk
from tkinter import messagebox
import random

# List of possible words
word_list = ["python", "coding", "tkinter", "program", "computer"]

# Randomly select a word
word = random.choice(word_list)

guessed_letters = []
attempts = 6

# Create main window
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x300")

# Functions
def update_display():
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label.config(text=display_word)
    attempts_label.config(text=f"Attempts left: {attempts}")

def guess_letter():
    global attempts
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
        return

    if guess in guessed_letters:
        attempts -= 1
        messagebox.showinfo("Repeated Guess", "Repeated letter! Attempt reduced.")
    else:
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            messagebox.showinfo("Wrong Guess", "Wrong letter!")

    update_display()

    if "_" not in word_label.cget("text"):
        messagebox.showinfo("Winner", "Congratulations! You guessed the word 🎉")
        root.quit()

    if attempts == 0:
        messagebox.showerror("Game Over", f"Game Over! The word was '{word}'")
        root.quit()

# UI Elements
title_label = tk.Label(root, text="Word Guessing Game", font=("Arial", 16))
title_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 18))
word_label.pack(pady=10)

attempts_label = tk.Label(root, text="")
attempts_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=5)

# Initialize display
update_display()

# Run the app
root.mainloop()
