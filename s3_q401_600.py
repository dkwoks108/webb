# Section 3 - Numerical Ability | Batch 3 (Q401-600)
# Format: (topic, subtopic, question, A, B, C, D, answer)

def get_questions():
    return [
# === SPEED, TIME & DISTANCE - 60 questions ===
("Speed Time Distance","Speed Formula",
 "A car covers 180 km in 3 hours. Speed?",
 "50 km/h","55 km/h","60 km/h","65 km/h","C"),

("Speed Time Distance","Speed Formula",
 "Speed = 40 km/h, Time = 5 hours. Distance?",
 "180 km","190 km","200 km","220 km","C"),

("Speed Time Distance","Speed Formula",
 "Distance = 300 km, Speed = 60 km/h. Time?",
 "4 hrs","4.5 hrs","5 hrs","5.5 hrs","C"),

("Speed Time Distance","Speed Formula",
 "A train covers 450 km in 5 hours. Speed?",
 "80 km/h","85 km/h","90 km/h","95 km/h","C"),

("Speed Time Distance","Speed Formula",
 "Speed = 72 km/h. Distance in 2.5 hrs?",
 "160 km","170 km","180 km","190 km","C"),

("Speed Time Distance","Speed Formula",
 "A man walks 6 km in 1.5 hours. Speed?",
 "3 km/h","3.5 km/h","4 km/h","4.5 km/h","C"),

("Speed Time Distance","Speed Formula",
 "A cyclist covers 45 km at 15 km/h. Time?",
 "2 hrs","2.5 hrs","3 hrs","3.5 hrs","C"),

("Speed Time Distance","Average Speed",
 "A car goes 60 km at 30 km/h and returns at 20 km/h. Average speed?",
 "22 km/h","24 km/h","25 km/h","26 km/h","B"),

("Speed Time Distance","Average Speed",
 "A man goes 100 km at 50 km/h and 100 km at 25 km/h. Average speed?",
 "30 km/h","33.3 km/h","35 km/h","37.5 km/h","B"),

("Speed Time Distance","Average Speed",
 "Travel 40 km at 40 km/h and 40 km at 60 km/h. Average speed?",
 "45 km/h","48 km/h","50 km/h","52 km/h","B"),

("Speed Time Distance","Conversion",
 "Convert 90 km/h to m/s:",
 "20 m/s","22 m/s","25 m/s","30 m/s","C"),

("Speed Time Distance","Conversion",
 "Convert 15 m/s to km/h:",
 "45 km/h","50 km/h","54 km/h","60 km/h","C"),

("Speed Time Distance","Conversion",
 "Convert 36 km/h to m/s:",
 "8 m/s","9 m/s","10 m/s","12 m/s","C"),

("Speed Time Distance","Speed Formula",
 "A bus travels 250 km in 5 hours. Speed?",
 "40 km/h","45 km/h","50 km/h","55 km/h","C"),

("Speed Time Distance","Speed Formula",
 "Speed 80 km/h. Time for 240 km?",
 "2 hrs","2.5 hrs","3 hrs","3.5 hrs","C"),

("Speed Time Distance","Speed Formula",
 "A horse runs at 60 km/h for 40 minutes. Distance?",
 "30 km","35 km","40 km","45 km","C"),

("Speed Time Distance","Average Speed",
 "Half distance at 40 km/h, other half at 60 km/h. Average speed?",
 "46 km/h","48 km/h","50 km/h","52 km/h","B"),

("Speed Time Distance","Speed Formula",
 "A train 200 m long passes a pole in 10 seconds. Speed?",
 "18 km/h","54 km/h","72 km/h","90 km/h","C"),

("Speed Time Distance","Speed Formula",
 "A person covers 12 km in 2 hours walking and 30 km in 1 hour by bus. Total time for 42 km?",
 "2 hrs","3 hrs","4 hrs","5 hrs","B"),

("Speed Time Distance","Conversion",
 "54 km/h in m/s:",
 "12 m/s","13 m/s","15 m/s","18 m/s","C"),

("Speed Time Distance","Speed Formula",
 "Time = 45 min, Speed = 80 km/h. Distance?",
 "50 km","55 km","60 km","65 km","C"),

("Speed Time Distance","Average Speed",
 "Goes 30 km at 10 km/h, 30 km at 30 km/h. Average speed?",
 "12 km/h","15 km/h","18 km/h","20 km/h","B"),

("Speed Time Distance","Speed Formula",
 "A car travels 150 km at 50 km/h. Departure 8 AM. Arrival?",
 "10 AM","10:30 AM","11 AM","11:30 AM","C"),

("Speed Time Distance","Conversion",
 "10 m/s = ? km/h",
 "30","32","36","40","C"),

("Speed Time Distance","Speed Formula",
 "A ship moves 20 km/h. How far in 6 hours?",
 "100 km","110 km","120 km","130 km","C"),

("Speed Time Distance","Average Speed",
 "First half at 20 km/h, second half at 30 km/h. Average speed for 120 km?",
 "22 km/h","24 km/h","25 km/h","26 km/h","B"),

("Speed Time Distance","Speed Formula",
 "A truck at 40 km/h takes 6 hours. At 60 km/h it takes?",
 "3 hrs","3.5 hrs","4 hrs","4.5 hrs","C"),

("Speed Time Distance","Speed Formula",
 "Train speed 90 km/h. How many km in 20 minutes?",
 "25 km","28 km","30 km","35 km","C"),

("Speed Time Distance","Average Speed",
 "30 km at 30 km/h, 30 km at 15 km/h. Average speed?",
 "18 km/h","20 km/h","22 km/h","25 km/h","B"),

("Speed Time Distance","Conversion",
 "108 km/h = ? m/s",
 "25 m/s","28 m/s","30 m/s","32 m/s","C"),

# === TWO-SPEED PROBLEMS - 30 questions ===
("Two-Speed Problems","Relative Speed",
 "Two cars move towards each other at 40 km/h and 60 km/h. Relative speed?",
 "20 km/h","80 km/h","100 km/h","120 km/h","C"),

("Two-Speed Problems","Relative Speed",
 "Two trains same direction: 80 km/h and 60 km/h. Relative speed?",
 "10 km/h","15 km/h","20 km/h","25 km/h","C"),

("Two-Speed Problems","Meeting Point",
 "A and B start from ends 100 km apart at 30 and 20 km/h towards each other. Meet in?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Meeting Point",
 "Two people 60 km apart walk towards each other at 4 km/h and 6 km/h. Meet in?",
 "4 hrs","5 hrs","6 hrs","8 hrs","C"),

("Two-Speed Problems","Relative Speed",
 "A car at 50 km/h chases one at 30 km/h. Gap = 40 km. Time to catch?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Meeting Point",
 "Two trains 200 km apart approach at 70 km/h and 30 km/h. Meet in?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Relative Speed",
 "A walks at 5 km/h, B at 3 km/h same direction. Gap increases by how much per hour?",
 "1 km","2 km","3 km","8 km","B"),

("Two-Speed Problems","Meeting Point",
 "P and Q start at same time from A and B (150 km apart) towards each other at 40 and 35 km/h. Meet in?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Relative Speed",
 "Two cyclists opposite direction: 12 km/h and 8 km/h. Relative speed?",
 "4 km/h","10 km/h","16 km/h","20 km/h","D"),

("Two-Speed Problems","Meeting Point",
 "A and B, 240 km apart, move towards each other at 50 and 70 km/h. Time to meet?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Relative Speed",
 "Train A: 90 km/h. Train B: 60 km/h (same direction). Relative speed in m/s?",
 "8.33 m/s","10 m/s","15 m/s","25 m/s","A"),

("Two-Speed Problems","Meeting Point",
 "Two children run towards each other from 80 m apart at 3 m/s and 5 m/s. Meet in?",
 "8 s","10 s","12 s","15 s","B"),

("Two-Speed Problems","Relative Speed",
 "If you walk at 6 km/h and a bus goes at 36 km/h in same direction, bus relative to you?",
 "6 km/h","26 km/h","30 km/h","42 km/h","C"),

("Two-Speed Problems","Meeting Point",
 "Two boats 120 km apart approach at 15 km/h each. Meet in?",
 "2 hrs","3 hrs","4 hrs","5 hrs","C"),

("Two-Speed Problems","Relative Speed",
 "Two friends walk in opposite directions from same point at 4 km/h and 5 km/h. After 3 hours, gap?",
 "3 km","9 km","12 km","27 km","D"),

("Two-Speed Problems","Meeting Point",
 "A starts from X at 20 km/h. B starts from Y (100 km away) at 30 km/h towards X. Meet in?",
 "1 hr","2 hrs","3 hrs","4 hrs","B"),

("Two-Speed Problems","Relative Speed",
 "Trains 120 m and 80 m long cross each other in 4 s (opposite). Sum of speeds in m/s?",
 "40 m/s","45 m/s","50 m/s","55 m/s","C"),

("Two-Speed Problems","Meeting Point",
 "Two joggers start from same point in opposite directions at 8 km/h and 12 km/h. After 1 hr, distance?",
 "4 km","10 km","16 km","20 km","D"),

("Two-Speed Problems","Relative Speed",
 "A 100 m train at 72 km/h passes a 50 m train (same direction) at 54 km/h. Time?",
 "20 s","25 s","30 s","35 s","C"),

("Two-Speed Problems","Meeting Point",
 "Two cars 300 km apart reach each other. Speeds 40 & 60 km/h. They meet after?",
 "2 hrs","3 hrs","4 hrs","5 hrs","B"),

# === WHEEL / REVOLUTION PROBLEMS - 30 questions ===
("Wheel Problems","Revolutions",
 "A wheel of circumference 2 m covers 100 m. Revolutions?",
 "40","45","50","55","C"),

("Wheel Problems","Revolutions",
 "Diameter of wheel = 70 cm. Circumference? (pi = 22/7)",
 "200 cm","210 cm","220 cm","240 cm","C"),

("Wheel Problems","Revolutions",
 "Wheel circumference = 4 m. Revolutions in 1 km?",
 "200","250","300","350","B"),

("Wheel Problems","Revolutions",
 "A wheel makes 500 revolutions to cover 1 km. Circumference?",
 "1 m","1.5 m","2 m","2.5 m","C"),

("Wheel Problems","Revolutions",
 "Wheel radius 35 cm. Circumference?",
 "200 cm","210 cm","220 cm","250 cm","C"),

("Wheel Problems","Revolutions",
 "Wheel circumference = 1.5 m. Distance in 200 revolutions?",
 "250 m","280 m","300 m","350 m","C"),

("Wheel Problems","Revolutions",
 "A tyre diameter 56 cm. Revolutions for 176 m? (pi=22/7)",
 "80","90","100","110","C"),

("Wheel Problems","Revolutions",
 "Wheel makes 10 revolutions per second. Circumference 3 m. Speed in m/s?",
 "20 m/s","25 m/s","30 m/s","35 m/s","C"),

("Wheel Problems","Revolutions",
 "Circumference 5 m. Revolutions in 500 m?",
 "50","80","100","120","C"),

("Wheel Problems","Revolutions",
 "A wheel of radius 14 cm makes 100 revolutions. Distance? (pi=22/7)",
 "8000 cm","8400 cm","8800 cm","9200 cm","C"),

("Wheel Problems","Revolutions",
 "Wheel diameter = 1 m. Circumference approx? (pi=3.14)",
 "2.14 m","2.94 m","3.14 m","3.54 m","C"),

("Wheel Problems","Revolutions",
 "A circular track radius 7 m. One lap distance? (pi=22/7)",
 "40 m","42 m","44 m","48 m","C"),

("Wheel Problems","Revolutions",
 "Wheel circumference 88 cm. Revolutions in 88 m?",
 "50","80","100","120","C"),

("Wheel Problems","Revolutions",
 "A wheel of diameter 2.8 m. Revolutions in 440 m? (pi=22/7)",
 "40","45","50","55","C"),

("Wheel Problems","Revolutions",
 "Wheel makes 600 revolutions/min. Circumference 0.5 m. Speed in m/min?",
 "250","280","300","350","C"),

("Wheel Problems","Revolutions",
 "Wheel radius 21 cm. How many revolutions for 132 m? (pi=22/7)",
 "80","90","100","110","C"),

("Wheel Problems","Revolutions",
 "Circumference = 66 cm. Distance in 1000 revolutions?",
 "550 m","600 m","660 m","700 m","C"),

("Wheel Problems","Revolutions",
 "A roller 2 m circumference covers a 50 m road. Revolutions?",
 "20","25","30","35","B"),

("Wheel Problems","Revolutions",
 "Wheel r = 7 m. Circumference? (pi=22/7)",
 "40 m","42 m","44 m","46 m","C"),

("Wheel Problems","Revolutions",
 "A wheel rotates 5 times per second, circumference 2 m. Distance in 1 minute?",
 "500 m","550 m","600 m","650 m","C"),

("Wheel Problems","Revolutions",
 "Wheel diameter 42 cm. Revolutions for 66 m? (pi=22/7)",
 "40","50","60","70","B"),

("Wheel Problems","Revolutions",
 "A gear wheel of circumference 10 cm meshes with one of 5 cm. Big wheel makes 100 revolutions. Small?",
 "100","150","200","250","C"),

("Wheel Problems","Revolutions",
 "Cycle wheel diameter 63 cm. Distance in 100 revolutions?",
 "180 m","190 m","198 m","210 m","C"),

("Wheel Problems","Revolutions",
 "Wheel circumference 110 cm. Distance in 500 revolutions?",
 "450 m","500 m","550 m","600 m","C"),

("Wheel Problems","Revolutions",
 "A miniature wheel of radius 3.5 cm. Circumference? (pi=22/7)",
 "20 cm","22 cm","24 cm","25 cm","B"),

("Wheel Problems","Revolutions",
 "A wheel moves 440 m in 200 revolutions. Circumference?",
 "1.8 m","2 m","2.2 m","2.5 m","C"),

("Wheel Problems","Revolutions",
 "Wheel radius 10.5 m, revolutions for 330 m? (pi=22/7)",
 "3","4","5","6","C"),

("Wheel Problems","Revolutions",
 "An engine wheel radius 0.5 m. rpm = 300. Distance per minute?",
 "900 m","942 m","960 m","1000 m","B"),

("Wheel Problems","Revolutions",
 "A toy car wheel circumference 22 cm travels 11 m. Revolutions?",
 "40","45","50","55","C"),

("Wheel Problems","Revolutions",
 "Wheel diameter 28 cm. Distance in 250 revolutions? (pi=22/7)",
 "200 m","210 m","220 m","240 m","C"),
]
