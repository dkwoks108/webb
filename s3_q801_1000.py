# Section 3 - Numerical Ability | Batch 5 (Q801-1000)
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# === MORE SIMPLE INTEREST - 20 ===
("Simple Interest","SI Formula",
 "SI on Rs. 6500 at 8% for 3 years:",
 "Rs. 1460","Rs. 1500","Rs. 1560","Rs. 1600","C"),

("Simple Interest","Amount",
 "Rs. 3500 at 6% SI for 4 years. Amount?",
 "Rs. 4240","Rs. 4300","Rs. 4340","Rs. 4400","C"),

("Simple Interest","Rate",
 "Rs. 4000 becomes Rs. 5200 in 3 years. Rate?",
 "8%","9%","10%","12%","C"),

("Simple Interest","Time",
 "In how many years does Rs. 3000 earn Rs. 900 at 10%?",
 "2","3","4","5","B"),

("Simple Interest","Principal",
 "Interest = Rs. 540 at 9% for 2 years. Principal?",
 "Rs. 2800","Rs. 3000","Rs. 3200","Rs. 3500","B"),

("Simple Interest","Amount",
 "Rs. 7500 at 4% SI for 5 years. Amount?",
 "Rs. 8800","Rs. 9000","Rs. 9200","Rs. 9500","B"),

("Simple Interest","SI Formula",
 "SI on Rs. 2400 at 7.5% for 2 years:",
 "Rs. 340","Rs. 350","Rs. 360","Rs. 380","C"),

("Simple Interest","Rate",
 "Rs. 5000 earns Rs. 750 in 2.5 years. Rate?",
 "5%","6%","7%","8%","B"),

("Simple Interest","Time",
 "Rs. 8000 at 5% gives Rs. 2000. Time?",
 "3 years","4 years","5 years","6 years","C"),

("Simple Interest","Principal",
 "Amount = Rs. 6600, SI = Rs. 600, Time = 2 years. Rate?",
 "4%","5%","6%","7%","B"),

("Simple Interest","Amount",
 "Rs. 9000 at 11% for 2 years. SI?",
 "Rs. 1800","Rs. 1900","Rs. 1980","Rs. 2000","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 1800 at 10% for 18 months:",
 "Rs. 240","Rs. 260","Rs. 270","Rs. 280","C"),

("Simple Interest","Rate",
 "A sum doubles in 5 years at SI. Rate?",
 "15%","18%","20%","25%","C"),

("Simple Interest","Time",
 "Rs. 2000 at 8% SI to earn Rs. 480. Time?",
 "2 years","3 years","4 years","5 years","B"),

("Simple Interest","Principal",
 "SI = Rs. 1200 at 10% for 4 years. Principal?",
 "Rs. 2500","Rs. 2800","Rs. 3000","Rs. 3200","C"),

("Simple Interest","Amount",
 "Rs. 4500 at 8% for 2.5 years. Amount?",
 "Rs. 5300","Rs. 5350","Rs. 5400","Rs. 5500","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 20000 at 6% for 9 months:",
 "Rs. 800","Rs. 850","Rs. 900","Rs. 950","C"),

("Simple Interest","Rate",
 "Rs. 3600 gives Rs. 432 SI in 2 years. Rate?",
 "5%","6%","7%","8%","B"),

("Simple Interest","Time",
 "A sum at 12% SI earns half of itself. Time?",
 "3 years","4 years","4.17 years","5 years","C"),

("Simple Interest","Amount",
 "Rs. 15000 at 10% for 3 years. Total amount?",
 "Rs. 18000","Rs. 19000","Rs. 19500","Rs. 20000","C"),

# === MORE PROFIT & LOSS - 20 ===
("Profit & Loss","Profit %",
 "CP Rs. 300, SP Rs. 360. Profit %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Loss %",
 "CP Rs. 450, SP Rs. 360. Loss %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","SP from Profit",
 "CP Rs. 750, gain 12%. SP?",
 "Rs. 830","Rs. 840","Rs. 850","Rs. 860","B"),

