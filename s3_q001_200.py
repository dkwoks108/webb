# Section 3 - Numerical Ability | Batch 1 (Q001-200)
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# === SIMPLE INTEREST (SI) - 50 questions ===
("Simple Interest","SI Formula",
 "Find the simple interest on Rs. 5000 at 10% per annum for 2 years.",
 "Rs. 800","Rs. 900","Rs. 1000","Rs. 1100","C"),

("Simple Interest","SI Formula",
 "Simple interest on Rs. 2000 at 5% per annum for 3 years is:",
 "Rs. 200","Rs. 250","Rs. 300","Rs. 350","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 8000 at 8% per annum for 1 year is:",
 "Rs. 540","Rs. 600","Rs. 640","Rs. 720","C"),

("Simple Interest","SI Formula",
 "Find SI on Rs. 1200 at 12% for 2 years.",
 "Rs. 240","Rs. 288","Rs. 300","Rs. 312","B"),

("Simple Interest","SI Formula",
 "SI on Rs. 6000 at 6% for 4 years is:",
 "Rs. 1200","Rs. 1320","Rs. 1440","Rs. 1560","C"),

("Simple Interest","Principal",
 "At what principal will SI be Rs. 600 at 10% in 2 years?",
 "Rs. 2500","Rs. 3000","Rs. 3500","Rs. 4000","B"),

("Simple Interest","Principal",
 "Find the principal if SI is Rs. 450 at 5% for 3 years.",
 "Rs. 2500","Rs. 3000","Rs. 3500","Rs. 4000","B"),

("Simple Interest","Principal",
 "Principal that gives Rs. 720 as SI at 8% in 3 years is:",
 "Rs. 2800","Rs. 3000","Rs. 3200","Rs. 3600","B"),

("Simple Interest","Principal",
 "What sum gives Rs. 1500 as SI at 10% in 5 years?",
 "Rs. 2500","Rs. 3000","Rs. 3500","Rs. 4000","B"),

("Simple Interest","Rate",
 "At what rate will Rs. 4000 give SI of Rs. 800 in 4 years?",
 "4%","5%","6%","8%","B"),

("Simple Interest","Rate",
 "Find the rate if Rs. 5000 gives SI of Rs. 1500 in 3 years.",
 "8%","9%","10%","12%","C"),

("Simple Interest","Rate",
 "At what rate does Rs. 2000 yield Rs. 480 SI in 4 years?",
 "5%","6%","7%","8%","B"),

("Simple Interest","Rate",
 "Rs. 3000 gives Rs. 900 SI in 5 years. Rate is:",
 "4%","5%","6%","7%","C"),

("Simple Interest","Time",
 "In how many years will Rs. 5000 give Rs. 2000 as SI at 10%?",
 "2","3","4","5","C"),

("Simple Interest","Time",
 "In how many years will Rs. 8000 give Rs. 1920 as SI at 8%?",
 "2","3","4","5","B"),

("Simple Interest","Time",
 "Time for Rs. 6000 to earn Rs. 3600 SI at 12% per annum:",
 "3 years","4 years","5 years","6 years","C"),

("Simple Interest","Amount",
 "Amount after 2 years on Rs. 4000 at 10% SI:",
 "Rs. 4600","Rs. 4800","Rs. 5000","Rs. 5200","B"),

("Simple Interest","Amount",
 "What is the total amount if Rs. 3000 is invested at 7% SI for 3 years?",
 "Rs. 3530","Rs. 3600","Rs. 3630","Rs. 3700","C"),

("Simple Interest","Amount",
 "Amount on Rs. 10000 at 5% SI for 4 years:",
 "Rs. 11500","Rs. 12000","Rs. 12500","Rs. 13000","B"),

