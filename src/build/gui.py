from tkinter import Tk, Canvas, Button, Frame, PhotoImage, StringVar, IntVar
import tkinter as tk
from tkinter.ttk import Combobox, Spinbox, Label
from tkinter import messagebox as msg
from gui3 import ControlPointFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os, time
from bruteForce import bezier_curve_bf
from divideandconquer import bezier_curve_dnc
from divideandconquergenap import bezier_curve_dncG
from matplotlib.animation import FuncAnimation

controlpoints = []
fig = None
canvas = None

def relative_to_assets(file_path):
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    return os.path.join(assets_dir, file_path)

def plot():
    global controlpoints, spintint, curveCount, seconds, fig, canvas, ax
    if (len(controlpoints) == 0):
        msg.showerror("Error", "Please add control points")
        return
    
    start = time.time()
    if (algorithm_var.get() == "Divide and Conquer"):
        if len(controlpoints) % 2 == 0:
            curve_points = bezier_curve_dncG(controlpoints, spintint.get(), 0, 0)
        else:
            curve_points = bezier_curve_dnc(controlpoints, spintint.get(), 0)
        framez = spintint.get()
        intervalz = 600
    else:
        curve_points = bezier_curve_bf(controlpoints, spintint.get())
        framez = len(curve_points) 
        intervalz = 50
    duration = time.time() - start

    if fig:
        plt.close(fig)
    if canvas:
        canvas.get_tk_widget().destroy()

    def update(frame):
        nonlocal line
        if (algorithm_var.get() == "Divide and Conquer"):
            if len(controlpoints) % 2 == 0:
                curves = bezier_curve_dncG(controlpoints, frame+1, 0, 0)
            else:
                curves = bezier_curve_dnc(controlpoints, frame+1, 0)
        else:
            curves = bezier_curve_bf(controlpoints, spintint.get())

            curves = curves[:frame+1]

        line.set_data([x for x, _ in curves], [y for _, y in curves])
        return line,
    
    fig, ax = plt.subplots(figsize=(5, 4.5), facecolor="#910A67", dpi = 100)

    ax.set_facecolor("#910A67")
    ax.set_xlabel('X', color="white")
    ax.set_ylabel('Y', color="white")
    ax.set_title('Bezier Curve', color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(True, color="white", linestyle="--", linewidth=0.8)

    ax.plot([x for x, _ in controlpoints], [y for _, y in controlpoints], linestyle = "dotted", linewidth = 1, color="#190482", marker="o")
    for (x, y) in controlpoints:
        x, y = round(x, 2), round(y, 2)
        ax.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color="white")

    line, = ax.plot([], [], linestyle="solid", linewidth=3, color="#A5A6F5")

    if toggle_state.get() and spintint.get() > 0:
        ani = FuncAnimation(fig, update, frames=framez, interval=intervalz, repeat=False)
    else:
        ax.plot([x for x, _ in curve_points], [y for _, y in curve_points], linestyle = "solid", linewidth = 3, color="#A5A6F5")

    canvas = FigureCanvasTkAgg(fig, master=frame3)
    canvas.draw()
    canvas.get_tk_widget().place(x=79, y=152)

    canvas3.itemconfigure(seconds_text, text=str(duration) + " seconds")

def page_one():
    show_frame(frame1)

def page_two():
    show_frame(frame2)

def page_three():
    show_frame(frame3)

def show_frame(frame):
    frame.tkraise()

def handle_submit(control_points):
    global controlpoints, canvas, fig
    if fig:
        plt.close(fig)
    if canvas:
        canvas.get_tk_widget().destroy()
    
    controlpoints = control_points
    fig, ax = plt.subplots(figsize=(5, 4.5), facecolor="#910A67", dpi = 100)
    ax.plot([x for x, _ in control_points], [y for _, y in control_points], linestyle = "dotted",linewidth =1, color="#190482", marker="o")
    ax.set_facecolor("#910A67")

    ax.set_xlabel('X', color="white")
    ax.set_ylabel('Y', color="white")
    ax.set_title('Bezier Curve', color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(True, color="white", linestyle="--", linewidth=0.8)
    
    for (x, y) in control_points:
        x, y = round(x, 2), round(y, 2)
        ax.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color="white")
    
    canvas = FigureCanvasTkAgg(fig, master=frame3)
    canvas.draw()
    canvas.get_tk_widget().place(x=79, y=152)

