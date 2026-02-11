# Section 2 - Logical Reasoning  |  Batch 3: Q 401-600
# Topics: Coding & Decoding, Number Series
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# ===============================================
# CODING & DECODING - Letter Shift
# ===============================================
("Coding & Decoding","Letter Shift",
 "If CAT is coded as DBU, how is DOG coded?",
 "EPH","CPF","EOH","FOG","A"),

("Coding & Decoding","Letter Shift",
 "In a code, BALL is written as CBMM. How is PLAY written?",
 "QMBZ","QMBY","OMBX","OKBX","A"),

("Coding & Decoding","Letter Shift",
 "If FISH is coded as GITI, how is BEAR coded?",
 "CFBS","CFAS","CEAQ","CEBR","A"),

("Coding & Decoding","Letter Shift",
 "If ROAD is coded as URDG, how is SWAN coded?",
 "VZDQ","VXDQ","VZCQ","TWDQ","A"),

("Coding & Decoding","Letter Shift",
 "If each letter is replaced by the next letter, PARK becomes:",
 "QBSL","QBRL","OZKJ","OBSM","A"),

("Coding & Decoding","Letter Shift",
 "In a code, GONE is written as IQPG (each letter +2). How is COME written?",
 "EQOG","EQPG","EROG","EQOH","A"),

("Coding & Decoding","Letter Shift",
 "If MANGO is coded as OCPIQ (+2 each), how is APPLE coded?",
 "CRRNG","CRRNH","CRRMG","BQQMF","A"),

("Coding & Decoding","Letter Shift",
 "If PEN is coded as ODM (-1 shift), how is RED coded?",
 "QDC","SDC","QEC","SDE","A"),

("Coding & Decoding","Letter Shift",
 "In a code, TIGER is written as UJHFS (+1). How is MOUSE coded?",
 "NPVTF","NPVSF","NPUTF","MOURF","A"),

("Coding & Decoding","Letter Shift",
 "If OPEN is written as RSHQ (+3 each), how is SHUT?",
 "VKXW","VJXW","VKYW","UKXW","A"),

("Coding & Decoding","Letter Shift",
 "If HOUSE is coded as Krxvh (+3), how is TABLE coded?",
 "WDEOH","WDEOF","WCEOH","WDFOH","A"),

("Coding & Decoding","Letter Shift",
 "If GIRL is written as JLUQ (+3), then BODY is:",
 "ERGB","ERFB","ERGY","ERHB","A"),

("Coding & Decoding","Letter Shift",
 "In a code where A=Z, B=Y, C=X, ..., COLD is written as:",
 "XLOW","XLOY","XLOG","XLOW","A"),

("Coding & Decoding","Letter Shift",
 "If RAIN is coded as UCJQ (+3 skip), how is SNOW coded?",
 "VQRZ","VSRZ","VPRZ","UQRY","A"),

("Coding & Decoding","Letter Shift",
 "If each letter is replaced by two positions ahead, DESK becomes:",
 "FGUM","FGVM","FGTM","EGUM","A"),

# -- Coding & Decoding - Reverse / Mirror --
("Coding & Decoding","Reverse Coding",
 "If CLOCK is written as KCOLC (reverse), how is TIMER?",
 "REMIT","RMIIT","RMITE","RIMIT","A"),

("Coding & Decoding","Reverse Coding",
 "If WATER is coded as RETAW, how is FIRE coded?",
 "ERIF","EFIR","IRFE","REFI","A"),

("Coding & Decoding","Reverse Coding",
 "If TRAIN is written as NIART, then PLANE is:",
 "ENALP","ENAPL","ENPAL","NAELP","A"),

("Coding & Decoding","Reverse Coding",
 "In a code, GARDEN is NEDRAG. How is FLOWER?",
 "REWOLF","ROWELF","REWLOF","REFLWO","A"),

("Coding & Decoding","Reverse Coding",
 "If EARTH is coded as HTRAE, how is OCEAN?",
 "NAECO","NCEAO","NOCAE","NEACO","A"),

("Coding & Decoding","Reverse Coding",
 "If DELHI is coded as IHLED, how is MUMBAI coded?",
 "IABMUM","IMBMUA","IABMMU","IABUMM","A"),

# -- Coding & Decoding - Word Pattern --
("Coding & Decoding","Word Pattern",
 "If FACE is coded as 6135, then CODE is coded as:",
 "3145","3154","3155","3155","A"),

("Coding & Decoding","Word Pattern",
 "If in a code APPLE = 50, GRAPE = 50, then MANGO = ?",
 "50","57","55","60","B"),

