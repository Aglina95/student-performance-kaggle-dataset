import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats


'''Open and read any csv file and return its rows as a list of lists'''
def open_csv(csvfile):
    with open(csvfile, newline="", encoding="utf-8-sig") as csvFile:
        csvReader = csv.reader(csvFile)
        csvData = list(csvReader)

    return csvData 

students_performance_data = open_csv('StudentsPerformance.csv')


'''Removes headers(first index in lst)'''
def remove_headers(lst):
    return lst[1:]

students_performance_data_without_headers = remove_headers(students_performance_data)

#print(students_performance_data_without_headers)


'''Extracts all values from a selected column in a list of rows'''
def get_column(lst, row_index):
    list_of_data = []
    for row in lst:
        selected_column = row[row_index]
        list_of_data.append(selected_column)
    return list_of_data

'''Extract data from individual columns'''
gender_data = get_column(students_performance_data_without_headers, 0)
race_ethnicity_data = get_column(students_performance_data_without_headers, 1)
parental_level_of_education_data = get_column(students_performance_data_without_headers, 2)
test_preparation_course_data = get_column(students_performance_data_without_headers, 4)
math_score_data = get_column(students_performance_data_without_headers, 5)
reading_score_data = get_column(students_performance_data_without_headers, 6)
writing_score_data = get_column(students_performance_data_without_headers, 7)


'''Counts how many times a value appears'''
def count_data_points(lst, category_data_point):
    total_responses = 0
    for i in lst:
        if category_data_point == i:
            total_responses += 1

    return total_responses

# Count occurrences of each gender in the dataset
total_female = count_data_points(gender_data, "female")
total_male = count_data_points(gender_data, "male")


'''Calculates percentage'''
def calc_percentage(total_data_points, total_count_of_category_data_points):
    division = total_count_of_category_data_points / len(total_data_points)
    percentage = division * 100
    
    return round(percentage,2)

female_percentage = calc_percentage(gender_data, total_female)
male_percentage = calc_percentage(gender_data, total_male)

print(female_percentage )

''' Converts to integer'''
def convert_to_integer(lst):
    integer_list = []
    for item in lst:
        integer_item = int(item)
        integer_list.append(integer_item)
    return integer_list

'''Call int to convert string list items to integers.'''
math_score_data_ints = convert_to_integer(math_score_data)
reading_score_data_ints = convert_to_integer(reading_score_data)
writing_score_data_ints = convert_to_integer(writing_score_data)


'''Calculates average score'''
def average_score(lst):
    total = 0
    for item in lst:
        total += item
    
    average = total / len(lst)

    return round(average, 1)

average_math_score = average_score(math_score_data_ints)
average_reading_score = average_score(reading_score_data_ints)
average_writing_score = average_score(writing_score_data_ints)


'''Pair lists to use data points for plotting or other calculations by specific categories'''
def pair_data(lst_1, lst_2):
    paired_data = []
    for i in range(len(lst_1)):
        paired_data.append([lst_1[i],lst_2[i]])
    
    return paired_data

math_score_and_gender = pair_data(gender_data, math_score_data_ints)
reading_score_and_gender = pair_data(gender_data, reading_score_data_ints)
writing_score_and_gender = pair_data(gender_data, writing_score_data_ints)

math_score_and_parental_education = pair_data(parental_level_of_education_data, math_score_data_ints)
reading_score_and_parental_education = pair_data(parental_level_of_education_data, reading_score_data_ints)
writing_score_and_parental_education = pair_data(parental_level_of_education_data, writing_score_data_ints)

math_score_and_test_preparation = pair_data(test_preparation_course_data, math_score_data_ints)
reading_score_and_test_preparation = pair_data(test_preparation_course_data, reading_score_data_ints)
writing_score_and_test_preparation = pair_data(test_preparation_course_data, writing_score_data_ints)


'''Finds average of specific data point by specific label/category in column'''
def find_average_score_by_specific_category_data_point(lst, category_data_point):
    score_by_category = []
    for i in lst:
        if i[0] == category_data_point:
            data_point_label = i[0]
            score_by_category.append([data_point_label, i[1]])
            subject_score = get_column(score_by_category, 1)
    mean = average_score(subject_score)
    return mean


