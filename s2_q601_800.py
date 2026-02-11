# Section 2 - Logical Reasoning  |  Batch 4: Q 601-800
# Topics: Cube & Dice Logic, Age-based Puzzles
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# ===============================================
# CUBE & DICE LOGIC - Painted Cube
# ===============================================
("Cube & Dice Logic","Painted Cube",
 "A cube is painted red on all faces and cut into 27 equal smaller cubes. How many small cubes have 3 faces painted?",
 "6","8","12","1","B"),

("Cube & Dice Logic","Painted Cube",
 "A cube is painted and cut into 27 smaller cubes. How many have exactly 2 faces painted?",
 "6","8","12","10","C"),

("Cube & Dice Logic","Painted Cube",
 "A cube painted on all sides is cut into 27 small cubes. How many have exactly 1 face painted?",
 "6","8","12","1","A"),

("Cube & Dice Logic","Painted Cube",
 "A cube painted on all faces is cut into 27 smaller cubes. How many have no face painted?",
 "0","1","6","8","B"),

("Cube & Dice Logic","Painted Cube",
 "A cube is painted blue on all faces and cut into 64 smaller cubes (4x4x4). How many have 3 faces painted?",
 "4","6","8","12","C"),

("Cube & Dice Logic","Painted Cube",
 "A 4x4x4 cube painted on all faces: how many small cubes have exactly 2 painted faces?",
 "12","24","16","8","B"),

("Cube & Dice Logic","Painted Cube",
 "A 4x4x4 cube painted on all faces: how many have exactly 1 face painted?",
 "8","12","16","24","D"),

("Cube & Dice Logic","Painted Cube",
 "A 4x4x4 painted cube: how many small cubes have no paint at all?",
 "0","1","4","8","D"),

("Cube & Dice Logic","Painted Cube",
 "A cube is painted and divided into 125 smaller cubes (5x5x5). How many have 3 painted faces?",
 "6","8","12","10","B"),

("Cube & Dice Logic","Painted Cube",
 "A 5x5x5 painted cube: how many cubes have exactly 2 faces painted?",
 "24","30","36","12","C"),

("Cube & Dice Logic","Painted Cube",
 "A 5x5x5 painted cube: how many have exactly 1 face painted?",
 "54","48","36","24","A"),

("Cube & Dice Logic","Painted Cube",
 "A 5x5x5 painted cube: how many have no face painted?",
 "8","12","27","1","C"),

("Cube & Dice Logic","Painted Cube",
 "A 2x2x2 painted cube: how many small cubes have 3 faces painted?",
 "2","4","6","8","D"),

("Cube & Dice Logic","Painted Cube",
 "A 2x2x2 painted cube: how many have exactly 2 faces painted?",
 "0","4","8","12","A"),

("Cube & Dice Logic","Painted Cube",
 "A painted cube cut into 8 smaller cubes (2x2x2): how many have 0 faces painted?",
 "0","1","2","4","A"),

# -- Cube & Dice Logic - Dice Faces --
("Cube & Dice Logic","Dice Faces",
 "On a standard die, opposite faces sum to:",
 "6","7","8","9","B"),

("Cube & Dice Logic","Dice Faces",
 "On a standard die, 1 is opposite to:",
 "2","3","5","6","D"),

("Cube & Dice Logic","Dice Faces",
 "On a standard die, 2 is opposite to:",
 "1","3","4","5","D"),

("Cube & Dice Logic","Dice Faces",
 "On a standard die, 3 is opposite to:",
 "1","2","4","6","C"),

("Cube & Dice Logic","Dice Faces",
 "If a die shows 4 on top, the bottom face has:",
 "1","2","3","5","C"),

("Cube & Dice Logic","Dice Faces",
 "A die is rolled and shows 5 on top. The number on the bottom is:",
 "1","2","3","6","B"),

("Cube & Dice Logic","Dice Faces",
 "How many faces does a cube have?",
 "4","5","6","8","C"),

("Cube & Dice Logic","Dice Faces",
 "How many edges does a cube have?",
 "6","8","10","12","D"),

("Cube & Dice Logic","Dice Faces",
 "How many vertices (corners) does a cube have?",
 "4","6","8","12","C"),

("Cube & Dice Logic","Dice Faces",
 "Two dice are rolled. The maximum sum of top faces is:",
 "10","11","12","13","C"),

# -- Cube & Dice Logic - Dice Rotation --
("Cube & Dice Logic","Dice Rotation",
 "A die has 3 on top. When rotated towards North, the new top face (if 5 was facing North) is:",
 "2","4","5","6","C"),

