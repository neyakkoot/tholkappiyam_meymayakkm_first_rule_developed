from meymayakkamfinal1 import *
#import matplotlib.pyplot as plt
#from matplotlib import font_manager
#import plotly.express as px

மொத்தம் = 0
செயல்முறைக்குள்ளாக்கு = 0
சரியான_சொற்கள் = 0 
தவறான_சொற்கள் = 0 
ஆய்விற்குட்படாச்சொற்கள் = 0 


#golden_words = []
#golden_words_file= open("golden_words.txt","r").readlines()
#for line in golden_words_file:
#    golden_words.append(line.strip())
    

rulesets = [meymayakkam1, meymayakkam2, meymayakkam3, meymayakkam4, meymayakkam5, meymayakkam6, meymayakkam7, meymayakkam8, meymayakkam9, meymayakkam10, meymayakkam11, meymayakkam12, meymayakkam13, meymayakkam14, meymayakkam15, meymayakkam16, meymayakkam17, meymayakkam18, meymayakkam19]

def rule_tagger(datalist):
    output_str = ""
    counter = 1
    for item in datalist:
        if item == True:
            output_str+=f"meymayakkam{counter}-"
        counter+=1
    return output_str


with open("dateset_meimayakkam_spelll2024_1.txt", "r") as myfile, open("சரியான_சொற்கள்.txt", 'w') as correctfile, open('தவறான_சொற்கள்.txt', 'w') as wrongfile, open('ஆய்விற்குட்படா_சொற்கள்.txt', 'w') as ommitedfile :
    for line in myfile.readlines():
        line = line.replace("\n","")
        மொத்தம்+=1
        if len(line.split())>1 or len(line.split("_"))>1:
            continue
        if len(line)==1:
            continue
        try:
            result = []
            for rule in rulesets:
                result.append(rule(line))

            if any(result):
                correctfile.write(line)
                correctfile.write(",")
                correctfile.write(rule_tagger(result))
                correctfile.write("\n")
                சரியான_சொற்கள்+=1


            elif result.count(False)>=1:
                wrongfile.write(line)
                wrongfile.write("\n")
                தவறான_சொற்கள்+=1


            elif result.count(None)==len(result):
                ommitedfile.write(line)
                ommitedfile.write("\n")
                ஆய்விற்குட்படாச்சொற்கள்+=1

        except ValueError:
            continue
        செயல்முறைக்குள்ளாக்கு+=1

print("சொற்தரவில் உள்ள சொற்களின் எண்ணிக்கை: ",மொத்தம்) 
print("ஓரெழுத்து, ஈரெழுத்துச் சொற்களின் எண்ணிக்கை: ", மொத்தம்-செயல்முறைக்குள்ளாக்கு)
print("மெய்மயக்கம் விதியின்படி சரியான சொற்களின் எண்ணிக்கை : ", சரியான_சொற்கள்)
print("மெய்மயக்கம் விதியின்படி தவறான சொற்களின் எண்ணிக்கை  :",தவறான_சொற்கள்)
print("மெய்மயக்கம் விதியின்படி பொருந்தாத சொற்களின் எண்ணிக்கை : ", ஆய்விற்குட்படாச்சொற்கள்)


# பை படம் வரைதல்

labels = ['மொத்தம்', 'செயல்முறைக்குள்ளாக்கு', 'சரியான_சொற்கள்', 'தவறான_சொற்கள்', 'ஆய்விற்குட்படாச்சொற்கள்']

வரைபடமதிப்பீடு = [மொத்தம், செயல்முறைக்குள்ளாக்கு, சரியான_சொற்கள், தவறான_சொற்கள், ஆய்விற்குட்படாச்சொற்கள்]



 
#fig = px.pie(values=வரைபடமதிப்பீடு, names=labels)
#fig.show()
