# This original practice without any modification
performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)

# tasksFirst, let's wrap the line of code that opens our file inside a try block.


#Then, after the try block we need an except block, or our program won't run. Inside our except block let's print File doesn't exist.


#In the except: line, let's also check for a specific FileNotFoundError and save it into a variable called err.


#Finally, let's just print 

#answer: https://github.com/ps-interactive/ics_solutions/tree/main/ic_python_using_lists_dictionaries_loops_files_and_modules/page.4-3-2.try_except_succeed/answer
