'''Create a dictionary that contain a list of people and one intersecting fact about each of them. Display each person and hisor her 
 interesting fact to the sreen. Next, change a fact about one of the people. Also add an additional person and correspondin g fact.
 Display the new list of people and facts. Run the program multiple times and notice if the order changes. 
 Sample output:
 Jeff: Is afraid of Dogs.
 David: play the piano.
 Jason: Can fly an airplane.

 Jeff: Is afraid of height.
 David: play the piano.
 Jason: Can fly an airplane.
 Jill: Can hula dance.'''

people_facts = {"Jeff" : "Is afraid of Dogs.", "David" : "play the piano.", "Jason" : "Can fly an airplane."}
print("Initial fact about peoples are: ")
for people, facts in  people_facts.items():
    print(f"{people} : {facts}")
print()
people_facts["Jeff"] = "Is afraid of height."
people_facts["jill"] = "Can hula dance."

print("updated fact about peoples are: ")
for people, facts in  people_facts.items():
    print(f"{people} : {facts}")
    
''' Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You have scores.
 Store them in list and find the score of the runner-up. 
 Sample input: [2,3,6,6,5]
 Sample output: 5
 Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum score is 5. Hence, we print 5 as the runner-up score.'''

def runner_up_score(scores):
    unique_scores = set(scores)
    sorted_scores = sorted(list(unique_scores))
    if len(sorted_scores) >=2:
        return sorted_scores[-2]
    else:
        return "No runner-up found."

participants_score = [2,3,6,6,5]
print("participant's score sheet")
for score in participants_score:
    print(score)
runner_up_score = runner_up_score(participants_score)    
print(f"The runner-up score is: {runner_up_score}")

''' You have a record of n student. Each record contains the student's name and their percent marks in Math, Physics, and Chemistry.
 The marks can be floating values. You are required to save the record in a dictionary data type.
 Student's name is the key. Marks store in a list is the value. The user enter a student's name. Output the average percentage marks 
 obtained by that student.
 Formula: (sum of marks)/(no. of subjects)
 sample input: {"krishna" : [67, 68, 69],
                 "Arjun" : [70, 98, 63]
                  "Malika" : [52, 56, 60]}
 Sample output: 
 Enter a name: Malika
 Average percentage mark: 56
 Explanation:
 Marks for Malika are [52, 56, 60] whose average is (52+56+60)/3 => 6'''

def average_score(students_record, student_name):
    if student_name in students_record:
        marks = students_record[student_name]
        average_mark = sum(marks)/len(marks)
    else:
        return f"{student_name} is not exist in student's records"
    return average_mark

student_records ={
    "krishna" : [67, 68, 69],
    "Arjun" : [70, 98, 63],
    "Malika" : [52, 56, 60]
}
student_name = input("Enter a name: ")
average_score = average_score(student_records, student_name )
print(f"Marks for {student_name} are {student_records[student_name]} whose average is {average_score}")

''' Given a string of n words, help Alex to find out how many times his name appears in the string.
 Constraint; 1 <= n <= 200
 Sample input: Hi Alex WelcomeAlex Bye Alex.
 Sample output: 3
 Explanation: Alex name appear 3 times in the string. Hi Alex WelcomeAlex Bye Alex.'''

def alex_count(string):
    count = string.count("Alex")
    return count

string = "Hi Alex WelcomeAlex Bye Alex."
count = alex_count(string)
print(f"{count} times his name appear in the given string.")