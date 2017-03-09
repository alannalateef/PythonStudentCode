def gui():
    samples=3#number of sample texts to be used
    language=['French','French','French','French','French']#contains list of languages that will be compared selected by user
    return samples, language

def translate(language,baselang):
    
    for z in baselang:
    #z will be the text to be translated into a languague in lang variable
    #will need to have a dictionary somewhere to convert from a language selected to a language code
        q=['hgfghf','oihih','hgkjhg','oihih','hgkjhg']

    return q

def stats(baselang,files,tran,language):
    #import numpy and matplot
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    #creates empty lists for word and character counting
    baselength=[] #characters in a given sample
    baseword=[] #words defined by spaces per sample (#spaces+1)
    tranlength=[]
    tranword=[]


    #counts length of samples in the base language-english
    for q in baselang:
        baselength.append(len(q))
        baseword.append(len(q.split(' ')))      


    #counts length of each sample for each target language
    for lang in tran:
        for samp in lang:
            tranlength.append(len(samp))
            tranword.append(len(q.split(' ')))
            
    #Changes lists of length values into numpy arrays for calculations
    #These arrays have rows containing the value for a given language
    #Colums correspond to the length for a given text sample
    tranlength=np.array(tranlength).reshape(len(language),len(files))
    tranword=np.array(tranword).reshape(len(language),len(files))
    baselength=np.array(baselength)
    baseword=np.array(baseword)

    #Creates zero arrays to store ratio of lengths between translated
    #and base texts
    tranlratio=np.zeros((len(tran),len(files)))
    tranwratio=np.zeros((len(tran),len(files)))
    
    #Creates arrays of the ratio between the target language and base language
    iteration=-1
    for row in tranlength:
        iteration=iteration+1
        for a in range(len(row)):
            tranlratio[iteration,a]=a/baselength[a]
            tranwratio[iteration,a]=a/baseword[a]

    #Calculate Stats
    avgl=np.average(tranlratio,axis=1)
    avgw=np.average(tranwratio,axis=1)
    stdevl=np.std(tranlratio,axis=1)
    stdevw=np.std(tranwratio,axis=1)

    bplotl=[]
    bplotw=[]
    
    #Creates lists to make boxplots
    for row in tranlratio:
        bplotl.append(row)
    for row in tranwratio:
        bplotw.append(row)


    #Create Data Frame
    statistics = {'Avg Char. Count': pd.Series(avgl,index=language),'Avg Word Count': pd.Series(avgw,index=language),'Stdev. Character Count': pd.Series(stdevl,index=language),'Stdev. Word Count': pd.Series(avgw,index=language)}
    statistics = pd.DataFrame(statistics)

    return statistics, bplotl, bplotw
    
         
def main():
    
    samples,language=gui()
    
    #list of file names to be read from
    files=(['SampleText1.txt','SampleText2.txt','SampleText3.txt','SampleText4.txt','SampleText5.txt'])
    #creates empty list to store string data for base language
    baselang=[]
    i=0
    #reads in sample text and appends to base language list
    for s in files:
        text=open(s,'r')
        baselang.append(text.read())
    
    #goes through language list and translates base language samples into each
        #appends these translation lists to ‘tran’ list
    tran=[]
    for a in language:
        t=translate(a,baselang)
        tran.append(t)      

    t, bplotl, bplotw=stats(baselang,files,tran,language)
    print(t)

    #Creats Boxplots!!!
    import numpy as np
    import matplotlib.pyplot as plt
    plt.subplot(2,1,1)
    plt.boxplot(bplotl)
    plt.xticks((range(1,len(language)+1)),language)
    
    plt.subplot(2,1,2)
    plt.boxplot(bplotw)
    plt.xticks((range(1,len(language)+1)),language)
    
    plt.show()
main()
