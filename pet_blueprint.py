import tkinter as tk

class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    def set_name(self, name): self.__name = name
    def set_animal_type(self, animal_type): self.__animal_type = animal_type
    def set_age(self, age): self.__age = age

    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age

class PetDashboard:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Pet Registry")
        self.main_window.geometry("350x400")
        self.main_window.configure(bg="#0b0c10")
        self.my_pet = Pet()

    def build_user_interface(self):
        tk.Label(self.main_window, text="PET REGISTRY", background="#0b0c10", foreground="#66fcf1", font=("Helvetica", 16, "bold")).pack(pady=(20, 10))

        tk.Label(self.main_window, text="Pet Name:", background="#0b0c10", foreground="white").pack()
        self.entry_name = tk.Entry(self.main_window, justify="center", background="#1f2833", foreground="#66fcf1", insertbackground="white")
        self.entry_name.pack(pady=5)

        tk.Label(self.main_window, text="Animal Type (e.g. Dog, Cat):", background="#0b0c10", foreground="white").pack()
        self.entry_type = tk.Entry(self.main_window, justify="center", background="#1f2833", foreground="#66fcf1", insertbackground="white")
        self.entry_type.pack(pady=5)

        tk.Label(self.main_window, text="Age:", background="#0b0c10", foreground="white").pack()
        self.entry_age = tk.Entry(self.main_window, justify="center", background="#1f2833", foreground="#66fcf1", insertbackground="white")
        self.entry_age.pack(pady=5)

        tk.Button(self.main_window, text="Save Data", background="#45a29e", foreground="white", command=self.save_pet_data).pack(pady=15)

        self.result_label = tk.Label(self.main_window, text="Waiting for input...", background="#0b0c10", foreground="#c5c6c7", font=("Courier", 10))
        self.result_label.pack(pady=10)