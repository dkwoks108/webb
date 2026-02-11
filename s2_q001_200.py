# Section 2 - Logical Reasoning  |  Batch 1: Q 1-200
# Topics: Direction Sense, Blood Relations
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# ===============================================
# DIRECTION SENSE - Basic Movement
# ===============================================
("Direction Sense","Basic Movement",
 "A man walks 5 km towards South, then turns left and walks 3 km. In which direction is he now facing?",
 "North","East","West","South","B"),

("Direction Sense","Basic Movement",
 "Ravi walks 10 m towards North, then turns right and walks 5 m. Which direction is he facing now?",
 "East","West","North","South","A"),

("Direction Sense","Basic Movement",
 "A person walks 4 km East, then turns left. Which direction is he facing now?",
 "South","North","East","West","B"),

("Direction Sense","Basic Movement",
 "Starting from point A, Meena walks 7 km West and then turns right. She is now facing:",
 "East","North","South","West","B"),

("Direction Sense","Basic Movement",
 "A boy walks 3 km North and then turns left. He is now facing:",
 "East","West","South","North","B"),

("Direction Sense","Basic Movement",
 "Sita walks 6 km towards South, then turns right. She is facing:",
 "East","North","West","South","C"),

("Direction Sense","Basic Movement",
 "If you face East and turn left, which direction will you face?",
 "West","South","North","East","C"),

("Direction Sense","Basic Movement",
 "Facing West, Raj turns right. He is now facing:",
 "East","North","South","West","B"),

("Direction Sense","Basic Movement",
 "A girl walks 2 km South and then 3 km East. Which direction is she from her starting point?",
 "South-East","North-East","South-West","North-West","A"),

("Direction Sense","Basic Movement",
 "If you are facing North and turn 90 degrees clockwise, which direction do you face?",
 "West","East","South","North","B"),

# -- Direction Sense - Turns & Rotation --
("Direction Sense","Turns & Rotation",
 "Facing North, a man turns 180 degrees. He is now facing:",
 "East","West","South","North","C"),

("Direction Sense","Turns & Rotation",
 "A person facing East turns 270 degrees clockwise. He now faces:",
 "North","South","East","West","A"),

("Direction Sense","Turns & Rotation",
 "Facing South, Anita turns 90 degrees anti-clockwise. She now faces:",
 "North","East","West","South","B"),

("Direction Sense","Turns & Rotation",
 "A man facing West turns 360 degrees. He is now facing:",
 "North","East","South","West","D"),

("Direction Sense","Turns & Rotation",
 "If you are facing South-East and turn 90 degrees clockwise, which direction do you face?",
 "South-West","North-East","North-West","East","A"),

("Direction Sense","Turns & Rotation",
 "A person facing North-East turns 180 degrees. He is now facing:",
 "South-West","North-West","South-East","East","A"),

("Direction Sense","Turns & Rotation",
 "Facing North, a man turns 45 degrees clockwise. He now faces:",
 "East","North-East","South-East","North-West","B"),

("Direction Sense","Turns & Rotation",
 "Facing East, a girl turns 90 degrees anti-clockwise twice. She is now facing:",
 "West","East","North","South","A"),

("Direction Sense","Turns & Rotation",
 "A person turns 90 degrees clockwise three times from North. He now faces:",
 "East","South","West","North","C"),

("Direction Sense","Turns & Rotation",
 "If you are facing West and turn 135 degrees clockwise, you face:",
 "North","North-West","North-East","South","B"),

# -- Direction Sense - Distance & Position --
("Direction Sense","Distance & Position",
 "A walks 5 km North, then 5 km East. How far is A from the starting point?",
 "10 km","5 sqrt(2) km","7 km","25 km","B"),

("Direction Sense","Distance & Position",
 "A man walks 3 km East, then 4 km North. His straight-line distance from start is:",
 "7 km","5 km","12 km","1 km","B"),

("Direction Sense","Distance & Position",
 "Raju walks 6 km South, then 8 km West. How far is he from the starting point?",
 "14 km","10 km","2 km","48 km","B"),

