# Section 3 - Numerical Ability | Batch 4 (Q601-800)
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# === BASIC ARITHMETIC & WORD PROBLEMS - 80 questions ===
("Basic Arithmetic","Addition",
 "567 + 433 = ?",
 "900","990","1000","1100","C"),

("Basic Arithmetic","Addition",
 "1234 + 4766 = ?",
 "5900","5990","6000","6100","C"),

("Basic Arithmetic","Subtraction",
 "5000 - 2345 = ?",
 "2555","2655","2755","2855","B"),

("Basic Arithmetic","Subtraction",
 "10000 - 6789 = ?",
 "3111","3211","3311","3411","B"),

("Basic Arithmetic","Multiplication",
 "125 x 8 = ?",
 "900","950","1000","1050","C"),

("Basic Arithmetic","Multiplication",
 "36 x 25 = ?",
 "800","850","900","950","C"),

("Basic Arithmetic","Division",
 "7200 / 90 = ?",
 "70","75","80","85","C"),

("Basic Arithmetic","Division",
 "1440 / 12 = ?",
 "110","115","120","125","C"),

("Basic Arithmetic","Squares",
 "What is 15 squared?",
 "200","215","225","250","C"),

("Basic Arithmetic","Squares",
 "What is 25 squared?",
 "525","575","600","625","D"),

("Basic Arithmetic","Cubes",
 "What is 5 cubed?",
 "100","115","120","125","D"),

("Basic Arithmetic","Cubes",
 "What is 4 cubed?",
 "48","56","64","72","C"),

("Basic Arithmetic","LCM",
 "LCM of 12 and 18?",
 "24","30","36","48","C"),

("Basic Arithmetic","LCM",
 "LCM of 6, 8, and 12?",
 "12","18","24","36","C"),

("Basic Arithmetic","HCF",
 "HCF of 24 and 36?",
 "6","8","10","12","D"),

("Basic Arithmetic","HCF",
 "HCF of 18, 27, and 45?",
 "3","6","9","18","C"),

("Basic Arithmetic","Fractions",
 "1/3 + 1/6 = ?",
 "1/4","1/3","1/2","2/3","C"),

("Basic Arithmetic","Fractions",
 "3/4 - 1/2 = ?",
 "1/8","1/6","1/4","1/3","C"),

("Basic Arithmetic","Fractions",
 "2/5 x 5/6 = ?",
 "1/4","1/3","2/6","2/3","B"),

("Basic Arithmetic","Fractions",
 "3/4 / (1/2) = ?",
 "1/2","3/4","3/2","2","C"),

("Basic Arithmetic","Decimals",
 "0.25 + 0.75 = ?",
 "0.90","0.95","1.00","1.05","C"),

("Basic Arithmetic","Decimals",
 "3.6 x 2.5 = ?",
 "7.5","8.0","8.5","9.0","D"),

("Basic Arithmetic","Decimals",
 "7.2 / 0.9 = ?",
 "7","7.5","8","8.5","C"),

("Basic Arithmetic","Number Problems",
 "Sum of two numbers is 50, difference is 10. Larger number?",
 "25","28","30","35","C"),

("Basic Arithmetic","Number Problems",
 "Product of two numbers = 192. One is 12. Other?",
 "14","15","16","18","C"),

("Basic Arithmetic","Number Problems",
 "A number when doubled and added to 15 gives 45. The number?",
 "10","12","15","18","C"),

("Basic Arithmetic","Number Problems",
 "Three consecutive numbers sum to 33. Middle number?",
 "10","11","12","13","B"),

("Basic Arithmetic","Number Problems",
 "Two-thirds of a number is 40. The number?",
 "50","55","60","65","C"),

("Basic Arithmetic","Squares",
 "Square root of 144?",
 "10","11","12","13","C"),

("Basic Arithmetic","Squares",
 "Square root of 196?",
 "12","13","14","15","C"),

