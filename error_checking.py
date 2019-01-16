def error_testc(testdate,save_position,testmode,howmany,DBDtext,text,cutline):
    #checking for date
    if testdate > len(save_position):
        print('ERROR : WRONG DATE')
        quit()

    # checking for Howmany
    if testmode ==1:
        if howmany > len(DBDtext[testdate-1]):
            print('ERROR : TOO MANY WORDS')
            quit()
    if testmode ==0:
        if howmany > (len(text)-len(save_position)):
            print('ERROR : TOO MANY WORDS')
            quit()

    #checking for cutline
    if cutline > 100 or cutline < 0:
        print('ERROR : WRONG CUTLINE')
        quit()

    return 0
