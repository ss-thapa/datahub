import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_column', None)


courses = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/courses.csv')
students = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/students.csv')

nov = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/reg-month1.csv')
dec = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/reg-month2.csv')

matches = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/matches.csv')
delivery = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/deliveries.csv')



regs = pd.concat([nov,dec]).reset_index(drop=True)

## total revenue earned by the institute
total_revenue =regs.merge(courses, how='inner', on='course_id')['price'].sum()

## multi index dataframe
regs_multi_index = pd.concat([nov,dec], keys=['nov', 'dec']).reset_index()

regs_multi_index = regs_multi_index.merge(courses, on='course_id')

revenue_accordint_to_month = regs_multi_index.groupby('level_0')['price'].sum()



## merging 3 tables and extracting desired 3 columns only

new_df = regs.merge(students, on='student_id').merge(courses, on= 'course_id')[['name', 'course_name', 'price']]



#merging the two table and plotting the sum of price of total courses
# one way
# total_courses_enroll = regs.merge(courses, on='course_id').groupby('course_name').agg(sum_price=('price', 'sum')).reset_index()

# sns.catplot(data=total_courses_enroll, x='course_name', y='sum_price', kind='bar')
# plt.show()


#another way

# regs.merge(courses, on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')
# plt.show()



##find the students who have enrolled in the both month


# both_month_stu = nov.merge(dec, how='inner', on='student_id').groupby('student_id').count()

# Student_enrolled_both_month = both_month_stu.merge(students, on='student_id')[['student_id', 'name']]


## find the courses in which on enrollment happened

all_coureses_with_students = regs.merge(courses, how='right', on='course_id')
courses_empty = all_coureses_with_students[all_coureses_with_students['student_id'].isna()].reset_index()


##students who did not enroll into any courses

# all_student_with_course = regs.merge(students, on='student_id', how='right')

# all_student_without_course = all_student_with_course[all_student_with_course['course_id'].isnull()].reset_index()


## create a new table with student name and its partner name (using self join)

# student_with_partner = students.merge(students, how='inner', left_on='partner', right_on='student_id')[['name_x', 'name_y']]



## top 3 students who did most number of enrollments

# print(regs.merge(students, on='student_id').groupby(['student_id', 'name'])['name'].count().sort_values(ascending=False).head(3))

##or 

# sun = regs.groupby('student_id').agg(count_num = ('course_id', 'count'))

# print(sun.merge(students, on='student_id')[['name', 'count_num']].sort_values(by='count_num', ascending=False).head(3))



### top 3 student who have spent most money

# total_tables = regs.merge(students, on="student_id").merge(courses, on='course_id')

# print(total_tables.groupby(['student_id', 'name']).agg(total_sum=('price', 'sum')).sort_values(by='total_sum', ascending=False).head(3))



total_table = delivery.merge(matches, left_on='match_id', right_on='id')

# six_table = total_table[total_table['batsman_runs']== 6]

# num_sixs = six_table.groupby('venue')['venue'].count()

# num_matches = matches['venue'].value_counts()
# print((num_sixs/num_matches).sort_values(ascending=False).head(3))



print(total_table.groupby(['season', 'batsman'])['batsman_runs'].sum().reset_index().sort_values(by='batsman_runs', ascending=False).drop_duplicates(subset=['season'], keep='first').sort_values(by='season'))

print(total_table.groupby(['season', 'batsman'])['batsman_runs'].sum().reset_index().sort_values(by='batsman_runs', ascending=False).first('season'))