parental_education_some_college_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, 'some college')
parental_education_high_school_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, 'high school')
parental_education_some_high_school_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, 'some high school')
parental_education_associatesdegree_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, "associate's degree")
parental_education_bachelors_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, "bachelor's degree")
parental_education_masters_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_parental_education, "master's degree")

parental_education_some_college_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, 'some college')
parental_education_high_school_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, 'high school')
parental_education_some_high_school_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, 'some high school')
parental_education_associatesdegree_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, "associate's degree")
parental_education_bachelors_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, "bachelor's degree")
parental_education_masters_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_parental_education, "master's degree")

parental_education_some_college_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, 'some college')
parental_education_high_school_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, 'high school')
parental_education_some_high_school_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, 'some high school')
parental_education_associatesdegree_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, "associate's degree")
parental_education_bachelors_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, "bachelor's degree")
parental_education_masters_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_parental_education, "master's degree")

female_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_gender, 'female')
male_average_math_score = find_average_score_by_specific_category_data_point(math_score_and_gender, 'male')

#female_math_score_average_values = [female_average_math_score , male_average_math_score]

female_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_gender, 'female')
male_average_reading_score = find_average_score_by_specific_category_data_point(reading_score_and_gender, 'male')

#female_reading_score_average_values = [female_average_reading_score , male_average_reading_score]

female_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_gender, 'female')
male_average_writing_score = find_average_score_by_specific_category_data_point(writing_score_and_gender, 'male')

#female_writing_score_average_values = [female_average_writing_score , male_average_writing_score]

test_preparation_math_score_none = find_average_score_by_specific_category_data_point(math_score_and_test_preparation, 'none')
test_preparation_math_score_completed = find_average_score_by_specific_category_data_point(math_score_and_test_preparation, 'completed')

test_preparation_reading_score_none = find_average_score_by_specific_category_data_point(reading_score_and_test_preparation, 'none')
test_preparation_reading_score_completed = find_average_score_by_specific_category_data_point(reading_score_and_test_preparation, 'completed')

test_preparation_writing_score_none = find_average_score_by_specific_category_data_point(writing_score_and_test_preparation, 'none')
test_preparation_writing_score_completed = find_average_score_by_specific_category_data_point(writing_score_and_test_preparation, 'completed')


'''Sorts the dataset and calculates its median, handling both odd and even numbers of values'''
def find_median(lst):
    lst.sort()
    number_of_values = len(lst)
    if number_of_values % 2 != 0:
        #if n(number of values) is odd, then get the number in the middle(median)
        n_plus_one = number_of_values + 1
        median_position = n_plus_one / 2 #find position
        median_index = int(median_position) - 1 # Since indexing starts at 0, subtract 1 from the normal position
        median = lst[median_index]
    else:
        #if n(number of values) is even, then get the two middle values
        # and calculate their average to find the median
        median_position = number_of_values / 2 #find position
        first_middle_value = lst[int(median_position) - 1] 
        second_middle_value = lst[int(median_position)]
        median = (first_middle_value + second_middle_value) / 2

    return  median


math_score_median = find_median(math_score_data_ints)
reading_score_median = find_median(reading_score_data_ints)
writing_score_median = find_median(writing_score_data_ints)


'''Calculates standard deviation'''
'''The formula used is:
        σ = sqrt( Σ (x - μ)² / N )

    Notation definition:
        σ (Sigma)   = Standard Deviation
        μ (Mu)      = Mean value of the dataset
        x           = Individual data point
        Σ (Sigma)   = Summation of all points
        N           = Total number of data points (population size)'''

def standard_deviation(lst, mean):
    total_squared_deviations = 0

    for item in lst:
        #Calculate the deviations from the mean
        deviation = item - mean
        #Square the deviations
        squared_results = deviation ** 2
        #Sum the squared deviations to find variance
        total_squared_deviations += squared_results

    #Final calculation
    variance = total_squared_deviations / len(lst)
    std_deviation = math.sqrt(variance)

    return round(std_deviation, 2)