("Simple Interest","Amount",
 "Rs. 7000 invested at 9% for 2 years. Total amount?",
 "Rs. 8160","Rs. 8200","Rs. 8260","Rs. 8300","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 1500 at 4% for 5 years is:",
 "Rs. 250","Rs. 275","Rs. 300","Rs. 350","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 9000 at 7% for 2 years:",
 "Rs. 1200","Rs. 1260","Rs. 1300","Rs. 1400","B"),

("Simple Interest","SI Formula",
 "Find SI on Rs. 4500 at 6% for 3 years.",
 "Rs. 710","Rs. 780","Rs. 810","Rs. 900","C"),

("Simple Interest","Principal",
 "What sum earns Rs. 840 SI at 7% in 4 years?",
 "Rs. 2800","Rs. 3000","Rs. 3200","Rs. 3500","B"),

("Simple Interest","Rate",
 "Rs. 6000 earns Rs. 720 in 2 years. Rate?",
 "5%","6%","7%","8%","B"),

("Simple Interest","Time",
 "Time for Rs. 2500 to earn Rs. 500 at 10%?",
 "1 year","2 years","3 years","4 years","B"),

("Simple Interest","Amount",
 "Amount on Rs. 5500 at 8% for 3 years (SI):",
 "Rs. 6700","Rs. 6820","Rs. 6900","Rs. 7000","B"),

("Simple Interest","SI Formula",
 "SI on Rs. 12000 at 10% for 6 months is:",
 "Rs. 500","Rs. 600","Rs. 700","Rs. 800","B"),

("Simple Interest","SI Formula",
 "SI on Rs. 3000 at 12% for 9 months is:",
 "Rs. 250","Rs. 270","Rs. 290","Rs. 300","B"),

("Simple Interest","SI Formula",
 "SI on Rs. 8000 at 15% for 8 months is:",
 "Rs. 700","Rs. 750","Rs. 800","Rs. 850","C"),

("Simple Interest","Principal",
 "What principal gives Rs. 360 SI at 6% in 2 years?",
 "Rs. 2800","Rs. 3000","Rs. 3200","Rs. 3600","B"),

("Simple Interest","Rate",
 "Rate at which Rs. 7500 gives Rs. 1125 in 3 years?",
 "4%","5%","6%","7%","B"),

("Simple Interest","Time",
 "Time needed for Rs. 4000 to double at 10% SI?",
 "8 years","10 years","12 years","15 years","B"),

("Simple Interest","Time",
 "Time needed for Rs. 5000 to become Rs. 8000 at 12% SI?",
 "3 years","4 years","5 years","6 years","C"),

("Simple Interest","Amount",
 "A man deposits Rs. 2000 at 8% SI for 5 years. He gets back:",
 "Rs. 2600","Rs. 2700","Rs. 2800","Rs. 2900","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 15000 at 4% for 2 years:",
 "Rs. 1000","Rs. 1100","Rs. 1200","Rs. 1400","C"),

("Simple Interest","SI Formula",
 "Find SI: P = Rs. 10000, R = 3%, T = 5 years.",
 "Rs. 1200","Rs. 1400","Rs. 1500","Rs. 1600","C"),

("Simple Interest","Principal",
 "A sum doubles in 10 years at SI. The rate is:",
 "5%","8%","10%","12%","C"),

("Simple Interest","Principal",
 "A sum triples in 20 years at SI. The rate is:",
 "5%","8%","10%","12%","C"),

("Simple Interest","Rate",
 "Rs. 1000 becomes Rs. 1400 in 4 years at SI. Rate?",
 "8%","9%","10%","12%","C"),

("Simple Interest","Time",
 "Rs. 6000 amounts to Rs. 7800 at 6% SI. Time?",
 "3 years","4 years","5 years","6 years","C"),

("Simple Interest","Amount",
 "Amount after 3 years on Rs. 2500 at 12% SI:",
 "Rs. 3200","Rs. 3300","Rs. 3400","Rs. 3500","C"),

("Simple Interest","SI Formula",
 "Difference of SI on Rs. 5000 at 10% and 8% for 2 years:",
 "Rs. 100","Rs. 150","Rs. 200","Rs. 250","C"),

