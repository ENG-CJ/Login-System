from tkinter import *
from tkinter import messagebox
import sqlite3





class LOGIN:
    def __init__(self,root):
        self.root=root
        Label(self.root,text='LOGIN',bg='#ade0f0',fg='#018',
              font=('Arial',35,'bold')).place(x=140,y=80)
        Label(self.root, text='ENJOY THE SITE ', bg='#ade0f0', fg='#018',
              font=('Arial', 9)).place(x=160,y=130)

        Label(self.root, text='Username', bg='#ade0f0', fg='#018',
              font=('Arial', 20, 'bold')).place(x=120,y=180)

        self.user=Entry(self.root,width=18,bg='#f4f4f4',font=('Sans Serif',19,'bold'),
                        bd=1,relief='groove')
        self.user.place(x=120,y=220)

#         pas
        Label(self.root, text='Password', bg='#ade0f0', fg='#018',
              font=('Arial', 20, 'bold')).place(x=120, y=280)

        self.pascode = Entry(self.root, width=18, bg='#f4f4f4', font=('Sans Serif', 19, 'bold'),
                          bd=1, relief='groove',show='*')
        self.pascode.place(x=120, y=320)

        self.log=Button(self.root, text='LOGIN', bg='#ade0f0', fg='#018',
              font=('Arial', 20, 'bold'),command=self.login,cursor='hand2',width=10,bd=1,relief='sunken').place(x=140, y=380)

        #         pas
        Label(self.root, text='_______________________________________________________________________', bg='#ade0f0', fg='black',
              font=('verdana', 7),width=85).place(x=0, y=450)

        #         pas
        Label(self.root, text="Don't Have Account?", bg='#ade0f0', fg='#018',
              font=('Arial', 15)).place(x=100, y=490)

        Button(self.root, text="Create Account", bg='#ade0f0', fg='red',
              font=('Arial', 15,'bold','underline'),
        activebackground='#ade0f0',bd=0,cursor='hand2',command=self.create_account).place(x=290, y=485)




    def create_account(self):
        self.root.iconify()
        self.screen = Toplevel()
        self.screen.focus_force()
        self.screen.title('Create Account')
        self.screen.geometry('500x600')
        self.screen.resizable(0, 0)
        self.screen.config(bg='#d6aeea')

        # screen
        Label(self.screen, text='Create Account', bg='#d6aeea', fg='#018',
              font=('Arial', 25, 'bold')).place(x=120, y=20)
        Label(self.screen, text='Once You Create You Must Login ', bg='#d6aeea', fg='#018',
              font=('Arial', 9),justify=LEFT).place(x=140, y=60)

        Label(self.screen, text='Username', bg='#d6aeea', fg='#018',
              font=('Arial', 18, 'bold')).place(x=120, y=100)

        self.user_2 = Entry(self.screen, width=18, bg='#f4f4f4', font=('Sans Serif', 19, 'bold'),
                          bd=1, relief='groove')
        self.user_2.place(x=120, y=130)

        #         pas
        Label(self.screen, text='Email', bg='#d6aeea', fg='#018',
              font=('Arial', 18, 'bold')).place(x=120, y=180)

        self.email = Entry(self.screen, width=18, bg='#f4f4f4', font=('Sans Serif', 19, 'bold'),
                             bd=1, relief='groove')
        self.email.place(x=120, y=210)

        Label(self.screen, text='Password', bg='#d6aeea', fg='#018',
              font=('Arial', 18, 'bold')).place(x=120, y=260)

        self.pas_code = Entry(self.screen, width=18, bg='#f4f4f4', font=('Sans Serif', 19, 'bold'),
                           bd=1, relief='groove')
        self.pas_code.place(x=120, y=290)



        Label(self.screen, text='Confirm', bg='#d6aeea', fg='#018',
              font=('Arial', 18, 'bold')).place(x=120, y=340)

        self.con_pass = Entry(self.screen, width=18, bg='#f4f4f4', font=('Sans Serif', 19, 'bold'),
                           bd=1, relief='groove')
        self.con_pass.place(x=120, y=370)




        self.log = Button(self.screen, text='Create', bg='#ade0f0', fg='#018',
                          font=('Arial', 20, 'bold'),command=self.create, cursor='hand2', width=10, bd=1, relief='sunken').place(x=140,
                                                                                                             y=420)


        Label(self.screen, text="I An Have Account?", bg='#d6aeea', fg='#018',
              font=('Arial', 15)).place(x=120, y=490)

        Button(self.screen, text="Sig In", bg='#d6aeea', fg='#018',
               font=('Arial', 15, 'bold', 'underline'),
               activebackground='#ade0f0', bd=0, cursor='hand2').place(x=310, y=485)

        self.screen.mainloop()

    def des(self):
        self.screen.destroy()
        self.root.deiconify()


    # create account
    def create(self):
        if self.user_2.get()=='' or self.email.get()=='' or self.pas_code.get()=='' or self.con_pass.get()=='':
            messagebox.showerror('ERR','Input Required')
        elif self.con_pass.get()!=self.pas_code.get():
            messagebox.showerror('ERR','Password Is Not match')
        else:
            try:
                conn=sqlite3.connect('users.db')
                cursor=conn.cursor()
                cursor.execute("INSERT INTO user values(?,?,?,?)",(
                    self.user_2.get(),
                    self.email.get(),
                    self.pas_code.get(),
                    self.con_pass.get()
                ))
                conn.commit()
                messagebox.showinfo('ADMIN',f'You Must Login')
                self.screen.destroy()
                self.root.deiconify()
            except Exception as err:
                messagebox.showerror('ERR',f'{err}')

    # login
    def login(self):
      if self.user.get()=='' or self.pascode.get()=='':
          messagebox.showerror('ERR','Input required')
      else:
          try:
              conn=sqlite3.connect('users.db')
              cursor=conn.cursor()
              cursor.execute("SELECT *FROM user where username=? and password=?",(self.user.get(),self.pascode.get()))
              self.row=cursor.fetchone()
              if self.row!=None:
                  messagebox.showinfo('ADMIN',f'Successfully login With {self.row[0]}')
                  self.root.destroy()
                  self.welcome()
              else:
                  messagebox.showerror('ERR','Invalid User')

          except Exception as err:
              messagebox.showerror('Err',f'{err}')
    # welcome page
    def welcome(self):
        wel=Tk()
        wel.geometry('400x400')
        wel.config(bg='#f4f4f4')
        wel.resizable(0,0)
        lb=Label(wel,text='',font=('Verdana',20))
        lb.config(text=f'WELCOME {self.row[0]}')
        lb.pack(pady=95)
        wel.mainloop()


if __name__=='__main__':
    root=Tk()
    app=LOGIN(root)
    root.title('Login System')
    root.geometry('500x600')
    root.resizable(0,0)
    root.config(bg='#ade0f0')
    root.mainloop()