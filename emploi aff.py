class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Frame(root)
                self.e.grid(row=i, column=j)
                self.s = Label(self.e, text = lst[i][j],width=10,height=2)
                self.s.pack()


# take the data
lst = [('', '8-10', '10-12', '' , 'aa'),
       ('lundi', 'Aaryan', 'Pune', 18,'aa'),
       (3, 'Vaishnavi', 'Mumbai', 20,'aa'),
       (4, 'Rachna', 'Mumbai', 21 , 'aa'),
    (5, 'Shubham', 'Delhi', 21, 'aa'),
(5, 'Shubham', 'Delhi', 21,'aa')
       ]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()

t = Table(root)
root.mainloop()