("Direction Sense","Distance & Position",
 "A girl walks 12 km North and then 5 km East. What is her distance from the start?",
 "17 km","7 km","13 km","60 km","C"),

("Direction Sense","Distance & Position",
 "A man walks 8 km East, 6 km North, then 8 km West. He is now how far from the start?",
 "6 km","8 km","10 km","22 km","A"),

("Direction Sense","Distance & Position",
 "Walking 5 km North, then 5 km East, then 5 km South. How far from start?",
 "5 km","10 km","15 km","0 km","A"),

("Direction Sense","Distance & Position",
 "A person walks 3 km West, 4 km South, 3 km East. How far from the start?",
 "10 km","4 km","6 km","3 km","B"),

("Direction Sense","Distance & Position",
 "Seema walks 10 km North, then 10 km East, then 10 km South. She is from start:",
 "10 km East","10 km North","10 km South","30 km East","A"),

("Direction Sense","Distance & Position",
 "P walks 7 km South, then turns left and walks 7 km. P is in which direction from start?",
 "South-East","South-West","North-East","North-West","A"),

("Direction Sense","Distance & Position",
 "A walks 4 km East, 3 km South, 4 km West. A is in which direction from start?",
 "South","North","East","West","A"),

# -- Direction Sense - Shadow-Based --
("Direction Sense","Shadow-Based",
 "In the morning, if a man faces East, his shadow falls towards:",
 "East","North","West","South","C"),

("Direction Sense","Shadow-Based",
 "At noon, the shadow of a vertical pole in the Northern hemisphere points towards:",
 "South","North","East","West","B"),

("Direction Sense","Shadow-Based",
 "In the evening, a person facing West will have their shadow falling towards:",
 "West","East","North","South","B"),

("Direction Sense","Shadow-Based",
 "If Ravi's shadow falls to his right in the morning, he is facing:",
 "North","South","East","West","A"),

("Direction Sense","Shadow-Based",
 "At 6 AM, a man is facing South. His shadow falls to which side?",
 "Left","Right","Front","Behind","B"),

("Direction Sense","Shadow-Based",
 "If a girl notices her shadow falling to her left in the evening, she is facing:",
 "South","North","East","West","B"),

("Direction Sense","Shadow-Based",
 "In the morning, a pole's shadow points West. By evening, the shadow points:",
 "East","West","North","South","A"),

("Direction Sense","Shadow-Based",
 "A man's shadow falls in front of him in the morning. He is facing:",
 "East","West","North","South","B"),

("Direction Sense","Shadow-Based",
 "If at sunrise your shadow is behind you, you are facing:",
 "West","North","East","South","C"),

("Direction Sense","Shadow-Based",
 "At sunset, if a man faces North, his shadow falls to his:",
 "Left","Right","Front","Behind","B"),

# -- Direction Sense - Complex Paths --
("Direction Sense","Complex Paths",
 "A man walks 2 km North, 3 km East, 2 km South, 3 km West. He is now at:",
 "North of start","East of start","His starting point","South of start","C"),

("Direction Sense","Complex Paths",
 "P walks 5 km South, turns left, walks 3 km, turns left, walks 5 km, turns left, walks 3 km. P is at:",
 "Starting point","5 km South","3 km East","5 km North","A"),

("Direction Sense","Complex Paths",
 "From home, Rani walks 4 km East, 3 km North, 4 km West, 3 km South. She is:",
 "At home","3 km North","4 km East","7 km away","A"),

("Direction Sense","Complex Paths",
 "A walks North 6 km, East 4 km, South 3 km, East 4 km. How far North of start?",
 "6 km","3 km","9 km","0 km","B"),

("Direction Sense","Complex Paths",
 "X walks 3 km North, turns right, walks 4 km, turns right, walks 7 km. Direction from start?",
 "South-East","South-West","North-East","North-West","A"),

