# Section 3 - Numerical Ability | Batch 2 (Q201-400)
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# === AVERAGE - 50 questions ===
("Average","Basic Average",
 "Average of 10, 20, 30, 40, 50 is:",
 "25","28","30","35","C"),

("Average","Basic Average",
 "Average of first 10 natural numbers:",
 "5","5.5","6","6.5","B"),

("Average","Basic Average",
 "Average of 12, 15, 18, 21, 24 is:",
 "16","17","18","19","C"),

("Average","Basic Average",
 "Average of 5, 10, 15, 20 is:",
 "10","12","12.5","15","C"),

("Average","Basic Average",
 "Average of first 5 even numbers (2,4,6,8,10):",
 "5","6","7","8","B"),

("Average","Basic Average",
 "Average of first 5 odd numbers (1,3,5,7,9):",
 "4","5","6","7","B"),

("Average","Basic Average",
 "Average of 100, 200, 300:",
 "150","180","200","250","C"),

("Average","Change in Average",
 "Average of 5 numbers is 20. If one number 15 is replaced by 25, new average?",
 "20","21","22","23","C"),

("Average","Change in Average",
 "Average of 4 numbers is 25. A 5th number 35 is added. New average?",
 "26","27","28","29","B"),

("Average","Change in Average",
 "Average of 10 students is 40. One student scoring 30 leaves. New average?",
 "40.5","41","41.1","42","C"),

("Average","Age Problems",
 "Average age of 5 members is 30 years. A baby is born. New average?",
 "24","25","26","27","B"),

("Average","Age Problems",
 "Average age of A, B, C is 25 years. Average of A and B is 20. C's age?",
 "30","33","35","40","C"),

("Average","Basic Average",
 "Sum of 6 numbers is 90. Average?",
 "12","14","15","18","C"),

("Average","Basic Average",
 "Average weight of 8 boys is 50 kg. Total weight?",
 "380 kg","400 kg","420 kg","450 kg","B"),

("Average","Change in Average",
 "Average marks of 30 students is 60. 5 students with average 40 leave. New average?",
 "62","63","64","65","C"),

("Average","Basic Average",
 "If average of x, x+2, x+4, x+6 is 5, find x.",
 "1","2","3","4","B"),

("Average","Age Problems",
 "Average age of 3 friends is 24. If youngest is 18, average of other two?",
 "25","27","28","30","B"),

("Average","Basic Average",
 "Average of 7 consecutive numbers starting from 4?",
 "6","7","8","9","B"),

("Average","Change in Average",
 "Average of 20 numbers is 15. If each number is increased by 5, new average?",
 "15","17","18","20","D"),

("Average","Change in Average",
 "Average of 10 numbers is 25. If each is doubled, new average?",
 "25","35","45","50","D"),

("Average","Basic Average",
 "Average of 3, 6, 9, 12, 15, 18 is:",
 "9.5","10","10.5","11","C"),

("Average","Age Problems",
 "Present average age of father and son is 35 years. 5 years ago, average was?",
 "25","28","30","32","C"),

("Average","Basic Average",
 "Average of first 20 natural numbers:",
 "9.5","10","10.5","11","C"),

("Average","Change in Average",
 "Average of 5 numbers is 40. One number removed, average becomes 35. Removed number?",
 "50","55","60","65","C"),

("Average","Basic Average",
 "Average of 8, 12, 16, 20, 24 is:",
 "14","15","16","18","C"),

("Average","Age Problems",
 "4 years ago, average age of a family of 4 was 20. Present average with a newborn?",
 "16","17","18","19.2","D"),

("Average","Change in Average",
 "Class average is 50. A new student with marks 70 joins (31 students now). New average?",
 "50.5","50.6","50.65","51","C"),

("Average","Basic Average",
 "Sum of 5 numbers is 125. Average?",
 "20","22","25","30","C"),

("Average","Basic Average",
 "Average speed if a car travels 120 km in 3 hours?",
 "30 km/h","35 km/h","40 km/h","45 km/h","C"),

("Average","Change in Average",
 "Average of 6 numbers is 30. One more number is 51. New average?",
 "31","32","33","34","C"),