("Cube & Dice Logic","Dice Rotation",
 "If a die with 1 on top is rotated once towards you (South), 2 was facing you. Now on top is:",
 "5","2","4","3","B"),

("Cube & Dice Logic","Dice Rotation",
 "A die shows 6 on top. If rotated to the right once, and 3 was on the right face, now on top is:",
 "3","4","1","2","A"),

("Cube & Dice Logic","Dice Rotation",
 "Two positions of a die are shown: (1) Top=2, Front=1 (2) Top=3, Front=1. What is opposite to 2?",
 "5","4","3","6","C"),

("Cube & Dice Logic","Dice Rotation",
 "In two views of a die: (1) Top=1, Front=2, Right=3 and (2) Top=4, Front=2, Right=3. Opposite of 1 is:",
 "6","5","3","4","D"),

("Cube & Dice Logic","Dice Rotation",
 "A die is rotated from position top=1 twice to the left. If the right face was 3 and front was 2, the new top is:",
 "4","5","3","6","C"),

# -- Cube & Dice Logic - Unfolded Cube --
("Cube & Dice Logic","Unfolded Cube",
 "A cube net (cross shape) has face A at center. The face opposite to A is:",
 "The face 2 squares away from A in a straight line",
 "The face adjacent to A",
 "A itself",
 "There is no opposite","A"),

("Cube & Dice Logic","Unfolded Cube",
 "An unfolded cube has 6 faces. How many different nets (unfoldings) of a cube exist?",
 "6","10","11","12","C"),

("Cube & Dice Logic","Unfolded Cube",
 "In a cube net shaped like a 'T', the bottom of the T is opposite to:",
 "The top of the T","The left of the T","Two squares above bottom","The rightmost square","C"),

("Cube & Dice Logic","Unfolded Cube",
 "In a cross-shaped cube net, if 1 is at center, 2 is on top, 3 is on right, 4 is on bottom, 5 is on left, 6 is two squares above center, then opposite of 1 is:",
 "6","2","3","4","A"),

("Cube & Dice Logic","Unfolded Cube",
 "When folding a cube net, adjacent squares in the net become:",
 "Opposite faces","Adjacent faces","The same face","Diagonal faces","B"),

# -- Cube & Dice Logic - Counting / Stacking --
("Cube & Dice Logic","Counting / Stacking",
 "If 8 unit cubes are arranged to form a larger cube, the side of the larger cube is:",
 "2 units","3 units","4 units","8 units","A"),

("Cube & Dice Logic","Counting / Stacking",
 "27 small cubes form a bigger cube. How many small cubes are completely hidden inside?",
 "0","1","8","27","B"),

("Cube & Dice Logic","Counting / Stacking",
 "64 cubes arranged in a 4x4x4 cube: cubes on the surface only?",
 "48","56","60","64","B"),

("Cube & Dice Logic","Counting / Stacking",
 "In a stack of cubes 3 wide, 3 deep, 3 high: total cubes on edges (including corners)?",
 "12","20","24","8","B"),

("Cube & Dice Logic","Counting / Stacking",
 "If you stack 6 cubes in a single row, how many faces are visible (from outside)?",
 "22","24","26","20","C"),

("Cube & Dice Logic","Counting / Stacking",
 "A 3x3x3 cube is built from unit cubes. Total surface area (in unit face squares)?",
 "27","36","45","54","D"),

# ===============================================
# AGE-BASED LOGIC PUZZLES - Present Age
# ===============================================
("Age-based Logic","Present Age",
 "Ram is twice as old as Shyam. If Shyam is 15, Ram's age is:",
 "25","30","20","35","B"),

("Age-based Logic","Present Age",
 "A is 5 years older than B. If B is 20, how old is A?",
 "15","20","25","30","C"),

("Age-based Logic","Present Age",
 "The ages of A and B are in the ratio 3:4. If A is 24, B is:",
 "28","30","32","36","C"),

("Age-based Logic","Present Age",
 "If a father is 4 times as old as his son and the son is 10 years old, the father is:",
 "30","35","40","45","C"),

("Age-based Logic","Present Age",
 "P's age is three times Q's age. If Q is 12, then P's age is:",
 "24","30","36","48","C"),

("Age-based Logic","Present Age",
 "Sum of ages of A and B is 50. A is 20. B's age is:",
 "20","25","30","35","C"),

