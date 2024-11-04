import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import logic as lgc




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # main window
        ctk.set_appearance_mode("dark")
        self.geometry("1200x700")
        self.title("Programming systems project")

        # widgets frame
        input_frame = ctk.CTkFrame(self, fg_color="#242424")
        input_frame.pack(pady=20, padx=20, fill="both", expand=False)

        # start label
        self.starting_address_label = ctk.CTkLabel(input_frame, text="Starting address:")
        self.starting_address_label.grid(row=0, column=0, padx=(10, 10), sticky="w")

        # start textbox
        self.starting_address_entry = ctk.CTkEntry(input_frame)
        self.starting_address_entry.grid(row=0, column=1, padx=(0, 10), sticky="ew")

        # length label
        self.length_label = ctk.CTkLabel(input_frame, text="Length:")
        self.length_label.grid(row=0, column=2, padx=(10, 10), sticky="w")

        # length textbox
        self.length_entry = ctk.CTkEntry(input_frame)
        self.length_entry.grid(row=0, column=3, padx=(0, 10), sticky="ew")

        # print button
        self.print_button = ctk.CTkButton(input_frame, text="Print", command=self.action)
        self.print_button.grid(row=0, column=4, padx=(30, 0), sticky="w")

        # responsive grid cells
        input_frame.columnconfigure(4, weight=1)

        # table frame
        table_frame = ctk.CTkScrollableFrame(self, corner_radius=15, fg_color="#2B2B2B")
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # table label
        self.table_label = ctk.CTkLabel(table_frame, text="Table will be printed here", anchor="center")
        self.table_label.pack(pady=20, padx=20, fill="both", expand=True)

    def throw_IncorrectStartingAddressError(self):
        tk.messagebox.showerror(title="Incorrect starting address error", message="Enter valid starting address (0-2047)")
        self.starting_address_entry.delete(0, "end")

    def throw_IncorrectLengthError(self):
        tk.messagebox.showerror(title="Incorrect length error", message="Enter valid length (0-2047)")
        self.length_entry.delete(0, "end")

    def throw_OutOfBoundsError(self):
        tk.messagebox.showerror(title="Out of bounds error", message="Enter valid numbers (0-2047)")

    def action(self):
        st = self.starting_address_entry.get()
        ln = self.length_entry.get()
        if not check(st): self.throw_IncorrectStartingAddressError()
        elif not check(ln): self.throw_IncorrectLengthError()
        elif not check_possible(st, ln): self.throw_OutOfBoundsError()
        else:
            obj = lgc.Logic(st, ln)
            self.table_label.configure(text=obj.generateTable(), anchor='nw', justify='left')

def try_parse_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def check(num):
    if num.strip()=='': return False
    if not try_parse_int(num): return False
    elif not int(num)>0 and int(num)<2047: return False
    return True

def check_possible(s, l):
    if (int(s)+int(l)) > 2048: return False
    return True