("Coding & Decoding","Word Pattern",
 "If SUN is coded as 54 (19+21+14), what is the code for MOON?",
 "57","51","53","56","A"),

("Coding & Decoding","Word Pattern",
 "If PEN = 35 (16+5+14), then INK = ?",
 "30","33","27","29","B"),

("Coding & Decoding","Word Pattern",
 "If DOG = 26 (4+15+7), then CAT = ?",
 "24","22","25","23","A"),

("Coding & Decoding","Word Pattern",
 "If GREEN is coded as 49 (7+18+5+5+14), then BLUE = ?",
 "40","42","44","38","B"),

("Coding & Decoding","Word Pattern",
 "If RED = 27, then BED = ?",
 "11","9","12","10","A"),

("Coding & Decoding","Word Pattern",
 "If BOOK = 42 (2+15+15+11), then COOK = ?",
 "43","44","45","46","B"),

("Coding & Decoding","Word Pattern",
 "If in a code, BAD = 7, then GOOD = ?",
 "34","36","40","42","C"),

("Coding & Decoding","Word Pattern",
 "If TAP = 37 (20+1+16), then PAT = ?",
 "37","35","39","41","A"),

# -- Coding & Decoding - Number Substitution --
("Coding & Decoding","Number Substitution",
 "If 1=A, 2=B, ..., 26=Z, then 3-1-20 spells:",
 "CAR","CAT","CAN","CAP","B"),

("Coding & Decoding","Number Substitution",
 "If 2-1-12-12 is coded, the word is:",
 "BELL","BALL","BILL","BULL","B"),

("Coding & Decoding","Number Substitution",
 "Decode: 8-5-12-16. The word is:",
 "HELP","HEAP","HELD","HELM","A"),

("Coding & Decoding","Number Substitution",
 "If KING = 11-9-14-7, then QUEEN = ?",
 "17-21-5-5-14","16-21-5-5-14","17-20-5-5-14","18-21-5-5-14","A"),

("Coding & Decoding","Number Substitution",
 "Coded as 4-15-7, this word is:",
 "DOG","DIG","DAG","DOT","A"),

("Coding & Decoding","Number Substitution",
 "The number code 19-20-1-18 represents the word:",
 "STAR","STAY","STEP","STEM","A"),

("Coding & Decoding","Number Substitution",
 "If FISH = 6-9-19-8, then DISH = ?",
 "4-9-19-8","4-8-19-8","4-9-18-8","3-9-19-8","A"),

("Coding & Decoding","Number Substitution",
 "Decode: 13-1-14. The word is:",
 "MAN","MAP","MAR","MAT","A"),

# -- Coding & Decoding - Mixed / Complex --
("Coding & Decoding","Mixed Coding",
 "If DELHI is coded as 73541 and CALCUTTA as 82589662, how is TALL coded?",
 "6255","6244","6233","6211","A"),

("Coding & Decoding","Mixed Coding",
 "In a code, BREAD = ESFBE. What is the pattern?",
 "Each letter shifted forward by different amounts",
 "B+3=E, R+1=S, E+1=F, A+1=B, D+1=E",
 "Random pattern",
 "Reverse coding","B"),

("Coding & Decoding","Mixed Coding",
 "If PENCIL is coded as RGPEKN (each letter +2), how is ERASER?",
 "GTCUGT","GTCUHS","GRDUFR","GSCUFR","A"),

("Coding & Decoding","Mixed Coding",
 "If CHAIR is coded as DIBJS (+1 each), how is TABLE?",
 "UBCMF","UBCMG","UBCKF","UBDMF","A"),

("Coding & Decoding","Mixed Coding",
 "If GO = 32 (7+15), COME = 36 (3+15+13+5), then BACK = ?",
 "17","18","14","20","B"),

("Coding & Decoding","Mixed Coding",
 "If WHITE is coded as 65 (23+8+9+20+5), then BLACK = ?",
 "29","30","31","32","A"),

("Coding & Decoding","Mixed Coding",
 "In a code, if MAP is written as PDP (+3 each), then KEY is:",
 "NHB","NHC","NGB","MHB","A"),

("Coding & Decoding","Mixed Coding",
 "If ZEBRA is coded as AFCSB (+1 shift), then HORSE is:",
 "IPSIF","IPRTF","IPSIE","IQSIF","A"),

("Coding & Decoding","Mixed Coding",
 "If NUMBER is coded as OVNCFS (+1 each), then DIGITAL is:",
 "EJHJUBM","EJHJUAL","EJHJTBM","DIHJUBM","A"),

# ===============================================
# NUMBER SERIES - Missing Term
# ===============================================
("Number Series","Missing Term",
 "Find the next number: 2, 4, 8, 16, ?",
 "20","24","30","32","D"),

