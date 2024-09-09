import tkinter as tk
from tkinter import filedialog

class SecNotesEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("SecNotes")
        self.root.geometry("1920x1080")

        self.light_mode = False
        
        self.toggle_button = tk.Button(root, text='Dark Mode', command=self.toggle_theme, relief=tk.RAISED)
        self.toggle_button.place(relx=1.0, x=-60, y=10, anchor='ne')  

        self.exit_button = tk.Button(root, text='X', command=root.destroy, relief=tk.RAISED)
        self.exit_button.place(relx=1.0, x=-10, y=10, anchor='ne')

        self.info_label = tk.Label(root, text="Welcome to SecNotes!", bg='white', fg='black')
        self.info_label.pack(pady=10)

        self.text_box = tk.Text(root, wrap='word', height=70, width=100)
        self.text_box.pack(padx=10, pady=40)

        self.root.bind('<Control-s>', self.save_file)

        self.set_dark_theme()

    def toggle_theme(self):
        if self.light_mode:
            self.set_dark_theme()
        else:
            self.set_light_theme()
        self.light_mode = not self.light_mode

    def set_light_theme(self):
        self.root.config(bg='white')
        self.toggle_button.config(text='Dark Mode', bg='lightgray', fg='black')
        self.info_label.config(bg='white', fg='black')
        self.text_box.config(bg='white', fg='black', insertbackground='black')  # Cursor color
        self.exit_button.config(text='X', bg='lightgray', fg='black')

    def set_dark_theme(self):
        self.root.config(bg='#282828')
        self.toggle_button.config(text='Light Mode', bg='#323232', fg='white')
        self.info_label.config(bg='#282828', fg='white')
        self.text_box.config(bg='#383838', fg='white', insertbackground='white')  # Cursor color
        self.exit_button.config(text='X', bg='#a60000', fg='white')

    def save_file(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:  
            with open(file_path, 'w') as file:
                content = self.text_box.get("1.0", tk.END) 
                file.write(content)
            print(f"File saved as: {file_path}")  

if __name__ == "__main__":
    root = tk.Tk()
    app = SecNotesEditor(root)
    root.mainloop()
