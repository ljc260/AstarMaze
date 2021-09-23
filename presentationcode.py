import xlsxwriter
import Astar as star
import time as t
import maze as Maze

from colorama import init
from colorama import Fore, Back, Style
from tkinter import *
class Ui_Form(object):
    def setupUi(self, root):
        root.title('A * was born')
        
        root.geometry("400x400")
        mylabel = Label(root, text="Enter FileName with no whitespace")
        mylabel.pack(pady=10)

        self.textbox = Entry(root, width=50, font=('Helvetica', 30))
        self.textbox.pack(padx=10, pady=10)

        mybutton2 = Button(root, text="A * FUN", command=lambda: self.main())
        mybutton2.pack(pady=10)

    def doAstarappendtoexcel(self, worksheet, row, height, width, heuristicType):
        count = 1
        print("Testing " + str(height) + "X" + str(width))
        t.sleep(1)
        while count < 7:
            print("Search: " + str(count))
            t.sleep(2)
            time = star.main(height, width, heuristicType) * 100000
            if heuristicType == 0:
                worksheet.write(row, 0, str(height)+"X"+str(width)+ " Manhattan Distance Time")
            elif heuristicType == 1:
                worksheet.write(row, 0, str(height)+"X"+str(width)+ " Euclidean Distance Time")
            elif heuristicType == 2:
                worksheet.write(row, 0, str(height)+"X"+str(width)+ " Educated Guess Distance Time")
            worksheet.write(row, 1, time)
            t.sleep(4)
            row += 1
            count += 1
        return row

    def main(self):
        workbook = xlsxwriter.Workbook(self.textbox.get() + 'AStarStats.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, "Maze and hueristic tested")
        worksheet.write(0, 1, "Average Time in MicroSeconds")
        # 10 X 10
        print("Staring with Manhattan Distance...")
        t.sleep(5)
        row = 1
        height = 10
        width = 10
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 0)
        #20 X 20
        height = 20
        width = 20
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 0)
        # 30 X 30
        height = 30
        width = 30
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 0)

        print("Next with Euclidean Distance...")
        t.sleep(5)

        # 10 X 10
        height = 10
        width = 10
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 1)
        #20 X 20
        height = 20
        width = 20
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 1)
        # 30 X 30
        height = 30
        width = 30
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 1)

        print("Lastly, my educated guess... :-)")
        t.sleep(5)
        # 10 X 10
        height = 10
        width = 10
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 2)
        #20 X 20
        height = 20
        width = 20
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 2)
        # 30 X 30
        height = 30
        width = 30
        row = self.doAstarappendtoexcel(worksheet, row, height, width, 2)
        row += 2
        worksheet.write(row, 0, "Average time")
        worksheet.write(row, 1, "Average Time in Micro Seconds")
        row += 1
        worksheet.write(row, 0, "10X10 Manhattan Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B2:B7)')
        row += 1
        worksheet.write(row, 0, "20X20 Manhattan Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B8:B13)')
        row += 1
        worksheet.write(row, 0, "30X30 Manhattan Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B14:B19)')
        row += 1

        worksheet.write(row, 0, "10X10 Euclidean Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B20:B25)')
        row += 1
        worksheet.write(row, 0, "20X20 Euclidean Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B26:B31)')
        row += 1
        worksheet.write(row, 0, "30X30 Euclidean Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B32:B37)')
        row += 1

        worksheet.write(row, 0, "10X10 Educated Guess Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B38:B43)')
        row += 1
        worksheet.write(row, 0, "20X20 Educated Guess Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B44:B49)')
        row += 1
        worksheet.write(row, 0, "30X30 Educated Guess Distance Avg")
        worksheet.write_formula(row, 1, '=AVERAGE(B50:B55)')
        row += 1
    
        workbook.close()
        print("Done and stats written to excel")

if __name__ == '__main__':
    root = Tk()
    ui = Ui_Form()
    ui.setupUi(root)
    root.mainloop()