("Age-based Logic","Present Age",
 "Rahul is half the age of his uncle. If uncle is 48, Rahul is:",
 "12","18","20","24","D"),

("Age-based Logic","Present Age",
 "A mother is 25 years older than her daughter. If the daughter is 18, mother's age is:",
 "40","42","43","45","C"),

("Age-based Logic","Present Age",
 "X is 3 years younger than Y. If Y is 28, X is:",
 "25","26","27","31","A"),

("Age-based Logic","Present Age",
 "The ages of three friends are 15, 20, and 25. Their average age is:",
 "18","19","20","21","C"),

# -- Age-based Logic - Future Age --
("Age-based Logic","Future Age",
 "A man is 30 years old now. How old will he be in 12 years?",
 "40","42","44","38","B"),

("Age-based Logic","Future Age",
 "If Anu is 10 now, her age after 5 years will be:",
 "12","13","14","15","D"),

("Age-based Logic","Future Age",
 "A father is 40 and son is 10. In how many years will the father be twice the son's age?",
 "10","15","20","25","C"),

("Age-based Logic","Future Age",
 "Ram is 25 now. Shyam is 15 now. After how many years will Ram be 1.5 times Shyam's age?",
 "5","10","15","20","A"),

("Age-based Logic","Future Age",
 "A is 32, B is 8. In how many years will A be 3 times B's age?",
 "2","4","6","8","B"),

("Age-based Logic","Future Age",
 "Present ages: Mother = 36, Daughter = 12. In how many years will mother be twice daughter's age?",
 "6","8","10","12","D"),

("Age-based Logic","Future Age",
 "If Ravi is 20 now, after how many years will his age be 35?",
 "10","12","15","18","C"),

("Age-based Logic","Future Age",
 "The sum of current ages of A and B is 40. After 5 years, their sum will be:",
 "45","48","50","55","C"),

("Age-based Logic","Future Age",
 "X's age is 18 now. In 7 years, X's age will be:",
 "22","23","24","25","D"),

("Age-based Logic","Future Age",
 "A person's age doubles in 30 years. His current age is:",
 "15","20","25","30","D"),

# -- Age-based Logic - Past Age --
("Age-based Logic","Past Age",
 "Ravi is 25 now. What was his age 10 years ago?",
 "10","12","15","20","C"),

("Age-based Logic","Past Age",
 "3 years ago, A was 4 times as old as B. A is 27 now. B's present age is:",
 "6","9","10","12","B"),

("Age-based Logic","Past Age",
 "5 years ago, P's age was 20. P's current age is:",
 "15","20","25","30","C"),

("Age-based Logic","Past Age",
 "4 years ago, the ratio of A's to B's age was 3:2. Now A is 19. B's current age is:",
 "12","14","16","18","B"),

("Age-based Logic","Past Age",
 "10 years ago, Mohan was half the age of Sohan. Sohan is 40 now. Mohan's current age is:",
 "20","22","25","30","C"),

("Age-based Logic","Past Age",
 "6 years ago, the ages of A and B were equal. Now A is 24. B's current age is:",
 "18","20","22","24","D"),

("Age-based Logic","Past Age",
 "2 years ago, a mother was 6 times her son's age. The son is 5 now. Mother's current age is:",
 "16","18","20","22","C"),

("Age-based Logic","Past Age",
 "8 years ago, X was thrice Y. Now X is 32. Y's present age is:",
 "14","16","18","20","B"),

# -- Age-based Logic - Ratio Problems --
("Age-based Logic","Ratio Problems",
 "Ages of A and B are in ratio 2:3. Sum of their ages is 50. A's age is:",
 "15","18","20","25","C"),

("Age-based Logic","Ratio Problems",
 "The ratio of ages of a father and son is 7:2. If the father is 42, the son is:",
 "10","12","14","16","B"),

("Age-based Logic","Ratio Problems",
 "A and B's ages are in ratio 5:3. If A is 10 years older, B's age is:",
 "10","12","15","20","C"),

("Age-based Logic","Ratio Problems",
 "Ages in ratio 4:5 with difference 6 years. The younger person's age is:",
 "20","22","24","26","C"),

("Age-based Logic","Ratio Problems",
 "The ratio of P and Q's ages 5 years hence will be 4:3. P is 23 now. Q's current age is:",
 "16","17","18","19","A"),

("Age-based Logic","Ratio Problems",
 "Present ages of X and Y are in ratio 3:5. After 10 years, ratio becomes 1:2. X's current age is:",
 "30","20","15","25","A"),

