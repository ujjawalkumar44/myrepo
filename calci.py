import tkinter as tk
import math
allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
allowed_names.update({"pow": pow, "abs": abs, "round": round})
def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None}, allowed_names)
    except Exception:
        raise
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.expr = ""
        self.memory = 0
        self.display = tk.Entry(self, font=("Arial", 20), bd=6, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=5, pady=5)
        buttons = [
            ("MC",1,0),("MR",1,1),("M+",1,2),("M-",1,3),("C",1,4),("⌫",1,5),
            ("7",2,0),("8",2,1),("9",2,2),("/",2,3),("sqrt",2,4),("%",2,5),
            ("4",3,0),("5",3,1),("6",3,2),("*",3,3),("(",3,4),(")",3,5),
            ("1",4,0),("2",4,1),("3",4,2),("-",4,3),("x^y",4,4),("1/x",4,5),
            ("0",5,0),(".",5,1),("+/-",5,2),("+",5,3),("ln",5,4),("log",5,5),
            ("sin",6,0),("cos",6,1),("tan",6,2),("!",6,3),("e",6,4),("π",6,5),
            ("Ans",7,0),("=" ,7,1,5)
        ]
        for b in buttons:
            text=b[0]; r=b[1]; c=b[2]; cs=b[3] if len(b)>3 else 1
            btn=tk.Button(self, text=text, font=("Arial",14), width=6, height=2, command=lambda t=text: self.on_click(t))
            btn.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=2, pady=2)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
        for j in range(6):
            self.grid_columnconfigure(j, weight=1)
        self.bind("<Return>", lambda e: self.on_click("="))
        self.bind("<BackSpace>", lambda e: self.on_click("⌫"))
        for k in "0123456789+-*/().%":
            self.bind(k, lambda e, ch=k: self.on_click(ch))
    def on_click(self, key):
        if key=="C":
            self.expr=""
            self.update_display()
            return
        if key=="⌫":
            self.expr=self.expr[:-1]
            self.update_display()
            return
        if key=="=":
            try:
                exp=self.expr.replace("π", str(math.pi)).replace("e", str(math.e)).replace("x^y","**")
                exp=exp.replace("Ans", str(self.last_answer)) if hasattr(self,"last_answer") else exp
                result=safe_eval(exp)
                if isinstance(result, float) and result.is_integer():
                    result=int(result)
                self.last_answer=result
                self.expr=str(result)
                self.update_display()
            except Exception:
                self.display.delete(0,tk.END)
                self.display.insert(0,"Error")
            return
        if key=="MC":
            self.memory=0
            return
        if key=="MR":
            self.expr+=str(self.memory)
            self.update_display()
            return
        if key=="M+":
            try:
                val=safe_eval(self.expr.replace("π", str(math.pi)))
                self.memory+=val
            except Exception:
                pass
            return
        if key=="M-":
            try:
                val=safe_eval(self.expr.replace("π", str(math.pi)))
                self.memory-=val
            except Exception:
                pass
            return
        if key=="sqrt":
            self.expr+="math.sqrt("
            self.update_display()
            return
        if key=="ln":
            self.expr+="log(" 
            self.update_display()
            return
        if key=="log":
            self.expr+="log10(" 
            self.update_display()
            return
        if key in ("sin","cos","tan"):
            self.expr+=f"{key}("
            self.update_display()
            return
        if key=="!":
            try:
                val=int(safe_eval(self.expr))
                self.expr=str(math.factorial(val))
                self.update_display()
            except Exception:
                self.display.delete(0,tk.END)
                self.display.insert(0,"Error")
            return
        if key=="%":
            self.expr+="/100"
            self.update_display()
            return
        if key=="+/-":
            if self.expr.startswith("-"):
                self.expr=self.expr[1:]
            else:
                self.expr="-"+self.expr
            self.update_display()
            return
        if key=="1/x":
            try:
                val=safe_eval(self.expr)
                self.expr=str(1/val)
                self.update_display()
            except Exception:
                self.display.delete(0,tk.END)
                self.display.insert(0,"Error")
            return
        if key=="x^y":
            self.expr+="**"
            self.update_display()
            return
        if key=="Ans":
            if hasattr(self,"last_answer"):
                self.expr+=str(self.last_answer)
                self.update_display()
            return
        if key=="π":
            self.expr+=str(math.pi)
            self.update_display()
            return
        if key=="e":
            self.expr+=str(math.e)
            self.update_display()
            return
        self.expr+=key
        self.update_display()
    def update_display(self):
        self.display.delete(0,tk.END)
        self.display.insert(0,self.expr)
if __name__=="__main__":
    app=Calculator()
    app.mainloop()
