import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

image1=[]
image2=[]
image3=[]
def socioeconomic_plots(dataframe = ["parameters", "externalinternal","externalexternal"]):
    cordon_defination = pd.read_csv("cordon_definition.csv") 
    dictonary = {i+1 : j for i,j in enumerate(cordon_defination.Name)}
    if dataframe == "externalinternal":        
        dataframe = pd.DataFrame(pd.read_csv("OLD_externalinternalControlTotals_by_year.csv")).pivot_table(['year','work','nonwork'],
								index = 'year', columns = 'taz')
        while True:
            string = str(input("Enter the Category (work / nonwork): - ")).lower()
            if string in ['work', 'nonwork'] :
                i = int(input("Enter the required taz number: - "))
                if string != " " and i in dataframe[(string)]:
                    fig = plt.figure()
                    plt.plot(dataframe.index, dataframe[(string,i)], '-p', color = 'gray',
                                                        markersize = 10, linewidth = 4,
                                                        markerfacecolor = 'black',
                                                        markeredgecolor = 'black') 
                    plt.title("{}".format(string.capitalize())+"ers in {} from 2010 to 2050".format(dictonary[i]))
                    plt.xlabel('Years')
                    plt.ylabel('{} in {}'.format(string,dictonary[i]))
                    plt.show()
                    fig.savefig("{}_vs_{}.png".format(string,dictonary[i]))
                    image1.append("{}_vs_{}.png".format(string,dictonary[i]))
            elif string in ["", "stop","exit"] :
                    return "Thank You. Task Completed"
            else:
                    print("please provide the correct input.")
                    break
                    
    elif dataframe == 'parameters':
        dataframe = pd.DataFrame(pd.read_csv("OLD_parameters_by_years.csv")); 
        dataframe.columns = ["year", "auto_fuel_cost","auto_maintenance_cost","airport_enplanements_passengers","airport_connecting_passengers","crossborder_tours" ]
        while True:
            i = input("Please enter any input from {} :-".format(dataframe.iloc[:,1:6].columns)).lower()
            if i in dataframe.iloc[:,1:6].columns:
                fig = plt.figure()
                plt.plot(dataframe.year,dataframe[str(i)], '-p', color = 'gray',
                                                  markersize = 10, linewidth = 4,
                                                  markerfacecolor = 'black',
                                                  markeredgecolor = 'black')
                plt.title("{} by Years".format(i.capitalize()))
                plt.xlabel("Years")
                plt.ylabel(i)
                plt.show()
                fig.savefig("{}_by_Years.png".format(i.capitalize()))
                image2.append("{}_by_Years.png".format(i.capitalize()))
            elif i in ["", "exit", "stop"]:
                return "Task Completed."
            else:
                print("Please enter the correct inputs.")
                
    elif dataframe == 'externalexternal':
        dataframe = pd.DataFrame(pd.read_csv("OLD_externalExternalTrips_by_year.csv")).pivot_table(index = 'year', columns = ['originTaz', 'destinationTaz'])
        while True:
            i = int(input("Please Enter the Origin Taz Number: - "))
            j = int(input("Please Enter the Destination Taz Number: - "))
            if i not in range(1,13) and j in range(1,13):
                return "you are entering the wrong input"
                
            elif i == 0 or j == 0:
                return "Task Completed"
            else:
                fig = plt.figure()
                plt.plot(dataframe.index, dataframe[("Trips",i,j)], '-p',
                                                    color = 'gray',
                                                    markersize = 10, linewidth = 4,
                                                    markerfacecolor = 'black',
                                                    markeredgecolor = 'black')
                plt.xlabel("Years")
                plt.ylabel("Number of Trips.")
                plt.title("{} to {}".format(dictonary[i],dictonary[j]))
                plt.show()
                plt.savefig("{}_vs_{}.png".format(dictonary[i],dictonary[j]))
                image3.append("{}_vs_{}.png".format(dictonary[i],dictonary[j]))
    else:
        print("Please enter the valid Data Set (parameter, externalinternal, externalexternal)")


         
from fpdf import FPDF
image1.extend(image2)
def multipage_simple():
    pdf = FPDF()
    pdf.set_font("Arial", size = 12)
    pdf.add_page()
#    pdf.image('work_vs_I-5 cordon.png')
#    pdf.image('work_vs_I-8 cordon.png')
    for i in image1:
        pdf.image("{}".format(i))
#    for j in image2:
#        pdf.image("{}".format(j))
    pdf.output("multipage_simple.pdf")


if __name__ == '__main__':
    multipage_simple()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        