math_score_std_deviation = standard_deviation(math_score_data_ints, average_math_score)
reading_score_std_deviation = standard_deviation(reading_score_data_ints, average_reading_score)
writing_score_std_deviation = standard_deviation(writing_score_data_ints, average_writing_score)

def muliply_lst_items(lst1, lst2):
    result = []

    for i in range(len(lst1)):
        result.append(lst1[i] * lst2[i])

    return result 

def find_slope_and_intercept(lst1, lst2, mean_x, mean_y):

    """Calculate the slope (a) and y-intercept (b) for linear regression (y = ax + b).

    Formulas:
        numerator   = Σ((x_i - x̄) * (y_i - ȳ))
        denominator = Σ((x_i - x̄)²)
        
        a = numerator / denominator
        b = ȳ - (a * x̄)"""
    
    '''Find slope'''
    dist_x = []
    dist_y = []

    for score in lst1:
        '''(\(x_i - \bar{x}\))'''
        distance_x = score - mean_x
        dist_x.append(distance_x)
    for score in lst2:
        '''(\(y_i - \bar{y}\))'''
        distance_y = score - mean_y
        dist_y.append(distance_y)

    #Calculates numerator
    multiplied_distances = muliply_lst_items(dist_x, dist_y)

    sum_it = 0
    for i in range(len(multiplied_distances)):
        sum_it = sum_it + multiplied_distances[i]

    #Calc denominator. Square Subject A distance
    squared_distance_subject_A_total = 0
    squared_distance_subject_A = muliply_lst_items(dist_x, dist_x)
    for i in range(len(squared_distance_subject_A)):
            squared_distance_subject_A_total = squared_distance_subject_A_total + squared_distance_subject_A[i] 

    slope_a = sum_it / squared_distance_subject_A_total
    '''b = ȳ - (a * x̄)'''

    intercept = mean_y - slope_a * mean_x

    
    return round(slope_a, 2) , round(intercept, 2)

    
slope, intercept = find_slope_and_intercept(math_score_data_ints, reading_score_data_ints, average_math_score, average_reading_score)

'''Linear regression'''
def linear_regression(x, alpha, beta):
    predicted_value = alpha * x + beta
    return predicted_value

#Generate predicted reading scores
predicted_reading_scores = []

for x in math_score_data_ints:
    y = linear_regression(x, intercept, slope)
    predicted_reading_scores.append(y)

#Print predicted scores
for score in predicted_reading_scores:
    print(round(score, 2))

'''Create scatter plot'''
slope, intercept, r, p, std_err = stats.linregress(math_score_data_ints, reading_score_data_ints)

def predicted_score(x):
  return slope * x + intercept

mymodel = list(map(lambda x: linear_regression(x,slope, intercept), math_score_data_ints))

plt.scatter(math_score_data_ints, reading_score_data_ints)
plt.plot(math_score_data_ints, mymodel)
plt.xlabel("Math scores")
plt.ylabel("Reading scores")
plt.title("Linear Regression: Math vs Reading Scores")
plt.show() 


'''Make descriptives table using matplotlib'''
list_of_descriptives = [[average_math_score,
                        average_reading_score,
                        average_writing_score], 
                        [math_score_median, 
                        reading_score_median, 
                        writing_score_median], 
                        [math_score_std_deviation, 
                        reading_score_std_deviation, 
                        writing_score_std_deviation]]

row_labels = ['Mean', 'Median', 'Standard Deviation']
col_labels = ['Math', 'Reading', 'Writing']

table = plt.table(cellText=list_of_descriptives, rowLabels=row_labels, colLabels=col_labels, loc='center')
plt.axis('off')
plt.show()


'''Create bar graph showing average scores by subject and gender'''

#Define categories and their corresponding values for two groups
categories = ['Math', 'Reading', 'Writing']
values1 = [
    female_average_math_score,
    female_average_reading_score,
    female_average_writing_score]

values2 = [
    male_average_math_score,
    male_average_reading_score,
    male_average_writing_score
]

#Set the width of the bars 
bar_width = 0.23
# Calculating bar positions for both groups
bar_positions1 = np.arange(len(categories))
bar_positions2 = bar_positions1 + bar_width

