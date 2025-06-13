import pandas as pd
dataset = pd.read_csv('CET_Database_Final2021.csv')
dataset2020 = pd.read_csv('CET_Database_Final2020.csv')
dataset2019 = pd.read_csv('CET_Database_Final2019.csv')

rank=0

#Maximum value of each
rank_max_1G = dataset['1G'].max()
rank_max_1K = dataset['1K'].max()
rank_max_1R = dataset['1R'].max()
rank_max_2AG = dataset['2AG'].max()
rank_max_2AK = dataset['2AK'].max()
rank_max_2AR = dataset['2AR'].max()
rank_max_2BG = dataset['2BG'].max()
rank_max_2BK = dataset['2BK'].max()
rank_max_2BR = dataset['2BR'].max()
rank_max_3AG = dataset['3AG'].max()
rank_max_3AK = dataset['3AK'].max()
rank_max_3AR = dataset['3AR'].max()
rank_max_3BG = dataset['3BG'].max()
rank_max_3BK = dataset['3BK'].max()
rank_max_3BR = dataset['3BR'].max()
rank_max_GM = dataset['GM'].max()
rank_max_GMK = dataset['GMK'].max()
rank_max_GMR = dataset['GMR'].max()
rank_max_SCG = dataset['SCG'].max() 
rank_max_SCK = dataset['SCK'].max()
rank_max_SCR = dataset['SCR'].max()
rank_max_STG = dataset['STG'].max()
rank_max_STK = dataset['STK'].max()
rank_max_STR = dataset['STR'].max()

#maximum value in the whole dataframe
rank_max = dataset.max(numeric_only=True).max()

#category input
category = input("Enter Your Category!\n")
while (rank<rank_max or rank>=0 or rank==int):
    try:
        rank = int(input("Enter Your Rank!\n"))
        if(rank>rank_max or rank<0 or rank==str):
            print("Exceeds rank limit! Please give valid input!")
        else:
            break
    except ValueError:
        print("Exceeds rank limit! Please give valid input!")
    
#Branch input
branch = input("Enter Your Branch!\n")

#sorting dataset based on category
if category=='1G':
    i=4;
    dataset = dataset.sort_values('1G')    

if category=='1K':
    i=5; 
    dataset = dataset.sort_values('1K') 
    
if category=='1R':
    i=6;
    dataset = dataset.sort_values('1R') 
    
if category=='2AG':
    i=7;
    dataset = dataset.sort_values('2AG') 

if category=='2AK':
    i=8;
    dataset = dataset.sort_values('2AK') 

if category=='2AR':
    i=9;
    dataset = dataset.sort_values('2AR') 

if category=='2BG':
    i=10;
    dataset = dataset.sort_values('2BG') 

if category=='2BK':
    i=11;
    dataset = dataset.sort_values('2BK') 
    
if category=='2BR':
    i=12;
    dataset = dataset.sort_values('2BR') 
    
if category=='3AG':
    i=13;
    dataset = dataset.sort_values('3AG') 
    
if category=='3AK':
    i=14;
    dataset = dataset.sort_values('3AK')
    
if category=='3AR':
    i=15;
    dataset = dataset.sort_values('3AR')
    
if category=='3BG':
    i=16;
    dataset = dataset.sort_values('3BG')
    
if category=='3BK':
    i=17;
    dataset = dataset.sort_values('3BK')
    
if category=='3BR':
    i=18;
    dataset = dataset.sort_values('3BR')
    
if category=='GM':
    i=19;    
    dataset = dataset.sort_values('GM')

if category=='GMK':
    i=20;    
    dataset = dataset.sort_values('GMK')

if category=='GMR':
    i=21;    
    dataset = dataset.sort_values('GMR')
    
if category=='SCG':
    i=22;    
    dataset = dataset.sort_values('SCG')
    
if category=='SCK':
    i=23;    
    dataset = dataset.sort_values('SCK')
    
if category=='SCR':
    i=24;    
    dataset = dataset.sort_values('SCR')
    
if category=='STG':
    i=25;    
    dataset = dataset.sort_values('STG')
    
if category=='STK':
    i=26;    
    dataset = dataset.sort_values('STK')
    
if category=='STR':
    i=27;    
    dataset = dataset.sort_values('STR')
    

dataset2 = dataset.iloc[:,[1,2,3,30,(i+2)]]

#fetching colleges based on the attributes given
if(rank!=0):
    dataset3 = dataset2.loc[(dataset2[category]>=rank) & (dataset2['Branch']== branch)]
elif(rank==0):
    dataset3 = dataset2.loc[(dataset2[category]>rank) & (dataset2['Branch']== branch)]
    
dataset3 = dataset3.reset_index(drop=True)
dataset3.index += 1
#top 10 colleges based on attributes are fetched
dataset3 = dataset3.head(10)

#college codes of top 10 colleges are stored in list
my_list = dataset3["Code"].tolist()

#ranks of those 10 colleges for the year 2020 is fetched
dataset6 = []
for j in range(len(my_list)): 
    dataset5 = dataset2020[dataset2020['Code']== my_list[j]]
    dataset5 = dataset5[dataset2020['Branch']== branch]
    dataset5 = dataset5[category].tolist()
    dataset6.append(dataset5)

#ranks of those 10 colleges for the year 2020 is fetched
dataset10 =[]
for j in range(len(my_list)): 
    dataset7 = dataset2019[dataset2019['Code']== my_list[j]]
    dataset7 = dataset7[dataset2019['Branch']== branch]
    dataset7 = dataset7[category].tolist()
    dataset10.append(dataset7)

dataset3["2020"] = dataset6
dataset3["2019"] = dataset10

print(dataset3)
