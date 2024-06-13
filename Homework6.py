my_dict={'German':2003,'Tanya':2005,'Konstantin':2009,'Savely':2010}
print('Dict:',my_dict)
print('Existing value:',my_dict['Tanya'])
print('Not existing value:',my_dict.get('Elena'))
my_dict.update({'Pavel':1999,
                'Milana':2002})
print('Deleted value:',my_dict.get('Savely'))
del my_dict['Savely']
print('Modified dictionary:',my_dict)
my_dict.get('Savely')
my_set={1,1,1,5,5,5,5,'s','s','u','u','u','n'}
print('Set:',my_set)
my_set.remove('s')
print('Modified set:',my_set)