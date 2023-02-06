
import tkinter as tk
from tkinter import filedialog
import text_correction

def select_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        text = f.read()
        
    corrected_text = text_correction.correct_text(text)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, corrected_text)
    
# GUI
root = tk.Tk()
root.title("Text Correction Tool")
root.geometry("400x400")

select_file_button = tk.Button(root, text="Select Text File", command=select_file)
select_file_button.pack()

result_text = tk.Text(root)
result_text.pack()

root.mainloop()
