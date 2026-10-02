"""Tense Transformation — English
So far, only for conversion of Affirmative sentences their present tense to past or future ones.
Structure: Subject (article + noun only) + verb (v1) + object + rest of sentence.
NOTE: Only affirmative sentences are supported. 100% accuracy is not guaranteed. The program is still in development, more features will be added soon. Avoid using compound subjects.
Tense options: past or future"""
import csv
import sys
import os

# Subject + verb(v1) + object. --Present Affirmative Sentences
# Subject + verb(v2) + object --Past Affirmative Sentences

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    """

    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_base_form(verb):
    """Reverse third-person-singular present tense formation to recover the base verb."""
    if verb == "has":
        return "have"
    if verb == "does":
        return "do"
    if verb == "goes":
        return "go"
    if verb in ("is", "am"):
        return "is"
    if verb == "are":
        return 'are'
    if verb.endswith(("sses", "shes", "ches", "xes", "zes", "oes")):
        return verb[:-2]    # washes -> wash
    if verb.endswith("ies") and len(verb) > 3:
        return verb[:-3] + "y"    # tries -> try
    if verb.endswith("s"):
        return verb[:-1]
    return verb 

with open(resource_path("irregular_verbs_list.csv"), "r", newline="") as f:
    reader = csv.reader(f, skipinitialspace=True)
    rows = [[field.strip() for field in row] for row in reader]

def is_plural_subject(subject_str):
    """Check if the subject is plural without misclassifying singular s-ending words."""
    subject_str = subject_str.lower().strip()
    
    if subject_str in ("they", "we", "you"):
        return True
        
    words = subject_str.split()
    noun = words[-1] #Target the noun 
    
    # known irregular plurals
    if noun in ("children", "people", "men", "women", "mice", "feet", "teeth"):
        return True
        
    # singular subjects ending in 's' / 'ss'
    if noun.endswith(("ss", "us", "is")):
        return False
        
    return noun.endswith("s")

irregular_verbs_past = {row[0]: row[1] for row in rows}
irregular_verbs_past_participle = {row[0]: row[2] for row in rows}

# The Subject
print(__doc__)

def program(user_input, tense="past"):
    input = user_input
    sentence = input.split(" ")

    if sentence[0].lower() in ("the", "a", "an") and len(sentence) > 1:
        sentence[0] = sentence[0] + " " + sentence[1]
        sentence.pop(1)


    # Improved system for time adverbials.
    for i, token in enumerate(sentence):
        clean_word = token.rstrip(",.?!")
        punctuation = token[len(clean_word):]
        
        if clean_word == "today":
            sentence[i] = "that day" + punctuation
        elif clean_word == "now":
            sentence[i] = "then" + punctuation
        elif clean_word == "tomorrow":
            sentence[i] = "the next day" + punctuation
        elif clean_word == "yesterday":
            sentence[i] = "the day before" + punctuation

    if not sentence[len(sentence)-1].endswith("."):
        sentence[len(sentence)-1] = sentence[len(sentence)-1] + "."

    # Verb transformation
    verb = sentence[1].strip(",.?!")
    base = get_base_form(verb)

    if base in irregular_verbs_past:
        converted_form = irregular_verbs_past[base] if tense == "past" else irregular_verbs_past_participle[base]
    else:
        if base.endswith("e"):
            converted_form = base + "d"
        elif base.endswith("y") and len(base) > 1 and base[-2] not in "aeiou":
            converted_form = base[:-1] + "ied"
        else:
            converted_form = base + "ed"

    if converted_form =="was" and is_plural_subject(sentence[0]):
        converted_form = "were"

    sentence[1] = converted_form

    transformed_sentence = " ".join(sentence)+"." if not sentence[-1].endswith(".") else " ".join(sentence)
    transformed_sentence = transformed_sentence.capitalize()
    return transformed_sentence


if __name__ == "__main__":
    transformed_sentence = program(input("Enter a sentence:\n"))
    print(transformed_sentence)

