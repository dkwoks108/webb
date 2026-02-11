# Section 2 - Logical Reasoning  |  Batch 2: Q 201-400
# Topics: Ranking & Order, Alphabet Reasoning
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# ===============================================
# RANKING & ORDER - Position from Left/Right
# ===============================================
("Ranking & Order","Position from Left/Right",
 "In a row of 30 students, Ravi is 12th from the left. His position from the right is:",
 "18th","19th","20th","17th","B"),

("Ranking & Order","Position from Left/Right",
 "In a row of 40 students, Priya is 15th from the right. Her position from the left is:",
 "25th","26th","27th","24th","B"),

("Ranking & Order","Position from Left/Right",
 "Arun is 10th from the left and 20th from the right. How many students are in the row?",
 "29","30","31","28","A"),

("Ranking & Order","Position from Left/Right",
 "In a queue, Ramu is 5th from the front and 10th from the back. Total people in the queue?",
 "14","15","16","13","A"),

("Ranking & Order","Position from Left/Right",
 "Sita is 18th from the left end. If total students are 35, what is her position from right?",
 "18th","17th","16th","19th","A"),

("Ranking & Order","Position from Left/Right",
 "In a row of 25 boys, Kiran is 8th from the left. How many boys are to his right?",
 "16","17","18","15","B"),

("Ranking & Order","Position from Left/Right",
 "In a class of 50 students, Meera ranks 20th from top. Her rank from the bottom is:",
 "30th","31st","32nd","29th","B"),

("Ranking & Order","Position from Left/Right",
 "Ajay is 14th from the right and there are 45 people. His position from left is:",
 "31st","32nd","33rd","30th","B"),

("Ranking & Order","Position from Left/Right",
 "Rahul is exactly in the middle of a row of 25 students. His position from either end is:",
 "12th","13th","14th","11th","B"),

("Ranking & Order","Position from Left/Right",
 "In a row of 33 students, who stands in the exact middle?",
 "16th from either end","17th from either end","15th from either end","18th from either end","B"),

# -- Ranking & Order - Interchanging Positions --
("Ranking & Order","Interchanging Positions",
 "In a row, A is 7th from the left and B is 11th from the right. They interchange positions. Now A is 11th from the right. B's new position from the left is:",
 "7th","8th","6th","9th","A"),

("Ranking & Order","Interchanging Positions",
 "X is 15th from the left and Y is 20th from the right. After interchange, X is 20th from right. How many students are in the row?",
 "34","35","33","36","A"),

("Ranking & Order","Interchanging Positions",
 "Ravi is 9th from left and Suresh is 16th from right. After swapping, Ravi becomes 16th from right. Total students?",
 "24","23","25","22","A"),

("Ranking & Order","Interchanging Positions",
 "A is 12th from left, B is 18th from right. After exchange, A is 18th from right. Minimum students?",
 "29","28","30","27","A"),

("Ranking & Order","Interchanging Positions",
 "In a row, P is 8th from front. After interchanging with Q who is 14th from end, P becomes 14th from end. Total?",
 "21","22","20","23","A"),

("Ranking & Order","Interchanging Positions",
 "Ram is 5th from left, Shyam is 5th from right. After swapping, Ram is 5th from right. Total in row?",
 "9","10","8","11","A"),

("Ranking & Order","Interchanging Positions",
 "M is 13th from the left and N is 22nd from the right. They swap. If M is now 22nd from right, total students?",
 "34","33","35","32","A"),

("Ranking & Order","Interchanging Positions",
 "After interchanging, P who was 6th from left becomes 10th from right. Q who was 10th from right becomes 6th from left. Total people?",
 "15","16","14","17","A"),

# -- Ranking & Order - Between Two People --
("Ranking & Order","Between Two People",
 "In a row of 50, A is 14th from left and B is 18th from right. How many students are between them?",
 "19","18","20","17","B"),

("Ranking & Order","Between Two People",
 "In a queue of 35, P is 10th from front and Q is 12th from back. How many between them?",
 "13","14","15","12","B"),

("Ranking & Order","Between Two People",
 "In a row of 40 children, Ram is 11th from left and Hari is 15th from right. Students between them?",
 "14","15","16","13","A"),