("Profit & Loss","CP from SP",
 "SP Rs. 936, profit 17%. CP?",
 "Rs. 780","Rs. 790","Rs. 800","Rs. 810","C"),

("Profit & Loss","Discount",
 "MP Rs. 600, discount 5%. SP?",
 "Rs. 550","Rs. 555","Rs. 560","Rs. 570","D"),

("Profit & Loss","Profit %",
 "Buy at Rs. 40/unit, sell at Rs. 52/unit. Profit %?",
 "25%","28%","30%","35%","C"),

("Profit & Loss","Loss %",
 "A laptop bought for Rs. 40000, sold for Rs. 34000. Loss %?",
 "12%","13%","15%","18%","C"),

("Profit & Loss","SP from Loss",
 "CP Rs. 1200, loss 8%. SP?",
 "Rs. 1090","Rs. 1096","Rs. 1100","Rs. 1104","D"),

("Profit & Loss","Discount",
 "MP Rs. 900, discount 20%, then 10%. Final SP?",
 "Rs. 620","Rs. 640","Rs. 648","Rs. 660","C"),

("Profit & Loss","CP from SP",
 "SP Rs. 450, loss 10%. CP?",
 "Rs. 480","Rs. 490","Rs. 500","Rs. 510","C"),

("Profit & Loss","Profit %",
 "Bought 15 items for Rs. 150, sold all for Rs. 12 each. Profit %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Discount",
 "MP Rs. 1500. After 10% discount, profit is 20% on CP. CP?",
 "Rs. 1100","Rs. 1125","Rs. 1150","Rs. 1200","B"),

("Profit & Loss","SP from Profit",
 "CP Rs. 2000, profit Rs. 300. Profit %?",
 "12%","13%","15%","18%","C"),

("Profit & Loss","Loss %",
 "CP Rs. 650, loss Rs. 65. Loss %?",
 "8%","9%","10%","12%","C"),

("Profit & Loss","Discount",
 "Discount of Rs. 150 on MP Rs. 750. Discount %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Profit %",
 "SP = 5/4 of CP. Profit %?",
 "20%","25%","30%","40%","B"),

("Profit & Loss","Loss %",
 "SP = 4/5 of CP. Loss %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","CP from SP",
 "After 25% profit, SP is Rs. 500. CP?",
 "Rs. 375","Rs. 380","Rs. 400","Rs. 420","C"),

("Profit & Loss","SP from Profit",
 "Profit 50% on CP Rs. 400. SP?",
 "Rs. 500","Rs. 550","Rs. 600","Rs. 650","C"),

("Profit & Loss","Discount",
 "A book MP Rs. 200. Discount 12.5%. SP?",
 "Rs. 170","Rs. 175","Rs. 180","Rs. 185","B"),

# === MORE RATIO - 15 ===
("Ratio & Proportion","Basic Ratio",
 "A:B = 3:4. A = 21. B?",
 "24","26","28","30","C"),

("Ratio & Proportion","Sharing",
 "Divide Rs. 1000 in 2:3. Smaller share?",
 "Rs. 350","Rs. 380","Rs. 400","Rs. 420","C"),

("Ratio & Proportion","Proportion",
 "If 7:x = 21:9, find x.",
 "2","3","4","5","B"),

("Ratio & Proportion","Division",
 "A:B:C = 1:3:5. Total = 180. C gets?",
 "80","90","100","110","C"),

("Ratio & Proportion","Sharing",
 "Rs. 480 in ratio 5:7. Difference?",
 "Rs. 60","Rs. 70","Rs. 80","Rs. 90","C"),

("Ratio & Proportion","Basic Ratio",
 "Ratio 2:7. If smaller = 14, larger?",
 "42","45","49","56","C"),

("Ratio & Proportion","Proportion",
 "If a/b = 3/5 and b/c = 5/8, then a:c?",
 "1:3","3:8","5:8","8:3","B"),

