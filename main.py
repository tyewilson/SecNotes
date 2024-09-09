import tkinter as tk

class SecNotesEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("SecNotes")
        self.root.geometry("1920x1080")

        self.light_mode = False
        
        self.toggle_button = tk.Button(root, text='Dark Mode', command=self.toggle_theme, relief=tk.RAISED)
        self.toggle_button.place(relx=1.0, x=-10, y=10, anchor='ne')  

        self.info_label = tk.Label(root, text="Welcome to SecNotes!", bg='white', fg='black')
        self.info_label.pack(pady=10)

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

    def set_dark_theme(self):
        self.root.config(bg='#282828')
        self.toggle_button.config(text='Light Mode', bg='#323232', fg='white')
        self.info_label.config(bg='#282828', fg='white')

if __name__ == "__main__":
    root = tk.Tk()
    app = SecNotesEditor(root)
    root.mainloop()