("Age-based Logic","Ratio Problems",
 "Father to son age ratio is 5:1. After 5 years, ratio is 3:1. Father's present age is:",
 "25","30","35","40","A"),

("Age-based Logic","Ratio Problems",
 "Ratio of A:B ages = 6:5. If sum of ages is 44, A is:",
 "22","24","26","20","B"),

# -- Age-based Logic - Complex Problems --
("Age-based Logic","Complex Problems",
 "The product of ages of A and B is 120. A is older by 2 years. Find A's age.",
 "10","12","14","8","B"),

("Age-based Logic","Complex Problems",
 "Sum of ages of a husband and wife is 70. The husband is 6 years older. Wife's age is:",
 "30","32","34","36","B"),

("Age-based Logic","Complex Problems",
 "A is twice B's age. 5 years ago, A was 3 times B's age. B's current age is:",
 "8","10","12","15","B"),

("Age-based Logic","Complex Problems",
 "The sum of the ages of 5 members of a family is 100. Average age is:",
 "18","20","22","25","B"),

("Age-based Logic","Complex Problems",
 "A man was 24 when his son was born. Now the son is 18. Father's current age is:",
 "36","40","42","44","C"),

("Age-based Logic","Complex Problems",
 "If I add 5 to twice my age, I get 45. My age is:",
 "18","19","20","22","C"),

("Age-based Logic","Complex Problems",
 "A is older than B by 2 years. B is older than C by 3 years. If C is 10, A is:",
 "14","15","16","17","B"),

("Age-based Logic","Complex Problems",
 "10 years hence, A will be twice as old as B was 10 years ago. A is 30 now. B is now:",
 "20","25","30","35","B"),

("Age-based Logic","Complex Problems",
 "At birth of the younger child, the elder child was 5. Now their sum is 25. Elder child's age is:",
 "15","14","13","12","A"),

("Age-based Logic","Complex Problems",
 "Three people X, Y, Z: X+Y=40, Y+Z=30, Z+X=34. Find Y's age.",
 "18","20","22","16","A"),

# -- Additional Cube & Dice --
("Cube & Dice Logic","Painted Cube",
 "A cube painted green on two opposite faces and red on rest, then cut into 27 cubes. How many have only green?",
 "2","4","6","8","A"),

("Cube & Dice Logic","Painted Cube",
 "A 3x3x3 cube has one face painted. How many small cubes have paint on them?",
 "9","6","3","1","A"),

("Cube & Dice Logic","Dice Faces",
 "Two dice are thrown. What is the minimum possible sum?",
 "1","2","3","4","B"),

("Cube & Dice Logic","Dice Faces",
 "On a standard die, if 4 faces towards you and 3 is on your right, what is on top?",
 "1","2","5","6","B"),

("Cube & Dice Logic","Dice Rotation",
 "Three views of a die: (1) 1,2,3 visible (2) 1,5,3 visible (3) 3,4,5 visible. Opposite of 1 is:",
 "3","4","5","6","B"),

("Cube & Dice Logic","Counting / Stacking",
 "125 unit cubes form a 5x5x5 cube. How many cubes are on the surface?",
 "96","98","100","102","B"),

("Cube & Dice Logic","Unfolded Cube",
 "Which of the following CANNOT be a cube net? A 2x3 rectangle, a cross shape, a T shape, or a straight line of 6?",
 "2x3 rectangle","Cross shape","T shape","Straight line of 6","D"),

("Cube & Dice Logic","Painted Cube",
 "A 6x6x6 cube painted on all faces: how many small cubes have 3 faces painted?",
 "6","8","12","24","B"),

# -- Additional Age Puzzles --
("Age-based Logic","Present Age",
 "Average age of 3 children in a family is 8 years. Average including parents is 20. Sum of parents' ages is:",
 "52","64","76","80","C"),

("Age-based Logic","Future Age",
 "The present ages of A and B differ by 16 years. 6 years ago, the elder was 3 times the younger. The present age of the elder is:",
 "24","26","28","30","C"),

("Age-based Logic","Past Age",
 "7 years ago, P was 7 times Q's age. P's age is 5 times Q's age now. P's current age is:",
 "25","30","35","40","C"),

("Age-based Logic","Ratio Problems",
 "A's age is to B's age as 3:7. After 6 years, ratio becomes 1:2. A's present age is:",
 "6","8","12","18","C"),

("Age-based Logic","Complex Problems",
 "A father is 30 years older than his son. In 12 years, he will be twice his son's age. Son's present age?",
 "14","16","18","20","C"),
]