("Number Series","Missing Term",
 "Complete: 3, 6, 9, 12, ?",
 "14","15","16","18","B"),

("Number Series","Missing Term",
 "Next in series: 5, 10, 20, 40, ?",
 "50","60","80","100","C"),

("Number Series","Missing Term",
 "Find the missing term: 1, 4, 9, 16, 25, ?",
 "30","35","36","49","C"),

("Number Series","Missing Term",
 "What comes next: 1, 1, 2, 3, 5, 8, ?",
 "11","12","13","10","C"),

("Number Series","Missing Term",
 "Complete: 7, 14, 21, 28, ?",
 "32","34","35","42","C"),

("Number Series","Missing Term",
 "Next number: 100, 90, 80, 70, ?",
 "65","60","50","55","B"),

("Number Series","Missing Term",
 "Find the next: 2, 6, 18, 54, ?",
 "108","162","72","216","B"),

("Number Series","Missing Term",
 "Complete the series: 1, 3, 7, 15, 31, ?",
 "47","55","63","72","C"),

("Number Series","Missing Term",
 "Next in: 11, 22, 33, 44, ?",
 "54","55","45","66","B"),

("Number Series","Missing Term",
 "Find: 1, 8, 27, 64, ?",
 "100","125","150","216","B"),

("Number Series","Missing Term",
 "What comes next: 2, 3, 5, 7, 11, ?",
 "12","13","14","15","B"),

("Number Series","Missing Term",
 "Complete: 4, 9, 16, 25, ?",
 "30","36","49","64","B"),

("Number Series","Missing Term",
 "Next: 6, 11, 16, 21, ?",
 "25","26","31","24","B"),

("Number Series","Missing Term",
 "Find next: 3, 9, 27, 81, ?",
 "162","243","324","100","B"),

# -- Number Series - Wrong Term --
("Number Series","Wrong Term",
 "Which number is wrong: 2, 5, 10, 17, __(28)__, 37?",
 "5","10","28","37","C"),

("Number Series","Wrong Term",
 "Find the wrong number: 1, 2, 6, 24, 96, 720",
 "6","24","96","720","C"),

("Number Series","Wrong Term",
 "Spot the error: 3, 6, 12, 24, 47, 96",
 "6","12","47","96","C"),

("Number Series","Wrong Term",
 "Which is wrong: 2, 3, 5, 9, 16, 33?",
 "5","9","16","33","C"),

("Number Series","Wrong Term",
 "Find the wrong number: 1, 4, 9, 15, 25, 36",
 "4","15","25","36","B"),

("Number Series","Wrong Term",
 "Wrong number: 5, 10, 15, 22, 25, 30",
 "10","22","25","30","B"),

("Number Series","Wrong Term",
 "Which does not fit: 121, 144, 169, __(196)__, __(__(__(225)__)__)__,  __(__(__(__(__(__(__(255)__)__)__)__)__)__)__",
 "121","196","225","255","D"),

("Number Series","Wrong Term",
 "Find the wrong number: 8, 27, 64, 100, 216",
 "27","64","100","216","C"),

# -- Number Series - Arithmetic Pattern --
("Number Series","Arithmetic Pattern",
 "5, 12, 19, 26, 33, ? (common difference 7)",
 "39","40","41","38","B"),

("Number Series","Arithmetic Pattern",
 "10, 15, 20, 25, ? (difference 5)",
 "28","29","30","35","C"),

("Number Series","Arithmetic Pattern",
 "17, 22, 27, 32, ?",
 "36","37","38","35","B"),

("Number Series","Arithmetic Pattern",
 "100, 92, 84, 76, ?",
 "60","64","68","72","C"),

("Number Series","Arithmetic Pattern",
 "3, 8, 13, 18, 23, ?",
 "26","27","28","29","C"),

("Number Series","Arithmetic Pattern",
 "50, 44, 38, 32, ?",
 "28","26","24","20","B"),

("Number Series","Arithmetic Pattern",
 "1, 5, 9, 13, ?",
 "15","16","17","18","C"),

("Number Series","Arithmetic Pattern",
 "200, 190, 180, 170, ?",
 "165","160","155","150","B"),

# -- Number Series - Geometric Pattern --
("Number Series","Geometric Pattern",
 "2, 8, 32, 128, ? (x4)",
 "256","512","384","640","B"),

("Number Series","Geometric Pattern",
 "5, 15, 45, 135, ? (x3)",
 "270","405","505","810","B"),

("Number Series","Geometric Pattern",
 "1, 2, 4, 8, 16, ? (x2)",
 "20","24","30","32","D"),