# === AGE PROBLEMS - 50 questions ===
("Age Problems","Present Age",
 "A is 5 years older than B. Sum of ages = 35. A's age?",
 "18","19","20","21","C"),

("Age Problems","Present Age",
 "Father is 3 times son's age. Sum = 48. Son's age?",
 "10","12","14","16","B"),

("Age Problems","Present Age",
 "Ratio of ages of X and Y is 3:5. Sum = 64. Y's age?",
 "20","24","36","40","D"),

("Age Problems","Future Age",
 "A is 20. In how many years will A be twice 18-year-old B's age?",
 "14","16","18","20","B"),

("Age Problems","Future Age",
 "Present ages: P=30, Q=10. After how many years P = 2Q?",
 "5","8","10","12","C"),

("Age Problems","Future Age",
 "Ram is 40, son is 10. In how many years will Ram be twice his son's age?",
 "15","18","20","25","C"),

("Age Problems","Past Age",
 "5 years ago, A was 3 times B's age. A is 35, B is now?",
 "12","14","15","16","C"),

("Age Problems","Past Age",
 "6 years ago, M's age was half of N's age. N is 40 now. M is?",
 "20","22","23","24","C"),

("Age Problems","Ratio Problems",
 "Ages of A and B in ratio 4:3. After 6 years ratio = 5:4. A's present age?",
 "20","24","28","32","B"),

("Age Problems","Ratio Problems",
 "Ratio of father to son = 7:2. Father is 42. Son?",
 "10","12","14","16","B"),

("Age Problems","Present Age",
 "Mother is 25 years older than daughter. Sum = 45. Mother's age?",
 "30","32","35","38","C"),

("Age Problems","Future Age",
 "A is 15. After how many years will he be 25?",
 "8","9","10","12","C"),

("Age Problems","Past Age",
 "10 years ago, Raj was half his present age. His present age?",
 "18","20","22","25","B"),

("Age Problems","Ratio Problems",
 "A:B ages = 5:3. Difference = 12. A's age?",
 "25","28","30","35","C"),

("Age Problems","Present Age",
 "Average of father and son is 30. Father is 20 years older. Son's age?",
 "15","18","20","22","C"),

("Age Problems","Future Age",
 "Ravi is 8. His father is 36. In how many years father = 3 times Ravi?",
 "4","5","6","8","C"),

("Age Problems","Past Age",
 "3 years ago, ratio of A to B was 4:3. Now A is 19. B is?",
 "14","15","16","17","C"),

("Age Problems","Present Age",
 "A person's age 15 years hence will be 4 times his age 5 years ago. Present age?",
 "10","11","12","15","B"),

("Age Problems","Ratio Problems",
 "A and B ages ratio 2:5. After 8 years, ratio = 1:2. A's age?",
 "14","16","18","20","B"),

("Age Problems","Future Age",
 "Sum of ages of A and B = 40. After 5 years, sum will be?",
 "45","48","50","55","C"),

("Age Problems","Past Age",
 "Present age of X = 2 times what Y was 10 years ago. Y = 25 now. X = ?",
 "25","28","30","35","C"),

("Age Problems","Present Age",
 "Difference of ages of two brothers is 4. Product is 60. Elder's age?",
 "8","10","12","14","B"),

("Age Problems","Ratio Problems",
 "Father:Son = 5:1. After 5 years, 3:1. Father's age now?",
 "25","30","35","40","A"),

("Age Problems","Future Age",
 "Mary is 12 now. In how many years will she be thrice her present age?",
 "18","20","22","24","D"),

("Age Problems","Past Age",
 "4 years ago, A was 4 times B. A = 28 now. B now?",
 "8","10","12","14","B"),

("Age Problems","Present Age",
 "A man is 24 years older than his son. After 2 years, he will be 3 times his son's age. Son's present age?",
 "8","10","12","14","B"),

("Age Problems","Ratio Problems",
 "Ages of mother and daughter 3:1. After 5 years, 5:2. Mother now?",
 "35","40","45","50","C"),

("Age Problems","Future Age",
 "P is 30, Q is 20. When will their ages be 3:2?",
 "After 5 years","Never possible","After 10 years","They are already 3:2","D"),

