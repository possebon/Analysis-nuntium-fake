# External Libraries
from translate import Translator
from faker import Faker

def translate_to_en(string:str) -> str:
    translator = get_new_translator()
    divide = False
    if len(string) > 500:
        divide = True
        first_index = 0
        last_index = string[:500].rfind(".")
    if not divide:    
        translation = translator.translate(string)
        
    while divide:
        translation = ""
        translation_ = translator.translate(string[first_index:last_index])
        
        # Check if exceeded requests amount
        while len(translation_) == 194 and "MYMEMORY" in translation_:
            translator = get_new_translator()
            translation_ = translator.translate(string[first_index:last_index])
        translation += translation_
        if len(string) - last_index > 500:
            step = last_index + 500
            print("Step: ", step)
            range_index = string[last_index:step].rfind(".")
            if range_index <= 0:
                range_index = string[last_index:step].rfind(",")
            if range_index <= 0:
                range_index = string[last_index:step].rfind(" ")
            print("Last index: ", last_index)
            print("Range: ", range_index)
            last_index = range_index + last_index
            print("New Last index: ", last_index)
            print("Len string: ", len(string))
        else:
            translation_ = translator.translate(string[last_index:])
            # Check if exceeded requests amount
            while len(translation_) == 194 and "MYMEMORY" in translation_:
                translator = get_new_translator()
                translation_ = translator.translate(string[first_index:last_index])
            translation += translation_      
            divide = False
            
    return translation

def get_new_translator():
    faker = Faker()
    email = faker.email()
    print(email)
    translator = Translator(from_lang="pt-br", to_lang="en", email=email)
    return translator