("Ratio & Proportion","Division",
 "Divide 240 in 3:5:4. Middle part?",
 "80","90","100","110","C"),

("Ratio & Proportion","Sharing",
 "Three friends share Rs. 3600 in 2:3:4. Middle friend gets?",
 "Rs. 800","Rs. 1000","Rs. 1200","Rs. 1600","C"),

("Ratio & Proportion","Basic Ratio",
 "A class has boys:girls = 3:2. Total 50. Girls?",
 "15","18","20","25","C"),

("Ratio & Proportion","Proportion",
 "4th proportional to 3, 5, 12 is?",
 "15","18","20","24","C"),

("Ratio & Proportion","Division",
 "Rs. 5400 divided in 4:5. Larger share?",
 "Rs. 2400","Rs. 2700","Rs. 3000","Rs. 3200","C"),

("Ratio & Proportion","Sharing",
 "Profit Rs. 2400 shared in ratio of investment 3:5. Smaller share?",
 "Rs. 800","Rs. 900","Rs. 1000","Rs. 1100","B"),

("Ratio & Proportion","Basic Ratio",
 "Ratio of 750 ml to 1.5 litres?",
 "1:3","1:2","2:3","3:4","B"),

("Ratio & Proportion","Division",
 "A:B = 3:4, B:C = 2:3. A:B:C = ?",
 "3:4:6","6:8:12","3:4:3","3:2:4","A"),

# === MORE TIME & WORK - 15 ===
("Time & Work","Two Workers",
 "A in 12 days, B in 24 days. Together?",
 "6 days","7 days","8 days","9 days","C"),

("Time & Work","Men-Days",
 "15 men in 8 days. 12 men in?",
 "8 days","9 days","10 days","12 days","C"),

("Time & Work","Efficiency",
 "A works 3 times faster than B. Together in 9 days. B alone?",
 "24 days","30 days","36 days","40 days","C"),

("Time & Work","Two Workers",
 "P in 10 days, Q in 30 days. Together?",
 "6.5 days","7 days","7.5 days","8 days","C"),

("Time & Work","Basic",
 "A does a work in 25 days. Work done in 10 days?",
 "1/5","2/5","3/5","4/5","B"),

("Time & Work","Men-Days",
 "6 women do work in 15 days. 9 women do it in?",
 "8 days","9 days","10 days","12 days","C"),

("Time & Work","Two Workers",
 "A in 7 days, B in 14 days. Together?",
 "4 days","4.67 days","5 days","5.5 days","B"),

("Time & Work","Efficiency",
 "Pipe A fills in 12 hrs, B empties in 24 hrs. Both open, fills in?",
 "20 hrs","22 hrs","24 hrs","28 hrs","C"),

("Time & Work","Men-Days",
 "18 workers in 10 days. 10 workers in?",
 "15 days","16 days","18 days","20 days","C"),

("Time & Work","Two Workers",
 "A in 4 days, B in 12 days, C in 6 days. Together?",
 "1.5 days","2 days","2.5 days","3 days","B"),

("Time & Work","Basic",
 "If 2/3 work done in 8 days, remaining work?",
 "2 days","3 days","4 days","5 days","C"),

("Time & Work","Efficiency",
 "X does 1/4 of work in 5 days. Full work?",
 "15 days","18 days","20 days","25 days","C"),

("Time & Work","Men-Days",
 "24 men do job in 5 days. To do in 3 days, men needed?",
 "35","38","40","42","C"),

("Time & Work","Two Workers",
 "A in 8 hrs, B in 12 hrs. A works 2 hrs alone, then both. Total time?",
 "4.2 hrs","4.8 hrs","5 hrs","5.4 hrs","C"),

("Time & Work","Basic",
 "A machine produces 100 units in 4 hrs. Units in 10 hrs?",
 "200","220","250","280","C"),

# === MORE AVERAGE - 15 ===
("Average","Basic Average",
 "Average of 25, 35, 45, 55, 65:",
 "40","43","45","48","C"),