("Ranking & Order","Between Two People",
 "A is 5th from left, B is 5th from right in a row of 20. People between them?",
 "10","11","9","8","A"),

("Ranking & Order","Between Two People",
 "In a row of 30, X is 8th from left and Y is 10th from right. How many people between them?",
 "12","13","11","10","A"),

("Ranking & Order","Between Two People",
 "In a class of 45, Sita ranks 20th from top, Gita ranks 30th from bottom. How many students between them?",
 "3","4","5","2","B"),

("Ranking & Order","Between Two People",
 "A is 6th from the left and B is 6th from the right in a row of 15. People between them?",
 "3","4","2","5","A"),

("Ranking & Order","Between Two People",
 "In a row of 25, M is 7th from left and N is 9th from right. Students between them?",
 "9","10","8","11","A"),

# -- Ranking & Order - Class Rank --
("Ranking & Order","Class Rank",
 "Suman ranks 7th in a class of 30. Her rank from the bottom is:",
 "23rd","24th","25th","22nd","B"),

("Ranking & Order","Class Rank",
 "In a class, Raj ranks 9th from top and 38th from bottom. Total students?",
 "46","47","45","48","A"),

("Ranking & Order","Class Rank",
 "Anita's rank in class is 12th from top and 25th from bottom. How many students?",
 "36","37","35","38","A"),

("Ranking & Order","Class Rank",
 "If Mohan is 16th from the top and Sohan is 29th from the bottom in a class of 44, who is ahead?",
 "Mohan","Sohan","Both same","Cannot determine","A"),

("Ranking & Order","Class Rank",
 "In a class of 60, Deepa's rank from top is 22nd. Her rank from bottom is:",
 "38th","39th","40th","37th","B"),

("Ranking & Order","Class Rank",
 "Riya ranks third from the top. Priya ranks fifth from the bottom in a class of 20. How many students are between them?",
 "12","13","14","11","A"),

("Ranking & Order","Class Rank",
 "In a class of 48, A is 15th from top, B is 20th from bottom. How many are between them?",
 "13","14","12","15","A"),

("Ranking & Order","Class Rank",
 "Ajay's rank improves by 5 positions and becomes 8th. His earlier rank was:",
 "3rd","13th","12th","11th","B"),

("Ranking & Order","Class Rank",
 "In a class of 32, Anil was ranked 14th. Next year, 3 students joined and Anil's rank dropped by 2. His new rank from bottom?",
 "18th","19th","20th","21st","C"),

# -- Ranking & Order - Arrangement --
("Ranking & Order","Linear Arrangement",
 "Five people A, B, C, D, E sit in a row. C sits in the middle, A sits at the left end. Who might sit at the right end?",
 "Only C","B, D, or E","Only A","Only D","B"),

("Ranking & Order","Linear Arrangement",
 "In a row of 6 people, P sits 3rd from left. Q sits 4th from right. Are P and Q the same person?",
 "Yes, always","No, never","Yes, if row has 6 people","Cannot determine","C"),

("Ranking & Order","Linear Arrangement",
 "Seven people sit in a row facing North. D is at one end. A is 3rd to the left of D. Who is at the other end if E is 4th from the right?",
 "A","B","E","Cannot determine","D"),

# ===============================================
# ALPHABET REASONING - Letter Position
# ===============================================
("Alphabet Reasoning","Letter Position",
 "What is the 15th letter of the English alphabet?",
 "N","O","P","M","B"),

("Alphabet Reasoning","Letter Position",
 "Which letter is 8th from the left in the alphabet?",
 "G","H","I","F","B"),

("Alphabet Reasoning","Letter Position",
 "What is the position of the letter 'M' in the English alphabet?",
 "12","13","14","11","B"),

("Alphabet Reasoning","Letter Position",
 "The 20th letter of the English alphabet is:",
 "S","T","U","R","B"),

("Alphabet Reasoning","Letter Position",
 "Which letter is exactly midway between A and K?",
 "E","F","G","D","B"),

("Alphabet Reasoning","Letter Position",
 "What is the 22nd letter of the English alphabet?",
 "U","V","W","T","B"),

