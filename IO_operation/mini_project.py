'''your friend has send you a text file containing n lines. He send a secret message with it, which tell you the place and time where 
you have to go and meet him.
He challenge you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking 
the challenge with our python code.
Hints to find the secret message:
1. The number of lines in the file tells you the meeting time.
   Note: 1<=number of lines<=24
   if the number of lines is exceeding 12, you need to convert it to 12 hour format. For example: 
       i. if the number of lines is 15, then the meeting time is 3 PM.
       ii.if the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the meeting place.
    Note: Meeting place will be street name. For example:
       i. if the word oxford appear for the maximum number of times, then meeting place is oxford street.
       ii.if the word park appear for the maximum number of times, then meeting place is park street.
'''

def secret_message(filepath):
    num_lines = 0
    word_count = {}
    with open(filepath, "r") as file:
        for lines in file:
            num_lines += 1
            words = lines.strip().lower().split()
            for word in words:
                word_count[word] = word_count.count(word)
        file.close()
    
    if not (1 <= num_lines <= 24):
        return "Number of lines is out of the specified range (1-24)"   
    if num_lines > 12:
        meeting_time_hour = num_lines - 12
        meeting_time_ampm = "PM"
    else:
        meeting_time_hour = num_lines
        meeting_time_ampm = "AM"   
    meeting_time = f"{meeting_time_hour} {meeting_time_ampm}"
    
    if not word_count:
        meeting_place = "No words found in file."
    else:
        max_count = 0
        meeting_place = ""
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                meeting_place = word
    return f"Meeting time: {meeting_time}, Meeting place: {meeting_place} "

file_name = input("Enter a text file ")
secret_message = secret_message(file_name)
print(secret_message)
        
    