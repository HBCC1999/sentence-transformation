"""Tense Transformation — English
So far, only for conversion of Affirmative sentences from Simple Present to Simple Past Tense.
Structure: Subject (article + noun only) + verb (v1) + object + rest of sentence."""
import csv

# Subject + verb(v1) + object. --Present Affirmative Sentences
# Subject + verb(v2) + object --Past Affirmative Sentences

def get_base_form(verb):
    """Reverse third-person-singular present tense formation to recover the base verb."""
    if verb == "has":
        return "have"
    if verb == "does":
        return "do"
    if verb == "goes":
        return "go"
    if verb == "is":
        return "is"
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

irregular_verbs_past = {row[0]: row[1] for row in rows}
irregular_verbs_past_participle = {row[0]: row[2] for row in rows}

# The Subject
print(__doc__)

def program(user_input, tense="past"):
    input = user_input
    sentence = input.split(" ")
    sentence[0] = sentence[0] + " " + sentence[1] if sentence[0].lower() == "the" or sentence[0].lower() == "a" else sentence[0]

    if len(" ".join(sentence)) != len(input):
        del sentence[1]
    
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
    verb = sentence[1]
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

    sentence[1] = converted_form

    transformed_sentence = " ".join(sentence)
    return transformed_sentence


if __name__ == "__main__":
    transformed_sentence = program(input("Enter a sentence:\n"))
    print("Enter a sentence:\n"+transformed_sentence)

