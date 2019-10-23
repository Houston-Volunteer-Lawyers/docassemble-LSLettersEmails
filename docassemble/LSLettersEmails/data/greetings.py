import docassemble.base.functions
def salutation_default(indiv, with_name=False, with_name_and_punctuation=False, language=None):
    return docassemble.base.functions.salutation_default(indiv, 
                                                         with_name=with_name, 
                                                         with_name_and_punctuation=with_name_and_punctuation)

def salutation_en(indiv, with_name=False, with_name_and_punctuation=False):
    if indiv.gender == 'female':
        salut = 'Ms.'
    elif indiv.gender == 'male':
        salut = 'Mr.'
    else:
        salut = 'Mx.'
    if with_name or with_name_and_punctuation:
        if indiv.gender == 'male' or indiv.gender == 'female':
            if with_name_and_punctuation:
                return salut + ' ' + indiv.name.last + ':'
            return salut + ' ' + indiv.name.last
        else:
            if with_name_and_punctuation:
                return indiv.name.first + ' ' + indiv.name.last + ':'
            return indiv.name.first + ' ' + indiv.name.last
    return salut    


def salutation_es(indiv, with_name=False, with_name_and_punctuation=False):
    if indiv.gender == 'female':
        salut = 'Sra.'
    elif indiv.gender == 'male':
        salut = 'Sr.'
    else:
        salut = 'Sr.'
        if with_name or with_name_and_punctuation:
        if indiv.gender == 'male' or indiv.gender == 'female':
            if with_name_and_punctuation:
                salut2 = salut + ' ' + indiv.name.last + ':'
            salut2 = salut + ' ' + indiv.name.last
        else:
            if with_name_and_punctuation:
                salut2 = indiv.name.first + ' ' + indiv.name.last + ':'
            salut2 = indiv.name.first + ' ' + indiv.name.last
    else: 
        salut2 = salut    
    return salut2


def salutation_vi(indiv, with_name=False, with_name_and_punctuation=False):
    if indiv.gender == 'female':
        salut = 'Bà.'
    elif indiv.gender == 'male':
        salut = 'Ông.'
    else:
        salut = 'Ông.'
    if with_name or with_name_and_punctuation:
        if indiv.gender == 'male' or indiv.gender == 'female':
            if with_name_and_punctuation:
                salut2 = salut + ' ' + indiv.name.last + ':'
            salut2 = salut + ' ' + indiv.name.last
        else:
            if with_name_and_punctuation:
                salut2 = indiv.name.first + ' ' + indiv.name.last + ':'
            salut2 = indiv.name.first + ' ' + indiv.name.last
    else: 
        salut2 = salut    
    return salut2


def salutation_zo(indiv, with_name=False, with_name_and_punctuation=False):
    if indiv.gender == 'female':
        salut = '太太。'
    elif indiv.gender == 'male':
        salut = '先生。'
    else:
        salut = '先生。'
    if with_name or with_name_and_punctuation:
        if indiv.gender == 'male' or indiv.gender == 'female':
            if with_name_and_punctuation:
                salut2 = salut + ' ' + indiv.name.last + ':'
            salut2 = salut + ' ' + indiv.name.last
        else:
            if with_name_and_punctuation:
                salut2 = indiv.name.first + ' ' + indiv.name.last + ':'
            salut2 = indiv.name.first + ' ' + indiv.name.last
    else: 
        salut2 = salut    
    return salut2    

def greeting(indiv, with_punctuation=False,language=none):
    if indiv.language == 'en':
        greet = "Dear " + client.salutation(with_name=True,language='en')
    elif indiv.language == 'es':
        if indiv.gender == 'male':
            greet = "Estimado " + client.salutation(with_name=True,language='es')
        elif indiv.gender == 'female':
            greet = "Estimada " + client.salutation(with_name=True,language='es')
        else: 
            greet = "Estimado/a" + client.salutation(with_name=True,language='es')
    elif indiv.language == 'vi':
        greet = "Kính gửi " + client.salutation(with_name=True,language='vi')
    elif indiv.language == 'zo':
        greet = "亲爱的 " + client.salutation(with_name=True,language='zo')
    else:
        greet = "Dear "  + client.salutation(with_name=True)
    if with_punctuation:
        return greet + ':' 
    return greet

docassemble.base.functions.update_language_function('*', 'salutation', salutation_default)
docassemble.base.functions.update_language_function('en', 'salutation', salutation_en)
docassemble.base.functions.update_language_function('es', 'salutation', salutation_es)
docassemble.base.functions.update_language_function('vi', 'salutation', salutation_vi)
docassemble.base.functions.update_language_function('zo', 'salutation', salutation_zo)