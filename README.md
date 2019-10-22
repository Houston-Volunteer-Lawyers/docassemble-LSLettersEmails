This package allows for the user to generate a letter or email in docassemble for a case from LegalServer.

This requires the `Docassemble.GBLS` package. There is a `Houston-Volunteer-Lawyers` fork of the original GBLS package. The HVL fork includes two additional individuals beyond `advocate`, `client`, and `adverse-parties`. HVL includes the `Pro Bono Advocate/Volunteer` as `pbadvocate` and the `User` in LegalServer as `initiator`. This is to allow for letters being sent by a paralegal assisting the advocate instead of just the advocate. The HVL version also pulls a few other LegalServer fields for reference (gender, language, case number, etc.)

Emails are sent via the `send_email` function in Docassemble. They are sent to the message recipient while copying the `case_email` from LegalServer. The template subject is the subject for the email. 

Letters can be sent to the Client or the Pro Bono Volunteer using either email or letters. The final version is sent back to the LegalServer instance and saved in the case notes of the case. In the case of letters being designed, the letter is sent to the case notes as both a DOCX and a PDF for the case. 

The letterhead template files are saved in the `templates` folder with one for the client and one for the volunteer attorney. The letter to the volunteer could be tweaked to not include all of the details of the client. You will also need to use your own letterhead. Letterhead should be saved as `letterhead-pbadvocate.docx` and `letterhead-client.docx`. This should override the HVL versions that are installed as a default into the package. 

The actual text of the letters is contained as `template` blocks in the `LSLetters-text.yml` file included in this package. The name of the template should be included as a choice in the first block in that document -- `clientmessage.text`. Letters should start with the `toline` and end with the `fromline`. There are custom variables for these fields -- `clientmessage.toline` and `clientmessage.fromline` that are based on who the sender/receipient are, their gender, their language, and salutation. Plan on overwriting the `clientmessage.text` and the appropriate templates with your organizations content by adding these fields to a new YML file that includes: `docassemble.LsLettersEmails`.  

It is presumed that the language included is English for anyone other than the client. For non-english letters, please see the example. Internal docassemble translation tools are not use to keep the interview itself in English. This includes languages for the client in English, Spanish, Chinese, and Vietnamese. It does not do further languages. For that you will need to:
* edit `docassemble.GBLS` to recognize other language codes based on language names in LegalServer
* add a code block that defines the `client.solicitation_custom` and the `client.title` fields for that language. Note that there are two client.title fields -- one final field `client.title` and one for each language. 



