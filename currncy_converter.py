from tkinter import *

class Converter:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")
        master.geometry("350x200")
        master.config(bg='black')
        master.resizable(False, False)

        self.qyma = StringVar()  # القيمة المدخلة
        self.urrnsy = StringVar()  # العملة المستهدفة
        self.value = StringVar()  # النتيجة النهائية

        self.omar = Entry(master, width=4, bg='white', font=('Arial Bold', 28), textvariable=self.qyma)
        self.omar.place(x=0, y=0)

        self.entry_value = Entry(master, width=4, bg='white', font=('Arial Bold', 28), textvariable=self.urrnsy)
        self.entry_value.place(x=262, y=0)

        self.result = Entry(master, width=4, bg='white', font=('Arial Bold', 28), textvariable=self.value)
        self.result.place(x=130, y=100)

        self.convert_button = Button(master, width=4, height=4, text="=", activebackground="#F5E216", relief="flat", bg="lightblue", command=self.convert)
        self.convert_button.place(x=130, y=20)

    def convert(self):
        # هنا نضع منطق تحويل العملات
        # مثلا، إذا كان التحويل من دولار إلى يورو
        try:
            amount = float(self.qyma.get())
            currency = self.urrnsy.get().lower()

            if currency == 'usd':
                result = amount * 0.85  # مثال على تحويل الدولار إلى اليورو
                self.value.set(f"{result:.2f}")

        except ValueError:
            self.value.set("Invalid Input")

root = Tk()
currncy = Converter(root)
root.mainloop()
