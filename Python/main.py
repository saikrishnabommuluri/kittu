#Importing the required libraries
import pandas as pd
import os


#Function to convert any dataframe into XML format
def to_xml(df):
    def row_xml(row):
        xml = ['<item>']
        for i, col_name in enumerate(row.index):
            xml.append('  <{0}>{1}</{0}>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)
    res = '\n'.join(df.apply(row_xml, axis=1))
    return(res)
1

#Function to merge all the csv files present in the data folder into 1 csv/XML/json file.
def process_extracts(path):
    csv_directory = os.listdir(path)
    f = []
    # To get the names and paths of all the files present in the data Folder
    print("These are the extracts present in the Data Folder:")
    for i in csv_directory:
        final_path = path + '\\' + i
        f.append(final_path)
        print(i,'\n')
    
    
    #Combining different csv files into a single dataFrame
    combined_csv_data = pd.concat([pd.read_csv(f) for f in f])
    
    #Generating the finalised csv file
    combined_csv_data.to_csv('Final_csv')
    
    # Genrating the finalised XML file
    with open('Final.XML', 'w') as f:
         f.write(to_xml(combined_csv_data))
            
    # Generating the finalised json file
    combined_csv_data.to_json('Final.json',orient='table')
    print('Finally generated the combination of the above files as unified file of csv,xml and json with names as  Final.csv, Final.XML and Final.json files')


def source():
    #Defining the required variables and dataframes     
    combined_csv_data = pd.DataFrame()
    str = ''
    #To get the current path
    c = os.getcwd()
    l = os.listdir(c)
    count = 0
    if 'Data' in l:
        count = 1
        str = l
    else:
        a = list(c.split('\\'))
        b = a[:len(a)-1]
        str = "\\".join(b)
        l = os.listdir(str)
        if 'Data' not in l:
            print("No Data folder forund which means none of the bank data we have received")
        else:
            count = 1
    if count == 1:
        print("We have found the Data folder where the different banks related data is usually available")
        str1 = str + '\\' + 'Data'
        m = os.listdir(str1)
    #To check if the data folder really contains any csv files
        if not m:
           print("There are no bank extracts in the data folder. So, we cannot generate a finalised csv now")
        else:
           n = len(m)
           print(f'We Have found {n} extracts in the data folder. We are about to generate a single extract')
           process_extracts(str1)


if __name__ == '__main__':
    # Calling the main source function
    source()