def popup_control_point_frame():
    popup = tk.Toplevel(window)
    popup.title("Add Points")
    popup.resizable(False, False)
    control_point_frame = ControlPointFrame(popup)
    control_point_frame.callback = handle_submit
    control_point_frame.pack()

def button_12_hover(e):
    button_12.config(
        image=button_image_hover_12
    )
def button_12_leave(e):
    button_12.config(
        image=button_image_12
    )

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

def button_1_hover(e):
    button_1.config(
    image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
    image=button_image_1
    )

def button_13_hover(e):
    button_13.config(
        image=button_image_hover_13
    )
def button_13_leave(e):
    button_13.config(
        image=button_image_13
    )

def button_23_hover(e):
    button_23.config(
        image=button_image_hover_23
    )
def button_23_leave(e):
    button_23.config(
        image=button_image_23
    )

def button_33_hover(e):
    button_33.config(
        image=button_image_hover_33
    )
def button_33_leave(e):
    button_33.config(
        image=button_image_33
    )

window = Tk()
window.title("Bezier This Curve")
window.geometry("1088x773")
window.configure(bg="#190482")

# Frame 1
frame1 = Frame(window, bg="#190482")
frame1.place(relwidth=1, relheight=1)

canvas1 = Canvas(
    frame1,
    bg="#190482",
    height=773,
    width=1088,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas1.place(x=0, y=0)

canvas1.create_text(
    538.0,
    107.0,
    anchor="nw",
    text="Curve.",
    fill="#FFFFFF",
    font=("JacquesFrancois Regular", 100 * -1)
)

canvas1.create_text(
    227.0,
    107.0,
    anchor="nw",
    text="Bezier",
    fill="#C2D9FF",
    font=("JacquesFrancois Regular", 100 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("frame0\\image_1.png"))

image_1 = canvas1.create_image(
    80.999999165535,
    644.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("frame0\\image_2.png"))
image_2 = canvas1.create_image(
    1042.0,
    713.0,
    image=image_image_2
)

canvas1.create_text(
    230.0,
    52.0,
    anchor="nw",
    text="create",
    fill="#7752FE",
    font=("Poppins Regular", 50 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("frame0\\image_3.png"))
image_3 = canvas1.create_image(
    844.0001831054688,
    176.00003051757812,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("frame0\\button_1.png"))
button_1 = Button(
    frame1,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=page_three,
    relief="flat"
)
button_1.place(
    x=366.0,
    y=313.0,
    width=354.0,
    height=109.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("frame0\\button_2.png"))
button_2 = Button(
    frame1,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=page_two,
    relief="flat"
)
button_2.place(
    x=366.0,
    y=456.0,
    width=354.0,
    height=111.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("frame0\\button_hover_1.png"))

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("frame0\\button_hover_2.png"))

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)

# Frame 2
frame2 = Frame(window, bg="#190482")
frame2.place(relwidth=1, relheight=1)

canvas2 = Canvas(
    frame2,
    bg="#190482",
    height=773,
    width=1088,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas2.place(x=0, y=0)

image_image_12 = PhotoImage(
    file=relative_to_assets("frame2\image_1.png"))
image_12 = canvas2.create_image(
    544.0,
    387.0,
    image=image_image_12
)

image_image_22 = PhotoImage(
    file=relative_to_assets("frame2\image_2.png"))
image_22 = canvas2.create_image(
    126.0,
    650.0,
    image=image_image_22
)

image_image_32 = PhotoImage(
    file=relative_to_assets("frame2\image_3.png"))
image_32 = canvas2.create_image(
    292.0,
    500.0,
    image=image_image_32
)

image_image_42 = PhotoImage(
    file=relative_to_assets("frame2\image_4.png"))
image_42 = canvas2.create_image(
    302.0,
    62.0,
    image=image_image_42
)

canvas2.create_text(
    283.0,
    64.0,
    anchor="nw",
    text="How to use",
    fill="#C2D9FF",
    font=("JacquesFrancois Regular", 100 * -1)
)

image_image_52 = PhotoImage(
    file=relative_to_assets("frame2\image_5.png"))
image_52 = canvas2.create_image(
    544.0,
    387.0,
    image=image_image_52
)

button_image_12 = PhotoImage(
    file=relative_to_assets("frame2\\button_1.png"))
button_12 = Button(
    frame2,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=page_three,
    relief="flat"
)
button_12.place(
    x=395.0,
    y=630.0,
    width=297.0,
    height=91.44915008544922
)

button_image_hover_12 = PhotoImage(
    file=relative_to_assets("frame2\\button_hover_1.png"))

button_12.bind('<Enter>', button_12_hover)
button_12.bind('<Leave>', button_12_leave)

image_image_62 = PhotoImage(
    file=relative_to_assets("frame2\image_6.png"))
image_62 = canvas2.create_image(
    284.0,
    280.0,
    image=image_image_62
)

image_image_72 = PhotoImage(
    file=relative_to_assets("frame2\image_7.png"))
image_72 = canvas2.create_image(
    814.0,
    500.0,
    image=image_image_72
)

image_image_82 = PhotoImage(
    file=relative_to_assets("frame2\image_8.png"))
image_82 = canvas2.create_image(
    812.0,
    280.0,
    image=image_image_82
)

image_image_92 = PhotoImage(
    file=relative_to_assets("frame2\image_9.png"))
image_92 = canvas2.create_image(
    543.0000591998146,
    275.0,
    image=image_image_92
)

image_image_102 = PhotoImage(
    file=relative_to_assets("frame2\image_10.png"))
image_102 = canvas2.create_image(
    265.0,
    397.99999930648755,
    image=image_image_102
)

image_image_112 = PhotoImage(
    file=relative_to_assets("frame2\image_11.png"))
image_112 = canvas2.create_image(
    685.6284596606265,
    439.88116018123674,
    image=image_image_112
)

image_image_122 = PhotoImage(
    file=relative_to_assets("frame2\image_12.png"))
image_122 = canvas2.create_image(
    59.0,
    231.0,
    image=image_image_122
)

#frame 3
frame3 = Frame(window, bg="#190482")
frame3.place(relwidth=1, relheight=1)

canvas3 = Canvas(
    frame3,
    bg="#190482",
    height=773,
    width=1088,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas3.place(x=0, y=0)

image_image_13 = PhotoImage(
    file=relative_to_assets("frame1\image_1.png"))
image_13 = canvas3.create_image(
    544.0,
    387.0,
    image=image_image_13
)

image_image_23 = PhotoImage(
    file=relative_to_assets("frame1\image_2.png"))
image_23 = canvas3.create_image(
    855.0,
    377.0,
    image=image_image_23
)

image_image_33 = PhotoImage(
    file=relative_to_assets("frame1\image_3.png"))
image_33 = canvas3.create_image(
    194.0,
    43.0,
    image=image_image_33
)

image_image_43 = PhotoImage(
    file=relative_to_assets("frame1\image_4.png"))
image_43 = canvas3.create_image(
    330.0,
    377.0,
    image=image_image_43
)

button_image_13 = PhotoImage(
    file=relative_to_assets("frame1\\button_1.png"))
button_13 = Button(
    frame3,
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=page_two,
    relief="flat"
)
button_13.place(
    x=873.0,
    y=17.0,
    width=175.0,
    height=54.87287902832031
)

button_image_hover_13 = PhotoImage(
    file=relative_to_assets("frame1\\button_hover_1.png"))

button_13.bind('<Enter>', button_13_hover)
button_13.bind('<Leave>', button_13_leave)

image_image_53 = PhotoImage(
    file=relative_to_assets("frame1\\image_5.png"))
image_53 = canvas3.create_image(
    330.0,
    711.0,
    image=image_image_53
)

canvas3.create_text(
    168,
    680,
    anchor="nw",
    text="created in",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 26 * -1)
)

seconds = IntVar()
seconds.set(0)
seconds_text = canvas3.create_text(
    168,
    717,
    anchor="nw",
    text=str(seconds.get()) + " seconds",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 26 * -1)
)

button_image_23 = PhotoImage(
    file=relative_to_assets("frame1\\button_2.png"))
button_23 = Button(
    frame3,
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=popup_control_point_frame,
    relief="flat"
)
button_23.place(
    x=740.0,
    y=162.0,
    width=232.0,
    height=61.0
)

button_image_hover_23 = PhotoImage(
    file=relative_to_assets("frame1\\button_hover_2.png"))

button_23.bind('<Enter>', button_23_hover)
button_23.bind('<Leave>', button_23_leave)


button_image_33 = PhotoImage(
    file=relative_to_assets("frame1\\button_3.png"))
button_33 = Button(
    frame3,
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=plot,
    relief="flat"
)
button_33.place(
    x=770.0,
    y=528.0,
    width=174.0,
    height=61.0
)

button_image_hover_33 = PhotoImage(
    file=relative_to_assets("frame1\\button_hover_3.png"))

button_33.bind('<Enter>', button_33_hover)
button_33.bind('<Leave>', button_33_leave)

canvas3.create_text(
    793,
    247.0,
    anchor="nw",
    text="Select method",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 20 * -1)
)

