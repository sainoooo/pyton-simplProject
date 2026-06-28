#choose a cube
print("     a    b    c")
row1 = ["🟪","🟪","🟪"]
row2 = ["🟪","🟪","🟪"]
row3 = ["🟪","🟪","🟪"]
map1 =  [row1,row2,row3]
print(f"1 {row1}\n2 {row2}\n3 {row3}")
choose = input("choose one of the cube \n example:b4 ==> ")
column = choose[0]
if column == "a":
    column = 0
if column == "b":
    column = 1
elif column == "c":
    column = 2
rowC = int(choose[1])
map1[rowC - 1][column] = "🟨"
print("     a    b    c")
print(f"1 {row1}\n2 {row2}\n3 {row3}")
