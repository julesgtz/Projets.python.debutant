import tkinter as tk
import random

class Wordle:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle")
        self.entries = []
        self.compteur = 0

        self.error_entries = []
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            self.list_words = [line.strip() for line in lines]

        self.get_new_word()

        for _ in range(6):
            entry = tk.Entry(root, width=20, font=("Arial", 14), validate='key')
            entry.config(validatecommand=(entry.register(self.validate_entry), '%P'))
            entry.grid(row=_, column=0, pady=5)
            self.entries.append(entry)

        for __ in range(6):
            entry = tk.Text(root, width=20, height=1,font=("Arial", 14))
            entry.tag_config('wrong_place',foreground="yellow")
            entry.tag_config('wrong',foreground="red")
            entry.tag_config('good_place',foreground="green")
            entry.grid(row=__, column=2, pady=5)
            self.error_entries.append(entry)


        self.clavier = 'azertyuiopqsdfghjklmwxcvbn'
        self.buttons = []
        row = _+1
        col = 3
        for letter in self.clavier:
            button = tk.Button(root, width=5, height=2, font=("Arial", 12), text=letter, command=lambda l=letter: self.button_click(l))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

            col += 1
            if letter == "p" or letter == "m":
                col = 3
                row += 1

        enter_button = tk.Button(root, text="Entrée", command=self.enter_click)
        enter_button.grid(row=row, column=col, padx=5, pady=5)
        self.buttons.append(enter_button)

        col += 1
        delete_button = tk.Button(root, text="Supprimer", command=self.delete_click)
        delete_button.grid(row=row, column=col, padx=5, pady=5)
        self.buttons.append(delete_button)

        print(f"mot a deviner : {self.word}")



    def get_new_word(self):
        self.word = str(self.list_words[random.randint(0, len(self.list_words)-1)])

    def button_click(self, letter):
        self.entries[self.compteur].insert(tk.END, letter)

    def enter_click(self):
        nb_letter = 0
        if len(self.entries[self.compteur].get()) != len(self.word):
            self.error_entries[self.compteur].delete('1.0', 'end')
            self.error_entries[self.compteur].insert(tk.END, "mauvaise taille", 'wrong')
        elif not self.entries[self.compteur].get() in self.list_words:
            self.error_entries[self.compteur].delete('1.0', 'end')
            self.error_entries[self.compteur].insert(tk.END, "mot existe pas", 'wrong')
        elif self.entries[self.compteur].get() == self.word:
            self.error_entries[self.compteur].insert(tk.END, self.word, 'good_place')
        else:
            self.error_entries[self.compteur].delete('1.0', 'end')
            for index, letter in enumerate(self.entries[self.compteur].get()):
                if letter == self.word[index]:
                    self.error_entries[self.compteur].insert(tk.END, letter, 'good_place')
                elif not letter in self.word:
                    self.error_entries[self.compteur].insert(tk.END, letter, 'wrong')
                else:
                    self.error_entries[self.compteur].insert(tk.END, letter, 'wrong_place')


            self.compteur = self.compteur + 1

    def delete_click(self):
        self.entries[self.compteur].delete(len(self.entries[self.compteur].get())-1, tk.END)

    def validate_entry(self, new_value):
        if len(new_value) <= len(self.word):
            return True
        else:
            return False

root = tk.Tk()
c = Wordle(root)
root.mainloop()
