import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    # Get the user inputs for password length and character selection
    length = length_entry.get()
    
    if not length.isdigit() or int(length) <= 0:
        output_label.config(text="Please enter a valid length.")
        return

    length = int(length)
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    character_set = ''
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        output_label.config(text="Select at least one character type.")
        return
    
    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    output_label.config(text=password)

def copy_to_clipboard():
    password = output_label.cget("text")
    if password:
        pyperclip.copy(password)
        output_label.config(text="Password copied to clipboard!")
    else:
        output_label.config(text="No password generated.")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")  # Increased height for better layout


tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)


upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
output_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)


root.mainloop()