#Create the first set of bars (Group 1)
plt.bar(bar_positions1, values1, width=bar_width, label='Female', color='purple')
#Create the second set of bars (Group 2) next to the first set
plt.bar(bar_positions2, values2, width=bar_width, label='Male', color='skyblue')

# Adding labels to the axes
plt.xlabel("Exam Subject")
plt.ylabel("Average Score")
plt.title("Average Exam Performance by Gender")
plt.xticks(bar_positions1 + bar_width / 2, categories)
# Adding a title to the graph
plt.title('Average Exam Scores by Gender and Subject')

#Display a legend to identify the groups
plt.legend()

#Show the plot
plt.show()

#Define categories
education_categories = [
    "Some college",
    "High school",
    "Some high school",
    "Associate's degree",
    "Bachelor's degree",
    "Master's degree"
]

#Average math scores
parental_education_math_score_average_values = [
    parental_education_some_college_average_math_score,
    parental_education_high_school_average_math_score,
    parental_education_some_high_school_average_math_score,
    parental_education_associatesdegree_average_math_score,
    parental_education_bachelors_average_math_score,
    parental_education_masters_average_math_score
]

#Average reading scores
parental_education_reading_score_average_values = [
    parental_education_some_college_average_reading_score,
    parental_education_high_school_average_reading_score,
    parental_education_some_high_school_average_reading_score,
    parental_education_associatesdegree_average_reading_score,
    parental_education_bachelors_average_reading_score,
    parental_education_masters_average_reading_score
]

#Average writing scores
parental_education_writing_score_average_values = [
    parental_education_some_college_average_writing_score,
    parental_education_high_school_average_writing_score,
    parental_education_some_high_school_average_writing_score,
    parental_education_associatesdegree_average_writing_score,
    parental_education_bachelors_average_writing_score,
    parental_education_masters_average_writing_score
]

#Set the width of the bars
bar_width = 0.23

#Calculate bar positions
bar_positions1 = np.arange(len(education_categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width

#Create the bars
plt.bar(bar_positions1, parental_education_math_score_average_values,
        width=bar_width, label='Math', color='#245C43')

plt.bar(bar_positions2, parental_education_reading_score_average_values,
        width=bar_width, label='Reading', color='#70A88A')

plt.bar(bar_positions3, parental_education_writing_score_average_values,
        width=bar_width, label='Writing', color='#B5D6BE')

#Add labels to the axes
plt.xlabel("Parental Education Level")
plt.ylabel("Average Score")

#Add the chart title
plt.title("Average Exam Performance by Parental Education Level")

#Position the category labels
plt.xticks(bar_positions1 + bar_width, education_categories,
           rotation=20, ha='right')

#Display the legend
plt.legend()

#Adjust the layout
plt.tight_layout()

#Show the plot
plt.show()


test_preparation_categories = ["completed" , "none"]

#Average math scores
test_preparation_average_math_score = [
    test_preparation_math_score_completed,
    test_preparation_math_score_none,
]

test_preparation_average_reading_score = [
    test_preparation_reading_score_completed,
    test_preparation_reading_score_none
]

test_preparation_average_writing_score = [
    test_preparation_writing_score_completed,
    test_preparation_writing_score_none
]


#Set the width of the bars
bar_width = 0.15

#Calculate bar positions
bar_positions1 = np.arange(len(test_preparation_categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width

#Create the bars
plt.bar(bar_positions1, test_preparation_average_math_score,
        width=bar_width, label='Math', color='#9966CC')

plt.bar(bar_positions2, test_preparation_average_reading_score,
        width=bar_width, label='Reading', color='#8F00FF')

plt.bar(bar_positions3, test_preparation_average_writing_score,
        width=bar_width, label='Writing', color='#4B0082')

#Add labels to the axes
plt.xlabel("Test Preparation")
plt.ylabel("Average Score")

#Add the chart title
plt.title("Average Exam Performance by Test Preparation")

#Position the category labels
plt.xticks(bar_positions1 + bar_width, test_preparation_categories,
           rotation=20, ha='right')

#Display the legend
plt.legend()

#Adjust the layout
plt.tight_layout()

#Show the plot
plt.show()


"""Data set link: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams/data"""