("Direction Sense","Complex Paths",
 "B walks 10 km East, 5 km South, 10 km West, 5 km North. B is at:",
 "10 km East","Starting point","5 km South","15 km East","B"),

("Direction Sense","Complex Paths",
 "A goes 6 km East, 3 km South, 2 km East, 3 km North. How far East from start?",
 "6 km","8 km","2 km","11 km","B"),

("Direction Sense","Complex Paths",
 "M walks 4 km West, turns left, walks 4 km, then turns right and walks 4 km. M is facing:",
 "West","East","South","North","A"),

("Direction Sense","Complex Paths",
 "Starting from office, Ram walks 8 km North, turns right, walks 6 km, turns right, walks 8 km. He is from office:",
 "6 km East","6 km West","8 km North","14 km away","A"),

("Direction Sense","Complex Paths",
 "Anu starts from X, walks 5 km South, 12 km East. Her shortest distance from X is:",
 "13 km","17 km","7 km","60 km","A"),

# -- Direction Sense - Relative Position --
("Direction Sense","Relative Position",
 "A is to the North of B. B is to the West of C. A is in which direction of C?",
 "North-East","North-West","South-East","South-West","B"),

("Direction Sense","Relative Position",
 "P is East of Q. R is South of P. R is in which direction of Q?",
 "South-East","North-East","South-West","North-West","A"),

("Direction Sense","Relative Position",
 "Town A is North of Town B. Town C is East of Town A. Town C is in which direction of B?",
 "North-East","North-West","South-East","South-West","A"),

("Direction Sense","Relative Position",
 "X is to the West of Y. Z is to the South of X. Z is in which direction of Y?",
 "North-West","South-West","South-East","North-East","B"),

("Direction Sense","Relative Position",
 "School is South of Hospital. Park is East of School. Park is in which direction of Hospital?",
 "South-East","North-East","South-West","North-West","A"),

("Direction Sense","Relative Position",
 "M is North-East of N. O is due South of M. If MO = MN, O is in which direction of N?",
 "East","South-East","South","North","A"),

("Direction Sense","Relative Position",
 "P is 5 km East of Q. R is 5 km North of P. R is from Q in direction:",
 "North-East","South-East","North-West","South-West","A"),

("Direction Sense","Relative Position",
 "House is West of School. Temple is South of House. Temple is in which direction of School?",
 "South-West","North-West","South-East","North-East","A"),

("Direction Sense","Relative Position",
 "D is North-West of E. F is East of D and North of E. So F is approximately ______ of E.",
 "North","North-East","East","North-West","A"),

("Direction Sense","Relative Position",
 "Village A is due East of Village B, and Village C is due South of Village A. B to C direction is:",
 "South-East","North-East","South-West","Due South","A"),

# ===============================================
# BLOOD RELATIONS - Basic Relations
# ===============================================
("Blood Relations","Basic Relations",
 "Pointing to a man, a woman says, 'He is my father's son.' How is the man related to the woman?",
 "Father","Uncle","Brother","Cousin","C"),

("Blood Relations","Basic Relations",
 "A says, 'B is my mother's husband.' How is B related to A?",
 "Uncle","Father","Brother","Grandfather","B"),

("Blood Relations","Basic Relations",
 "Pointing to a lady, Ram says, 'She is the daughter of my grandfather's only son.' How is the lady related to Ram?",
 "Sister","Mother","Aunt","Cousin","A"),

("Blood Relations","Basic Relations",
 "If X is the son of Y's mother's brother, how is X related to Y?",
 "Brother","Cousin","Uncle","Nephew","B"),

("Blood Relations","Basic Relations",
 "Anu says, 'Ravi is the brother of the son of my mother's sister.' How is Ravi related to Anu?",
 "Son","Cousin","Brother","Uncle","B"),

("Blood Relations","Basic Relations",
 "A's father is B's son. How is A related to B?",
 "Son","Grandson / Granddaughter","Father","Brother","B"),

