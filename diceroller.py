import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Dice Roll Generator")
        self.root.geometry("400x500")
        
        # Load background image
        image_path = "dice.jpg"
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((400, 500), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)
        
        self.dice_labels = {
            2: "2-sided", 4: "4-sided", 6: "6-sided", 8: "8-sided",
            10: "10-sided", 12: "12-sided", 20: "20-sided"
        }
        
        self.dice_entries = {}
        for i, (sides, label) in enumerate(self.dice_labels.items()):
            ttk.Label(root, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(root, width=5)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.dice_entries[sides] = entry
        
        self.advantage_var = tk.BooleanVar()
        self.advantage_check = ttk.Checkbutton(root, text="Advantage?", variable=self.advantage_var)
        self.advantage_check.grid(row=len(self.dice_labels), column=0, columnspan=2, pady=5)
        
        self.roll_button = ttk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=len(self.dice_labels) + 1, column=0, columnspan=2, pady=10)
        
        self.result_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
        self.result_text.grid(row=len(self.dice_labels) + 2, column=0, columnspan=2, pady=10)
        
    def roll_dice(self):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        
        for sides, entry in self.dice_entries.items():
            try:
                num_dice = int(entry.get()) if entry.get() else 0
                if num_dice > 0:
                    rolls = [random.randint(1, sides) for _ in range(num_dice)]
                    
                    self.result_text.insert(tk.END, f"{self.dice_labels[sides]}: ")
                    total = sum(rolls)
                    
                    if self.advantage_var.get():
                        highest_roll = max(rolls)
                        lowest_roll = min(rolls)
                        
                        for roll in rolls:
                            if roll == highest_roll:
                                self.result_text.insert(tk.END, f"{roll} ", "green")
                            elif roll == lowest_roll:
                                self.result_text.insert(tk.END, f"{roll} ", "red")
                            else:
                                self.result_text.insert(tk.END, f"{roll} ", "black")
                    else:
                        for roll in rolls:
                            self.result_text.insert(tk.END, f"{roll} ", "black")
                        self.result_text.insert(tk.END, f"Total: {total}", "black")
                    
                    self.result_text.insert(tk.END, "\n")
            except ValueError:
                pass  # Ignore invalid input
        
        self.result_text.tag_config("green", foreground="green")
        self.result_text.tag_config("red", foreground="red")
        self.result_text.tag_config("black", foreground="black")
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