("Basic Arithmetic","LCM",
 "LCM of 15 and 20?",
 "40","50","60","80","C"),

("Basic Arithmetic","HCF",
 "HCF of 48 and 60?",
 "6","8","10","12","D"),

("Basic Arithmetic","Fractions",
 "Which is greater: 3/5 or 5/8?",
 "3/5","5/8","Both equal","Cannot tell","B"),

("Basic Arithmetic","Number Problems",
 "If 5x - 3 = 12, then x = ?",
 "2","3","4","5","B"),

("Basic Arithmetic","Number Problems",
 "A number increased by 25% becomes 100. The number?",
 "70","75","80","85","C"),

("Word Problems","Purchases",
 "20 pens cost Rs. 300. Cost of 8 pens?",
 "Rs. 100","Rs. 110","Rs. 120","Rs. 130","C"),

("Word Problems","Purchases",
 "12 notebooks cost Rs. 180. Cost of 20 notebooks?",
 "Rs. 280","Rs. 290","Rs. 300","Rs. 310","C"),

("Word Problems","Purchases",
 "A dozen eggs costs Rs. 60. Cost of 30 eggs?",
 "Rs. 120","Rs. 140","Rs. 150","Rs. 180","C"),

("Word Problems","Money",
 "A man has Rs. 500. He spends Rs. 150 on food, Rs. 100 on travel. Left?",
 "Rs. 200","Rs. 225","Rs. 250","Rs. 275","C"),

("Word Problems","Money",
 "Ravi earns Rs. 800/day. In 15 days he earns?",
 "Rs. 10000","Rs. 11000","Rs. 12000","Rs. 13000","C"),

("Word Problems","Distribution",
 "24 chocolates distributed equally among 8 children. Each gets?",
 "2","3","4","5","B"),

("Word Problems","Distribution",
 "Rs. 3000 divided equally among 12 workers. Each gets?",
 "Rs. 200","Rs. 225","Rs. 250","Rs. 275","C"),

("Word Problems","Mixtures",
 "Mix 3 litres at Rs. 40/L and 2 litres at Rs. 60/L. Cost per litre of mix?",
 "Rs. 44","Rs. 46","Rs. 48","Rs. 50","C"),

("Word Problems","Purchases",
 "5 kg apples at Rs. 120/kg. Total cost?",
 "Rs. 500","Rs. 550","Rs. 600","Rs. 650","C"),

("Word Problems","Money",
 "A worker earns Rs. 450/day and spends Rs. 300. Savings in 30 days?",
 "Rs. 3500","Rs. 4000","Rs. 4500","Rs. 5000","C"),

("Word Problems","Distribution",
 "A rope of 20 m cut into 5 equal pieces. Each piece?",
 "3 m","3.5 m","4 m","5 m","C"),

("Word Problems","Purchases",
 "A shirt costs Rs. 600 and a trouser Rs. 900. Total for 2 shirts and 1 trouser?",
 "Rs. 1800","Rs. 2000","Rs. 2100","Rs. 2200","C"),

("Word Problems","Money",
 "Total bill: Rs. 5000. Paid Rs. 3200. Balance due?",
 "Rs. 1600","Rs. 1700","Rs. 1800","Rs. 1900","C"),

("Word Problems","Distribution",
 "72 students in 6 equal groups. Students per group?",
 "10","11","12","14","C"),

("Word Problems","Mixtures",
 "A tank has 200 L of 30% salt solution. How much salt?",
 "50 L","55 L","60 L","65 L","C"),

("Word Problems","Purchases",
 "3 kg rice at Rs. 50/kg and 2 kg dal at Rs. 80/kg. Total?",
 "Rs. 290","Rs. 300","Rs. 310","Rs. 320","C"),

("Word Problems","Money",
 "Pocket money Rs. 1000/month. Save 30%. Savings?",
 "Rs. 250","Rs. 280","Rs. 290","Rs. 300","D"),