("Blood Relations","Basic Relations",
 "Pointing to a boy, Seema says, 'He is the son of my husband's father.' How is the boy related to Seema?",
 "Son","Nephew","Brother-in-law","Husband","C"),

("Blood Relations","Basic Relations",
 "M is the daughter of K. K is the daughter of N. How is M related to N?",
 "Daughter","Granddaughter","Sister","Mother","B"),

("Blood Relations","Basic Relations",
 "'He is my mother's only son.' The speaker is referring to:",
 "His uncle","His brother","Himself","His cousin","C"),

("Blood Relations","Basic Relations",
 "Pointing to a woman, a man says, 'Her mother is the only daughter of my mother.' Who is the woman?",
 "Sister","Daughter","Mother","Cousin","B"),

# -- Blood Relations - Father / Mother / Parents --
("Blood Relations","Father / Mother",
 "A says, 'C is the father of my mother.' How is C related to A?",
 "Father","Grandfather (maternal)","Uncle","Brother","B"),

("Blood Relations","Father / Mother",
 "Pointing to a man, Rani says, 'His mother is my mother-in-law.' How is the man related to Rani?",
 "Father-in-law","Brother-in-law","Husband","Son","C"),

("Blood Relations","Father / Mother",
 "X's mother is Y's daughter. How is X related to Y?",
 "Son","Grandson / Granddaughter","Daughter","Nephew","B"),

("Blood Relations","Father / Mother",
 "A's mother is B's mother's daughter. How is A related to B?",
 "Nephew / Niece","Son / Daughter","Cousin","Brother / Sister","A"),

("Blood Relations","Father / Mother",
 "P's father is Q's mother's husband and Q is not P's sister. How is Q related to P?",
 "Brother","Cousin","Uncle","Father","A"),

("Blood Relations","Father / Mother",
 "If D is the mother of E, and E is the sister of F, how is D related to F?",
 "Aunt","Mother","Sister","Grandmother","B"),

("Blood Relations","Father / Mother",
 "Raj says, 'My mother's father is your father.' How is Raj related to the listener?",
 "Grandson","Nephew","Son","Brother","B"),

("Blood Relations","Father / Mother",
 "Kiran's mother is Priya. Priya's mother is Lata. How is Kiran related to Lata?",
 "Daughter","Granddaughter","Sister","Mother","B"),

("Blood Relations","Father / Mother",
 "R says, 'P is the husband of the daughter of the mother of my mother.' How is P related to R?",
 "Father","Uncle","Brother","Grandfather","B"),

("Blood Relations","Father / Mother",
 "Arun's mother says to Geeta, 'Your son is my son's cousin.' How is Geeta related to Arun's mother?",
 "Sister","Sister-in-law","Daughter","Mother","B"),

# -- Blood Relations - Siblings --
("Blood Relations","Siblings",
 "A and B are sisters. C is A's brother. D is C's father. How is B related to D?",
 "Mother","Daughter","Sister","Wife","B"),

("Blood Relations","Siblings",
 "Anu is Ravi's sister. Mohan is Ravi's father. How is Anu related to Mohan?",
 "Mother","Daughter","Wife","Sister","B"),

("Blood Relations","Siblings",
 "If P is the brother of Q, Q is the sister of R, and R is the father of S, how is P related to S?",
 "Father","Uncle","Brother","Grandfather","B"),

("Blood Relations","Siblings",
 "X and Y are children of Z. X is not the brother of Y. How is X related to Y?",
 "Brother","Sister","Cousin","Father","B"),

("Blood Relations","Siblings",
 "Deepa and Mala are sisters. Ravi is Deepa's son. How is Ravi related to Mala?",
 "Son","Brother","Nephew","Cousin","C"),

("Blood Relations","Siblings",
 "Two sisters have one brother each. How many siblings are there in total?",
 "4","6","3","5","C"),

("Blood Relations","Siblings",
 "A is B's brother. C is B's sister. D is C's brother. How is A related to D?",
 "Brother","They are the same person","Cousin","Uncle","B"),

