"""Tense Transformation — English
So far, only for conversion of Affirmative sentences from Simple Present to Simple Past Tense.
Structure: Subject (article + noun only) + verb (v1) + object + rest of sentence."""
import csv

# Subject + verb(v1) + object. --Present Affirmative Sentences
# Subject + verb(v2) + object --Past Affirmative Sentences

def get_base_form(verb):
    """Reverse third-person-singular present tense formation to recover the base verb."""
    global subject_is_plural
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

with open("irregular_verbs_list.csv", "r", newline="") as f:
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
    
    # sentence = list(map(lambda x: x.lower(), sentence))
    # sentence = [string.lower() for string in sentence]

    # with open("prepositions.txt", "r") as f:
    #     prepositions = f.read().splitlines()
    # for i in prepositions:
    #     if sentence[1] == i:
    #         sentence[1]

    for i, j in enumerate(sentence):
        if j == "today":
            sentence[i] = 'that day'
        elif j == "now":
            sentence[i] = 'then'
        elif j=="tomorrow":
            sentence[i] = 'the next day'
        elif j=="yesterday":
            sentence[i] = 'the day before'

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

