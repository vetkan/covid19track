start = 'c'
history = []
while start == 'c':
    
    value = input('enter the inputs: ')

    x = value.replace('+','').replace('-','').replace('/','').replace('*','').replace('%','').replace('^','').replace(' ','')
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
    start = input('Do you want to perform another Calculation/ History/ Quit (first letter of option - c/h/q): ')
    if start.lower() == 'h':
        reverse_history = reversed(history)
        for i in reverse_history:
            print(str(i[0])+' - '+str(i[1]))
        start = input('Do you want to perform another Calculation/ History/ Quit (first letter of option - c/h/q): ')
    elif startlower() == 'c':
        pass
    elif start.lower() == 'q':
        break
    else:
        start = input('Do you want to perform another Calculation/ History/ Quit (first letter of option - c/h/q): ')