("Simple Interest","SI Formula",
 "SI on Rs. 7200 at 11% for 3 years:",
 "Rs. 2176","Rs. 2276","Rs. 2376","Rs. 2400","C"),

("Simple Interest","Rate",
 "In what time does Rs. 1250 at 4% give Rs. 50 SI?",
 "1 year","2 years","3 years","4 years","A"),

("Simple Interest","Amount",
 "Rs. 4000 at 5% SI. Amount after 6 years?",
 "Rs. 5000","Rs. 5100","Rs. 5200","Rs. 5400","C"),

("Simple Interest","Principal",
 "SI on a sum for 4 years at 5% is Rs. 400. The sum is:",
 "Rs. 1800","Rs. 2000","Rs. 2200","Rs. 2500","B"),

("Simple Interest","Rate",
 "Rs. 800 at SI becomes Rs. 920 in 3 years. Rate?",
 "4%","5%","6%","7%","B"),

("Simple Interest","Time",
 "In how many years will Rs. 900 earn Rs. 162 at 6%?",
 "2 years","3 years","4 years","5 years","B"),

("Simple Interest","Amount",
 "Rs. 11000 at 9% SI for 2 years. Amount?",
 "Rs. 12800","Rs. 12900","Rs. 12980","Rs. 13100","C"),

# === PROFIT & LOSS - 50 questions ===
("Profit & Loss","Profit %",
 "An article bought for Rs. 200 is sold for Rs. 250. Profit %?",
 "20%","25%","30%","35%","B"),

("Profit & Loss","Profit %",
 "CP = Rs. 400, SP = Rs. 480. Profit %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Loss %",
 "CP = Rs. 500, SP = Rs. 400. Loss %?",
 "10%","15%","20%","25%","C"),

("Profit & Loss","Loss %",
 "An article costing Rs. 800 is sold at Rs. 680. Loss %?",
 "10%","12%","15%","18%","C"),

("Profit & Loss","SP from Profit",
 "CP = Rs. 600. Profit = 20%. SP = ?",
 "Rs. 680","Rs. 700","Rs. 720","Rs. 740","C"),

("Profit & Loss","SP from Profit",
 "CP = Rs. 1500. Profit = 10%. SP?",
 "Rs. 1600","Rs. 1650","Rs. 1700","Rs. 1750","B"),

("Profit & Loss","SP from Loss",
 "CP = Rs. 1000. Loss = 15%. SP?",
 "Rs. 800","Rs. 850","Rs. 900","Rs. 950","B"),

("Profit & Loss","SP from Loss",
 "CP = Rs. 2000. Loss = 5%. SP?",
 "Rs. 1800","Rs. 1850","Rs. 1900","Rs. 1950","C"),

("Profit & Loss","CP from SP",
 "SP = Rs. 660, Profit = 10%. CP?",
 "Rs. 580","Rs. 600","Rs. 620","Rs. 640","B"),

("Profit & Loss","CP from SP",
 "SP = Rs. 480, Loss = 20%. CP?",
 "Rs. 550","Rs. 575","Rs. 600","Rs. 625","C"),

("Profit & Loss","Discount",
 "MP = Rs. 500, Discount = 10%. SP?",
 "Rs. 400","Rs. 425","Rs. 440","Rs. 450","D"),

("Profit & Loss","Discount",
 "MP = Rs. 1200, Discount = 25%. SP?",
 "Rs. 800","Rs. 850","Rs. 900","Rs. 950","C"),

("Profit & Loss","Discount",
 "SP = Rs. 720, Discount = 10%. MP?",
 "Rs. 750","Rs. 780","Rs. 800","Rs. 850","C"),

("Profit & Loss","Discount",
 "An item marked at Rs. 2000 is sold at Rs. 1600. Discount %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Profit %",
 "A man buys 10 pens for Rs. 100 and sells them at Rs. 12 each. Profit %?",
 "10%","15%","20%","25%","C"),

