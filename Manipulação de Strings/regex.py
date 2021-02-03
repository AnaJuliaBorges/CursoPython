import re

pattern = "[0-9]{4,5}-?[0-9]{4,5}"

text = "Meu número para contato é 92633-3572 kjasdhfkjasd 916728913, alkjdlfkjalkdsf 2534-2341"
search = re.findall(pattern, text)
print(search)
