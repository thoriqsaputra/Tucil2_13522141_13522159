import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

class ControlPointFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="white")
        
        self.canvas = tk.Canvas(self, width=440, bg="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.points = []
        self.add_control_point()
        
        self.add_button = ttk.Button(self, text="Add Point", command=self.add_control_point)
        self.add_button.grid(row=1, column=0, pady=10)
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, pady=10)
        
    def add_control_point(self):
        idx = len(self.points) + 1
        label = tk.Label(self.scrollable_frame, text=f"Point {idx}:", bg="white")
        label.grid(row=idx, column=0, padx=5, pady=5)
        x_entry = ttk.Entry(self.scrollable_frame)
        x_entry.grid(row=idx, column=1, padx=5, pady=5)
        y_entry = ttk.Entry(self.scrollable_frame)
        y_entry.grid(row=idx, column=2, padx=5, pady=5)
        delete_button = ttk.Button(self.scrollable_frame, text="Delete", command=lambda i=idx: self.delete_control_point(i))
        delete_button.grid(row=idx, column=3, padx=5, pady=5)
        self.points.append((label, x_entry, y_entry, delete_button))

    def delete_control_point(self, idx):
        control_point = self.points.pop(idx - 1)
        for widget in control_point:
            widget.grid_forget()

        for i, (lbl, x_entry, y_entry, delete_button) in enumerate(self.points[idx-1:], start=idx):
            lbl.grid(row=i, column=0, padx=5, pady=5)
            x_entry.grid(row=i, column=1, padx=5, pady=5)
            y_entry.grid(row=i, column=2, padx=5, pady=5)
            delete_button.grid(row=i, column=3, padx=5, pady=5)
            delete_button.configure(command=lambda j=i: self.delete_control_point(j+1))
        
    def submit(self):
        control_points_data = []
        for _, x_entry, y_entry, _ in self.points:
            x = x_entry.get()
            y = y_entry.get()
            if x and y:
                try:
                    x = float(x)
                    y = float(y)
                    control_points_data.append((x, y))
                except ValueError:
                    msg.showerror("Error", "Control points must be numbers.")
                    self.master.grab_set()
                    return
            else:
                msg.showerror("Error", "All fields must be filled.")
                self.master.grab_set()
                return
        
        self.callback(control_points_data)
        
    def set_callback(self, callback):
        self.callback = callback
