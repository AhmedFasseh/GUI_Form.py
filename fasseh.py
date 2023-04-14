from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.geometry("750x500+100+100")
root.minsize(width=400,height=400)
root.maxsize(width=750,height=500)
root.title('Fasseh Official')

style=ttk.Style()
style.theme_use('classic')

ttk.Label(root, text="Full Name:").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=30,font=('Arial',16))
EntryFullName.grid(row=0,column=1,columnspan=2,pady=10)

ttk.Label(root, text="ID:").grid(row=1,column=0,padx=10,pady=10)
EntryID=ttk.Entry(root,width=30,font=('Arial',16))
EntryID.grid(row=1,column=1,columnspan=2,pady=10)

ttk.Label(root, text="Gender:").grid(row=2,column=0,padx=10,pady=10)
Gender=StringVar()
ttk.Radiobutton(root,text="Male",variable=Gender,value="Male").grid(row=2,column=1,padx=10,pady=10)
ttk.Radiobutton(root,text="Female",variable=Gender,value="Female").grid(row=2,column=2,padx=10,pady=10)

ttk.Label(root, text="Phone:").grid(row=3,column=0,padx=10,pady=10)
EntryPhone=ttk.Entry(root,width=30,font=('Arial',16))
EntryPhone.grid(row=3,column=1,columnspan=2,pady=10)

ttk.Label(root, text="Email:").grid(row=4,column=0,padx=10,pady=10)
EntryEmail=ttk.Entry(root,width=30,font=('Arial',16))
EntryEmail.grid(row=4,column=1,columnspan=2,pady=10)

ttk.Label(root, text="Address:").grid(row=5,column=0,padx=10,pady=10)
EntryAddress=ttk.Entry(root,width=30,font=('Arial',16))
EntryAddress.grid(row=5,column=1,columnspan=2,pady=10)

btnSave=ttk.Button(root,text="Save")
btnSave.grid(row=7,column=1)

btnDelete=ttk.Button(root,text="Delete")
btnDelete.grid(row=7,column=2)


def BuSaveData():
    print("Full Name:{}".format(EntryFullName.get()))
    print("ID:{}".format(EntryID.get()))
    print("Gender:{}".format(Gender.get()))
    print("Phone:{}".format(EntryPhone.get()))
    print("Email:{}".format(Gender.get()))
    print("Address:{}".format(EntryAddress.get()))


    data = {
        "Name": EntryFullName.get(),
        "ID": EntryID.get(),
        "Gender": Gender.get(),
        "phone": EntryPhone.get(),
        "Email": EntryEmail.get(),
        "Address": EntryAddress.get()
    }
    with open("data.txt","a") as f:
        f.write(str(data) + "\n")

    EntryFullName.delete(0,'end')
    EntryID.delete(0,'end')
    EntryPhone.delete(0,'end')
    EntryEmail.delete(0,'end')
    EntryAddress.delete(0,'end')

def BuListData():
    print('not implemented yet')
    
def BuDeleteData():
    EntryFullName.delete(0,'end')
    EntryID.delete(0,'end')
    EntryPhone.delete(0,'end')
    EntryEmail.delete(0,'end')
    EntryAddress.delete(0,'end')


btnSave.config(command=BuSaveData)
btnDelete.config(command=BuDeleteData)


root.mainloop()