# строковые методы
# методы lower() и upper() позволяют сменить регистр

s = 'AbAcAba'
print(s.lower())
print(s.upper())

# методы islower() и isupper() позволяют проверить регистр

for i in s:
    print(i, 'islower():', i.islower(), ', isupper():', i.isupper())