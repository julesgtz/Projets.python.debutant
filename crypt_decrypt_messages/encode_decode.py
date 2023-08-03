import random
import tkinter as tk

class Message:
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..'}
    morse_inv = {key: value for value, key in morse.items()}
    points = 'abcdefghi'
    tirets = 'nopqrstuv'
    separator = 'xyzklmwj'
    def __init__(self, root):
        self.root = root
        self.root.title("Message Encoder / Decoder")

        self.input_text = tk.Text(height=5)
        self.input_text.pack(padx=10, pady=10)

        self.button_frame = tk.Frame()
        self.button_frame.pack()

        self.reset_button = tk.Button(self.button_frame, text="Réinitialiser", command=self.reset)
        self.reset_button.pack(side="left")

        self.convert_button = tk.Button(self.button_frame, text="Convertir", command=self.convert)
        self.convert_button.pack(side="left")

        self.result_text = tk.Text(height=5)
        self.result_text.pack(pady=10)

    def isencoded(self):
        if self.input_text.get("1.0", tk.END)[0:2] == '$/':
            return True
        else:
            return False


    def reset(self):
        self.input_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)

    def convert(self):
        self.result_text.delete("1.0", tk.END)
        if self.isencoded():
            word = ""
            _ = []
            for letter in self.input_text.get("1.0", tk.END).strip()[2:] + " ":
                if letter in self.points:
                    word = word + "."
                elif letter in self.tirets:
                    word = word + "-"
                elif letter == " ":
                    _.append("space")
                else:
                    _.append(word)
                    word = ""
            decoded = []
            letter = ""
            for word in _:
                if word != "space":
                    try:
                        letter = letter + self.morse_inv[word]
                    except:
                        letter = letter + "APAGNAN"
                else:
                    decoded.append(letter)
                    letter = ""
            sentance = " ".join(decoded)
            self.result_text.insert(tk.END, sentance.lower())


        else:
            word = ""
            _ = []
            for letter in self.input_text.get("1.0", tk.END).strip() + " ":
                if letter == " ":
                    _.append(word)
                    word = ""
                else:
                    word = word + self.morse[letter.upper()] + "|"
            encoded = []
            for word in _:
                new_word = ""
                for char in word + " ":
                    if char == "-":
                        new_word = new_word + random.choice(self.tirets)
                    elif char == ".":
                        new_word = new_word + random.choice(self.points)
                    elif char == "|":
                        new_word = new_word + random.choice(self.separator)
                    else:
                        encoded.append(new_word)
            sentance = "$/"+" ".join(encoded)
            self.result_text.insert(tk.END, sentance)





root = tk.Tk()
c = Message(root)
root.mainloop()
