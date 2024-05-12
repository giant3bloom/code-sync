from frontend import idx

def test(name, password):
        
    #login
    print('login', end='->')
    print(idx.login(name, password))
    #signup
    print('signup', end='->')
    print(idx.signup(name, password))
    #login
    print('login', end='->')
    print(idx.login(name, password))
    #add
    print('add', end='->')
    print(idx.add())
    #push
    print('push', end='->')
    print(idx.push())
    #pull
    print('pull', end='->')
    print(idx.pull())
    #push
    print('end...', end='->')
    print(idx.end())

if '__main__'==__name__:
    test('jhon', 'jhon123')