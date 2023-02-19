performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)

schedule_file.close() 

# instructions: Now that we have the performance and time from each line in our file, let's save them into a dictionary. Instead of just printing the show and time, we can also save them to our performances dictionary. On the last line of the for loop, delete the print statement. Instead, add a new entry to the performances dictionary using the key show and the value time.
# instructions: Now we should have our schedule in our performances dictionary, so let's print it to see if it looks right. We can do this outside of our loop after we closed our file.
# instructions: Our dictionary looks correct, except we have some newline characters in there from reading our lines. We can get rid of these by calling the .strip() function on the time variable when we add it to the dictionary. (Note: strip() removes all leading and trailing whitespace.)
# answer: https://github.com/ps-interactive/ics_solutions/blob/main/ic_python_using_lists_dictionaries_loops_files_and_modules/page.4-2-4.reading_into_a_dictionary/answer/circus.py
