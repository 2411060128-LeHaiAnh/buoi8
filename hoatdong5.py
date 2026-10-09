import tkinter as tk


def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    if not ho_ten or not tuoi or not email:
        nhan_ket_qua.config(
            text="Vui long nhap day du thong tin!",
            fg="red"
        )
        return

    try:
        tuoi_so = int(tuoi)
        if tuoi_so <= 0:
            raise ValueError
    except ValueError:
        nhan_ket_qua.config(
            text="Tuoi phai la so nguyen duong!",
            fg="red"
        )
        return

    nhan_ket_qua.config(
        text=f"Da nhan: {ho_ten} - {tuoi_so} tuoi - {email}",
        fg="blue"
    )


def xoa_thong_tin():
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    nhan_ket_qua.config(text="")

    entry_ho_ten.focus()


cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("450x320")
cua_so.resizable(False, False)

# Dong 1: Ho ten
tk.Label(
    cua_so,
    text="Ho ten:"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_ho_ten = tk.Entry(cua_so, width=30)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

# Dong 2: Tuoi
tk.Label(
    cua_so,
    text="Tuoi:"
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_tuoi = tk.Entry(cua_so, width=30)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

# Dong 3: Email
tk.Label(
    cua_so,
    text="Email:"
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_email = tk.Entry(cua_so, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Dong 4: Cac nut chuc nang
nut_submit = tk.Button(
    cua_so,
    text="Submit",
    command=xu_ly_submit
)
nut_submit.grid(row=3, column=0, padx=10, pady=15)

nut_xoa = tk.Button(
    cua_so,
    text="Xoa",
    command=xoa_thong_tin
)
nut_xoa.grid(row=3, column=1, padx=10, pady=15, sticky="w")

# Dong 5: Hien thi ket qua
nhan_ket_qua = tk.Label(
    cua_so,
    text="",
    font=("Arial", 11),
    fg="blue",
    wraplength=420
)
nhan_ket_qua.grid(
    row=4,
    column=0,
    columnspan=2,
    padx=10,
    pady=10
)

cua_so.mainloop()