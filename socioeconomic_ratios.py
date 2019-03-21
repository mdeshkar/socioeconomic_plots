import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def socioeconomic_ratios():
    mgra_b = pd.read_csv("mgra13_based_input2012.csv")
    mgra_sb = pd.read_csv("mgra13_based_input2012_sb.csv")
    households = pd.read_csv("households.csv")
    persons = pd.read_csv("persons.csv")
    
    # Manupulating the variables of interest
    cs = [1 if x == 2 else 0 for x in persons.PSTUDENT]
    ss = [1 if x == 1 else 0 for x in persons.PSTUDENT]
    emp = [1 if x == 1 or x == 2 else 0 for x in persons.PEMPLOY ]

    df1 = pd.merge(pd.groupby(pd.DataFrame({"HHID": persons.HHID,
                                            "college_students": cs,
                                            "school_students": ss,
                                            "employed": emp}), by = "HHID", as_index = False, sort = True, group_keys = True).sum(), households, on = "HHID", sort = True)
    
    df2 = pd.groupby(pd.DataFrame({"taz": df1.TAZ,
                                   "mgra": df1.MGRA,
                                   "college_students": df1.college_students,
                                   "school_students": df1.school_students,
                                   "employed":df1.employed,
                                   "HWORKERS": df1.HWORKERS})
    ,by = "mgra" and "taz", as_index = False, sort = True)["college_students", "school_students","HWORKERS"].sum()
    
    df3 = pd.DataFrame({"mgra" : mgra_b.mgra,
                        "taz" : mgra_b.TAZ,
                        "school_enrollments": mgra_b.EnrollGradeKto8 + mgra_b.EnrollGrade9to12,
                        "college_enrollments": mgra_b.collegeEnroll + mgra_b.otherCollegeEnroll + mgra_b.AdultSchEnrl,
                        "emp_total": mgra_b.emp_total
                        })
    
    df4 = pd.groupby(df3, by = "mgra" and "taz", as_index = False, sort = True)["college_enrollments","school_enrollments", "emp_total"].sum()
    
    ############################################################################################################
    a = df4.school_enrollments.sum() / df2.school_students.sum()
    b = df4.college_enrollments.sum() / df2.college_students.sum()
    c = df4.emp_total.sum() / df2.HWORKERS.sum()
    
    ############################################################################################################
#    ratio = {"School_Enrollment to Number of Student": a, "College_Enrollment to College Students": b, "Employment to workers": c}
#    output = open("output.txt", 'w')
#    for i, j in ratio.items():
#        if 0.90 <= j <= 1.10:
#            output.write("The ratio for {} is {}.\n The ratio is within our expected threshold therefore we can proceed with this data.\n\n".format(i, round(j,2)))
#        else:
#            output.write("Ratio for {} is {}. We will have to recheck our data as \n it is not within our required threshold \n\n".format(i, round(j,2)))
#    output.close()
#    file = open("output.txt", "r")
#    return file.read()
#####################################################################################################
ratio = {"School_Enrollment to Number of Student": a, "College_Enrollment to College Students": b, "Employment to workers": c}
string = ""
for i, j in ratio.item():
    if 0.90 <= j <= 1.10:
        string + "The ratio for {} is {}.\n The ratio is within our expected threshold therefore we can proceed with this data.\n\n".format(i, round(j,2))
    else:
        string + "Ratio for {} is {}. We will have to recheck our data as \n it is not within our required threshold \n\n".format(i, round(j,2))

    