("Average","Change in Average",
 "Average of 8 numbers is 30. If 6 is added to each, new average?",
 "32","34","36","38","C"),

("Average","Age Problems",
 "Average age of couple is 30. Baby born. New average?",
 "18","20","22","25","B"),

("Average","Basic Average",
 "Average of first 50 natural numbers?",
 "24.5","25","25.5","26","C"),

("Average","Change in Average",
 "Class of 40, average 60. 10 students of average 80 join. New average?",
 "62","64","66","68","B"),

("Average","Basic Average",
 "Runs in 5 innings: 36, 45, 53, 62, 4. Average?",
 "38","39","40","42","C"),

("Average","Age Problems",
 "3 brothers average age 15. Eldest is 20. Average of other two?",
 "10","12","12.5","13","C"),

("Average","Change in Average",
 "Average of 5 numbers is 50. One number 45 replaced by 60. New average?",
 "51","52","53","54","C"),

("Average","Basic Average",
 "Average of 11 results is 50. First 6 average 49, last 6 average 52. 6th result?",
 "50","51","56","60","C"),

("Average","Change in Average",
 "If each of 10 numbers is multiplied by 3, average becomes?",
 "Same","Double","Triple","Quadruple","C"),

("Average","Basic Average",
 "Sum of 3 numbers is 99. Ratio 1:2:3. Average?",
 "30","33","35","36","B"),

("Average","Age Problems",
 "Average of 4 friends: 22. If 5th friend age 32 joins, new average?",
 "23","24","25","26","B"),

("Average","Basic Average",
 "Average marks of 5 students: 70, 80, 60, 90, 50. Average?",
 "65","68","70","72","C"),

("Average","Change in Average",
 "Average of 15 numbers is 18. 5 numbers removed with average 12. Remaining average?",
 "20","21","22","24","B"),

("Average","Basic Average",
 "Weighted average: 3 items at 10 and 2 items at 20. Average?",
 "13","14","15","16","B"),

# === MORE PERCENTAGE - 15 ===
("Percentage","Basic",
 "What is 12% of 500?",
 "50","55","60","65","C"),

("Percentage","Increase",
 "A number 150 increased by 40%. New number?",
 "190","200","210","220","C"),

("Percentage","Decrease",
 "Price drops from Rs. 250 to Rs. 200. Decrease %?",
 "15%","18%","20%","25%","C"),

("Percentage","Conversion",
 "5/6 as a percentage (approx)?",
 "80%","82%","83.33%","85%","C"),

("Percentage","Basic",
 "What percent is 45 of 180?",
 "20%","22%","25%","30%","C"),

("Percentage","Increase",
 "Salary Rs. 15000, hike 20%. New salary?",
 "Rs. 16500","Rs. 17000","Rs. 17500","Rs. 18000","D"),

("Percentage","Decrease",
 "After 30% discount, price is Rs. 350. Original?",
 "Rs. 450","Rs. 480","Rs. 500","Rs. 520","C"),

("Percentage","Conversion",
 "0.125 as percentage?",
 "1.25%","10.5%","12.5%","125%","C"),

("Percentage","Basic",
 "60% of what number is 90?",
 "120","130","140","150","D"),

("Percentage","Increase",
 "Students increase from 400 to 500. Increase %?",
 "20%","22%","25%","30%","C"),

("Percentage","Decrease",
 "Temperature drops from 40 to 32. Percentage drop?",
 "15%","18%","20%","25%","C"),

("Percentage","Basic",
 "35% of 600?",
 "200","205","210","220","C"),

("Percentage","Increase",
 "If a number is first increased by 10% then by 10%, net increase?",
 "20%","21%","22%","25%","B"),

("Percentage","Decrease",
 "Two successive discounts of 10% and 20% on Rs. 1000. Final price?",
 "Rs. 700","Rs. 720","Rs. 750","Rs. 800","B"),

