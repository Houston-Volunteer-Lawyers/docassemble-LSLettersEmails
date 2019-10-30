# Letters/Emails from LegalServer

This package allows for the user to generate a letter or email in docassemble for a case from LegalServer.

## Requirements
This requires the `Docassemble.GBLS` package. There is a `Houston-Volunteer-Lawyers` fork of the original GBLS package that has since been merged back in with the main package. The HVL fork includes two additional individuals beyond `advocate`, `client`, and `adverse-parties`. HVL includes the `Pro Bono Advocate/Volunteer` as `pbadvocate` and the `User` in LegalServer as `initiator`. This is to allow for letters being sent by a paralegal assisting the advocate instead of just the advocate. The HVL version also pulls a few other LegalServer fields for reference (gender, language, case number, etc.)

This project requires the Docassemble configuration: `new markdown to docx: True` to properly generate the letters on the letterhead in the appropriate format. Adding the `convertapi` feature to Docassemble may be necessary depending on the graphics of your letterhead and how `pandoc` handles the PDF conversion of that letterhead. It may also be helpful to add the `use cloud urls: False` configuration item if there are problems downloading the PDF/DOCX versions of letters.

## Functionality
The user will have the option of selecting the recipient (either the Client or the Pro Bono Volunteer (if there is one)), then the sender (either the LegalServer user who started the process or the LegalServer Advocate on the case), and then the message they wish to send. The message can then be editted if there are any changes to the standard text before sending. 

Emails are sent via the `send_email` function in Docassemble. They are sent to the message recipient while copying the `case_email` from LegalServer. The template subject is the subject for the email. The user is copied on these emails. 

Letters can be sent to the Client or the Pro Bono Volunteer using either email or letters. The final version is sent back to the LegalServer `case_email` and saved in the case notes of the case as both a DOCX and a PDF. The user is then given download links.  

## Customization
The letterhead template files are saved in the `templates` folder with one for the client and one for the volunteer attorney. You will also need to use your own letterhead. Letterhead should be saved as `letterhead-pbadvocate.docx` and `letterhead-client.docx`. This should override the HVL versions that are installed as a default into the package. Please note that you can include an envelope with the letterhead to plan for those as well. 

The actual text of the letters is contained as `template` blocks in the `LSLetters-text.yml` file included in this package. The name of the template should be included as a choice in the first block in that document -- `clientmessage.textoption`. Letters should start with the `toline` and end with the `fromline`. There are custom variables for these fields -- `clientmessage.toline` and `clientmessage.fromline` that are based on who the sender/receipient are, their gender, their language, and salutation. Plan on overwriting the `clientmessage.textoption` and the appropriate templates with your organizations content by adding these fields to a new YML file that includes: `docassemble.LSLettersEmails`. When creating the `client.toline`, it will use `Dear Mr. So-and-So` as the toline if there is a language and a gender. If the gender is not `male` or `female`, it will use the client's entire name -- `Dear James So-and-So` -- instead. This is done by the `greeting` language option in the Python module associated  with the package.

It is presumed that the language included is English for anyone other than the client. For non-english letters, please see the example. Internal docassemble translation tools are not use to keep the interview itself in English. This includes languages for the client in English, Spanish, Chinese, and Vietnamese. It does not do further languages. For that you will need to:
* edit `docassemble.GBLS` to recognize other language codes based on language names from LegalServer
* add a code block that defines the `client.solicitation_custom` and the `client.title` fields for that language. Note that there are two client.title fields -- one final field `client.title` and one for each language. 