("Alphabet Reasoning","Letter Position",
 "If A = 1, B = 2, ..., Z = 26, then C + A + T = ?",
 "36","37","42","45","B"),

("Alphabet Reasoning","Letter Position",
 "Which letter is at position 11 in the alphabet?",
 "J","K","L","I","B"),

("Alphabet Reasoning","Letter Position",
 "The sum of positions of A and Z is:",
 "27","26","25","28","A"),

("Alphabet Reasoning","Letter Position",
 "Which letter is 5th from the right end of the alphabet?",
 "V","U","W","T","A"),

# -- Alphabet Reasoning - Reverse Alphabet --
("Alphabet Reasoning","Reverse Alphabet",
 "In the reverse alphabet (Z=1, Y=2, ..., A=26), the position of 'D' is:",
 "22","23","24","21","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "Which letter is 10th from the right end of the alphabet?",
 "P","Q","R","O","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "In the reverse order, which letter occupies the 5th position?",
 "V","U","W","T","A"),

("Alphabet Reasoning","Reverse Alphabet",
 "If the alphabet is reversed, the 13th letter is:",
 "M","N","O","L","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "What is the 18th letter from the right in the English alphabet?",
 "H","I","J","G","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "In reverse order (Z, Y, X, ...), the 7th letter is:",
 "T","S","U","R","A"),

("Alphabet Reasoning","Reverse Alphabet",
 "Which letter is at position 20 from the end of the alphabet?",
 "F","G","H","E","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "In reverse, what is the position of 'R'?",
 "8","9","10","7","B"),

# -- Alphabet Reasoning - Gaps & Midpoint --
("Alphabet Reasoning","Gaps & Midpoint",
 "Which letter is exactly midway between E and Q?",
 "J","K","L","I","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters are between G and P?",
 "7","8","9","6","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "The letter midway between H and T is:",
 "M","N","O","L","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters are between D and L?",
 "6","7","8","5","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "The letter exactly between M and S is:",
 "O","P","Q","N","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters lie between B and J in the alphabet?",
 "7","6","8","5","A"),

("Alphabet Reasoning","Gaps & Midpoint",
 "Which letter is midway between A and Y?",
 "L","M","N","K","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters are between K and R?",
 "5","6","7","4","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "The letter midway between C and I is:",
 "E","F","G","D","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters are between N and U?",
 "5","6","7","4","B"),

# -- Alphabet Reasoning - Series Pattern --
("Alphabet Reasoning","Series Pattern",
 "Find the next letter: A, C, E, G, ?",
 "H","I","J","K","B"),

("Alphabet Reasoning","Series Pattern",
 "Complete the series: B, D, F, H, ?",
 "I","J","K","L","B"),

("Alphabet Reasoning","Series Pattern",
 "Find the missing letter: Z, X, V, T, ?",
 "S","R","Q","P","B"),

("Alphabet Reasoning","Series Pattern",
 "Complete: A, D, G, J, ?",
 "L","M","N","K","B"),

("Alphabet Reasoning","Series Pattern",
 "Find the next: C, F, I, L, ?",
 "N","O","P","M","B"),

("Alphabet Reasoning","Series Pattern",
 "What comes next: A, B, D, G, K, ?",
 "N","O","P","Q","C"),

("Alphabet Reasoning","Series Pattern",
 "Complete: Z, W, T, Q, ?",
 "O","N","M","P","B"),

("Alphabet Reasoning","Series Pattern",
 "Next in the series: B, E, H, K, ?",
 "M","N","O","L","B"),

("Alphabet Reasoning","Series Pattern",
 "Find the next letter: M, N, P, S, ?",
 "U","V","W","T","C"),

("Alphabet Reasoning","Series Pattern",
 "What comes next: A, C, F, J, ?",
 "N","O","P","M","B"),

# -- Alphabet Reasoning - Word Formation --
("Alphabet Reasoning","Word Formation",
 "If the letters of 'BRAIN' are arranged alphabetically, which letter is in the middle?",
 "A","B","I","N","C"),