("Profit & Loss","Loss %",
 "Buys for Rs. 350, sells for Rs. 280. Loss %?",
 "15%","18%","20%","22%","C"),

("Profit & Loss","SP from Profit",
 "CP = Rs. 250. Profit = 40%. SP?",
 "Rs. 300","Rs. 325","Rs. 350","Rs. 375","C"),

("Profit & Loss","CP from SP",
 "SP = Rs. 1350, Profit = 35%. CP?",
 "Rs. 900","Rs. 950","Rs. 1000","Rs. 1050","C"),

("Profit & Loss","Profit %",
 "Bought a pen for Rs. 50 and sold for Rs. 65. Profit %?",
 "20%","25%","30%","35%","C"),

("Profit & Loss","Loss %",
 "CP = Rs. 1200, SP = Rs. 960. Loss %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Discount",
 "MP = Rs. 800, Discount = 15%. SP?",
 "Rs. 660","Rs. 670","Rs. 680","Rs. 700","C"),

("Profit & Loss","Profit %",
 "Buy 5 kg rice at Rs. 40/kg, sell at Rs. 50/kg. Profit %?",
 "20%","25%","30%","35%","B"),

("Profit & Loss","SP from Loss",
 "CP = Rs. 900, Loss = 10%. SP?",
 "Rs. 800","Rs. 810","Rs. 820","Rs. 830","B"),

("Profit & Loss","Discount",
 "After 20% discount, SP = Rs. 640. MP?",
 "Rs. 750","Rs. 780","Rs. 800","Rs. 820","C"),

("Profit & Loss","Profit %",
 "A trader buys goods for Rs. 4000 and sells at Rs. 4800. Profit %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","CP from SP",
 "SP = Rs. 560, Loss = 20%. CP?",
 "Rs. 650","Rs. 680","Rs. 700","Rs. 720","C"),

("Profit & Loss","Discount",
 "MP = Rs. 3000, successive discounts 10% and 10%. Final SP?",
 "Rs. 2400","Rs. 2430","Rs. 2500","Rs. 2700","B"),

("Profit & Loss","Profit %",
 "CP of 12 articles = SP of 10 articles. Profit %?",
 "10%","15%","20%","25%","C"),

("Profit & Loss","Loss %",
 "SP of 20 items = CP of 16 items. Loss %?",
 "10%","15%","20%","25%","C"),

("Profit & Loss","SP from Profit",
 "CP = Rs. 1800, Profit = 15%. SP?",
 "Rs. 2000","Rs. 2050","Rs. 2070","Rs. 2100","C"),

("Profit & Loss","Profit %",
 "Bought a cycle for Rs. 1400, repaired for Rs. 200, sold for Rs. 2000. Profit %?",
 "20%","22%","25%","30%","C"),

("Profit & Loss","Discount",
 "List price Rs. 600. After discount, sold at Rs. 510. Discount %?",
 "10%","12%","15%","18%","C"),

("Profit & Loss","SP from Profit",
 "CP = Rs. 450, gain = Rs. 90. Profit %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","CP from SP",
 "A chair sold for Rs. 690 at 15% profit. CP?",
 "Rs. 580","Rs. 590","Rs. 600","Rs. 620","C"),

("Profit & Loss","Loss %",
 "A phone bought for Rs. 15000, sold for Rs. 12000. Loss %?",
 "15%","18%","20%","25%","C"),

("Profit & Loss","Discount",
 "MP = Rs. 1000, Discount = 30%. SP?",
 "Rs. 650","Rs. 680","Rs. 700","Rs. 750","C"),

("Profit & Loss","Profit %",
 "Buys at Rs. 80/dozen, sells at Rs. 10 each. Profit %?",
 "40%","45%","50%","60%","C"),

("Profit & Loss","SP from Loss",
 "CP = Rs. 3500, Loss = 20%. SP?",
 "Rs. 2700","Rs. 2750","Rs. 2800","Rs. 2900","C"),

