import main
import tkinter as tk

root = tk.Tk()
root.title("Sentence Transformation Program")
root.resizable(False, False)
WIDTH = 800
HEIGHT = 500
root.config(bg="#D9E4E4")
root.geometry(f"{WIDTH}x{HEIGHT}")

result_label = tk.Label(
    root,
    text="",
    font="LucidaSans 18",
    bg="#D9E4E4",
    fg="black",
    wraplength=WIDTH - 100,
    justify="center",
    relief="raised"
)

def transform_input_sentence(sentence, tense):
    transformed_sentence = main.program(sentence, tense) if sentence!="Enter a sentence here..." and tense!="Enter a tense here..." else "Please enter valid inputs."
    result_label.config(text=transformed_sentence,
    bg="#BDF9F9",
    fg="black",
    wraplength=WIDTH - 100,
    justify="center")

    result_label.place(x=WIDTH//2-result_label.winfo_reqwidth()//2, y=400)


title_label = tk.Label(root, text="Sentence Transformation Program",
                       font="LucidaSans 20 bold", bg="white", fg="black",
                       relief="sunken")
title_label.place(x=WIDTH//2-title_label.winfo_reqwidth()//2, y=30)

instructions:str = main.__doc__
instructions_label = tk.Label(
    root, text=instructions, font="LucidaSans 15", bg="#D9E4E4", fg="black",
    wraplength=WIDTH-100, justify="center")
instructions_label.place(x=WIDTH//2-instructions_label.winfo_reqwidth()//2, y=80)

input_sentence = tk.StringVar(value="Enter a sentence here...")
sentence_entry = tk.Entry(root,textvariable=input_sentence ,font="LucidaSans 15", width=50)
sentence_entry.place(x=WIDTH//2-sentence_entry.winfo_reqwidth()//2, y=200)

def clear_if_placeholder_sentence(_):
    if sentence_entry.get() == "Enter a sentence here...":
        sentence_entry.delete(0, tk.END)

sentence_entry.bind("<FocusIn>", clear_if_placeholder_sentence)

input_tense = tk.StringVar(value="Enter a tense here...")
tense_entry = tk.Entry(root,textvariable=input_tense ,font="LucidaSans 15", width=20)
tense_entry.place(x=WIDTH//2-tense_entry.winfo_reqwidth()//2, y=250)

def clear_if_placeholder_tense(_):
    if tense_entry.get() == "Enter a tense here...":
        tense_entry.delete(0, tk.END)

tense_entry.bind("<FocusIn>", clear_if_placeholder_tense)

button = tk.Button(
    root,
    text="Transform",
    font="LucidaSans 15 bold",
    bg="#4CAF50",
    fg="white",
    command = lambda: transform_input_sentence(input_sentence.get(), input_tense.get())
)

button.place(x=WIDTH//2-button.winfo_reqwidth()//2, y=300)

root.mainloop()