("Blood Relations","Siblings",
 "If Karan is the only brother of Neha, and Neha's mother has only two children, how is Karan related to Neha?",
 "Cousin","Brother","Uncle","Father","B"),

("Blood Relations","Siblings",
 "P has two children Q and R. Q's son is S. How is S related to R?",
 "Son","Brother","Nephew","Cousin","C"),

("Blood Relations","Siblings",
 "Lakshmi is Rani's sister. Rani is Shyam's wife. How is Lakshmi related to Shyam?",
 "Sister","Wife","Sister-in-law","Mother-in-law","C"),

# -- Blood Relations - In-Laws --
("Blood Relations","In-Laws",
 "A is married to B. C is A's mother. How is C related to B?",
 "Mother","Mother-in-law","Aunt","Sister","B"),

("Blood Relations","In-Laws",
 "Ravi's wife's father is Mohan. How is Mohan related to Ravi?",
 "Father","Father-in-law","Uncle","Brother","B"),

("Blood Relations","In-Laws",
 "Sita is the daughter-in-law of Geeta. Ramu is Geeta's son. How is Sita related to Ramu?",
 "Sister","Daughter","Wife","Mother","C"),

("Blood Relations","In-Laws",
 "P is the brother-in-law of Q. R is Q's husband. How is P related to R?",
 "Brother","Cousin","Father","Uncle","A"),

("Blood Relations","In-Laws",
 "X's sister-in-law is Y. Y is married to Z. How is Z related to X?",
 "Brother or Sister","Father","Uncle","Cousin","A"),

("Blood Relations","In-Laws",
 "Meera's husband's sister is Kavita. How is Kavita related to Meera?",
 "Sister","Sister-in-law","Cousin","Aunt","B"),

("Blood Relations","In-Laws",
 "A says to B, 'Your son is my son-in-law.' How is B's son's wife related to A?",
 "Niece","Daughter","Daughter-in-law","Granddaughter","B"),

("Blood Relations","In-Laws",
 "Rani is the mother-in-law of Preeti, who is the wife of Suresh. How is Rani related to Suresh?",
 "Mother","Aunt","Mother-in-law","Grandmother","A"),

("Blood Relations","In-Laws",
 "G is the father-in-law of H. H is married to K. K is G's:",
 "Son","Daughter","Brother","Nephew","B"),

("Blood Relations","In-Laws",
 "My wife's brother's wife is my:",
 "Sister-in-law","Cousin","Aunt","Niece","A"),

# -- Blood Relations - Generations --
("Blood Relations","Generations",
 "My father's father is your father. How am I related to you?",
 "Son","Grandson","Nephew","Brother","C"),

("Blood Relations","Generations",
 "A is B's grandson. C is A's mother. How is C related to B?",
 "Daughter","Daughter-in-law","Wife","Mother","B"),

("Blood Relations","Generations",
 "Ravi says, 'I am the only grandson of my grandfather who has only one son.' How many brothers does Ravi have?",
 "One","Two","None","Three","C"),

("Blood Relations","Generations",
 "P is the great-grandfather of Q. R is Q's father. How is R related to P?",
 "Son","Grandson","Brother","Nephew","B"),

("Blood Relations","Generations",
 "My grandmother's only daughter is my:",
 "Sister","Aunt","Mother","Cousin","C"),

("Blood Relations","Generations",
 "A's grandfather's son's daughter is:",
 "A's sister or cousin","A's aunt","A's niece","A's grandmother","A"),

("Blood Relations","Generations",
 "C is A's grandmother. B is A's mother. How is C related to B?",
 "Mother","Mother-in-law","Grandmother","Sister","A"),

("Blood Relations","Generations",
 "X is the nephew of Y. Y's father is Z. How is Z related to X?",
 "Father","Grandfather","Uncle","Brother","B"),

("Blood Relations","Generations",
 "My maternal grandfather's wife is my:",
 "Grandmother","Mother","Aunt","Sister","A"),

