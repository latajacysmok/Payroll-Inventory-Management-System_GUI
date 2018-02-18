from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

Pay_Inv = Tk()
Pay_Inv.geometry("1550x700")
Pay_Inv.resizable(0, 0)
Pay_Inv.title("Payroll Inventory Management System")
Pay_Inv.configure(background='black')

def Exit():
    qExit = messagebox.askyesno("Billing System", "Do you want to exit the system")
    if qExit > 0:
        Pay_Inv.destroy()

def Reset():
    Name.set("")
    Employer.set("")
    HoursWorked.set(0)
    Tax.set(0)
    GrossPay.set(0)
    Address.set("")
    NINumber.set("")
    HourlyRate.set(0)
    OverTime.set(0)
    NetPay.set(0)
    txtPaySlip.delete("1.0", END)

def WeeklySalary():
    HoursWorksPerWeek = float(HoursWorked.get())
    WagesPerHours = float(HourlyRate.get())

    paydue = HoursWorksPerWeek * WagesPerHours
    PaymnetDue = "pln", str(format(paydue, '.2f'))
    GrossPay.set(PaymnetDue)

    tax = paydue * 0.2
    TaxAbles = "pln", str(format(tax, '.2f'))
    Tax.set(TaxAbles)

    netPay = paydue - tax
    NetPays = "pln", str(format(netPay, '.2f'))
    NetPay.set(NetPays)

    if HoursWorksPerWeek > 40:
        OverTimeHours = (HoursWorksPerWeek - 40) * (WagesPerHours * 1.5)
        OverTimeHour = "pln", str(format(OverTimeHours, '.2f'))
        OverTime.set(OverTimeHour)
    else:
        OverTime.set(0)

def ViewPayslip():
    txtPaySlip.delete("1.0", END)
    txtPaySlip.insert(END, "\t\tPay Slip\n\n")
    txtPaySlip.insert(END, "Name:\t\t" + Name.get() + "\n\n")
    txtPaySlip.insert(END, "Address:\t\t" + Address.get() + "\n\n")
    txtPaySlip.insert(END, "Employer:\t\t" + Employer.get() + "\n\n")
    txtPaySlip.insert(END, "NINumber:\t\t" + NINumber.get() + "\n\n")
    txtPaySlip.insert(END, "Hours Worked:\t\t" + HoursWorked.get() + "\n\n")
    txtPaySlip.insert(END, "Net Payable :\t\t" + NetPay.get() + "\n\n")
    txtPaySlip.insert(END, "Wages per hour:\t\t" + HourlyRate.get() + "\n\n")
    txtPaySlip.insert(END, "Tax Paid:\t\t" + Tax.get() + "\n\n")
    txtPaySlip.insert(END, "Payable:\t\t" + GrossPay.get() + "\n\n")
#---Variable
Name = StringVar()
Employer = StringVar()
HoursWorked = StringVar()
Tax = StringVar()
GrossPay = StringVar()
Address = StringVar()
NINumber = StringVar()
HourlyRate = StringVar()
OverTime = StringVar()
NetPay = StringVar()
PaySlip = StringVar()
DateofOrder = StringVar()

HoursWorked.set(0)
Tax.set(0)
GrossPay.set(0)
OverTime.set(0)
NetPay.set(0)
HourlyRate.set(0)
DateofOrder.set(time.strftime("%d-%m-%Y"))

#---frame

