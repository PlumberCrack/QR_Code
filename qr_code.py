'''
 ,-----.   ,------.      ,-----.          ,--.        
'  .-.  '  |  .--. '    '  .--./ ,---.  ,-|  | ,---.  
|  | |  |  |  '--'.'    |  |    | .-. |' .-. || .-. : 
'  '-'  '-.|  |\  \     '  '--'\' '-' '\ `-' |\   --. 
 `-----'--'`--' '--'     `-----' `---'  `---'  `----'                                                
'''
import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

#Functions---------------------------------------------------------------------------------
def on_click(event): #Replace starter text when user wants to add text
    if data_entry.get() == 'Enter in a link':
        data_entry.delete(0, tk.END)


def qr_func(*data): #Create QR Code :)    
        global qr_img
        data = data_entry.get() 
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(data)
        qr.make(fit = True)
        qr_img = qr.make_image(fill_color = 'black', back_color = 'white')
        qr_img = qr_img.resize((350,350))
    
        global photo_label #Place the QR code o the window using a label 
        img = ImageTk.PhotoImage(qr_img)
        photo_label.config(image=img)
        photo_label.image = img

        save_button.config(state=tk.NORMAL) #Unlocks the save button 



def save_func(): #Save Qr Code
    global filename
    data = data_entry.get() 
    filename = data.replace(".", "") + ".png"
    filepath = filedialog.asksaveasfilename(defaultextension=".png", initialfile=filename, filetypes=[("PNG files", "*.png")])
    if filepath:
            qr_img.save(filepath)  # Save the QR code image to the specified path
            print(f'File: {filename} saved succsefully')


#window---------------------------------------------------------------------------------
window = tk.Tk()
window.title('QR Code')
window.geometry('490x490')

#Frame---------------------------------------------------------------------------------
data_frame = tk.Frame(window)
data_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

#Data entry---------------------------------------------------------------------------------
data_string = tk.StringVar()
data_entry = tk.Entry(data_frame)
data_entry.pack(side=tk.LEFT)
data_entry.insert(0, 'Enter in a link')  
data_entry.bind('<FocusIn>', on_click)
data = data_entry.get() 

#QR Code Button---------------------------------------------------------------------------------
qr_button = tk.Button(data_frame,text='Create QR Code', command=qr_func)
qr_button.pack(side=tk.LEFT)
#Display Qr code on window---------------------------------------------------------------------------------
photo_label = ttk.Label(window)
photo_label.pack(pady=25)
#Save QR code---------------------------------------------------------------------------------
#Save button
save_button = tk.Button(data_frame,text='Save', command=save_func,state=tk.DISABLED)
save_button.pack(side=tk.RIGHT, padx=8)

#Run---------------------------------------------------------------------------------
window.mainloop()
print(f'QR Code sucsffully created and saved as {filename}')
#By Custer