("Percentage","Conversion",
 "What fraction is 37.5%?",
 "1/3","3/8","2/5","5/12","B"),

# === MORE SPEED - 15 ===
("Speed Time Distance","Speed Formula",
 "A car at 75 km/h covers a distance in 4 hours. Distance?",
 "280 km","290 km","300 km","320 km","C"),

("Speed Time Distance","Average Speed",
 "Goes 50 km at 25 km/h and 50 km at 50 km/h. Average speed?",
 "30 km/h","33.3 km/h","35 km/h","37.5 km/h","B"),

("Speed Time Distance","Conversion",
 "20 m/s to km/h:",
 "60 km/h","68 km/h","72 km/h","80 km/h","C"),

("Speed Time Distance","Speed Formula",
 "Speed 15 km/h, time 40 min. Distance?",
 "8 km","9 km","10 km","12 km","C"),

("Speed Time Distance","Speed Formula",
 "A boat covers 36 km in 4 hours downstream. Speed?",
 "7 km/h","8 km/h","9 km/h","10 km/h","C"),

("Speed Time Distance","Average Speed",
 "Round trip: goes at 40 km/h, returns at 60 km/h. Avg speed?",
 "46 km/h","48 km/h","50 km/h","52 km/h","B"),

("Speed Time Distance","Conversion",
 "5 km/h = ? m/min (approx)",
 "75 m/min","80 m/min","83.3 m/min","90 m/min","C"),

("Speed Time Distance","Speed Formula",
 "Distance 500 m, time 25 s. Speed?",
 "18 m/s","20 m/s","22 m/s","25 m/s","B"),

("Speed Time Distance","Speed Formula",
 "A walks 4 km/h for 45 min. Distance?",
 "2 km","2.5 km","3 km","3.5 km","C"),

("Speed Time Distance","Average Speed",
 "Half time at 20 km/h, half time at 40 km/h. Average speed?",
 "25 km/h","28 km/h","30 km/h","32 km/h","C"),

("Speed Time Distance","Speed Formula",
 "A plane at 600 km/h. 1500 km journey takes?",
 "2 hrs","2.5 hrs","3 hrs","3.5 hrs","B"),

("Speed Time Distance","Conversion",
 "1 m/s = ? km/h",
 "2.4","3.2","3.6","4.0","C"),

("Speed Time Distance","Speed Formula",
 "A runner covers 1.5 km in 5 min. Speed in km/h?",
 "15 km/h","16 km/h","18 km/h","20 km/h","C"),

("Speed Time Distance","Average Speed",
 "Travels 120 km at 60 km/h, 80 km at 40 km/h. Average speed?",
 "48 km/h","50 km/h","52 km/h","55 km/h","B"),

("Speed Time Distance","Speed Formula",
 "A train at 54 km/h. Speed in m/s?",
 "12 m/s","13 m/s","14 m/s","15 m/s","D"),

# === MORE AGE - 15 ===
("Age Problems","Present Age",
 "A is 4 years older than B. 4 years later A will be twice B. B's age?",
 "0","2","4","6","A"),

("Age Problems","Future Age",
 "A man is 42, son 12. In how many years man = 2 x son?",
 "14","16","18","20","C"),

("Age Problems","Past Age",
 "8 years ago, A was 3 times B. A is 32 now. B now?",
 "14","16","18","20","B"),

("Age Problems","Ratio Problems",
 "Father:Son = 4:1. After 6 years, 3:1. Son's age?",
 "6","8","10","12","A"),

("Age Problems","Present Age",
 "Sum of ages of 5 children born 3 years apart is 50. Youngest?",
 "4","5","6","8","A"),

("Age Problems","Future Age",
 "After 10 years, A will be 3 times B (B is 5 now). A's present age?",
 "30","35","40","45","B"),

("Age Problems","Past Age",
 "4 years ago, mother was 6 times daughter. Mother 40 now. Daughter?",
 "9","10","11","12","B"),

