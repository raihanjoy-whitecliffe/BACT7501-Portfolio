#This is a simple code to generate a users final grades by asking their Assignment, Test and Exam Marks by weighing them.
# done by MD Raihan Joy on 25th Feb,2026.
Assignment_mark_out_of_100= int(input('Enter your Assignment Mark (out of 100): '))     #user input for assignment mark out of 100
Test_mark_out_of_100= int(input('Enter your Test Mark (out of 100): '))                 #user input for test mark out of 100
Exam_mark_out_of_100= int(input('Enter your Exam Mark (out of 100): '))                 #user input for exam mark out of 100
Assignment_after_weighing= Assignment_mark_out_of_100 * 0.30                            #converting assignment marks to weighed percentage
Test_after_weighing= Test_mark_out_of_100 * 0.30                                        #converting test marks to weighed percentage
Exam_after_weighing= Exam_mark_out_of_100 * 0.40                                        #converting exam marks to weighed percentage
final_grade= Assignment_after_weighing + Test_after_weighing + Exam_after_weighing
print(f'---------------- STUDENT RESULT ---------------')                               #printing the STUDENT RESULT heading as per expected output
print(f'Assignment Mark: {Assignment_mark_out_of_100}')                                 #printing the assignment mark as per expected output
print(f'Test Mark: {Test_mark_out_of_100}')                                             #printing the test mark as per expected output
print(f'Exam Mark: {Exam_mark_out_of_100}')                                             #printing the exam mark as per expected output

print(f'Assignment Contribution (30%): {Assignment_mark_out_of_100 * 0.30 : .2f}')      #printing the assignment contribution as per expected output in 2 d.p
print(f'Test Contribution (30%): {Test_mark_out_of_100 * 0.30 : .2f}')                  #printing the test contribution as per expected output in 2 d.p
print(f'Exam Contribution (40%): {Exam_mark_out_of_100 * 0.40 : .2f}')                  #printing the exam contribution as per expected output in 2 d.p

print(f'Final Grade: {final_grade : .2f}%')                                             #printing the Final Grade as per expected output in 2 d.p
print(f'---------------------------------------')                                       #printing the ending border as per expected output in 2 d.p