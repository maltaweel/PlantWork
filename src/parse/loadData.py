'''
Created on Jun 1, 2020

@author: mark
'''
import os
import csv

class LoadData:
    
    def loadPath(self):
        
        pn=os.path.abspath(__file__)
        pn=pn.split("src")[0]
        

        #The data file path is now created where the data folder and dataFile.csv is referenced
        path=os.path.join(pn,'data')
        
        return path
    
    
    def readFile(self,location):
        
        self.sites=[]
        self.sites_phases={}
        self.domestic={}
        self.proportion={}
        self.ubiquity={}
        
        location=os.path.join(location,'ademnes_export_samples_flora.csv')
        
        
        with open(location,encoding = "ISO-8859-1", mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
 
                for row in reader:
                    
                    site=row['Site']
                    
                    if site not in self.sites:
                        self.sites.append(site)
                    
                    
                    phaseS=row['Phase'].split("_")
                    phase=""
                    if len(phaseS) > 1:
                        phase=phaseS[1]
                    
                       
                    site_phase=site+":"+phase
                            
                    taxon=row['Taxon']
                    taxa=[]
                    
                    if site_phase in self.sites_phases.keys():
                        taxa=self.sites_phases[site_phase]
                    
                    site_p_taxon=site+":"+phase+":"+taxon
                    if taxon not in taxa:
                        taxa.append(taxon)
                                
                    self.sites_phases[site_phase]=taxa
                    
                    family=row['Family']
                    genus=row['Genus']
                    
                    domestic_wild=row['domestic_wild']
                    prop=row['Proportion_per_Phase']
                    ubquity=row['Ubquity']
                    
                    self.domestic[site_p_taxon]=domestic_wild
                    self.proportion[site_p_taxon]=prop
                    self.ubiquity[site_p_taxon]=ubquity
                    
                    print(self.ubiquity[site_p_taxon])
    
    
    def outputPlants(self):
        
        path=self.loadPath()
       

    def run(self):
        path=self.loadPath()
        self.readFile(path)
        
    
    
if __name__ == '__main__':
    ld=LoadData()
    ld.run()                  
                    
            