("Alphabet Reasoning","Word Formation",
 "How many meaningful English words can be formed using the 2nd, 3rd, 6th, and 8th letters of 'COMPUTER'?",
 "None","One","Two","Three","B"),

("Alphabet Reasoning","Word Formation",
 "If the letters of the word 'ORANGE' are rearranged alphabetically, which letter comes first?",
 "O","R","A","E","C"),

("Alphabet Reasoning","Word Formation",
 "In the word 'EDUCATION', how many letters are there between E and N as they appear?",
 "6","7","8","5","B"),

("Alphabet Reasoning","Word Formation",
 "If the word 'TROUBLE' is written in reverse, the 3rd letter from the right is:",
 "O","U","B","R","A"),

("Alphabet Reasoning","Word Formation",
 "In the word 'SHOULDER', if the consonants are arranged in alphabetical order and vowels in alphabetical order, what is the 4th letter?",
 "E","H","L","O","D"),

("Alphabet Reasoning","Word Formation",
 "If the first and last letters of 'SHARP' are interchanged, the new word formed is:",
 "PHARS","PSARH","PHARH","PHARP","D"),

("Alphabet Reasoning","Word Formation",
 "In 'QUESTION', how many pairs of letters have as many letters between them as in the alphabet?",
 "1","2","3","4","B"),

# -- Alphabet Reasoning - Number-Letter Coding --
("Alphabet Reasoning","Number-Letter Coding",
 "If A=1, B=2, ..., Z=26, what is the value of H + E + L + P?",
 "40","36","42","44","C"),

("Alphabet Reasoning","Number-Letter Coding",
 "If A=26, B=25, ..., Z=1, what is the value of C + A + R?",
 "56","53","50","47","A"),

("Alphabet Reasoning","Number-Letter Coding",
 "If each vowel is replaced by the next letter: A->B, E->F, I->J, O->P, U->V, what does 'ACE' become?",
 "BCF","BDF","ADF","BCE","A"),

("Alphabet Reasoning","Number-Letter Coding",
 "If A=2, B=4, C=6, ..., Z=52, then G + O + D = ?",
 "60","62","64","58","A"),

("Alphabet Reasoning","Number-Letter Coding",
 "If letters are coded as their squares (A=1, B=4, C=9, ...), what is the code for D?",
 "8","12","16","20","C"),

# -- Additional Ranking & Order --
("Ranking & Order","Position from Left/Right",
 "In a row, Hari is 20th from both ends. Total students in the row?",
 "39","40","41","38","A"),

("Ranking & Order","Position from Left/Right",
 "Ram is 11th from the left and 11th from the right. Total people?",
 "21","22","20","23","A"),

("Ranking & Order","Between Two People",
 "In a row of 18, A is at position 5 from left and B is at position 5 from right. How many are between them?",
 "8","7","9","6","A"),

("Ranking & Order","Class Rank",
 "In a test, Ravi's rank is 13th from both top and bottom. How many students took the test?",
 "25","26","24","27","A"),

("Ranking & Order","Class Rank",
 "Geeta's rank improves by 10 to become 5th. Her earlier rank was:",
 "10th","15th","14th","16th","B"),

("Ranking & Order","Linear Arrangement",
 "8 friends sit in a row. A is 3rd from the left. B is 2nd to the right of A. B's position from right end is:",
 "3rd","4th","2nd","5th","A"),

("Ranking & Order","Position from Left/Right",
 "In a row of 55 students, X is 22nd from the left. X's position from the right is:",
 "34th","33rd","35th","32nd","A"),

("Ranking & Order","Interchanging Positions",
 "In a row, A is 10th from left, B is 12th from right. After swap, A is 12th from right. Minimum students?",
 "21","22","20","23","A"),

# -- Additional Alphabet Reasoning --
("Alphabet Reasoning","Letter Position",
 "How many letters are in the English alphabet between K and T?",
 "8","7","9","6","A"),

("Alphabet Reasoning","Letter Position",
 "Which letter is 3rd to the right of the 14th letter from the left?",
 "P","Q","R","O","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "What letter is 15th from the right end of the English alphabet?",
 "K","L","M","J","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "Midpoint letter between F and L is:",
 "H","I","J","G","B"),