("Age Problems","Past Age",
 "10 years ago, mother was 3 times son. Mother is 40 now. Son?",
 "18","20","22","25","B"),

("Age Problems","Present Age",
 "Grandson is 1/6 of grandfather's age. Grandfather is 72. Grandson?",
 "10","12","14","16","B"),

# === PERCENTAGE PROBLEMS - 40 questions ===
("Percentage","Basic",
 "What is 25% of 200?",
 "40","45","50","55","C"),

("Percentage","Basic",
 "15% of 400 is:",
 "50","55","60","65","C"),

("Percentage","Basic",
 "What is 8% of 250?",
 "18","19","20","22","C"),

("Percentage","Basic",
 "40% of 350 is:",
 "130","135","140","145","C"),

("Percentage","Conversion",
 "Express 3/5 as a percentage:",
 "50%","55%","60%","65%","C"),

("Percentage","Conversion",
 "Express 0.45 as percentage:",
 "4.5%","40%","45%","450%","C"),

("Percentage","Conversion",
 "What fraction is 75%?",
 "1/2","2/3","3/4","4/5","C"),

("Percentage","Increase",
 "A number increased by 20% becomes 60. The number?",
 "45","48","50","55","C"),

("Percentage","Increase",
 "Price of item goes from Rs. 80 to Rs. 100. Percentage increase?",
 "15%","20%","25%","30%","C"),

("Percentage","Decrease",
 "A value decreases from 200 to 150. Decrease %?",
 "20%","22%","25%","30%","C"),

("Percentage","Decrease",
 "Population drops from 5000 to 4500. Decrease %?",
 "8%","9%","10%","12%","C"),

("Percentage","Basic",
 "30% of 600:",
 "160","170","180","190","C"),

("Percentage","Basic",
 "12.5% of 480:",
 "50","55","58","60","D"),

("Percentage","Increase",
 "A salary of Rs. 20000 increased by 10%. New salary?",
 "Rs. 21000","Rs. 22000","Rs. 23000","Rs. 24000","B"),

("Percentage","Decrease",
 "After 20% discount, price is Rs. 320. Original price?",
 "Rs. 380","Rs. 390","Rs. 400","Rs. 420","C"),

("Percentage","Basic",
 "What percent of 50 is 10?",
 "15%","18%","20%","25%","C"),

("Percentage","Basic",
 "What percent of 80 is 20?",
 "20%","22%","25%","30%","C"),

("Percentage","Conversion",
 "1/8 as percentage:",
 "8%","10%","12%","12.5%","D"),

("Percentage","Increase",
 "Marks: 60 out of 80. Percentage?",
 "70%","72%","75%","80%","C"),

("Percentage","Decrease",
 "Salary Rs. 25000, tax 10%. Take-home pay?",
 "Rs. 22000","Rs. 22500","Rs. 23000","Rs. 24000","B"),

("Percentage","Basic",
 "What is 33.33% of 900?",
 "280","290","300","310","C"),

("Percentage","Increase",
 "If 40% of a number is 80, the number is:",
 "180","190","200","220","C"),

("Percentage","Decrease",
 "A stock drops 25% from Rs. 800. New price?",
 "Rs. 550","Rs. 575","Rs. 600","Rs. 625","C"),

("Percentage","Conversion",
 "Express 7/20 as percentage:",
 "30%","32%","35%","37%","C"),

("Percentage","Increase",
 "Population increases from 10000 to 12000. Increase?",
 "15%","18%","20%","25%","C"),

("Percentage","Decrease",
 "Exam: Max marks 500, pass marks 40%. Pass marks?",
 "180","190","200","220","C"),

("Percentage","Basic",
 "5% of 1200 is:",
 "50","55","60","65","C"),

("Percentage","Increase",
 "Rs. 500 invested, returns Rs. 550. % return?",
 "8%","9%","10%","12%","C"),

("Percentage","Decrease",
 "Weight goes from 80 kg to 68 kg. % decrease?",
 "12%","13%","14%","15%","D"),

("Percentage","Conversion",
 "Express 2/25 as percentage:",
 "6%","7%","8%","10%","C"),
]
