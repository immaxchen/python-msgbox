import os

if os.name == "nt":
    import ctypes

    def MessageBox(text, caption="", options=0):
        return ctypes.windll.user32.MessageBoxW(0, text, caption, options)


else:
    import textwrap
    import tkinter

    from PIL import Image, ImageTk

    def MessageBox(text, caption="", options=0):
        if not options == 0:
            errmsg = "Options other than 0 (OK only) is not yet implemented."
            raise NotImplementedError(errmsg)
        room = " " * 8
        icon = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        text = "\n".join(
            [
                line + room
                for para in text.split("\n")
                for line in textwrap.wrap(para, width=76)
            ]
        ).ljust(32)
        root = tkinter.Tk()
        root.title(caption)
        root.iconphoto(root, ImageTk.PhotoImage(icon))
        lbl = tkinter.Label(root, text=text, bg="white", justify="left")
        lbl.pack(ipadx=12, ipady=24)
        btn = tkinter.Button(root, text="OK", width=11, command=root.destroy)
        btn.pack(padx=12, pady=12, anchor="e")
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        root.mainloop()
        return 1