Tops = Frame(Pay_Inv, width=1550, height=50, bd=16, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(Pay_Inv, width=700, height=700, bd=16, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(Pay_Inv, width=440, height=700, bd=16, relief="raise")
f2.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='yellow')
f2.configure(background='red')

#---Tops

lblInfo = Label(Tops, font=('arial', 52, 'bold'), text="    Payroll Inventory Management System      ",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

#---f1
f1a = Frame(f1, width=700, height=200, bd=8, relief="raise")
f1a.pack(side=TOP)

f1b = Frame(f1, width=700, height=600, bd=8, relief="raise")
f1b.pack(side=BOTTOM)

#---f2
f2a = Frame(f2, width=400, height=700, bd=8, relief="raise")
f2a.pack(side=TOP)

#---windows f1a
#---L
lblName = Label(f1a, font=('arial', 20, 'bold'), text="Name",
                fg='black', bd=10, anchor='w')
lblName.grid(row=0, column=0)

txtName = Entry(f1a, font=('arial', 14, 'bold'), textvariable=Name,
               bd=20, width=25, bg='white', justify='left')
txtName.grid(row=0, column=1)

lblEmployer = Label(f1a, font=('arial', 20, 'bold'), text="Employer",
                fg='black', bd=10, anchor='w')
lblEmployer.grid(row=1, column=0)

txtEmployer = Entry(f1a, font=('arial', 14, 'bold'), textvariable=Employer,
               bd=20, width=25, bg='white', justify='left')
txtEmployer.grid(row=1, column=1)

lblHoursWorked = Label(f1a, font=('arial', 20, 'bold'), text="Hours Worked",
                fg='black', bd=10, anchor='w')
lblHoursWorked.grid(row=2, column=0)

txtHoursWorked = Entry(f1a, font=('arial', 14, 'bold'), textvariable=HoursWorked,
               bd=20, width=25, bg='white', justify='left')
txtHoursWorked.grid(row=2, column=1)

lblTax = Label(f1a, font=('arial', 20, 'bold'), text="Tax",
                fg='black', bd=10, anchor='w')
lblTax.grid(row=3, column=0)

txtTax = Entry(f1a, font=('arial', 14, 'bold'), textvariable=Tax,
               bd=20, width=25, bg='white', justify='left')
txtTax.grid(row=3, column=1)

lblGrossPay = Label(f1a, font=('arial', 20, 'bold'), text="Gross Pay",
                fg='black', bd=10, anchor='w')
lblGrossPay.grid(row=4, column=0)

txtGrossPay = Entry(f1a, font=('arial', 14, 'bold'), textvariable=GrossPay,
               bd=20, width=25, bg='white', justify='left')
txtGrossPay.grid(row=4, column=1)

#--R

lblAddress = Label(f1a, font=('arial', 20, 'bold'), text="Address",
                fg='black', bd=10, anchor='w')
lblAddress.grid(row=0, column=2)

txtAddress = Entry(f1a, font=('arial', 14, 'bold'), textvariable=Address,
               bd=20, width=25, bg='white', justify='left')
txtAddress.grid(row=0, column=3)

lblNINumber = Label(f1a, font=('arial', 20, 'bold'), text="NI Number",
                fg='black', bd=10, anchor='w')
lblNINumber.grid(row=1, column=2)

txtNINumber = Entry(f1a, font=('arial', 14, 'bold'), textvariable=NINumber,
               bd=20, width=25, bg='white', justify='left')
txtNINumber.grid(row=1, column=3)

lblHourlyRate = Label(f1a, font=('arial', 20, 'bold'), text="Hourly Rate",
                fg='black', bd=10, anchor='w')
lblHourlyRate.grid(row=2, column=2)

txtHourlyRate = Entry(f1a, font=('arial', 14, 'bold'), textvariable=HourlyRate,
               bd=20, width=25, bg='white', justify='left')
txtHourlyRate.grid(row=2, column=3)

lblOverTime = Label(f1a, font=('arial', 20, 'bold'), text="Over Time",
                fg='black', bd=10, anchor='w')
lblOverTime.grid(row=3, column=2)

txtOverTime = Entry(f1a, font=('arial', 14, 'bold'), textvariable=OverTime,
               bd=20, width=25, bg='white', justify='left')
txtOverTime.grid(row=3, column=3)

lblNetPay = Label(f1a, font=('arial', 20, 'bold'), text="Net Pay",
                fg='black', bd=10, anchor='w')
lblNetPay.grid(row=4, column=2)

txtNetPay = Entry(f1a, font=('arial', 14, 'bold'), textvariable=NetPay,
               bd=20, width=25, bg='white', justify='left')
txtNetPay.grid(row=4, column=3)

#---f2

lblPaySlip = Label(f2a, font=('arial', 21, 'bold'), textvariable=DateofOrder,
                fg='black', bd=10, anchor='w')
lblPaySlip.grid(row=0, column=0)

txtPaySlip = Text(f2a, height=25, width=35, font=('arial', 12, 'bold'),
               bd=20, bg='white')
txtPaySlip.grid(row=1, column=0)


#---buttons f1b

btnWeeklySalary = Button(f1b, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                         height=1,text="Weekly Salary", bg='white', command=WeeklySalary).grid(row=0, column=0)

btnViewPayslip = Button(f1b, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        height=1,text="View Payslip", bg='white', command=ViewPayslip).grid(row=0, column=1)

btnReset = Button(f1b, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                  height=1,text="Reset", bg='white', command=Reset).grid(row=0, column=2)

btnExit = Button(f1b, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        height=1, text="Exit", bg='white', command=Exit).grid(row=0, column=3)

Pay_Inv.mainloop()