("Number Series","Geometric Pattern",
 "7, 21, 63, 189, ? (x3)",
 "378","567","756","945","B"),

("Number Series","Geometric Pattern",
 "10, 50, 250, 1250, ? (x5)",
 "6250","5250","3750","2500","A"),

("Number Series","Geometric Pattern",
 "6, 12, 24, 48, ? (x2)",
 "60","72","96","84","C"),

("Number Series","Geometric Pattern",
 "4, 20, 100, 500, ? (x5)",
 "1000","1500","2000","2500","D"),

("Number Series","Geometric Pattern",
 "3, 12, 48, 192, ? (x4)",
 "384","576","768","960","C"),

# -- Number Series - Mixed Pattern --
("Number Series","Mixed Pattern",
 "2, 3, 5, 8, 12, 17, ? (differences increase by 1)",
 "20","21","22","23","D"),

("Number Series","Mixed Pattern",
 "1, 2, 4, 7, 11, 16, ?",
 "20","22","24","25","B"),

("Number Series","Mixed Pattern",
 "3, 5, 9, 15, 23, ?",
 "30","33","35","37","B"),

("Number Series","Mixed Pattern",
 "2, 5, 11, 23, 47, ?",
 "89","93","95","99","C"),

("Number Series","Mixed Pattern",
 "1, 4, 13, 40, ?",
 "121","120","110","100","A"),

("Number Series","Mixed Pattern",
 "4, 7, 12, 19, 28, ?",
 "37","38","39","40","C"),

("Number Series","Mixed Pattern",
 "2, 6, 12, 20, 30, ?",
 "40","42","44","38","B"),

("Number Series","Mixed Pattern",
 "1, 3, 6, 10, 15, 21, ? (triangular numbers)",
 "25","26","27","28","D"),

# -- Additional Coding & Decoding --
("Coding & Decoding","Letter Shift",
 "If HIT = IJU (+1), then MISS = ?",
 "NJTT","NKTT","NJTU","NJSS","A"),

("Coding & Decoding","Letter Shift",
 "If DARK = FCTN (+2 each), how is LIGHT coded?",
 "NKIJV","NKIJW","NKIJT","MKIJV","A"),

("Coding & Decoding","Reverse Coding",
 "If COMPUTER is coded as RETUPMOC, then PROGRAM is:",
 "MARGORP","MARGRPO","MARGOPR","MRAGORP","A"),

("Coding & Decoding","Word Pattern",
 "If MATH = 42 (13+1+20+8), then HOME = ?",
 "36","38","40","42","B"),

("Coding & Decoding","Mixed Coding",
 "If A=1, B=2, C=3, what is the code for the word FAD?",
 "10","11","12","9","A"),

# -- Additional Number Series --
("Number Series","Missing Term",
 "Next term: 0, 1, 1, 2, 3, 5, 8, 13, ?",
 "18","20","21","17","C"),

("Number Series","Missing Term",
 "Find next: 10, 20, 40, 80, ?",
 "100","120","160","200","C"),

("Number Series","Arithmetic Pattern",
 "15, 25, 35, 45, ?",
 "50","55","60","65","B"),

("Number Series","Geometric Pattern",
 "1, 3, 9, 27, ?",
 "54","72","81","108","C"),

("Number Series","Mixed Pattern",
 "1, 2, 6, 24, 120, ?",
 "240","600","720","840","C"),

("Number Series","Wrong Term",
 "Which is wrong: 2, 4, 8, 14, 32?",
 "4","8","14","32","C"),

("Number Series","Missing Term",
 "2, 5, 10, 17, 26, ?",
 "33","35","37","39","C"),

("Number Series","Arithmetic Pattern",
 "8, 11, 14, 17, ?",
 "19","20","21","22","B"),

("Number Series","Mixed Pattern",
 "1, 4, 9, 16, 25, 36, ?",
 "42","45","49","50","C"),

("Number Series","Geometric Pattern",
 "1000, 500, 250, 125, ?",
 "62.5","60","55","50","A"),

("Coding & Decoding","Letter Shift",
 "If FOOD is coded as HQQF (+2 each), how is GOOD?",
 "IQQF","IQQG","IQQD","HQQF","A"),

("Coding & Decoding","Number Substitution",
 "Decode: 18-1-9-14. The word is:",
 "RAIN","RAIL","RAMP","RAID","A"),

("Number Series","Missing Term",
 "What comes next: 256, 128, 64, 32, ?",
 "8","12","16","24","C"),

("Number Series","Wrong Term",
 "Find wrong number: 1, 2, 3, 5, 8, 13, 20",
 "3","5","13","20","D"),
]
