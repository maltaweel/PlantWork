'''
Created on Jun 2, 2020

@author: mark
'''

import os
import csv

sites=[]
sites_phases={}
domestic={}
proportion={}
ubiquity={}

def loadPath():
        
    pn=os.path.abspath(__file__)
    pn=pn.split("src")[0]
        

    #The data file path is now created where the data folder and dataFile.csv is referenced
    path=os.path.join(pn,'data')
        
    return path

 
def mergeData():
        
    data=[]
    location=loadPath()
        
    files=os.listdir(location)
    
    for f in files:
        with open(os.path.join(location,f),encoding = "ISO-8859-1", mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
 
                for row in reader:
                    line={}
                    line['Site']=row['Site']
                    line['Phase']=row['Phase']
                    line['Taxon']=row['Taxon']
                    line['Family']=row['Family']
                    line['Genus']=row['Genus']
                    line['domestic_wild']=row['domestic_wild']
                    line['Proportion_per_Phase']=row['Proportion_per_Phase']
                    line['Ubquity']=row['Ubquity']
                    line['Period']=row['Period']
                    data.append(line)
    return data    
                    
 
def printData(data):  
    pn=os.path.abspath(__file__)
    pn=pn.split("src")[0]
    
    pathway=os.path.join(pn,'output','merged_flora_data.csv')
    
    fieldnames = ["Site","Phase","Taxon","Family","Genus","Domestic_Wild","Proportion_per_Phase","Ubquity","Period"]
    #print results out
    try:
        with open(pathway, 'w') as csvf:
             
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for d in data:
                writer.writerow({'Site': str(d['Site']),'Phase':str(d['Phase']),
                        'Taxon':str(d['Taxon']),'Family':str(d['Family']),'Genus':str(d['Genus']),
                        'Domestic_Wild':str(d['domestic_wild']),'Proportion_per_Phase':str(d['Proportion_per_Phase']),
                        'Ubquity':str(d['Ubquity']),'Period':str(d['Period'])})
    
    except IOError:
        print ("Could not read file:", IOError)                     
                    
def run():
    data=mergeData()
    printData(data)
    
if __name__ == '__main__':
    run()                  
               