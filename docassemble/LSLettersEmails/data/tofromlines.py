from docassemble.base.core import DAObject, DAList, DADict, DAOrderedDict
from docassemble.base.util import Value, PeriodicValue, FinancialList, PeriodicFinancialList
from decimal import Decimal
import datetime
import docassemble.base.functions
from collections import OrderedDict

def my_salutation(indiv):
    if indiv.language == "en":
        if indiv.gender == "male":
            return "Dear Mr."
        elif indiv.gender == "female":  
            return "Dear Ms."
        else: 
            return "Dear Mx"
    elif indiv.language == "es":
        if indiv.gender == "male": 
            return "Estimado Sr."
        elif indiv.gender == "female":
            return "Estimada Sra."
        else:
            return "Estimado/a"
    elif indiv.language == "vi":
        if indiv.gender == "male":
            return "Kính gửi Ông."
        elif indiv.gender == "female":
            return "Kính gửi Bà."
        else: 
            return "Kính gửi"
    elif indiv.language == "zo":
        if indiv.gender == "male":
            return "亲爱的 先生。"
        elif indiv.gender == "female":
            return "亲爱的 太太。"
        else: 
            return "亲爱的"
    else:
        return "Dear"
    
docassemble.base.util.update_language_function('*', 'salutation', my_salutation)