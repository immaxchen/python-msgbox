# python-msgbox
Tkinter implementation of a simple message box if not in Windows

If in Windows, it will call user32.MessageBoxW for you.

# Example

```python
from msgbox import MessageBox

MessageBox("Hello World!")
```

# Reference

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
