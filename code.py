start = 'y'
while start == 'y':
    history = []
    value = input('enter the inputs: ')

    x = value.replace('+','').replace('-','').replace('/','').replace('*','').replace('%','').replace('^','')
    if x.isdigit():
        outvalues = value.replace(' ','*').replace('^','**')
        output = eval(outvalues)
        if len(history) < 11:
            history.append((value,output))
        else:
            history.pop(0)
            history.append((value,output))
        print(output)
    
    else:
        print('Invalid Inputs')
    start = input('Do you want to perform another calculation (Y/N): ')
    if start.lower() == 'n':
        break
        
        