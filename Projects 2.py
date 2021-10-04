#PygLatin
pyg = 'ay'

original = input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1 : len(new_word)]
if  len(original) > 0 and original.isalpha():
  print (new_word)
else:
  print ('empty')
#########################################################

#Taking a vication
def hotel_cost (nights):
  return 140*nights

def plane_ride_cost (city):
  if city == "Charlotte" :
    return 183
  elif city == "Tampa" :
    return 220
  elif city == "Pittsburgh" :
    return 222
  else :
    return 475

def rental_car_cost (days):
  cost = days * 40
  if days >= 7 :
     cost -= 50
    
  elif days >= 3 :
     cost -=20   
  return cost

def trip_cost (city,days, spending_money):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) +spending_money

print (trip_cost("Los Angeles" , 5 , 600))
##############################################################

#student becomes the teacher 
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  return float(total) / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return homework*.1 +quizzes*.3+ tests*.6

def get_letter_grade(score):
  if score >= 90 :
    return "A"
  elif score >= 80 :
    return "B"
  elif score >= 70 :
    return "C"
  elif score >= 60 :
    return "D" 
  else :
    return "F"
  
print (get_letter_grade(get_average(lloyd)))

def get_class_average(class_list):
  results=[]
  for student in class_list:
    results.append(get_average(student))
  return average(results)

students = [alice ,lloyd , tyler]
print (get_class_average(students))
print (get_letter_grade(students))
##################################################

#Exam statiscs
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores :
    variance += (average - score) ** 2
  variance /= float(len(scores))
  return variance

print (grades_variance(grades))

def grades_std_deviation(variance):
  return variance**.5

print_grades(grades)
print (grades_sum(grades))
print (grades_average(grades))
print (grades_variance(grades))
variance = grades_variance(grades)
print (grades_std_deviation(variance))

##################################################################