("Profit & Loss","CP from SP",
 "SP = Rs. 1080, Profit = 20%. CP?",
 "Rs. 850","Rs. 880","Rs. 900","Rs. 920","C"),

("Profit & Loss","Discount",
 "An article marked Rs. 1500 sold at Rs. 1200. Discount %?",
 "15%","18%","20%","25%","C"),

# === RATIO & PROPORTION - 50 questions ===
("Ratio & Proportion","Basic Ratio",
 "Simplify 24:36.",
 "1:2","2:3","3:4","4:5","B"),

("Ratio & Proportion","Basic Ratio",
 "Simplify 45:60.",
 "2:3","3:4","4:5","5:6","B"),

("Ratio & Proportion","Basic Ratio",
 "Ratio of 18 to 27 in simplest form:",
 "1:2","2:3","3:4","3:5","B"),

("Ratio & Proportion","Sharing",
 "Divide Rs. 500 in 2:3. Larger share?",
 "Rs. 200","Rs. 250","Rs. 300","Rs. 350","C"),

("Ratio & Proportion","Sharing",
 "Rs. 1200 divided among A, B in 3:5. B gets?",
 "Rs. 650","Rs. 700","Rs. 750","Rs. 800","C"),

("Ratio & Proportion","Sharing",
 "Divide Rs. 3500 in 2:3:5. The largest share?",
 "Rs. 1500","Rs. 1600","Rs. 1750","Rs. 1800","C"),

("Ratio & Proportion","Sharing",
 "Rs. 900 is divided among A, B, C in 1:2:3. A's share?",
 "Rs. 100","Rs. 125","Rs. 150","Rs. 200","C"),

("Ratio & Proportion","Division",
 "If A:B = 3:4 and B:C = 2:5, find A:B:C.",
 "3:4:10","6:8:20","3:4:5","6:4:10","A"),

("Ratio & Proportion","Basic Ratio",
 "A:B = 5:7. If A = 35, B = ?",
 "42","45","49","56","C"),

("Ratio & Proportion","Proportion",
 "If 3:5 :: x:20, find x.",
 "10","12","14","15","B"),

("Ratio & Proportion","Proportion",
 "If 4:7 :: 12:x, find x.",
 "18","20","21","24","C"),

("Ratio & Proportion","Sharing",
 "Two numbers in ratio 4:5, sum = 63. Smaller number?",
 "24","27","28","30","C"),

("Ratio & Proportion","Sharing",
 "Rs. 630 divided among A, B, C in ratio 1:2:4. C gets?",
 "Rs. 300","Rs. 350","Rs. 360","Rs. 400","C"),

("Ratio & Proportion","Basic Ratio",
 "Ratio of 50 cm to 2 m:",
 "1:2","1:3","1:4","1:5","C"),

("Ratio & Proportion","Basic Ratio",
 "Ratio of 500 g to 2 kg:",
 "1:2","1:3","1:4","1:5","C"),

("Ratio & Proportion","Division",
 "Divide 120 in ratio 3:5. Difference of parts?",
 "20","25","30","35","C"),

("Ratio & Proportion","Proportion",
 "Mean proportional of 4 and 16 is:",
 "6","8","10","12","B"),

("Ratio & Proportion","Proportion",
 "Third proportional to 3 and 6 is:",
 "9","10","12","15","C"),

("Ratio & Proportion","Sharing",
 "Rs. 2100 divided among P, Q, R in 3:4:7. Q's share?",
 "Rs. 500","Rs. 600","Rs. 700","Rs. 800","B"),

("Ratio & Proportion","Basic Ratio",
 "If A:B = 2:3 and A = 10, then A+B = ?",
 "20","22","25","30","C"),

("Ratio & Proportion","Division",
 "Two numbers in ratio 7:3. Difference = 20. Larger number?",
 "30","32","35","40","C"),

