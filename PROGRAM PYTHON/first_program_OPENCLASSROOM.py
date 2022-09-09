
Type "help", "copyright", "credits" or "license()" for more information.
>>> total = 3
>>> total
3
>>> total++
SyntaxError: invalid syntax
>>> total
3
>>> total = total - 1
>>> total
2
>>> chaine_de_caractere = "J'adore codé en phyton"
>>> chaine_de_caractere
"J'adore codé en phyton"
>>> chaine_de_caractere_2 = [ "J'adore", "coder" , "en", "python"]
>>> chaine_de_caractere_2
["J'adore", 'coder', 'en', 'python']
>>> chaine_de_caractere_2[1]
'coder'
>>> chaine_de_caractere_2.append("Ouais")
>>> chaine_de_caractere_2
["J'adore", 'coder', 'en', 'python', 'Ouais']
>>> chaine_de_caractere_2.remove("Ouais")
>>> chaine_de_caractere_2
["J'adore", 'coder', 'en', 'python']
>>> len(chaine_de_caractere_2)
4
>>> taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
SyntaxError: multiple statements found while compiling a single statement
>>> taux_de_conversion = {}
>>> taux_de_conversion = {"Facebook" : "60%", "Instagram": "40%"}
>>> taux_de_conversion
{'Facebook': '60%', 'Instagram': '40%'}
>>> taux_de_conversion['Facebook']
'60%'
>>> 
KeyboardInterrupt
>>> taux_de_conversion['Twiter'] = '20%' , taux_de_conversion['Facebook'] = '40%'
SyntaxError: cannot assign to literal
>>> taux_de_conversion['Twiter'] = '20%'
>>> taux_de_conversion['Twiter'] = '20%'
>>> taux_de_conversion['Facebook'] = '40%'
>>> taux_de_conversion
{'Facebook': '40%', 'Instagram': '40%', 'Twiter': '20%'}
>>> 