def FakeNameGen():
    
    #install Faker module in cmd----pip install Faker
    from faker import Faker 
    print('Welcome to Fake name generator\n')
    
    c1=True
    while c1:
        lang=input('Do you want names in  English(E) or Hindi(H) = ')
        if lang.upper()=='E':
            l='en'
            fake = Faker ([f'{l}_IN'])
            c1=False
        elif lang.upper()=='H':
            l='hi'
            fake = Faker ([f'{l}_IN'])
            c1=False
        else:
            print('Invalid Choice!!!')
            c1=True
        
    
    m=int(input('Number of Male names= '))   
    f=int(input('Number of Female names= '))
    
    
    c2=True
    
    while c2:    
        n=input('\nDo you want:\n1. Full Names\n2. First Names\n3. Last Names\nChoice = ')
        print('\n')
        if n=='1':
            for x in range(m):
                print('Full Name (Male):',fake.name_male())
            print('\n')
            for x in range(f):
                print('Full Name (Female):',fake.name_female())
            
            c2= False
        
        elif n=='2':
            for x in range(m):
                print('Last Name (Male):',fake.first_name_male())
            print('\n')
            for x in range(f):
                print('Last Name (Female):',fake.first_name_female())
            
            c2= False

        elif n=='3':
            for x in range(m):
                print('Full Name (Male):',fake.last_name_male())
            print('\n')
            for x in range(f):
                print('Full Name (Female):',fake.last_name_female())
            
            c2= False

        else:
            print('Invalid Choice!!!')
            c2=False
            continue


    #print('Prefix Name:',fake.prefix())
    #print('Sufffix Name:',fake.suffix())#
