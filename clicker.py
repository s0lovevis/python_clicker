from tkinter import *
from functools import partial
import time


class Finance:
    balance = 0

    income_per_click = 1
    income_update_effect = 1
    income_update_price = 1

    autoclick_income = 0
    autoclick_update_effect = 1
    autoclick_update_price = 5

    def textgenBalanceLabel(self):
        message = "You have " + str(self.balance) + " $"
        return message

    def textgenClickIncomeLabel(self):
        message = "Now you earn " + str(self.income_per_click) + " $ per click"
        return message

    def textgenUpdateClickIncomeButton(self):
        message = "Buy +" + str(self.income_update_effect) + " $ per click.\n"
        message += "Price is " + str(self.income_update_price) + " $"
        return message

    def textgenAutoclickIncomeLabel(self):
        message = "Now you autoclick earns " + str(self.autoclick_income) + " $ per second"
        return message

    def textgenUpdateAutoclickIncomeButton(self):
        message = "Buy +" + str(self.autoclick_update_effect) + " $ per second.\n"
        message += "Price is " + str(self.autoclick_update_price) + " $"
        return message

    def makeClick(self, event, BalanceLabel):
        self.balance += self.income_per_click
        BalanceLabel['text'] = self.textgenBalanceLabel()

    def updateClickIncome(self, ClickIncomeLabel, UpdateClickIncomeButton, BalanceLabel):
        self.balance -= self.income_update_price
        BalanceLabel['text'] = self.textgenBalanceLabel()
        self.income_per_click += self.income_update_effect
        ClickIncomeLabel['text'] = self.textgenClickIncomeLabel()
        self.income_update_price = self.income_update_price * 2
        UpdateClickIncomeButton['text'] = self.textgenUpdateClickIncomeButton()

    def updateAutoclickIncome(self, AutoclickIncomeLabel, UpdateAutoclickIncomeButton, BalanceLabel):
        self.balance -= self.autoclick_update_price
        BalanceLabel['text'] = self.textgenBalanceLabel()
        self.autoclick_income += self.autoclick_update_effect
        AutoclickIncomeLabel['text'] = self.textgenAutoclickIncomeLabel()
        self.autoclick_update_price = self.autoclick_update_price * 2
        UpdateAutoclickIncomeButton['text'] = self.textgenUpdateAutoclickIncomeButton()

    def doAutoclick(self):
        self.balance += self.autoclick_income

    def doRestart(self, BalanceLabel, ClickIncomeLabel, UpdateClickIncomeButton, AutoclickIncomeLabel,
                  UpdateAutoclickIncomeButton):
        self.balance = 0
        self.income_per_click = 1
        self.income_update_price = 1
        self.autoclick_income = 0
        self.autoclick_update_price = 5
        BalanceLabel['text'] = self.textgenBalanceLabel()
        ClickIncomeLabel['text'] = self.textgenClickIncomeLabel()
        UpdateClickIncomeButton['text'] = self.textgenUpdateClickIncomeButton()
        AutoclickIncomeLabel['text'] = self.textgenAutoclickIncomeLabel()
        UpdateAutoclickIncomeButton['text'] = self.textgenUpdateAutoclickIncomeButton()


def autoclickProcessing():
    finance.doAutoclick()
    BalanceLabel['text'] = finance.textgenBalanceLabel()
    clicker_window.after(1000, autoclickProcessing)


def buttonsStateProcessing():
    if finance.balance < finance.autoclick_update_price:
        UpdateAutoclickIncomeButton['state'] = DISABLED
    else:
        UpdateAutoclickIncomeButton['state'] = NORMAL

    if finance.balance < finance.income_update_price:
        UpdateClickIncomeButton['state'] = DISABLED
    else:
        UpdateClickIncomeButton['state'] = NORMAL

    clicker_window.after(100, buttonsStateProcessing)


def exit():
    clicker_window.quit()


finance = Finance()

clicker_window = Tk()

BalanceLabel = Label(clicker_window, text=finance.textgenBalanceLabel(), width=30, height=3)
BalanceLabel.grid(row=0, column=0, columnspan=4)

clicker_window.bind("<space>", lambda event: finance.makeClick(event, BalanceLabel))

ClickUpdateFrame = LabelFrame(clicker_window, text="Here you can update click income")
ClickUpdateFrame.grid(row=1, column=0, columnspan=2)

AutoclickUpdateFrame = LabelFrame(clicker_window, text="Here you can update autoclick income")
AutoclickUpdateFrame.grid(row=1, column=2, columnspan=2)

ClickIncomeLabel = Label(ClickUpdateFrame, text=finance.textgenClickIncomeLabel())
ClickIncomeLabel.pack()

UpdateClickIncomeButton = Button(ClickUpdateFrame, text=finance.textgenUpdateClickIncomeButton())
UpdateClickIncomeButton['command'] = partial(finance.updateClickIncome, ClickIncomeLabel, UpdateClickIncomeButton,
                                             BalanceLabel)
UpdateClickIncomeButton.pack()

AutoclickIncomeLabel = Label(AutoclickUpdateFrame, text=finance.textgenAutoclickIncomeLabel())
AutoclickIncomeLabel.pack()

UpdateAutoclickIncomeButton = Button(AutoclickUpdateFrame, text=finance.textgenUpdateAutoclickIncomeButton())
UpdateAutoclickIncomeButton['command'] = partial(finance.updateAutoclickIncome, AutoclickIncomeLabel,
                                                 UpdateAutoclickIncomeButton,
                                                 BalanceLabel)
UpdateAutoclickIncomeButton.pack()

RestartButton = Button(clicker_window, text="press this button to restart", width=30,
                       command=partial(finance.doRestart, BalanceLabel, ClickIncomeLabel, UpdateClickIncomeButton,
                                       AutoclickIncomeLabel, UpdateAutoclickIncomeButton))
RestartButton.grid(row=2, column=0, columnspan=4)

ExitButton = Button(clicker_window, text="go out from this amazing game", width=30, command=exit)
ExitButton.grid(row=3, column=0, columnspan=4)

clicker_window.after(1000, autoclickProcessing)
clicker_window.after(100, buttonsStateProcessing)
clicker_window.mainloop()
