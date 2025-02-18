import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('340x415')
        self.configure(bg="midnight blue")
        
        self.equation = ""
        self.create_widgets()

    def create_widgets(self):
        self.lab_result = tk.Label(self, width=14, height=2, text="", font=('arial', 30), fg='white', bg='MediumOrchid4')
        self.lab_result.place(x=0, y=0)

        # Button layout
        buttons = [
            ('AC   ',10, 100, self.clear), ('()  ', 90, 100, lambda: self.show('()')), ('%  ', 170, 100, lambda: self.show('%')), ('/  ', 250, 100, lambda: self.show('/')),
            ('7  ', 10, 160, lambda: self.show('7')), ('8  ', 90, 160, lambda: self.show('8')), ('9  ', 170, 160, lambda: self.show('9')), ('X  ', 250, 160, lambda: self.show('*')),
            ('4  ', 10, 220, lambda: self.show('4')), ('5  ', 90, 220, lambda: self.show('5')), ('6  ', 170, 220, lambda: self.show('6')), ('-  ', 250, 220, lambda: self.show('-')),
            ('1  ', 10, 280, lambda: self.show('1')), ('2  ', 90, 280, lambda: self.show('2')), ('3  ', 170, 280, lambda: self.show('3')), ('+  ', 250, 280, lambda: self.show('+')),
            ('0  ', 10, 340, lambda: self.show('0')), ('()  ', 90, 340, lambda: self.clear()), ('.   ', 170, 340, lambda: self.show('.')), ('=  ', 250, 340, self.calculate)
        ]

        for text, x, y, command in buttons:
            button = tk.Button(self, text=text, width=5, height=1, font=('arial', 30), bd=5, fg="white", bg='steel blue', command=command)
            button.place(x=x, y=y)

    def show(self, value):
        self.equation += value
        self.lab_result.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.lab_result.config(text=self.equation)

    def calculate(self):
        try:
            result = eval(self.equation)
        except:
            result = "error"
        self.lab_result.config(text=result)
        self.equation = str(result)

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
