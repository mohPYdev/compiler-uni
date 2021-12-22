
TERMINALS = ['int' , 'float' , 'char' , 'double','ID', 'Number' , 'if' , 'else' , 'while' , 'for' , 'break', 'continue' , 'case' , 'switch' , 'static' , 'return', ")" , "(" , ":",  ',',  ';', '{', '}', '=', '<', '>', '+', '-', '*', '/', '%', '&', '|', '!', '++','--','==','+=', '-=' , '||' , '&&']
NON_TERMINALS = []
FIRSTS = dict()
FOLLOWS = dict()
starting_symbol = 'program'

grammar = '''program -> declList 
declList ->  decl declList^
declList^ ->  decl declList^ | @
decl -> varDecl | funDecl
varDecl -> int
funDecl -> float'''


productions_dict = dict()

def find_nonTerminals():
    # TODO add file to read
    lines = grammar.split('\n')
    for line in lines:
        production = line.split('->')
        production[0] = production[0].strip()
        production[1] = production[1].strip()
        rightsides = production[1].split('|')
        for i in range(len(rightsides)):
            rightsides[i] = rightsides[i].strip()
            
        productions_dict[production[0]] = rightsides



        ter = line.split('->')[0].strip()
        NON_TERMINALS.append(ter)

def first(string):
 
    first_ = set()
    if string in NON_TERMINALS:
        alternatives = [x.split()[0] for x in productions_dict[string]]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in TERMINALS:
        first_ = {string}

    elif string=='' or string=='@':
        first_ = {'@'}

    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                # print("inside while")

                first_ = first_ | (first_2 - {'@'})
                # print('string[i:]=', string[i:])
                if string[i:] in TERMINALS:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2

    # print("returning for first({})".format(string),first_)
    return  first_


def follow(nT):
    #print("inside follow({})".format(nT))
    follow_ = set()
    #print("FOLLOW", FOLLOW)
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ =  follow_ | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    #print("returning for follow({})".format(nT),follow_)
    return follow_

def main():
    find_nonTerminals()
    for nonterminal in NON_TERMINALS:
        FIRSTS[nonterminal] = first(nonterminal)

    


    for non_terminal in NON_TERMINALS:
        FOLLOWS[non_terminal] = set()

    FOLLOWS[starting_symbol] = FOLLOWS[starting_symbol] | {'$'}
    for non_terminal in NON_TERMINALS:
        FOLLOWS[non_terminal] = FOLLOWS[non_terminal] | follow(non_terminal)
    
    print(FOLLOWS)


if __name__ == '__main__':
    main()