("Age Problems","Ratio Problems",
 "Husband:Wife = 5:4. After 3 years 11:9. Husband's age?",
 "40","45","50","55","A"),

("Age Problems","Present Age",
 "Average age of class of 40 is 15. Teacher included, average = 16. Teacher's age?",
 "50","52","55","56","D"),

("Age Problems","Future Age",
 "A is 20, B is 5. When will A = 3B?",
 "3 years","5 years","7.5 years","10 years","C"),

("Age Problems","Past Age",
 "6 years ago, ratio 1:2. Sum now is 45. Ages?",
 "15, 30","17, 28","18, 27","20, 25","A"),

("Age Problems","Ratio Problems",
 "A:B = 2:3. Sum = 25. A?",
 "8","10","12","15","B"),

("Age Problems","Present Age",
 "C is twice D's age minus 6. Sum = 30. D's age?",
 "10","12","14","16","B"),

("Age Problems","Future Age",
 "After 5 years, sum of ages of X(20) and Y(25) will be?",
 "48","50","52","55","B"),

("Age Problems","Past Age",
 "7 years ago average age of family of 5 was 25. Present average?",
 "30","32","34","35","B"),

# === MORE WORD PROBLEMS - 15 ===
("Word Problems","Purchases",
 "A pen Rs. 15, a notebook Rs. 25. Buy 4 pens and 3 notebooks. Total?",
 "Rs. 125","Rs. 130","Rs. 135","Rs. 140","C"),

("Word Problems","Money",
 "Rohit saves Rs. 200/week. Savings in 6 months (26 weeks)?",
 "Rs. 4800","Rs. 5000","Rs. 5200","Rs. 5400","C"),

("Word Problems","Distribution",
 "A 12 m cloth cut into pieces of 1.5 m each. Number of pieces?",
 "6","7","8","9","C"),

("Word Problems","Mixtures",
 "20 L of 25% sugar solution. Sugar content?",
 "3 L","4 L","5 L","6 L","C"),

("Word Problems","Purchases",
 "A kg of mangoes Rs. 80. How much for 3.5 kg?",
 "Rs. 250","Rs. 260","Rs. 270","Rs. 280","D"),

("Word Problems","Money",
 "Income Rs. 50000/month. Expenditure 70%. Savings?",
 "Rs. 12000","Rs. 13000","Rs. 15000","Rs. 17000","C"),

("Word Problems","Distribution",
 "120 balls in boxes of 15 each. Boxes needed?",
 "6","7","8","9","C"),

("Word Problems","Mixtures",
 "Mix 10 L at Rs. 30 and 10 L at Rs. 50. Rate per litre?",
 "Rs. 35","Rs. 38","Rs. 40","Rs. 42","C"),

("Word Problems","Purchases",
 "Train ticket Rs. 250. Return Rs. 400. Savings on return?",
 "Rs. 80","Rs. 90","Rs. 100","Rs. 110","C"),

("Word Problems","Money",
 "Bill Rs. 840. Split equally among 7 friends. Each pays?",
 "Rs. 110","Rs. 115","Rs. 120","Rs. 125","C"),

("Word Problems","Distribution",
 "Pack 480 oranges, 24 per box. Boxes?",
 "18","19","20","22","C"),

("Word Problems","Mixtures",
 "40 L solution: 60% acid. Pure acid?",
 "20 L","22 L","24 L","26 L","C"),

("Word Problems","Purchases",
 "Taxi: Rs. 30 base + Rs. 12/km. Cost for 10 km?",
 "Rs. 140","Rs. 145","Rs. 150","Rs. 155","C"),

("Word Problems","Money",
 "A borrows Rs. 10000 at 5% SI for 2 years. Returns?",
 "Rs. 10500","Rs. 10800","Rs. 11000","Rs. 11200","C"),

("Word Problems","Distribution",
 "Pizza cut into 8 slices. 3 friends eat 2 each. Remaining?",
 "1","2","3","4","B"),
]
