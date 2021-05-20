# Challenge: List of lists
# from RealPython, Python Basics, chapter 9.4
#


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(univ_list):
    """ The function get datas from universities list and creats two lists, 
        one for students and one for tuitions."""
    all_students = []
    all_tuitions = []
    for i in range (0,len(univ_list)):
        all_students.append(univ_list[i][1])
        all_tuitions.append(univ_list[i][2])
        results = all_students, all_tuitions        # Function can't return more than one argument, it's need to create one list, which contains two others
    return list(results)                            # It schould be a list, so it is :)


def mean(univ_list):
    """ The function calculates the average values ​​for the data from the university list. """
    sum_of_students = sum(univ_list[0])    
    sum_of_tuitions = sum(univ_list[1]) 
    lenght = univ_list[0]    
    total_univ = len(lenght)
    mean_student = sum_of_students/total_univ
    mean_tuitions = sum_of_tuitions/total_univ
    means_results = mean_student, mean_tuitions
    return list(means_results)


def median(univ_list):
    """The function calculates the median values ​​depending on the length of the university list and an even or less number of items"""
    datas = univ_list
    students_datas = sorted(datas[0])                           # sort is needed to calculate the median
    tuitions_datas = sorted(datas[1])

    if len(students_datas)%2 == 1:                              # if modulo 2 equals 1, then number is odd
        middle_students = len(students_datas)//2                # in a 7-element list, 3 is the middle one from 0
        middle_tuitions = len(tuitions_datas)//2
        med_students = students_datas[middle_students]
        med_tuitions = tuitions_datas[middle_tuitions]
        mediana_results = med_students, med_tuitions
        return list(mediana_results)
    else:
        med_high_students = len(students_datas)//2              # if modulo 2 not equals 1, then number is even
        med_low_students = len(students_datas)//2-1             # and you need to get two numbers from the middle of the list
        med_students = (med_high_students + med_low_students)/2 
        med_high_tuitions = len(tuitions_datas)//2
        med_low_tuitions = len(tuitions_datas)//2-1
        med_tuitions = (med_high_tuitions + med_low_tuitions)/2 # and you need to sum two adjacent numbers in the middle of the list divided by 2
        mediana_results = med_students, med_tuitions
        return list(mediana_results)


# Print results
totals = enrollment_stats(universities)
means = mean(enrollment_stats(universities))
medians = median(enrollment_stats(universities))
print('*'*30)
print(f"Total students:     {sum(totals[0]):,}")
print(f"Total tuition:    $ {sum(totals[1]):,} \n")
print(f"Student mean:       {means[0]:,.2f}")
print(f"Student median:     {medians[0]:,} \n")
print(f"Tution mean:      $ {means[1]:,.2f}")
print(f"Tuition median:   $ {medians[1]:,}")
print('*'*30)
    