("Ratio & Proportion","Proportion",
 "If 5:8 :: 15:x, find x.",
 "20","22","24","28","C"),

("Ratio & Proportion","Sharing",
 "Divide 80 kg in ratio 3:5. Larger part?",
 "45 kg","48 kg","50 kg","55 kg","C"),

("Ratio & Proportion","Basic Ratio",
 "Ratio of 1 hour 20 min to 2 hours:",
 "1:2","2:3","3:4","4:5","B"),

("Ratio & Proportion","Division",
 "A, B, C share profit in 2:3:5. Total profit = Rs. 5000. A gets?",
 "Rs. 800","Rs. 900","Rs. 1000","Rs. 1100","C"),

("Ratio & Proportion","Proportion",
 "If 6:x :: x:24, find x.",
 "10","12","14","16","B"),

("Ratio & Proportion","Sharing",
 "Rs. 810 divided in ratio 2:3:4. Middle share?",
 "Rs. 240","Rs. 270","Rs. 300","Rs. 330","B"),

("Ratio & Proportion","Basic Ratio",
 "A:B = 5:6. Sum = 44. Find B.",
 "20","22","24","26","C"),

("Ratio & Proportion","Division",
 "Divide Rs. 7200 among X, Y in 5:7. Y's share?",
 "Rs. 3600","Rs. 4000","Rs. 4100","Rs. 4200","D"),

("Ratio & Proportion","Proportion",
 "If 2:3 :: 8:x, find x.",
 "10","11","12","14","C"),

# === TIME & WORK - 50 questions ===
("Time & Work","Basic",
 "A can do a work in 10 days. How much does A do in 1 day?",
 "1/8","1/9","1/10","1/12","C"),

("Time & Work","Basic",
 "A can do a piece of work in 12 days. In how many days will A complete half the work?",
 "4 days","5 days","6 days","8 days","C"),

("Time & Work","Two Workers",
 "A does a job in 10 days, B in 15 days. Together in how many days?",
 "5 days","6 days","7 days","8 days","B"),

("Time & Work","Two Workers",
 "A finishes work in 12 days, B in 18 days. Together?",
 "6 days","7 days","7.2 days","8 days","C"),

("Time & Work","Two Workers",
 "A can do a work in 6 days, B in 12 days. Together in?",
 "3 days","4 days","5 days","6 days","B"),

("Time & Work","Men-Days",
 "12 men finish a job in 10 days. 15 men will finish it in?",
 "6 days","7 days","8 days","9 days","C"),

("Time & Work","Men-Days",
 "8 workers do a job in 15 days. How many workers for 10 days?",
 "10","12","14","16","B"),

("Time & Work","Men-Days",
 "20 men do a work in 12 days. 24 men do it in?",
 "8 days","9 days","10 days","11 days","C"),

("Time & Work","Efficiency",
 "A is twice as efficient as B. B does work in 20 days. A does it in?",
 "8 days","10 days","12 days","15 days","B"),

("Time & Work","Efficiency",
 "A is 3 times as fast as B. Together they do work in 12 days. A alone?",
 "14 days","15 days","16 days","18 days","C"),

("Time & Work","Basic",
 "A does 1/5 of work in 3 days. Whole work in?",
 "12 days","15 days","18 days","20 days","B"),

("Time & Work","Two Workers",
 "A in 8 days, B in 24 days. Together?",
 "5 days","6 days","7 days","8 days","B"),

("Time & Work","Men-Days",
 "6 men complete work in 20 days. 10 men in?",
 "10 days","12 days","14 days","15 days","B"),

("Time & Work","Two Workers",
 "A in 15 days, B in 10 days. Together?",
 "5 days","6 days","7 days","8 days","B"),

("Time & Work","Efficiency",
 "A does in 10 days what B does in 15 days. A's one day work is more by how much?",
 "1/20","1/25","1/30","1/35","C"),

("Time & Work","Basic",
 "A can complete a task in 20 days. Work done in 5 days?",
 "1/5","1/4","1/3","1/2","B"),

