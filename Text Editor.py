""" Import """
import tkinter as Tk
import tkinter.filedialog as FileD


""" Body """
class Text_Editor():
    def __init__(self, App):
        ######################################################################################           
        ##############################          Window          ##############################
        self.App = App
        self.App.title("Text Editor")
        self.App.geometry("600x950+300+5")
        self.App.resizable=True
        self.Fnt_CourierNew = "Courier New"#"Copperplate Gothic Bold"
        self.V_Path = None


        ######################################################################################           
        ##############################          Title          ##############################
        L_Title = Tk.Label(self.App, text="Text Editor", font=(self.Fnt_CourierNew, '12'),width=16)
        L_Title.place(x=217, y=0)
        ##############################          Menu Bar          ##############################
        B_Menu_Open = Tk.Button(self.App, text="Open", width=16, bg='black', fg='white', borderwidth=0, command=self.F_Menu_Open)
        B_Menu_Open.place(x=000, y=20)
        B_Menu_New = Tk.Button(self.App, text="New", width=16, bg='black', fg='white', borderwidth=0, command=self.F_Menu_New)
        B_Menu_New.place(x=120, y=20)
        B_Menu_Save = Tk.Button(self.App, text="Save", width=16, bg='black', fg='white', borderwidth=0, command=self.F_Menu_Save)
        B_Menu_Save.place(x=240, y=20)
        B_Menu_SaveAs = Tk.Button(self.App, text="Save As", width=16, bg='black', fg='white', borderwidth=0, command=self.F_Menu_SaveAs)
        B_Menu_SaveAs.place(x=360, y=20)
        B_Menu_About = Tk.Button(self.App, text="About", width=16, bg='black', fg='white', borderwidth=0, command=self.F_Menu_About)
        B_Menu_About.place(x=480, y=20)
        ##############################          Text Box          ##############################
        self.T_Write_Area = Tk.Text(self.App, width=73, height=55)
        self.T_Write_Area.place(x=5, y=48)
        ##############################          Status          ##############################
        self.L_Status = Tk.Label(self.App, text="Every Thing Is Good!!")
        self.L_Status.place(x=0, y=932)

        L_Status_Copy = Tk.Label(self.App, text="©MahiKaishar2020 ",width=16)
        L_Status_Copy.place(x=490, y=932)
    
    def F_Menu_Open(self):
        self.V_Path = FileD.askopenfilename(title="Open", filetypes=(("All Files", "*.*"), ("Text File", "*.txt"), ("XML File", "*.xml")))
        ### Open The File
        try:
            with open(self.V_Path, 'r') as O_File:
                V_Read_File = O_File.read()
                ### Show The Read File
                self.T_Write_Area.delete(0.1, Tk.END)
                self.T_Write_Area.insert(0.1, str(V_Read_File))
        except Exception as Error:
            self.L_Status["text"] = f"Found An Error! {Error}"


    def F_Menu_New(self):
        ### Remove All The Text
        self.T_Write_Area.delete(0.1, Tk.END)     


    def F_Menu_Save(self):
        if self.V_Path != None:
            ### Open The File
            try:
                with open(self.V_Path, 'w') as O_File:
                    ### Collect Text Area Data
                    V_Data = self.T_Write_Area.get(0.1, Tk.END)
                    ### Write Data
                    O_File.write(str(V_Data))
            except Exception as Error:
                self.L_Status["text"] = f"Found An Error! {Error}"


    def F_Menu_SaveAs(self):
        self.V_Path = FileD.asksaveasfilename(title="Save As", filetypes=(("Text File", "*.txt"), ("XML File", "*.xml"), ("All Files", "*.*")))
        ### Open The File
        try:
            with open(self.V_Path, 'w') as O_File:
                ### Collect Text Area Data
                V_Data = self.T_Write_Area.get(0.1, Tk.END)
                ### Write Data
                O_File.write(str(V_Data))
        except Exception as Error:
            self.L_Status["text"] = f"Found An Error! {Error}"


    def F_Menu_About(self):
        V_About = "I'm Mahi Kaishar.\nI'm A Begineer Coder.\nThis Text Editor Only For Txt File.\nI Think All Of You Like My Text Editor.\nTry To Stay With Me Always!!!"
        ### Remove All The Text
        self.T_Write_Area.delete(0.1, Tk.END)
        self.T_Write_Area.insert(0.1, str(V_About))




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
######################################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
### Main Window ###
App = Tk.Tk()
### Class Object ###
Class_Object = Text_Editor(App)
### Main Loop ###
App.mainloop()