TODO: Reflect on what you learned this week and what is still unclear.

Run this test:
python ..\course\set2\tests.py


Other solutions to Exercise 3 Engineering Problem
######
    if moves == should_move:
        return "No Problem"
    if moves and not should_move:
        return "Duct Tape"
    if not moves and should_move:
        return "WD-40"

######
    if moves == should_move:
        return "No Problem"
    elif moves and not should_move:
        return "Duct Tape"
    elif not moves and should_move:
        return "WD-40"
    else:
        print ("OMG, you broke the fabric of the universe")


    if moves:
        if should_move:
            return "No Problem"
        if not should_move:
            return "Duct Tape"
    if not moves:
        if should_move:
            return "WD-40"
        if not should_move:
            return "No Problem"


loops 1a alternative solution
["*"] * 10


loops 1b alternative solution
append ["*"] * 10 to list

loops 2 alternative solution
star_square = []
for j in range(10):
    star_square.append(loops_1c(number_of_items=10, symbol="*"))
