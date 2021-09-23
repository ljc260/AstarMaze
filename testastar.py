import xlsxwriter
import Astar as star
def doAstarappendtoexcel(worksheet, row, height, width, heuristicType):
    count = 0
    while count < 6:
        time = star.main(height, width, heuristicType) * 100000
        if heuristicType == 0:
            worksheet.write(row, 0, str(height)+"X"+str(width)+ " Manhattan Distance Time")
        elif heuristicType == 1:
            worksheet.write(row, 0, str(height)+"X"+str(width)+ " Euclidean Distance Time")
        elif heuristicType == 2:
            worksheet.write(row, 0, str(height)+"X"+str(width)+ " Educated Guess Distance Time")
        worksheet.write(row, 1, time)
        row += 1
        count += 1
    return row

def main():
    workbook = xlsxwriter.Workbook('AStarStats.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Maze and hueristic tested")
    worksheet.write(0, 1, "Average Time in MicroSeconds")
    # 10 X 10
    row = 1
    height = 10
    width = 10
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    #20 X 20
    height = 20
    width = 20
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    # 30X 30
    height = 30
    width = 30
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 40
    width = 40
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 50
    width = 50
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 60
    width = 60
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 70
    width = 70
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 80
    width = 80
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 90
    width = 90
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)
    height = 100
    width = 100
    row = doAstarappendtoexcel(worksheet, row, height, width, 0)

    # 10 X 10
    height = 10
    width = 10
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    #20 X 20
    height = 20
    width = 20
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    # 30X 30
    height = 30
    width = 30
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 40
    width = 40
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 50
    width = 50
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 60
    width = 60
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 70
    width = 70
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 80
    width = 80
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 90
    width = 90
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)
    height = 100
    width = 100
    row = doAstarappendtoexcel(worksheet, row, height, width, 1)

    # 10 X 10
    height = 10
    width = 10
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    #20 X 20
    height = 20
    width = 20
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    # 30X 30
    height = 30
    width = 30
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 40
    width = 40
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 50
    width = 50
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 60
    width = 60
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 70
    width = 70
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 80
    width = 80
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 90
    width = 90
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    height = 100
    width = 100
    row = doAstarappendtoexcel(worksheet, row, height, width, 2)
    workbook.close()

if __name__ == '__main__':
    main()