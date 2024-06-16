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


def meymayakkam1(word):
    letters=tamil.utf8.get_letters(word)
    if "க்" in letters and letters.index("க்")!=len(letters)-1:
        return meymayakkam_checker(letters, "க்", ["க்"])
    else:
		    return None
		    
