import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import random


class MainWindow(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.labels = []
        self.dice_table = []  # list used in roll func (player)
        self.c_dice_table = []  # list used in computer_action func (computer)
        style = ttk.Style()
        style.configure("TC.TLabel", width=10, font='Arial', fontsize=12,
                        borderwidth=3, relief="solid", padding=2)
        style.configure("TC1.TLabel", width=12, font='Arial', fontsize=12,
                        borderwidth=3, relief="solid", padding=2)
        ttk.Label(self, text="TYPE").grid(row=0, column=6)
        ttk.Label(self, text="PLAYER 1").grid(row=0, column=7)
        ttk.Label(self, text="COMPUTER").grid(row=0, column=8)

        # player variables
        self.value1 = IntVar(self)
        self.value2 = IntVar(self)
        self.value3 = IntVar(self)
        self.value4 = IntVar(self)
        self.value5 = IntVar(self)
        self.value6 = IntVar(self)
        self.value7 = IntVar(self)
        self.value8 = IntVar(self)
        self.value9 = IntVar(self)
        self.value10 = IntVar(self)
        self.value11 = IntVar(self)
        self.value12 = IntVar(self)
        self.value13 = IntVar(self)
        self.value14 = IntVar(self)
        self.value15 = IntVar(self)

        # computer variables
        self.cvalue1 = IntVar(self)
        self.cvalue2 = IntVar(self)
        self.cvalue3 = IntVar(self)
        self.cvalue4 = IntVar(self)
        self.cvalue5 = IntVar(self)
        self.cvalue6 = IntVar(self)
        self.cvalue7 = IntVar(self)
        self.cvalue8 = IntVar(self)
        self.cvalue9 = IntVar(self)
        self.cvalue10 = IntVar(self)
        self.cvalue11 = IntVar(self)
        self.cvalue12 = IntVar(self)
        self.cvalue13 = IntVar(self)
        self.cvalue14 = IntVar(self)
        self.cvalue15 = IntVar(self)

        # additional computer var to help with algorithm
        self.cvalue_pair = BooleanVar()

        self.cvalue_bool1 = False
        self.cvalue_bool2 = False
        self.cvalue_bool3 = False
        self.cvalue_bool4 = False
        self.cvalue_bool5 = False
        self.cvalue_bool6 = False
        self.cvalue_bool7 = False
        self.cvalue_bool8 = False  # 3 of kind
        self.cvalue_bool9 = False  # 4 of kind
        self.cvalue_bool10 = False  # full house
        self.cvalue_bool11 = False  # small straight
        self.cvalue_bool12 = False  # large straight
        self.cvalue_bool13 = False  # yahtzee
        self.cvalue_bool14 = False  # chance

        self.cvalue_second_bool1 = False
        self.cvalue_second_bool2 = False
        self.cvalue_second_bool3 = False
        self.cvalue_second_bool4 = False
        self.cvalue_second_bool5 = False
        self.cvalue_second_bool6 = False
        self.cvalue_second_bool7 = False
        self.cvalue_second_bool8 = False
        self.cvalue_second_bool9 = False
        self.cvalue_second_bool10 = False
        self.cvalue_second_bool11 = False
        self.cvalue_second_bool12 = False
        self.cvalue_second_bool13 = False
        self.cvalue_second_bool14 = False

        #  additional computer var to help with adding to total score
        self.cvalue_help_add_int1 = 0
        self.cvalue_help_add_int2 = 0

        # values of player dices
        self.pdice1 = IntVar()
        self.pdice2 = IntVar()
        self.pdice3 = IntVar()
        self.pdice4 = IntVar()
        self.pdice5 = IntVar()

        # values of computer dices
        self.cdice1 = 0
        self.cdice2 = 0
        self.cdice3 = 0
        self.cdice4 = 0
        self.cdice5 = 0

        # cvalue list
        self.c_dice_table = [self.cdice1, self.cdice2, self.cdice3, self.cdice4, self.cdice5]

        # additional variables
        self.addit_var1 = 0
        self.addit_var2 = 0

        # dice images
        self.img1 = ImageTk.PhotoImage(Image.open('graphics/dice1.jpg'))
        self.img2 = ImageTk.PhotoImage(Image.open('graphics/dice2.jpg'))
        self.img3 = ImageTk.PhotoImage(Image.open('graphics/dice3.jpg'))
        self.img4 = ImageTk.PhotoImage(Image.open('graphics/dice4.jpg'))
        self.img5 = ImageTk.PhotoImage(Image.open('graphics/dice5.jpg'))
        self.img6 = ImageTk.PhotoImage(Image.open('graphics/dice6.jpg'))

        # player1 text
        player_label = ttk.Label(self, text="Player")
        player_label.grid(column=1, row=2, columnspan=4)

        # computer label
        computer_label = ttk.Label(self, text="Computer")
        computer_label.grid(column=10, row=2, columnspan=4)

        # player roll button
        btn = tk.Button(self, text='Roll', command=self.roll, width=8, height=2, borderwidth=2,
                        relief='solid', padx=4)
        btn.grid(column=0, row=7, rowspan=2)

        # blank player roll button
        self.btn_blank = tk.Button(self, text='Roll', width=8, height=2, borderwidth=2,
                        relief='solid', padx=4)

        # player dices panels
        self.panel1 = ttk.Label(self, text="text", image=self.img1, padding=3)
        self.panel1.grid(column=1, row=5, rowspan=2)
        self.panel2 = ttk.Label(self, text="text", image=self.img2, padding=3)
        self.panel2.grid(column=2, row=5, rowspan=2)
        self.panel3 = ttk.Label(self, text="text", image=self.img3, padding=3)
        self.panel3.grid(column=3, row=5, rowspan=2)
        self.panel4 = ttk.Label(self, text="text", image=self.img4, padding=3)
        self.panel4.grid(column=4, row=5, rowspan=2)
        self.panel5 = ttk.Label(self, text="text", image=self.img5, padding=3)
        self.panel5.grid(column=5, row=5, rowspan=2, columnspan=1)

        # computer dices panels
        self.cpanel1 = ttk.Label(self, text="text", image=self.img1, padding=3)
        self.cpanel1.grid(column=9, row=5, rowspan=2)
        self.cpanel2 = ttk.Label(self, text="text", image=self.img2, padding=3)
        self.cpanel2.grid(column=10, row=5, rowspan=2)
        self.cpanel3 = ttk.Label(self, text="text", image=self.img3, padding=3)
        self.cpanel3.grid(column=11, row=5, rowspan=2)
        self.cpanel4 = ttk.Label(self, text="text", image=self.img4, padding=3)
        self.cpanel4.grid(column=12, row=5, rowspan=2)
        self.cpanel5 = ttk.Label(self, text="text", image=self.img5, padding=3)
        self.cpanel5.grid(column=13, row=5, rowspan=2)

        # player dice block check buttons variables
        self.check_box_var1 = IntVar(self)
        self.check_box_var2 = IntVar(self)
        self.check_box_var3 = IntVar(self)
        self.check_box_var4 = IntVar(self)
        self.check_box_var5 = IntVar(self)

        # player dice block check buttons
        self.player_c1 = ttk.Checkbutton(self, variable=self.check_box_var1, onvalue=1, offvalue=0)
        self.player_c2 = ttk.Checkbutton(self, variable=self.check_box_var2, onvalue=1, offvalue=0)
        self.player_c3 = ttk.Checkbutton(self, variable=self.check_box_var3, onvalue=1, offvalue=0)
        self.player_c4 = ttk.Checkbutton(self, variable=self.check_box_var4, onvalue=1, offvalue=0)
        self.player_c5 = ttk.Checkbutton(self, variable=self.check_box_var5, onvalue=1, offvalue=0)

        # block label
        bd = ttk.Label(self, text='block dice?')
        bd.grid(column=4, row=8, columnspan=2)

        # throws left label
        self.tleft_help_int_value = 0
        self.tleft_var_int = IntVar()
        self.tleft_var_int.set(3)
        self.tleft_var_str = StringVar()
        self.tleft_var_str.set(str(self.tleft_var_int) + ' throws left')

        tl = ttk.Label(self, textvariable=self.tleft_var_int, font=15)
        tl.grid(column=1, row=9)
        tl2 = ttk.Label(self, text ="throws left", font=15)
        tl2.grid(column=2, row=9, columnspan=2, sticky=W)

        # player cells
        self.p1 = ttk.Label(self, textvariable=self.value1, style='TC.TLabel')
        self.p1.grid(column=7, row=1)
        self.p2 = ttk.Label(self, textvariable=self.value2, style='TC.TLabel')
        self.p2.grid(column=7, row=2)
        self.p3 = ttk.Label(self, textvariable=self.value3, style='TC.TLabel')
        self.p3.grid(column=7, row=3)
        self.p4 = ttk.Label(self, textvariable=self.value4, style='TC.TLabel')
        self.p4.grid(column=7, row=4)
        self.p5 = ttk.Label(self, textvariable=self.value5, style='TC.TLabel')
        self.p5.grid(column=7, row=5)
        self.p6 = ttk.Label(self, textvariable=self.value6, style='TC.TLabel')
        self.p6.grid(column=7, row=6)
        self.p7 = ttk.Label(self, textvariable=self.value7, style='TC.TLabel')
        self.p7.grid(column=7, row=7)
        self.p8 = ttk.Label(self, textvariable=self.value8, style='TC.TLabel')
        self.p8.grid(column=7, row=8)
        self.p9 = ttk.Label(self, textvariable=self.value9, style='TC.TLabel')
        self.p9.grid(column=7, row=9)
        self.p10 = ttk.Label(self, textvariable=self.value10, style='TC.TLabel')
        self.p10.grid(column=7, row=10)
        self.p11 = ttk.Label(self, textvariable=self.value11, style='TC.TLabel')
        self.p11.grid(column=7, row=11)
        self.p12 = ttk.Label(self, textvariable=self.value12, style='TC.TLabel')
        self.p12.grid(column=7, row=12)
        self.p13 = ttk.Label(self, textvariable=self.value13, style='TC.TLabel')
        self.p13.grid(column=7, row=13)
        self.p14 = ttk.Label(self, textvariable=self.value14, style='TC.TLabel')
        self.p14.grid(column=7, row=14)
        self.p15 = ttk.Label(self, textvariable=self.value15, style='TC.TLabel')
        self.p15.grid(column=7, row=15)

        # computer cells
        c1 = ttk.Label(self, textvariable=self.cvalue1, style='TC.TLabel')
        c1.grid(column=8, row=1)
        c2 = ttk.Label(self, textvariable=self.cvalue2, style='TC.TLabel')
        c2.grid(column=8, row=2)
        c3 = ttk.Label(self, textvariable=self.cvalue3, style='TC.TLabel')
        c3.grid(column=8, row=3)
        c4 = ttk.Label(self, textvariable=self.cvalue4, style='TC.TLabel')
        c4.grid(column=8, row=4)
        c5 = ttk.Label(self, textvariable=self.cvalue5, style='TC.TLabel')
        c5.grid(column=8, row=5)
        c6 = ttk.Label(self, textvariable=self.cvalue6, style='TC.TLabel')
        c6.grid(column=8, row=6)
        c7 = ttk.Label(self, textvariable=self.cvalue7, style='TC.TLabel')
        c7.grid(column=8, row=7)
        c8 = ttk.Label(self, textvariable=self.cvalue8, style='TC.TLabel')
        c8.grid(column=8, row=8)
        c9 = ttk.Label(self, textvariable=self.cvalue9, style='TC.TLabel')
        c9.grid(column=8, row=9)
        c10 = ttk.Label(self, textvariable=self.cvalue10, style='TC.TLabel')
        c10.grid(column=8, row=10)
        c11 = ttk.Label(self, textvariable=self.cvalue11, style='TC.TLabel')
        c11.grid(column=8, row=11)
        c12 = ttk.Label(self, textvariable=self.cvalue12, style='TC.TLabel')
        c12.grid(column=8, row=12)
        c13 = ttk.Label(self, textvariable=self.cvalue13, style='TC.TLabel')
        c13.grid(column=8, row=13)
        c14 = ttk.Label(self, textvariable=self.cvalue14, style='TC.TLabel')
        c14.grid(column=8, row=14)
        c15 = ttk.Label(self, textvariable=self.cvalue15, style='TC.TLabel')
        c15.grid(column=8, row=15)

        # computer variables that freeze showing number in table after being chosen
        # and another labels that cover these original
        self.two_cvalue1 = IntVar(self)
        self.c2_1 = ttk.Label(self, textvariable=self.two_cvalue1, style='TC.TLabel')
        self.two_cvalue2 = IntVar(self)
        self.c2_2 = ttk.Label(self, textvariable=self.two_cvalue2, style='TC.TLabel')
        self.two_cvalue3 = IntVar(self)
        self.c2_3 = ttk.Label(self, textvariable=self.two_cvalue3, style='TC.TLabel')
        self.two_cvalue4 = IntVar(self)
        self.c2_4 = ttk.Label(self, textvariable=self.two_cvalue4, style='TC.TLabel')
        self.two_cvalue5 = IntVar(self)
        self.c2_5 = ttk.Label(self, textvariable=self.two_cvalue5, style='TC.TLabel')
        self.two_cvalue6 = IntVar(self)
        self.c2_6 = ttk.Label(self, textvariable=self.two_cvalue6, style='TC.TLabel')
        self.two_cvalue8 = IntVar(self)
        self.c2_8 = ttk.Label(self, textvariable=self.two_cvalue8, style='TC.TLabel')
        self.two_cvalue9 = IntVar(self)
        self.c2_9 = ttk.Label(self, textvariable=self.two_cvalue9, style='TC.TLabel')
        self.two_cvalue10 = IntVar(self)
        self.c2_10 = ttk.Label(self, textvariable=self.two_cvalue10, style='TC.TLabel')
        self.two_cvalue11 = IntVar(self)
        self.c2_11 = ttk.Label(self, textvariable=self.two_cvalue11, style='TC.TLabel')
        self.two_cvalue12 = IntVar(self)
        self.c2_12 = ttk.Label(self, textvariable=self.two_cvalue12, style='TC.TLabel')
        self.two_cvalue13 = IntVar(self)
        self.c2_13 = ttk.Label(self, textvariable=self.two_cvalue13, style='TC.TLabel')
        self.two_cvalue14 = IntVar(self)
        self.c2_14 = ttk.Label(self, textvariable=self.two_cvalue14, style='TC.TLabel')

        # player table check buttons variables
        self.table_check_box_var1 = IntVar(self)
        self.table_check_box_var2 = IntVar(self)
        self.table_check_box_var3 = IntVar(self)
        self.table_check_box_var4 = IntVar(self)
        self.table_check_box_var5 = IntVar(self)
        self.table_check_box_var6 = IntVar(self)
        self.table_check_box_var8 = IntVar(self)
        self.table_check_box_var9 = IntVar(self)
        self.table_check_box_var10 = IntVar(self)
        self.table_check_box_var11 = IntVar(self)
        self.table_check_box_var12 = IntVar(self)
        self.table_check_box_var13 = IntVar(self)
        self.table_check_box_var14 = IntVar(self)

        # player table check buttons
        tc1 = ttk.Checkbutton(self, variable=self.table_check_box_var1, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc1, self.value1, self.p1))
        tc1.grid(column=7, row=1)
        tc2 = ttk.Checkbutton(self, variable=self.table_check_box_var2, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc2, self.value2, self.p2))
        tc2.grid(column=7, row=2)
        tc3 = ttk.Checkbutton(self, variable=self.table_check_box_var3, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc3, self.value3, self.p3))
        tc3.grid(column=7, row=3)
        tc4 = ttk.Checkbutton(self, variable=self.table_check_box_var4, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc4, self.value4, self.p4))
        tc4.grid(column=7, row=4)
        tc5 = ttk.Checkbutton(self, variable=self.table_check_box_var5, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc5, self.value5, self.p5))
        tc5.grid(column=7, row=5)
        tc6 = ttk.Checkbutton(self, variable=self.table_check_box_var6, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc6, self.value6, self.p6))
        tc6.grid(column=7, row=6)
        tc8 = ttk.Checkbutton(self, variable=self.table_check_box_var8, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc8, self.value8, self.p8))
        tc8.grid(column=7, row=8)
        tc9 = ttk.Checkbutton(self, variable=self.table_check_box_var9, onvalue=1, offvalue=0,
                              command=lambda: self.table_checkbutton(tc9, self.value9, self.p9))
        tc9.grid(column=7, row=9)
        tc10 = ttk.Checkbutton(self, variable=self.table_check_box_var10, onvalue=1, offvalue=0,
                               command=lambda: self.table_checkbutton(tc10, self.value10, self.p10))
        tc10.grid(column=7, row=10)
        tc11 = ttk.Checkbutton(self, variable=self.table_check_box_var11, onvalue=1, offvalue=0,
                               command=lambda: self.table_checkbutton(tc11, self.value11, self.p11))
        tc11.grid(column=7, row=11)
        tc12 = ttk.Checkbutton(self, variable=self.table_check_box_var12, onvalue=1, offvalue=0,
                               command=lambda: self.table_checkbutton(tc12, self.value12, self.p12))
        tc12.grid(column=7, row=12)
        tc13 = ttk.Checkbutton(self, variable=self.table_check_box_var13, onvalue=1, offvalue=0,
                               command=lambda: self.table_checkbutton(tc13, self.value13, self.p13))
        tc13.grid(column=7, row=13)
        tc14 = ttk.Checkbutton(self, variable=self.table_check_box_var14, onvalue=1, offvalue=0,
                               command=lambda: self.table_checkbutton(tc14, self.value14, self.p14))
        tc14.grid(column=7, row=14)

        self.was_table_checkbutton_func_called = False  # bool var for checking if checkbutton was clicked

    def col1_title(self):
        label_col1_titles = {1: 'ONES', 2: 'TWOS', 3: 'THREES', 4: 'FOURS', 5: 'FIVES', 6: 'SIXS', 7: 'BONUS', 8: '3 OF KIND'
                                , 9: '4 OF KIND', 10: 'FULL HOUSE', 11: 'SM STRAIGHT', 12: 'LG STRAIGHT',
                             13: 'YAHTZEE', 14: 'CHANCE', 15: 'TOTAL'}
        for i, (row_col1, text_col1) in enumerate(label_col1_titles.items()):
            label_col0 = ttk.Label(self, text=text_col1, style='TC1.TLabel')
            label_col0.grid(row=row_col1, column=6)
            self.labels.append(label_col0)

    def roll(self):

        # showing dice checkboxes after roll so player cannot lock dice after choosing category
        # and roll with dice value from previous turn blocked
        self.player_c1.grid(column=1, row=7)
        self.player_c2.grid(column=2, row=7)
        self.player_c3.grid(column=3, row=7)
        self.player_c4.grid(column=4, row=7)
        self.player_c5.grid(column=5, row=7)

        if self.check_box_var1.get() == 0:  # if check button isn't checked (check_box_var1 = 0) then roll, else not
            self.pdice1 = random.randint(1, 6)
        if self.check_box_var2.get() == 0:
            self.pdice2 = random.randint(1, 6)
        if self.check_box_var3.get() == 0:
            self.pdice3 = random.randint(1, 6)
        if self.check_box_var4.get() == 0:
            self.pdice4 = random.randint(1, 6)
        if self.check_box_var5.get() == 0:
            self.pdice5 = random.randint(1, 6)
        self.dice_table = [self.pdice1, self.pdice2, self.pdice3, self.pdice4, self.pdice5]

        if 1 in self.dice_table and self.table_check_box_var1.get() != 1:
            self.value1.set(self.dice_table.count(1) * 1)

        if 2 in self.dice_table and self.table_check_box_var2.get() != 1:
            self.value2.set(self.dice_table.count(2) * 2)

        if 3 in self.dice_table and self.table_check_box_var3.get() != 1:
            self.value3.set(self.dice_table.count(3) * 3)

        if 4 in self.dice_table and self.table_check_box_var4.get() != 1:
            self.value4.set(self.dice_table.count(4) * 4)

        if 5 in self.dice_table and self.table_check_box_var5.get() != 1:
            self.value5.set(self.dice_table.count(5) * 5)

        if 6 in self.dice_table and self.table_check_box_var6.get() != 1:
            self.value6.set(self.dice_table.count(6) * 6)

        if self.value1.get() + self.value2.get() + self.value3.get() + self.value4.get() + self.value5.get() + self.value6.get() > 63:
            self.value7.set(35)

        # 3 of kind value 8
        y1 = sum(x * 3 for x in set(self.dice_table) if self.dice_table.count(x) > 2 and self.table_check_box_var8.get() != 1)
        if y1 > 0:
            self.value8.set(y1)

        # four of kind value 9
        y2 = sum(x * 4 for x in set(self.dice_table) if self.dice_table.count(x) > 3 and self.table_check_box_var9.get() != 1)
        if y2 > 0:
            self.value9.set(y2)

        # full house value 10
        if len(set(self.dice_table)) == 2 and self.dice_table.count(self.dice_table[0]) in (2, 3) and self.table_check_box_var10.get() != 1:
            self.value10.set(sum(self.dice_table))

        # ls value 11
        if set(self.dice_table) == set(range(1, 6)) and self.table_check_box_var11.get() != 1:
            self.value11.set(30)

        # bs value 12
        if set(self.dice_table) == set(range(2, 7)) and self.table_check_box_var12.get() != 1:
            self.value12.set(40)

        # yahtzee value 13
        if len(set(self.dice_table)) == 1 and self.table_check_box_var13.get() != 1:
            self.value13.set(50)

        # chance value 14
        if self.table_check_box_var14.get() != 1:
            self.value14.set(sum(self.dice_table))

        self.p_img1 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.pdice1) + '.jpg'))
        self.panel1.configure(image=self.p_img1)
        self.panel1.photo = self.p_img1
        self.p_img2 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.pdice2) + '.jpg'))
        self.panel2.configure(image=self.p_img2)
        self.panel2.photo = self.p_img2
        self.p_img3 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.pdice3) + '.jpg'))
        self.panel3.configure(image=self.p_img3)
        self.panel3.photo = self.p_img3
        self.p_img4 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.pdice4) + '.jpg'))
        self.panel4.configure(image=self.p_img4)
        self.panel4.photo = self.p_img4
        self.p_img5 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.pdice5) + '.jpg'))
        self.panel5.configure(image=self.p_img5)
        self.panel5.photo = self.p_img5

        self.tleft_help_int_value += 1
        self.tleft_var_int.set(3 - self.tleft_help_int_value)

        if self.tleft_var_int.get() == 0:
            self.btn_blank.grid(column=0, row=7, rowspan=2)  # if throws left = 0 then add fake roll button

    def computer_turn(self):
        self.tleft_var_int.set(3)
        self.tleft_help_int_value = 0
        self.was_table_checkbutton_func_called = False
        self.cdice1 = random.randint(1, 6)
        self.cdice2 = random.randint(1, 6)
        self.cdice3 = random.randint(1, 6)
        self.cdice4 = random.randint(1, 6)
        self.cdice5 = random.randint(1, 6)
        self.computer_action()
        self.computer_algorithm()
        self.computer_algorithm()
        self.computer_choose_category()

    # function that removes checkbutton after click, add value to total, hides blank roll button
    # sets not selected values of cells to zero, and gives computer a turn
    def table_checkbutton(self, button, val1, cel1):
        # code for creating and adding bonus for upper table to total score
        is_bonus_for_upper = BooleanVar()
        if self.value1.get() + self.value2.get() + self.value3.get() + self.value4.get() + self.value5.get() + self.value6.get() > 63:
            self.value7.set(35)
            is_bonus_for_upper = True

        self.was_table_checkbutton_func_called = True
        self.addit_var1 = val1.get()
        self.addit_var2 += self.addit_var1

        if is_bonus_for_upper is True:
            self.value15.set(self.addit_var2 + 35)
        else:
            self.value15.set(self.addit_var2)

        # hiding block dice checkbox so player cannot keep dice from previous turn
        self.player_c1.grid_forget()
        self.player_c2.grid_forget()
        self.player_c3.grid_forget()
        self.player_c4.grid_forget()
        self.player_c5.grid_forget()

        if self.table_check_box_var1.get() != 1:
            self.value1.set(0)
        if self.table_check_box_var2.get() != 1:
            self.value2.set(0)
        if self.table_check_box_var3.get() != 1:
            self.value3.set(0)
        if self.table_check_box_var4.get() != 1:
            self.value4.set(0)
        if self.table_check_box_var5.get() != 1:
            self.value5.set(0)
        if self.table_check_box_var6.get() != 1:
            self.value6.set(0)
        if self.table_check_box_var8.get() != 1:
            self.value8.set(0)
        if self.table_check_box_var9.get() != 1:
            self.value9.set(0)
        if self.table_check_box_var10.get() != 1:
            self.value10.set(0)
        if self.table_check_box_var11.get() != 1:
            self.value11.set(0)
        if self.table_check_box_var12.get() != 1:
            self.value12.set(0)
        if self.table_check_box_var13.get() != 1:
            self.value13.set(0)
        if self.table_check_box_var14.get() != 1:
            self.value14.set(0)
        val1.set(self.addit_var1)

        button.grid_forget()
        self.btn_blank.grid_forget()

        self.check_box_var1.set(0)
        self.check_box_var2.set(0)
        self.check_box_var3.set(0)
        self.check_box_var4.set(0)
        self.check_box_var5.set(0)

        cel1.config(background="Green")

        self.computer_turn()

    def computer_action(self):
        self.c_dice_table = [self.cdice1, self.cdice2, self.cdice3, self.cdice4, self.cdice5]

        if 1 in self.c_dice_table and self.cvalue_second_bool1 is False:  # second condition is to block the category after choosing it
            self.cvalue1.set(self.c_dice_table.count(1) * 1)
        else:
            self.cvalue1.set(0)  # when returning cvalueX it doesnt add, but refresh every time

        if 2 in self.c_dice_table and self.cvalue_second_bool2 is False:
            self.cvalue2.set(self.c_dice_table.count(2) * 2)
        else:
            self.cvalue2.set(0)

        if 3 in self.c_dice_table and self.cvalue_second_bool3 is False:
            self.cvalue3.set(self.c_dice_table.count(3) * 3)
        else:
            self.cvalue3.set(0)

        if 4 in self.c_dice_table and self.cvalue_second_bool4 is False:
            self.cvalue4.set(self.c_dice_table.count(4) * 4)
        else:
            self.cvalue4.set(0)

        if 5 in self.c_dice_table and self.cvalue_second_bool5 is False:
            self.cvalue5.set(self.c_dice_table.count(5) * 5)
        else:
            self.cvalue5.set(0)

        if 6 in self.c_dice_table and self.cvalue_second_bool6 is False:
            self.cvalue6.set(self.c_dice_table.count(6) * 6)
        else:
            self.cvalue6.set(0)

        # 3 of kind value 8
        y1 = sum(x * 3 for x in set(self.c_dice_table) if self.c_dice_table.count(x) > 2)
        if y1 > 0 and self.cvalue_second_bool8 is False:
            self.cvalue8.set(y1)
        else:
            self.cvalue8.set(0)

        # four of kind value 9
        y2 = sum(x * 4 for x in set(self.c_dice_table) if self.c_dice_table.count(x) > 3)
        if y2 > 0:
            self.cvalue9.set(y2)

        # full house value 10
        if len(set(self.c_dice_table)) == 2 and self.c_dice_table.count(self.c_dice_table[0]) in (2, 3):
            self.cvalue10.set(sum(self.c_dice_table))

        # ls value 11
        if set(self.c_dice_table) == set(range(1, 6)):
            self.cvalue11.set(30)

        # bs value 12
        if set(self.dice_table) == set(range(2, 7)):
            self.cvalue12.set(40)

        # yahtzee value 13
        if len(set(self.c_dice_table)) == 1:
            self.cvalue13.set(50)

        # chance value 14
        if True and self.cvalue_second_bool14 is False:
            self.cvalue14.set(sum(self.c_dice_table))
        else:
            self.cvalue14.set(0)

        return self.cvalue1, self.cvalue2, self.cvalue3, self.cvalue4, self.cvalue5, self.cvalue6, self.cvalue7,\
               self.cvalue8, self.cvalue9, self.cvalue10, self.cvalue11, self.cvalue12, self.cvalue13, self.cvalue14, self.c_dice_table

    def computer_algorithm(self):
        y0 = sum(x for x in set(self.c_dice_table) if self.c_dice_table.count(x) > 1)
        if y0 > 0:
            self.cvalue_pair = True

        ### computer algorithm ###

        if self.cvalue_pair == True:  # if pair
            if self.cvalue8.get() > 0:  # if 3 of kind # y1
                if self.cvalue9.get() > 0:  # if 4 of kind # y2
                    if len(set(self.c_dice_table)) == 1 and self.cvalue_bool13 is False:  # if yahtzee
                        self.cvalue_bool13 = True
                        return self.cvalue13  # set yahtzee
                    elif self.cvalue_bool9 is False:
                        self.cvalue_bool9 = True
                        return self.cvalue9  # set 4 of kind
                elif len(set(self.c_dice_table)) == 2 and self.c_dice_table.count(self.c_dice_table[0]) in (
                        2, 3) and self.cvalue_bool10 is False:  # full house
                    self.cvalue_bool10 = True
                    return self.cvalue10  # set full house score
                else:  # else reroll dices not matching 3 of kind | if not 4 of kind
                    if self.cvalue8.get() == 3:
                        if self.cdice1 != 1:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 1:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 1:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 1:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 1:
                            self.cdice5 = random.randint(1, 6)
                    elif self.cvalue8.get() == 6:
                        if self.cdice1 != 2:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 2:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 2:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 2:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 2:
                            self.cdice5 = random.randint(1, 6)
                    elif self.cvalue8.get() == 9:
                        if self.cdice1 != 3:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 3:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 3:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 3:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 3:
                            self.cdice5 = random.randint(1, 6)
                    elif self.cvalue8.get() == 12:
                        if self.cdice1 != 4:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 4:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 4:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 4:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 4:
                            self.cdice5 = random.randint(1, 6)
                    elif self.cvalue8.get() == 15:
                        if self.cdice1 != 5:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 5:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 5:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 5:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 5:
                            self.cdice5 = random.randint(1, 6)
                    elif self.cvalue8.get() == 18:
                        if self.cdice1 != 6:
                            self.cdice1 = random.randint(1, 6)
                        if self.cdice2 != 6:
                            self.cdice2 = random.randint(1, 6)
                        if self.cdice3 != 6:
                            self.cdice3 = random.randint(1, 6)
                        if self.cdice4 != 6:
                            self.cdice4 = random.randint(1, 6)
                        if self.cdice5 != 6:
                            self.cdice5 = random.randint(1, 6)

            elif len(set(self.c_dice_table)) == 3:  # elif another pair in the rest of dices
                not_pair = [z for z in set(self.c_dice_table) if
                            self.c_dice_table.count(z) == 1]  # reroll dice with no match
                if self.cdice1 == not_pair[0]:
                    self.cdice1 = random.randint(1, 6)
                if self.cdice2 == not_pair[0]:
                    self.cdice2 = random.randint(1, 6)
                if self.cdice3 == not_pair[0]:
                    self.cdice3 = random.randint(1, 6)
                if self.cdice4 == not_pair[0]:
                    self.cdice4 = random.randint(1, 6)
                if self.cdice5 == not_pair[0]:
                    self.cdice5 = random.randint(1, 6)
            else:  # else reroll all dices except 6's
                if self.cdice1 != 6:
                    self.cdice1 = random.randint(1, 6)
                if self.cdice2 != 6:
                    self.cdice2 = random.randint(1, 6)
                if self.cdice3 != 6:
                    self.cdice3 = random.randint(1, 6)
                if self.cdice4 != 6:
                    self.cdice4 = random.randint(1, 6)
                if self.cdice5 != 6:
                    self.cdice5 = random.randint(1, 6)
        elif set(range(1, 4)) in set(self.c_dice_table):  # if close to large straight or small straight
            if set(self.dice_table) == set(range(2, 7)) and self.cvalue_bool12 is False:  # large straight
                self.cvalue_bool2 = True
                return self.cvalue12
            elif set(self.dice_table) == set(range(1, 6)) and self.cvalue_bool11 is False:  # small straight
                self.cvalue_bool11 = True
                return self.cvalue11
            elif self.cdice1 == 4 or 5 or 6 or self.cdice2 or self.cdice3 or self.cdice4 or self.cdice5:
                self.cdice1 = random.randint(1, 6)
            elif self.cdice2 == 4 or 5 or 6 or self.cdice1 or self.cdice3 or self.cdice4 or self.cdice5:
                self.cdice2 = random.randint(1, 6)
            elif self.cdice3 == 4 or 5 or 6 or self.cdice2 or self.cdice1 or self.cdice4 or self.cdice5:
                self.cdice3 = random.randint(1, 6)
            elif self.cdice4 == 4 or 5 or 6 or self.cdice2 or self.cdice3 or self.cdice1 or self.cdice5:
                self.cdice4 = random.randint(1, 6)
            elif self.cdice5 == 4 or 5 or 6 or self.cdice2 or self.cdice3 or self.cdice4 or self.cdice1:
                self.cdice5 = random.randint(1, 6)
        else:
            self.cdice1 = random.randint(1, 6)
            self.cdice2 = random.randint(1, 6)
            self.cdice3 = random.randint(1, 6)
            self.cdice4 = random.randint(1, 6)
            self.cdice5 = random.randint(1, 6)
        self.c_dice_table = [self.cdice1, self.cdice2, self.cdice3, self.cdice4, self.cdice5]
        self.computer_action()  # adding this so program will calculate values of cvalueX every time dices are rolled and not leave cvalues of previous roll

        self.c_img1 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.cdice1) + '.jpg'))
        self.cpanel1.configure(image=self.c_img1)
        self.cpanel1.photo = self.c_img1
        self.c_img2 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.cdice2) + '.jpg'))
        self.cpanel2.configure(image=self.c_img2)
        self.cpanel2.photo = self.c_img2
        self.c_img3 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.cdice3) + '.jpg'))
        self.cpanel3.configure(image=self.c_img3)
        self.cpanel3.photo = self.c_img3
        self.c_img4 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.cdice4) + '.jpg'))
        self.cpanel4.configure(image=self.c_img4)
        self.cpanel4.photo = self.c_img4
        self.c_img5 = ImageTk.PhotoImage(Image.open('graphics/dice' + str(self.cdice5) + '.jpg'))
        self.cpanel5.configure(image=self.c_img5)
        self.cpanel5.photo = self.c_img5

        return self.cvalue1, self.cvalue2, self.cvalue3, self.cvalue4, self.cvalue5, self.cvalue6, self.cvalue7,\
               self.cvalue8, self.cvalue9, self.cvalue10, self.cvalue11, self.cvalue12, self.cvalue13, self.cvalue14, self.c_dice_table

    def computer_choose_category(self):
        is_bonus_for_upper_computer = BooleanVar()  # bonus for upper table for computer
        if self.cvalue1.get() + self.cvalue2.get() + self.cvalue3.get() + self.cvalue4.get() + self.cvalue5.get() + self.cvalue6.get() > 63:
            self.cvalue7.set(35)
            is_bonus_for_upper_computer = True
        if is_bonus_for_upper_computer is True:
            self.cvalue15.set(self.cvalue_help_add_int2 + 35)
        else:
            self.cvalue15.set(self.cvalue_help_add_int2)

        if self.cvalue13.get() == 50 and self.cvalue_second_bool13 is False:
            self.cvalue_second_bool13 = True
            self.cvalue_help_add_int1 = self.cvalue13.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue13.set(self.cvalue13.get())
            self.c2_13.grid(column=8, row=13)
            self.c2_13.config(background="Yellow")
            return
        if self.cvalue12.get() == 40 and self.cvalue_second_bool12 is False:
            self.cvalue_second_bool12 = True
            self.cvalue_help_add_int1 = self.cvalue12.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue12.set(self.cvalue12.get())
            self.c2_12.grid(column=8, row=12)
            self.c2_12.config(background="Yellow")
            return
        if self.cvalue11.get() == 30 and self.cvalue_second_bool11 is False:
            self.cvalue_second_bool11 = True
            self.cvalue_help_add_int1 = self.cvalue11.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue11.set(self.cvalue11.get())
            self.c2_11.grid(column=8, row=11)
            self.c2_11.config(background="Yellow")
            return
        if self.cvalue10.get() > 0 and self.cvalue_second_bool10 is False:
            self.cvalue_second_bool10 = True
            self.cvalue_help_add_int1 = self.cvalue10.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue10.set(self.cvalue10.get())
            self.c2_10.grid(column=8, row=10)
            self.c2_10.config(background="Yellow")
            return
        if self.cvalue9.get() > 0 and self.cvalue_second_bool9 is False:
            self.cvalue_second_bool9 = True
            self.cvalue_help_add_int1 = self.cvalue9.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue9.set(self.cvalue9.get())
            self.c2_9.grid(column=8, row=9)
            self.c2_9.config(background="Yellow")
            return

        if self.cvalue_bool13 is True and self.cvalue_second_bool13 is False:  # yahtzee
            self.cvalue_second_bool13 = True
            self.cvalue_help_add_int1 = self.cvalue13.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue13.set(self.cvalue13.get())
            self.c2_13.grid(column=8, row=13)
            self.c2_13.config(background="Yellow")
            return
        if self.cvalue_bool12 is True and self.cvalue_second_bool12 is False:  # large straight
            self.cvalue_second_bool12 = True
            self.cvalue_help_add_int1 = self.cvalue12.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue12.set(self.cvalue12.get())
            self.c2_12.grid(column=8, row=12)
            self.c2_12.config(background="Yellow")
            return
        if self.cvalue_bool11 is True and self.cvalue_second_bool11 is False:  # small straight
            self.cvalue_second_bool11 = True
            self.cvalue_help_add_int1 = self.cvalue11.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue11.set(self.cvalue11.get())
            self.c2_11.grid(column=8, row=11)
            self.c2_11.config(background="Yellow")
            return
        if self.cvalue_bool10 is True and self.cvalue_second_bool10 is False:  # full house
            self.cvalue_second_bool10 = True
            self.cvalue_help_add_int1 = self.cvalue10.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue10.set(self.cvalue10.get())
            self.c2_10.grid(column=8, row=10)
            self.c2_10.config(background="Yellow")
            return
        if self.cvalue_bool9 is True and self.cvalue_second_bool9 is False:  # 4 of kind
            self.cvalue_second_bool9 = True
            self.cvalue_help_add_int1 = self.cvalue9.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue9.set(self.cvalue9.get())
            self.c2_9.grid(column=8, row=9)
            self.c2_9.config(background="Yellow")
            return
        # upper
        max_cvalue = max(self.cvalue1.get(), self.cvalue2.get(), self.cvalue3.get(), self.cvalue4.get(), self.cvalue5.get(),
            self.cvalue6.get(), self.cvalue8.get(), self.cvalue14.get())

        if max_cvalue == self.cvalue1.get() and self.cvalue_second_bool1 is False:
            self.cvalue_second_bool1 = True
            self.cvalue_help_add_int1 = self.cvalue1.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue1.set(self.cvalue1.get())
            self.c2_1.grid(column=8, row=1)
            self.c2_1.config(background="Yellow")
            return
        if max_cvalue == self.cvalue2.get() and self.cvalue_second_bool2 is False:
            self.cvalue_second_bool2 = True
            self.cvalue_help_add_int1 = self.cvalue2.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue2.set(self.cvalue2.get())
            self.c2_2.grid(column=8, row=2)
            self.c2_2.config(background="Yellow")
            return
        if max_cvalue == self.cvalue3.get() and self.cvalue_second_bool3 is False:
            self.cvalue_second_bool3 = True
            self.cvalue_help_add_int1 = self.cvalue1.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue3.set(self.cvalue3.get())
            self.c2_3.grid(column=8, row=3)
            self.c2_3.config(background="Yellow")
            return
        if max_cvalue == self.cvalue4.get() and self.cvalue_second_bool4 is False:
            self.cvalue_second_bool4 = True
            self.cvalue_help_add_int1 = self.cvalue4.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue4.set(self.cvalue4.get())
            self.c2_4.grid(column=8, row=4)
            self.c2_4.config(background="Yellow")
            return
        if max_cvalue == self.cvalue5.get() and self.cvalue_second_bool5 is False:
            self.cvalue_second_bool5 = True
            self.cvalue_help_add_int1 = self.cvalue5.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue5.set(self.cvalue5.get())
            self.c2_5.grid(column=8, row=5)
            self.c2_5.config(background="Yellow")
            return
        if max_cvalue == self.cvalue6.get() and self.cvalue_second_bool6 is False:
            self.cvalue_second_bool6 = True
            self.cvalue_help_add_int1 = self.cvalue6.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue6.set(self.cvalue6.get())
            self.c2_6.grid(column=8, row=6)
            self.c2_6.config(background="Yellow")
            return
        if max_cvalue == self.cvalue8.get() and self.cvalue_second_bool8 is False:
            self.cvalue_second_bool8 = True
            self.cvalue_help_add_int1 = self.cvalue8.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue8.set(self.cvalue8.get())
            self.c2_8.grid(column=8, row=8)
            self.c2_8.config(background="Yellow")
            return
        if max_cvalue == self.cvalue14.get() and self.cvalue_second_bool14 is False:
            self.cvalue_second_bool14 = True
            self.cvalue_help_add_int1 = self.cvalue14.get()
            self.cvalue_help_add_int2 += self.cvalue_help_add_int1
            self.cvalue15.set(self.cvalue_help_add_int2)
            self.two_cvalue14.set(self.cvalue14.get())
            self.c2_14.grid(column=8, row=14)
            self.c2_14.config(background="Yellow")
            return


def main():
    root = tk.Tk()
    root.title("Yahtzee")
    win = MainWindow(root)
    win.col1_title()
    win.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