("Word Problems","Distribution",
 "132 books on 12 shelves equally. Books per shelf?",
 "10","11","12","13","B"),

("Word Problems","Purchases",
 "Bus fare Rs. 15 per trip. Cost for 20 trips?",
 "Rs. 250","Rs. 280","Rs. 300","Rs. 320","C"),

("Word Problems","Money",
 "A and B together have Rs. 600. A has Rs. 100 more than B. B has?",
 "Rs. 200","Rs. 225","Rs. 250","Rs. 300","C"),

("Word Problems","Distribution",
 "A teacher distributes 45 sweets among 5 students equally. Each gets?",
 "7","8","9","10","C"),

("Word Problems","Mixtures",
 "60 L milk, 40 L water. Ratio?",
 "2:3","3:2","3:4","4:3","B"),

("Word Problems","Purchases",
 "Petrol at Rs. 100/L. Cost for 15 litres?",
 "Rs. 1200","Rs. 1400","Rs. 1500","Rs. 1600","C"),

("Word Problems","Money",
 "EMI of Rs. 5000 for 12 months. Total paid?",
 "Rs. 50000","Rs. 55000","Rs. 60000","Rs. 65000","C"),

("Basic Arithmetic","Number Problems",
 "Half of 3/4 of 200 = ?",
 "50","60","75","100","C"),

("Basic Arithmetic","Number Problems",
 "What is 40% of 250?",
 "80","90","100","110","C"),

("Basic Arithmetic","Multiplication",
 "999 x 5 = ?",
 "4985","4990","4995","5000","C"),

("Basic Arithmetic","Division",
 "4800 / 60 = ?",
 "70","75","80","85","C"),

("Basic Arithmetic","LCM",
 "LCM of 4, 6, 10?",
 "30","40","50","60","D"),

("Basic Arithmetic","HCF",
 "HCF of 36, 54?",
 "9","12","16","18","D"),

("Basic Arithmetic","Decimals",
 "0.5 x 0.5 = ?",
 "0.10","0.20","0.25","0.50","C"),

("Basic Arithmetic","Fractions",
 "5/8 - 3/8 = ?",
 "1/8","1/4","3/8","1/2","B"),

("Word Problems","Purchases",
 "A pen costs Rs. 10, pencil Rs. 5. Cost of 6 pens and 4 pencils?",
 "Rs. 70","Rs. 75","Rs. 80","Rs. 85","C"),

("Word Problems","Money",
 "Salary Rs. 30000. Rent 25%. Amount for rent?",
 "Rs. 6000","Rs. 6500","Rs. 7000","Rs. 7500","D"),

("Word Problems","Distribution",
 "A cake cut into 8 equal pieces. 3 people eat 2 pieces each. Remaining?",
 "1","2","3","4","B"),

("Basic Arithmetic","Number Problems",
 "Sum of first 10 even numbers?",
 "100","110","120","130","B"),

("Basic Arithmetic","Number Problems",
 "Sum of first 10 odd numbers?",
 "90","95","100","110","C"),

("Basic Arithmetic","Squares",
 "What is 12 squared?",
 "124","134","144","154","C"),

("Basic Arithmetic","Cubes",
 "Cube of 3?",
 "9","18","27","36","C"),

("Word Problems","Money",
 "Buy 3 shirts at Rs. 700 each, get 10% off total. You pay?",
 "Rs. 1800","Rs. 1890","Rs. 1950","Rs. 2000","B"),

("Word Problems","Purchases",
 "1 kg sugar Rs. 45. Cost of 8 kg?",
 "Rs. 340","Rs. 350","Rs. 360","Rs. 370","C"),

("Word Problems","Distribution",
 "A garden 120 m perimeter, fence posts every 4 m. Posts needed?",
 "25","28","30","32","C"),

("Word Problems","Money",
 "Monthly income Rs. 40000. Saves 20%. Annual savings?",
 "Rs. 80000","Rs. 88000","Rs. 96000","Rs. 100000","C"),
]