("Alphabet Reasoning","Series Pattern",
 "Find the next: D, H, L, P, ?",
 "R","S","T","U","C"),

("Alphabet Reasoning","Series Pattern",
 "Next letter: A, E, I, M, ?",
 "O","P","Q","R","C"),

("Alphabet Reasoning","Number-Letter Coding",
 "If A=1, B=2, ..., Z=26, the value of W + O + R + K = ?",
 "63","67","61","65","B"),

("Alphabet Reasoning","Word Formation",
 "How many vowels are in the word 'BEAUTIFUL'?",
 "3","4","5","6","C"),

("Alphabet Reasoning","Word Formation",
 "If the letters of 'MASTER' are arranged in alphabetical order, which is the last letter?",
 "T","S","R","E","A"),

("Alphabet Reasoning","Series Pattern",
 "Complete: Y, V, S, P, ?",
 "N","M","L","O","B"),

# -- More Ranking & Order --
("Ranking & Order","Class Rank",
 "In a class of 39, Rakesh's rank from the top is 14th. His rank from the bottom is:",
 "25th","26th","27th","24th","B"),

("Ranking & Order","Between Two People",
 "In a row of 42, A is 16th from left and B is 20th from right. How many between them?",
 "6","7","5","8","A"),

("Ranking & Order","Position from Left/Right",
 "Nita is 25th from the right in a row of 40. Her position from the left is:",
 "15th","16th","17th","14th","B"),

("Ranking & Order","Interchanging Positions",
 "In a row, X is 7th from left, Y is 9th from right. After swap, X is 9th from right. Total?",
 "15","16","14","17","A"),

("Ranking & Order","Linear Arrangement",
 "In a row of 10, if P is at position 4 from left, how many are to P's right?",
 "5","6","7","4","B"),

("Ranking & Order","Class Rank",
 "Sunita was 14th from bottom among 40 students. Her rank from top is:",
 "27th","26th","28th","25th","A"),

("Ranking & Order","Between Two People",
 "In a row of 32, M is 10th from left and N is 15th from right. Students between M and N?",
 "7","8","6","9","A"),

("Ranking & Order","Position from Left/Right",
 "In a row of 27 boys, Suresh is 13th from the left. His position from right is:",
 "14th","15th","16th","13th","B"),

("Ranking & Order","Class Rank",
 "Amit's rank in class is 3rd from top. There are 35 students. His rank from bottom is:",
 "32nd","33rd","34th","31st","B"),

("Ranking & Order","Linear Arrangement",
 "Six people A to F sit in a row. A is at one end, F is at the other end. B is next to A. C is next to F. D and E are in the middle. Who sits 3rd from the left?",
 "C","D","E","B","C"),

# -- More Alphabet Reasoning --
("Alphabet Reasoning","Letter Position",
 "Which letter comes 4th after the 12th letter of the alphabet?",
 "O","P","Q","N","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "In the reverse alphabet, which letter is at position 14?",
 "L","M","N","K","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "How many letters are there between R and X?",
 "4","5","6","3","B"),

("Alphabet Reasoning","Series Pattern",
 "Find the odd one out: A, E, I, O, S",
 "A","I","O","S","D"),

("Alphabet Reasoning","Word Formation",
 "If the first half of the English alphabet is reversed, which letter is at position 10?",
 "D","C","E","F","A"),

("Alphabet Reasoning","Number-Letter Coding",
 "If A=1, B=3, C=5, D=7, ..., what is the value of E?",
 "8","9","10","11","B"),

("Alphabet Reasoning","Gaps & Midpoint",
 "Which letter is exactly midway between J and P?",
 "L","M","N","K","B"),

("Alphabet Reasoning","Series Pattern",
 "What is the next letter in: P, N, L, J, ?",
 "I","H","G","F","B"),

("Alphabet Reasoning","Letter Position",
 "The 7th letter from the left plus the 7th letter from the right equals (A=1 scheme):",
 "26","27","28","25","B"),

("Alphabet Reasoning","Reverse Alphabet",
 "In the reverse alphabet series, which letter is 3rd?",
 "X","W","Y","V","A"),
]