("Blood Relations","Generations",
 "D is the great-grandson of E. F is D's father. G is F's father. How is G related to E?",
 "Son","Grandson","Brother","Nephew","A"),

# -- Blood Relations - Complex / Puzzle --
("Blood Relations","Complex Puzzle",
 "A + B means A is the father of B. A - B means A is the wife of B. If P + Q - R, how is R related to P?",
 "Son","Son-in-law","Brother","Father","B"),

("Blood Relations","Complex Puzzle",
 "In a family of 6, A is the father of B. C is the mother of D. B and D are married. E is A's daughter. How is E related to D?",
 "Mother-in-law","Sister-in-law","Daughter","Cousin","B"),

("Blood Relations","Complex Puzzle",
 "If 'A $ B' means A is the mother of B, and 'A # B' means A is the brother of B, then in X $ Y # Z, how is Z related to X?",
 "Son","Daughter","Grandson","Son or Daughter","D"),

("Blood Relations","Complex Puzzle",
 "Six people P, Q, R, S, T, U are in a family. P is the father of Q. R is the mother of S. Q and R are married. How is S related to P?",
 "Son","Grandson / Granddaughter","Nephew","Daughter","B"),

("Blood Relations","Complex Puzzle",
 "A is married to B. C is A's sister. D is B's brother. How are C and D related?",
 "Brother and Sister","Husband and Wife","No blood relation","Cousins","C"),

("Blood Relations","Complex Puzzle",
 "If X @ Y means X is the daughter of Y, X & Y means X is the husband of Y, then A @ B & C means:",
 "A is the daughter of B, who is the husband of C",
 "A is the mother of B",
 "A is married to B",
 "A is the sister of C","A"),

("Blood Relations","Complex Puzzle",
 "In a family, there are 2 married couples, 1 grandfather, 1 grandmother, 2 fathers, 2 mothers, 1 son, 1 daughter, and 2 grandchildren. What is the minimum number of members?",
 "8","6","5","4","B"),

("Blood Relations","Complex Puzzle",
 "A says to B, 'The girl playing there is the younger of the two daughters of my father's wife.' How is the girl related to B if B is A's brother?",
 "Cousin","Sister","Daughter","Niece","B"),

("Blood Relations","Complex Puzzle",
 "If 'D is the mother of S' and 'S is the son of P' and 'P is the father of S,' then D and P are:",
 "Siblings","Married couple","Cousins","Parent and child","B"),

("Blood Relations","Complex Puzzle",
 "A family has a husband, wife, two sons, and one daughter. One son is married with one child. How many total members?",
 "7","6","8","5","A"),

# -- Blood Relations - Coded / Symbol-Based --
("Blood Relations","Coded Relations",
 "If A + B means A is the father of B, A - B means A is the mother of B, A x B means A is the brother of B, then what does P + Q x R mean?",
 "P is the father of Q, who is the brother of R",
 "P is the brother of Q",
 "P is the mother of R",
 "P is the father of R","A"),

("Blood Relations","Coded Relations",
 "If 'M > N' means M is the mother of N, and 'M < N' means M is the daughter of N, then in A > B < C, how is C related to A?",
 "Mother","Grandmother","Daughter","Granddaughter","A"),

("Blood Relations","Coded Relations",
 "If '#' means 'father of' and '$' means 'mother of', what does A # B $ C mean?",
 "A is grandfather of C","A is father of B who is mother of C","A is uncle of C","Both A and B","B"),

("Blood Relations","Coded Relations",
 "If A * B = A is the wife of B, and A + B = A is the son of B, then P * Q + R means:",
 "P is wife of Q, who is son of R",
 "P is son of Q",
 "P is mother of R",
 "P is the daughter of R","A"),

("Blood Relations","Coded Relations",
 "If '->' means son of, and '<-' means wife of, then A -> B <- C means:",
 "A is son of B, B is wife of C","A is son of B, C is husband of B","A is father of C","A is brother of C","A"),

