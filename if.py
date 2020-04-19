is_male = True
is_tall = True

if is_male and is_tall:
    print('You r a tall male')
elif is_male and not(is_tall):
    print('You r a short male')
elif not(is_male) and is_tall:
    print('You r not a male but are tall')
else:
    print('You neither male nor tall')

