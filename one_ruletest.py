from meymayakkamfinal import *
#import matplotlib.pyplot as plt
#from matplotlib import font_manager
import numpy as np
import plotly.express as px

மொத்தம் = 0
செயல்முறைக்குள்ளாக்கு = 0
சரியான_சொற்கள் = 0 
தவறான_சொற்கள் = 0 
ஆய்விற்குட்படாச்சொற்கள் = 0 


golden_words = []
golden_words_file= open("golden_words.txt","r").readlines()
for line in golden_words_file:
    golden_words.append(line.strip())
    



with open("all-tamil-nouns.txt", "r") as myfile, open("சரியான_சொற்கள்.txt", 'w') as correctfile, open('தவறான_சொற்கள்.txt', 'w') as wrongfile, open('ஆய்விற்குட்படா_சொற்கள்.txt', 'w') as ommitedfile :
    for line in myfile.readlines():
        line = line.replace("\n","")
        மொத்தம்+=1
        if len(line.split())>1 or len(line.split("_"))>1:
            continue
        if len(line)==1:
            continue
        try:
            result = meymayakkam1(line)
            if result==None:
                ommitedfile.write(line)
                ommitedfile.write("\n")
                ஆய்விற்குட்படாச்சொற்கள்+=1

            elif result:
                if line in golden_words:
                    correctfile.write(line)
                    correctfile.write("\n")
                    சரியான_சொற்கள்+=1
                else:
                    wrongfile.write(line)
                    wrongfile.write("\n")
                    தவறான_சொற்கள்+=1

            elif result==False:
                wrongfile.write(line)
                wrongfile.write("\n")
                தவறான_சொற்கள்+=1
        except ValueError:
            continue
        செயல்முறைக்குள்ளாக்கு+=1

print("சொற்தரவில் உள்ள சொற்களின் எண்ணிக்கை: ",மொத்தம்) 
print("ஓரெழுத்து, ஈரெழுத்துச் சொற்களின் எண்ணிக்கை: ", மொத்தம்-செயல்முறைக்குள்ளாக்கு)
print("விதி1_ற்குட்பட்ட சொற்களின் எண்ணிக்கை: ", சரியான_சொற்கள்)
print("விதி1-ற்குட்படாத சொற்களின் எண்ணிக்கை: ",தவறான_சொற்கள்)
print("விதி1-ற்குப் பொருந்தாத சொற்களின் எண்ணிக்கை: ", ஆய்விற்குட்படாச்சொற்கள்)


# பை படம் வரைதல்

labels = ['மொத்தம்', 'செயல்முறைக்குள்ளாக்கு', 'சரியான_சொற்கள்', 'தவறான_சொற்கள்', 'ஆய்விற்குட்படாச்சொற்கள்']

வரைபடமதிப்பீடு = [மொத்தம், செயல்முறைக்குள்ளாக்கு, சரியான_சொற்கள், தவறான_சொற்கள், ஆய்விற்குட்படாச்சொற்கள்]



 
fig = px.pie(values=வரைபடமதிப்பீடு, names=labels)
fig.show()
