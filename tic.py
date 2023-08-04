s = input("Enter pattern as XXX___OO_ or any pattern have x , o and _in (0-9) \n") 
ls = [s[0:3], s[3:6], s[6:9], s[0] + s[3] + s[6], s[1] + s[4] + s[7], s[2] + s[5] + s[8], s[0] + s[4] + s[8], s[6] + s[4] + s[2]]

print(f"""
---------
| {s[0]} {s[1]} {s[2]} |
| {s[3]} {s[4]} {s[5]} |
| {s[6]} {s[7]} {s[8]} |
---------""")
if ("XXX" in ls and "OOO" in ls) or abs(s.count("X") - s.count("O")) >= 2:
    print("Impossible")
elif "_" not in s and "XXX" not in ls and "OOO" not in ls:
     print("Draw")
elif "_" in s and "XXX" not in ls and "OOO" not in ls:
    print("Game not finished")
elif "XXX" in ls:
    print("X wins")
elif "OOO" in ls:
     print("O wins") 

#- s[0:3] - First row
#- s[3:6] - Second row
#- s[6:9] - Third row
#- s[0] + s[3] + s[6] - First column
#- s[1] + s[4] + s[7] - Second column
#- s[2] + s[5] + s[8] - Third column
#- s[0] + s[4] + s[8] - Main diagonal
#- s[6] + s[4] + s[2] - Anti-diagonal


# Input: 
# XXXOOOO__

# Output:
# --------- 
# | X X X |
# | O O O |
# | _ _ _ |
# ---------
# Impossible

# Input:  
# XO_X__O_O

# Output:
# ---------
# | X O _ |  
# | X _ _ |
# | O _ O |
# ---------
# Game not finished

# Input:
# XXX___OO_

# Output: 
# ---------
# | X X X |
# | _ _ _ |
# | _ _ O O |  
# ---------
# X wins

# Input:
# _O_OXX_X_

# Output: 
# ---------
# | _ O _ |
# | O X X |
# | _ X _ |
# ---------
# O wins