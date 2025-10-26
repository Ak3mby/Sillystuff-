#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json, pickle, os, pathlib

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ren’Py pickle ↔ JSON")
        self.geometry("500x260")
        self.resizable(False, False)
        self.config(bg="#fafafa")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Accent.TButton", background="#1976d2", foreground="white", borderwidth=0, focusthickness=0)

        self.in_path  = tk.StringVar()
        self.out_path = tk.StringVar()

        ttk.Label(self, text="Input file:").place(x=20, y=20)
        ttk.Entry(self, textvariable=self.in_path, width=50, state="readonly").place(x=100, y=20)
        ttk.Button(self, text="Browse…", command=self.browse_in, width=8).place(x=410, y=18)

        ttk.Label(self, text="Output file:").place(x=20, y=60)
        ttk.Entry(self, textvariable=self.out_path, width=50).place(x=100, y=60)
        ttk.Button(self, text="Browse…", command=self.browse_out, width=8).place(x=410, y=58)

        self.log = tk.Text(self, height=6, width=62, wrap="word", bg="#f5f5f5", relief="flat")
        self.log.place(x=20, y=100)

        ttk.Button(self, text="Convert", command=self.convert, style="Accent.TButton").place(x=210, y=210)

    def browse_in(self):
        f = filedialog.askopenfilename(title="Select input file",
                                       filetypes=[("All relevant", "*.log *.pkl *.json"), ("All files", "*.*")])
        if f:
            self.in_path.set(f)
            # pre-fill output name
            p = pathlib.Path(f)
            if p.suffix.lower() == ".json":
                self.out_path.set(str(p.with_suffix(".log")))
            else:
                self.out_path.set(str(p.with_suffix(".json")))

    def browse_out(self):
        f = filedialog.asksaveasfilename(title="Save output as",
                                         defaultextension="",
                                         filetypes=[("All files", "*.*")])
        if f:
            self.out_path.set(f)

    def log_msg(self, msg):
        self.log.insert("end", msg + "\n")
        self.log.see("end")

    def convert(self):
        src = pathlib.Path(self.in_path.get())
        dst = pathlib.Path(self.out_path.get())
        if not src.is_file():
            messagebox.showerror("Error", "Input file not found"); return
        try:
            if src.suffix.lower() == ".json":   # JSON -> pickle
                data = json.loads(src.read_text(encoding="utf-8"))
                dst.write_bytes(pickle.dumps(data))
                self.log_msg("JSON → pickle  ✅")
            else:                               # pickle -> JSON
                data = pickle.loads(src.read_bytes())
                dst.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str),
                               encoding="utf-8")
                self.log_msg("Pickle → JSON  ✅")
        except Exception as e:
            messagebox.showerror("Conversion failed", str(e))

if __name__ == "__main__":
    App().mainloop()