# -- Additional Direction Sense --
("Direction Sense","Basic Movement",
 "A man starts walking towards North. After walking 10 m, he turns left. He is now facing:",
 "South","East","West","North","C"),

("Direction Sense","Basic Movement",
 "Starting from her house, Lata walks North for 5 km, then turns right and walks 3 km. She is now facing:",
 "North","East","South","West","B"),

("Direction Sense","Basic Movement",
 "Ramesh wants to go to the hospital which is due North. He starts walking East for 5 km and turns left. He is now walking towards:",
 "North","South","East","West","A"),

("Direction Sense","Turns & Rotation",
 "A person faces South-West and turns 90 degrees anti-clockwise. He now faces:",
 "South-East","North-West","North-East","West","A"),

("Direction Sense","Turns & Rotation",
 "From North, turning 45 degrees clockwise four times makes you face:",
 "South","East","West","North","A"),

("Direction Sense","Distance & Position",
 "A man walks 15 m East and then 20 m North. His shortest distance from start is:",
 "35 m","25 m","5 m","175 m","B"),

("Direction Sense","Distance & Position",
 "A man walks 9 km East, then 12 km North. How far is he from start?",
 "21 km","15 km","3 km","108 km","B"),

("Direction Sense","Distance & Position",
 "Going 7 km North and then 24 km East, the distance from start is:",
 "31 km","25 km","17 km","168 km","B"),

("Direction Sense","Complex Paths",
 "P walks 4 km North, 2 km East, 4 km South, 6 km West. P is from starting point:",
 "4 km West","2 km East","6 km West","4 km North","A"),

("Direction Sense","Complex Paths",
 "A boy walks 1 km East, 1 km South, 1 km East, 1 km South, 1 km West, 1 km North. How far East from start?",
 "3 km","1 km","2 km","0 km","B"),

# -- Additional Blood Relations --
("Blood Relations","Basic Relations",
 "Pointing to a man in a photograph, Asha says, 'His mother is the only daughter of my mother.' How is the man related to Asha?",
 "Nephew","Son","Brother","Uncle","B"),

("Blood Relations","Basic Relations",
 "A woman says, 'This girl is the wife of the grandson of my mother.' Who is the woman to the girl?",
 "Mother-in-law","Grandmother","Aunt","Sister","A"),

("Blood Relations","Basic Relations",
 "If Neha is the daughter of Ramesh's brother, how is Neha's father related to Ramesh?",
 "Father","Uncle","Brother","Cousin","C"),

("Blood Relations","Father / Mother",
 "Anand says, 'The mother of my son's wife is my wife's mother.' What is the relationship between Anand and his son's wife?",
 "Father-in-law and daughter-in-law","Uncle and niece","Brother and sister","Grandfather and granddaughter","A"),

("Blood Relations","Father / Mother",
 "My mother's husband is my:",
 "Uncle","Father","Brother","Grandfather","B"),

("Blood Relations","Siblings",
 "Rajan has a sister. His sister's father's mother is Rajan's:",
 "Mother","Sister","Grandmother","Aunt","C"),

("Blood Relations","Siblings",
 "Tom and Jerry are brothers. Tim is Tom's father. What is Jerry to Tim?",
 "Nephew","Son","Brother","Grandson","B"),

("Blood Relations","In-Laws",
 "My brother's wife's sister is the daughter of my:",
 "Mother-in-law","Father-in-law","Father","There is no such relation","B"),

("Blood Relations","Generations",
 "My daughter's son's sister is my:",
 "Granddaughter","Daughter","Niece","Cousin","A"),

("Blood Relations","Complex Puzzle",
 "A's mother is B's father's wife. How is A related to B?",
 "Cousin","Brother/Sister","Uncle","Nephew","B"),

# -- More Direction Sense for depth --
("Direction Sense","Shadow-Based",
 "At 4 PM, a person facing North has his shadow to his:",
 "Left","Right","Front","Behind","B"),

("Direction Sense","Shadow-Based",
 "Early morning, a girl notices her shadow is to her right. She is facing:",
 "North","South","East","West","A"),