algorithm_var = StringVar()
algorithm_var.set("Divide and Conquer")
algorithm_combobox = Combobox(
    frame3,
    values=["Divide and Conquer", "Brute Force"],
    textvariable=algorithm_var,
    state="readonly",
    width=30,
)
algorithm_combobox.bind("<<ComboboxSelected>>", lambda e: print(algorithm_var.get()))
algorithm_combobox.place(x=749.0, y=285)

algorithm_combobox_label = Label(
    frame3,
    textvariable= algorithm_var,
    font=("SourceSerifPro Regular", 20 * -1),
    background="#3C0753",
    foreground="#FFFFFF"
)

algorithm_combobox_label.place(x=79.0, y=120)

canvas3.create_text(
    803,
    354.0,
    anchor="nw",
    text="Set iteration",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 20 * -1)
)

spinbox = Spinbox(frame3, from_=0, to = 1000, increment=1, width=30)
spinbox.set(0)
spinbox.place(x=749, y=395)
spinbox.bind("<Return>", lambda e: spintint.set(spinbox.get()))

spintint = IntVar()

spintint_label = Label(
    frame3,
    textvariable= spintint,
    font=("SourceSerifPro Regular", 20 * -1),
    background="#3C0753",
    foreground="#FFFFFF"
)

spintint_label.place(x=410.0, y=120)

def toggle():
    global toggle_state
    if toggle_state.get():
        toggle_state.set(False)
        toggle_button.config(text="OFF", bg="#FF0707")
    else:
        toggle_state.set(True)
        toggle_button.config(text="ON", bg="#5FE131")

toggle_state = tk.BooleanVar()
toggle_state.set(False)

# Create the toggle button
toggle_button = tk.Button(frame3, text="OFF", command=toggle, bg="#FF0707", width=10)
toggle_button.place(x=810.0, y=473)

canvas3.create_text(
    810,
    440,
    anchor="nw",
    text="Animation",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 20 * -1)
)

canvas3.create_text(
    320.0,
    120,
    anchor="nw",
    text= f"Iterations:",
    fill="#FFFFFF",
    font=("SourceSerifPro Regular", 20 * -1)
)

show_frame(frame1)

window.resizable(False, False)
window.mainloop()
