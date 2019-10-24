import docassemble.base.functions
from docassemble.base.util import Individual

__all__ = ['greeting']

def salutation_default(indiv, with_name=False, with_name_and_punctuation=False, language=None):
    return docassemble.base.functions.salutation_default(indiv,
                                                         with_name=with_name,
                                                         with_name_and_punctuation=with_name_and_punctuation)

def salutation_es(indiv, with_name=False, with_name_and_punctuation=False, language=None):
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

def salutation_vi(indiv, with_name=False, with_name_and_punctuation=False, language=None):
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

def salutation_zo(indiv, with_name=False, with_name_and_punctuation=False, language=None):
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

def greeting_default(indiv, with_punctuation=False, language=None):
    greet = "Dear " + indiv.salutation(with_name=True, language='en')
    if with_punctuation:
        return greet + ':'
    return greet

def greeting_es(indiv, with_punctuation=False, language=None):
    if indiv.gender == 'male':
        greet = "Estimado " + indiv.salutation(with_name=True, language='es')
    elif indiv.gender == 'female':
        greet = "Estimada " + indiv.salutation(with_name=True, language='es')
    else:
        greet = "Estimado/a" + indiv.salutation(with_name=True, language='es')
    if with_punctuation:
        return greet + ':'
    return greet

def greeting_vi(indiv, with_punctuation=False, language=None):
    greet = "Kính gửi " + indiv.salutation(with_name=True, language='vi')
    if with_punctuation:
        return greet + ':'
    return greet

def greeting_zo(indiv, with_punctuation=False, language=None):
    greet = "亲爱的 " + indiv.salutation(with_name=True, language='zo')
    if with_punctuation:
        return greet + ':'
    return greet

docassemble.base.functions.update_language_function('*', 'salutation', salutation_default)
docassemble.base.functions.update_language_function('es', 'salutation', salutation_es)
docassemble.base.functions.update_language_function('vi', 'salutation', salutation_vi)
docassemble.base.functions.update_language_function('zo', 'salutation', salutation_zo)
docassemble.base.functions.update_language_function('*', 'greeting', greeting_default)
docassemble.base.functions.update_language_function('en', 'greeting', greeting_default)
docassemble.base.functions.update_language_function('es', 'greeting', greeting_es)
docassemble.base.functions.update_language_function('vi', 'greeting', greeting_vi)
docassemble.base.functions.update_language_function('zo', 'greeting', greeting_zo)
greeting = docassemble.base.functions.language_function_constructor('greeting')