("Direction Sense","Relative Position",
 "Bank is to the East of Hospital. Temple is to the South of Bank. Temple is in which direction of Hospital?",
 "North-East","South-East","North-West","South-West","B"),

("Direction Sense","Relative Position",
 "Rani's house is 5 km North and 5 km West of Sita's house. Rani's house is in which direction of Sita's?",
 "North-East","South-West","North-West","South-East","C"),

("Direction Sense","Distance & Position",
 "Two friends start from the same point. A walks 4 km East and B walks 3 km North. How far are they from each other?",
 "7 km","5 km","1 km","12 km","B"),

("Direction Sense","Basic Movement",
 "A car moves 20 km towards North, turns left, and moves 15 km. It is now facing:",
 "East","West","South","North","B"),

("Direction Sense","Turns & Rotation",
 "Facing South, turning 90 degrees clockwise gives:",
 "North","East","West","South","C"),

("Direction Sense","Complex Paths",
 "Ram walks 3 km North, 4 km East, 7 km South, 4 km West. He is how far from start?",
 "4 km South","3 km North","7 km South","18 km","A"),

("Blood Relations","Coded Relations",
 "If '+' = father, 'x' = brother, '-' = mother, then P + Q x R - S means:",
 "P is father of Q; Q is brother of R; R is mother of S",
 "P is brother of Q",
 "S is the father",
 "R is the grandfather","A"),

("Blood Relations","Coded Relations",
 "If M @ N means M is the sister of N, M # N means M is the mother of N, then X @ Y # Z means:",
 "X is sister of Y, Y is mother of Z","X is mother of Y","Z is sister of X","X is aunt of Z","A"),

("Blood Relations","Basic Relations",
 "Pointing to Deepak, Neelam says, 'I am the only daughter of his mother.' How is Neelam related to Deepak?",
 "Mother","Niece","Sister","Daughter","C"),

("Blood Relations","Generations",
 "My father's mother's daughter is my:",
 "Sister","Mother","Aunt","Grandmother","C"),

("Blood Relations","In-Laws",
 "My husband's mother is my:",
 "Mother","Mother-in-law","Aunt","Grandmother","B"),

("Blood Relations","Siblings",
 "My sister's mother is my:",
 "Aunt","Sister","Mother","Grandmother","C"),

("Direction Sense","Distance & Position",
 "A man walks 40 m East and 30 m North. What is the shortest distance from start?",
 "70 m","50 m","10 m","35 m","B"),

("Blood Relations","Complex Puzzle",
 "A family has a father, mother, three sons, and two daughters. Each son is married. How many females are in the family?",
 "5","4","6","7","A"),

("Blood Relations","Basic Relations",
 "If Priya says, 'He is the only son of my mother's mother,' she is talking about her:",
 "Father","Brother","Maternal uncle","Cousin","C"),

("Direction Sense","Basic Movement",
 "I face North and take a left turn, then immediately take a right turn. I am now facing:",
 "East","West","South","North","D"),

("Direction Sense","Turns & Rotation",
 "If you spin 540 degrees clockwise from facing East, you now face:",
 "East","West","North","South","B"),

("Direction Sense","Shadow-Based",
 "If the shadow of a signpost falls towards the East, the time is likely:",
 "Morning","Afternoon","Evening","Midnight","C"),

("Direction Sense","Complex Paths",
 "A woman drives 5 km South, 3 km East, 5 km North. She is from the start:",
 "5 km East","3 km East","8 km away","At start","B"),

("Blood Relations","In-Laws",
 "Pointing to a photo, a lady says, 'She is my husband's sister's daughter.' The girl in the photo is the lady's:",
 "Sister","Daughter","Niece","Cousin","C"),

("Blood Relations","Coded Relations",
 "If A % B means A is the husband of B, A & B means A is the son of B, then X % Y & Z means:",
 "X is husband of Y, Y is son of Z",
 "X is son of Z",
 "Y is husband of X",
 "Z is the wife","A"),
]
