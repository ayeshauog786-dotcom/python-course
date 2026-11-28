from tkinter import *
window = Tk()
window.title("Fatima's profile card")
window.geometry("400x380")

title_label=Label(window, text="Fatima's profile card", bg="red", fg="white").grid(row=0, column=0, columnspan=2)
name_label=Label(window, text="Name", bg="red", fg="white").grid(row=1, column=0, columnspan=2)
name_entry=Entry(window, bg="red").grid(row=1, column=2, columnspan=2)

hobby_label=Label(window, text="Hobby", bg="red", fg="white").grid(row=2, column=0, columnspan=2)
hobby_entry=Entry(window, bg="red").grid(row=2, column=2, columnspan=2)

frame =Frame(window, relief=RAISED, borderwidth=3)
frame.grid(row=3, column=0, columnspan=2)
about_label=Label(frame, text="About me").pack()
about_text=Text(frame, width=35, height=4, bg="lightyellow").pack

Button(window, text="show my card", bg="purple", fg="white").grid(row=4, column=0, columnspan=2)


window.mainloop()