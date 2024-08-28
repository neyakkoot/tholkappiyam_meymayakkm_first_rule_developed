import tamil

# 1) க் + க
# ஒரு சொல்லில் க் எழுத்துக்குப் பின்பு க எழுத்து மயங்கி வரும். எ-டு. அக்கா, ஆக்கம்

#word=input("Enter the word to check: ")

def meymayakkam_checker(word_letters, letter, allowed_list, Mei=["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"] ): 
    ind=word_letters.index(letter)
    if word_letters[ind+1] in Mei:# Need to check on this point since some are overlapping. we can use sets here
	    return False
    else:
	    root_words=tamil.utf8.splitMeiUyir(word_letters[ind+1])
	    if type(root_words)==tuple:
		    root_last=root_words[0]
	    else:
		    root_last=root_words
	    if root_last in allowed_list: 
		    return True
	    else:
		    return False

#"மெய்ம்மயக்கம்1": "க்+க"
def meymayakkam1(word):
    letters=tamil.utf8.get_letters(word)
    if "க்" in letters and letters.index("க்")!=len(letters)-1:
        return meymayakkam_checker(letters, "க்", ["க்"])
    else:
		    return None
		    
#"மெய்ம்மயக்கம்2": "ங்+கங"
def meymayakkam2(word):
    letters=tamil.utf8.get_letters(word)
    if "ங்" in letters and letters.index("ங்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ங்", ["க்", "ங்"])
    else:
		    return None

#"மெய்ம்மயக்கம்3": "ச்+ச"
def meymayakkam3(word):
    letters=tamil.utf8.get_letters(word)
    if "ச்" in letters and letters.index("ச்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ச்", ["ச்"])
    else:
		    return None

#"மெய்ம்மயக்கம்4": "ஞ்+சஞய
def meymayakkam4(word):
    letters=tamil.utf8.get_letters(word)
    if "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ஞ்", ["ச்", "ஞ்", "ய்"])
    else:
		    return None

#"மெய்ம்மயக்கம்5": "ட்+கசடப"
def meymayakkam5(word):
    letters=tamil.utf8.get_letters(word)
    if "ட்" in letters and letters.index("ட்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ட்", ["க்", "ச்", "ட்", "ப்"])
    else:
		    return None

#"மெய்ம்மயக்கம்6": "ண்+கசஞடணபமயவ"
def meymayakkam6(word):
    letters=tamil.utf8.get_letters(word)
    if "ண்" in letters and letters.index("ண்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ண்", ["க்", "ச்", "ஞ்", "ட்", "ண்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்7": "த்+த"
def meymayakkam7(word):
    letters=tamil.utf8.get_letters(word)
    if "த்" in letters and letters.index("த்")!=len(letters)-1:
        return meymayakkam_checker(letters, "த்", ["த்"])
    else:
		    return None

#"மெய்ம்மயக்கம்8": "ந்+தநய"
def meymayakkam8(word):
    letters=tamil.utf8.get_letters(word)
    if "ந்" in letters and letters.index("ந்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ந்", ["த்", "ந்", "ய்"])
    else:
		    return None

#"மெய்ம்மயக்கம்9": "ப்+ப"
def meymayakkam9(word):
    letters=tamil.utf8.get_letters(word)
    if "ப்" in letters and letters.index("ப்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ப்", ["ப்"])
    else:
		    return None

#"மெய்ம்மயக்கம்10": "ம்+பமயவ"
def meymayakkam10(word):
    letters=tamil.utf8.get_letters(word)
    if "ம்" in letters and letters.index("ம்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ம்", ["ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்11": "ய்+கசதபஞநமயவங"
def meymayakkam11(word):
    letters=tamil.utf8.get_letters(word)
    if "ய்" in letters and letters.index("ய்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ய்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்12": "ர்+கசதபஞநமயவங"
def meymayakkam12(word):
    letters=tamil.utf8.get_letters(word)
    if "ர்" in letters and letters.index("ர்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ர்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்13": "ழ்+கசதபஞநமயவங"
def meymayakkam13(word):
    letters=tamil.utf8.get_letters(word)
    if "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ழ்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்14": "வ்+வ"
def meymayakkam14(word):
    letters=tamil.utf8.get_letters(word)
    if "வ்" in letters and letters.index("வ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "வ்", ["வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்15": "ல்+கசபலயவ"
def meymayakkam15(word):
    letters=tamil.utf8.get_letters(word)
    if "ல்" in letters and letters.index("ல்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ல்", ["க்", "ச்", "ப்", "ல்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்16": "ள்+கசபளயவ"
def meymayakkam16(word):
    letters=tamil.utf8.get_letters(word)
    if "ள்" in letters and letters.index("ள்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ள்", ["க்", "ச்", "ப்", "ள்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்17": "ற்+கசபற"
def meymayakkam17(word):
    letters=tamil.utf8.get_letters(word)
    if "ற்" in letters and letters.index("ற்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ற்", ["க்", "ச்", "ப்", "ற்"])
    else:
		    return None

#"மெய்ம்மயக்கம்18": "ன்+கசஞபமயவறன"
def meymayakkam18(word):
    letters=tamil.utf8.get_letters(word)
    if "ன்" in letters and letters.index("ன்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ன்", ["க்", "ச்", "ஞ்", "ப்", "ம்", "ய்", "வ்", "ற்", "ன்"])
    else:
		    return None
		    
def meymayakkam19(word):
	letters=tamil.utf8.get_letters(word)
	குறிலெழுத்துக்கள்=['அ', 'க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன', 'இ', 'கி', 'ஙி', 'சி', 'ஞி', 'டி', 'ணி', 'தி', 'நி', 'பி', 'மி', 'யி', 'ரி', 'லி', 'வி', 'ழி', 'ளி', 'றி', 'னி', 'உ', 'கு', 'ஙு', 'சு', 'ஞு', 'டு', 'ணு', 'து', 'நு', 'பு', 'மு', 'யு', 'ரு', 'லு', 'வு', 'ழு', 'ளு', 'று', 'னு', 'எ', 'கெ', 'ஙெ', 'செ', 'ஞெ', 'டெ', 'ணெ', 'தெ', 'நெ', 'பெ', 'மெ', 'யெ', 'ரெ', 'லெ', 'வெ', 'ழெ', 'ளெ', 'றெ', 'னெ', 'ஒ', 'கொ', 'ஙொ', 'சொ', 'ஞொ', 'டொ', 'ணொ', 'தொ', 'நொ', 'பொ', 'மொ', 'யொ', 'ரொ', 'லொ', 'வொ', 'ழொ', 'ளொ', 'றொ', 'னொ']
	
	if "ர்" in letters:
		ind=letters.index("ர்")
		if letters[ind-1] in குறிலெழுத்துக்கள்:
			print (False)
		else:
			print(True)
			
	elif "ழ்" in letters:
		ind=letters.index("ழ்")
		if letters[ind-1] in குறிலெழுத்துக்கள்:
			print (False)
		else:
			print(True)
	