("Time & Work","Two Workers",
 "P finishes in 40 days, Q in 60 days. Together?",
 "20 days","22 days","24 days","28 days","C"),

("Time & Work","Men-Days",
 "5 men build a wall in 8 days. 4 men build it in?",
 "8 days","9 days","10 days","12 days","C"),

("Time & Work","Efficiency",
 "X is half as efficient as Y. Y finishes in 14 days. X in?",
 "21 days","24 days","28 days","35 days","C"),

("Time & Work","Two Workers",
 "A in 20 days, B in 30 days. Together?",
 "10 days","12 days","14 days","15 days","B"),

("Time & Work","Basic",
 "If 3/4 of work is done in 12 days, whole work done in?",
 "14 days","15 days","16 days","18 days","C"),

("Time & Work","Men-Days",
 "10 women do a job in 6 days. 15 women do it in?",
 "3 days","4 days","5 days","6 days","B"),

("Time & Work","Two Workers",
 "A in 5 days, B in 20 days. Together?",
 "3 days","4 days","5 days","6 days","B"),

("Time & Work","Efficiency",
 "Machine A fills tank in 6 hrs, B in 12 hrs. Together?",
 "3 hrs","4 hrs","5 hrs","6 hrs","B"),

("Time & Work","Two Workers",
 "A in 18 days, B in 36 days. Together?",
 "10 days","12 days","14 days","16 days","B"),

("Time & Work","Men-Days",
 "16 workers in 25 days. 20 workers in?",
 "18 days","20 days","22 days","25 days","B"),

("Time & Work","Basic",
 "A completes work in 8 days. How much in 2 days?",
 "1/5","1/4","1/3","1/2","B"),

("Time & Work","Two Workers",
 "A in 6 days, B in 6 days. Together?",
 "2 days","3 days","4 days","5 days","B"),

("Time & Work","Efficiency",
 "Pipe A fills tank in 8 hrs, Pipe B empties in 16 hrs. Net fill time?",
 "12 hrs","14 hrs","16 hrs","18 hrs","C"),

("Time & Work","Men-Days",
 "If 4 men can mow a lawn in 6 hours, 3 men can mow it in?",
 "7 hrs","8 hrs","9 hrs","10 hrs","B"),

("Time & Work","Two Workers",
 "A in 14 days, B in 21 days. Together?",
 "7.2 days","8 days","8.4 days","9 days","C"),

("Time & Work","Efficiency",
 "A does 2/5 of work in 8 days. Remaining work done in?",
 "10 days","12 days","14 days","16 days","B"),

("Time & Work","Men-Days",
 "If 3 machines produce 300 units in 5 days, 5 machines produce 300 units in?",
 "2 days","3 days","4 days","5 days","B"),

("Time & Work","Two Workers",
 "A in 16 days, B in 48 days. Together?",
 "10 days","12 days","14 days","16 days","B"),

("Time & Work","Basic",
 "A paints a wall in 4 hours. 3/4 of wall takes?",
 "2 hrs","2.5 hrs","3 hrs","3.5 hrs","C"),

("Time & Work","Efficiency",
 "Tap A fills in 10 hrs, Tap B in 15 hrs. Both open, time to fill?",
 "4 hrs","5 hrs","6 hrs","7 hrs","C"),

("Time & Work","Men-Days",
 "9 children finish puzzle in 12 min. 6 children finish in?",
 "15 min","16 min","18 min","20 min","C"),

("Time & Work","Two Workers",
 "A in 9 days, B in 18 days. Together?",
 "5 days","6 days","7 days","8 days","B"),

("Time & Work","Efficiency",
 "A's efficiency is 1.5 times B's. B does work in 30 days. A in?",
 "15 days","18 days","20 days","22 days","C"),

("Time & Work","Basic",
 "A finishes 1/3 work in 4 days. Total work in?",
 "10 days","12 days","14 days","15 days","B"),
]
