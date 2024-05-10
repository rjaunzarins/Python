# Code Fragment 1.1: A Python program that computes a GPA

print( '\nWelcome to the GPA calculator.' )
print( 'Please enter all your letter grades, one per line.' )
print( '\nEnter a blank line to designate the end.' )

# map from letter grade to point value
points = { 'A+' : 4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67, 'C+' :2.33, 
          'C' :2.0, 'C' : 1.67, 'D+' :1.33,'D' :1.0, 'F' :0.0 }
numCourses = 0
totalPoints = 0
done = False
while not done:
    grade = input( )								# read line from user
    if grade == '':									# empty line was entered
        done = True
    elif grade not in points:						    # unrecognized grade entered
        print( "Unknown grade '{0}' being ignored".format(grade) )
    else:
        numCourses += 1
        totalPoints += points[ grade ]
if numCourses > 0:									# avoid division by 0
    print( 'Your GPA is {0:.3}'.format( totalPoints / numCourses ) + '\n')