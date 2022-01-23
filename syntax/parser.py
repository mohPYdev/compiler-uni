import sys , os , uuid
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Lexical'))
# import lexical

import graphviz
dot = graphviz.Digraph('round-table', comment='The Round Table')  


# get the tokens from lexical analyser
# tokens , token_type = lexical.main()



TERMINALS = ['main','printf','true', 'false' ,  'CHARCONST' , 'String', '?','@','int' , 'float' , 'char' , 'double' , 'ID', 'Number' , 'if' , 'else' , 'while' , 'for' , 'break', 'continue' , 'case' , 'switch' , 'static' , 'return', ")" , "(" , ":",  ',',  ';', '{', '}', '=', '<', '>', '+', '-', '*', '/', '%', '&', '|', '!', '++','--','==', '*=','/=' ,'+=', '-=' , '||' , '&&', '[', ']' , '<=' , '>=' , '!=']
NON_TERMINALS = []

firsts = dict()
follows = dict()

productions = dict()
table = dict()
input = str()

class ParseError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ParseError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'
class TypeCheckError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'TypeCheckError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'

def get_input():
    global input
    x = os.path.join(os.path.dirname(__file__), 'grammar.txt')
    with open(x , 'r') as f:
        input = f.read()

def create_prods_dict():
    ''' it will create a dictionary of the rules -> {a : [b,c, ...] , ...} '''
    for line in input.splitlines():
        line = line.strip()
        p = line.split('->')
        p[0] = p[0].strip()
        p[1] = p[1].strip()
        if p[0] in productions.keys():
            productions[p[0]].append(p[1])
        else:
            productions[p[0]] = [p[1]]

            # add the non-terminal to the table's key and the value of it equals to an empty dictionary
            table[p[0]] = dict()
    
def create_table():
    for nonterminal in productions.keys():
        rule = dict()
        # add the production related to this first in the table using the production dict 
        for res in productions[nonterminal]:
            if res.split()[0] in firsts[nonterminal]:
                if res.split()[0] == '@':
                    for f in follows[nonterminal]:
                        rule[f] = '@'
                else:
                    rule[res.split()[0]] = res     
                    
            else:
                for f in firsts[res.split()[0]]:
                    if f == '@':
                        for f in follows[nonterminal]:
                            rule[f] = '@'
                    else:
                        rule[f] = res

        # add the dictionary in the table
        table[nonterminal] = rule

def parse(tokens, token_type):

    types = []
    ids = []
    t1 = ''
    t2 = ''

    nodes = dict()
    stack = []
    stack.append('$')
    stack.append('InitiateSt')
    nodes['InitiateSt'] = str(uuid.uuid4())
    dot.node(nodes['InitiateSt'] , 'InitiateSt')

    tokens.append('$')
    token_type.append('operator')

    matched = ''
    found = False
    for i in range(len(tokens)):
        found = False
        while(not found):
            print(stack)
            if (t1 != t2 and t1 != '' and t2 != ''):
                raise TypeCheckError('missmatch in types')
            if token_type[i] in ['keyword' , 'operator']:
                if stack[-1] == tokens[i]:
                    found = True
                    n = stack.pop()
                    if n == ';':
                        t1 = ''
                        t2 = ''
                    matched += tokens[i]
                else:
                    n = stack.pop()
                    try:
                        prods = table[n][tokens[i]].split()
                        if n == 'type':
                            types.append(prods[0])
                    except KeyError:
                        return False
                    for prod in reversed(prods):
                        stack.append(prod)
                   
                    for prod in prods:
                        nodes[prod] = str(uuid.uuid4())
                        dot.node(nodes[prod], prod)
                        dot.edge(nodes[n] , nodes[prod])

                    if stack[-1] == '@':
                        stack.pop()

            else:
                if stack[-1] == token_type[i]:
                    found=  True
                    n= stack.pop()
                    if n == 'ID':
                        if tokens[i] not in ids:
                            ids.append(tokens[i])
                        else:
                            if t1 == '': t1 = types[ids.index(tokens[i])]
                            else: t2 = types[ids.index(tokens[i])]
                    elif n == 'String':
                        t2 = 'String'
                    matched += tokens[i]
                    continue
                else:
                    n = stack.pop()
                    try:
                        prods = table[n][token_type[i]].split()
                        if n == 'type':
                            types.append(prods[0])
                    except KeyError:
                        return False
                    for prod in reversed(prods):
                        stack.append(prod) 
                    for prod in prods:          
                        nodes[prod] = str(uuid.uuid4())
                        dot.node(nodes[prod], prod)
                        dot.edge(nodes[n] , nodes[prod])
                    if stack[-1] == '@':
                        stack.pop()
    return True
  
def find_nonTerminals():
    for line in input.splitlines():
        ter = line.split('->')[0].strip()
        if ter not in NON_TERMINALS:
            NON_TERMINALS.append(ter)

def first(nonterminal):
    for line in input.splitlines():
        line = line.strip()
        sides = line.split('->')
        sides[0] = sides[0].strip()
        sides[1] = sides[1].strip()
        if sides[0] == nonterminal:
            if sides[1].split()[0] in TERMINALS:
                firsts[nonterminal].add(sides[1].split()[0])
            else:
                if (firsts[sides[1].split()[0]]):
                    firsts[nonterminal] = set.union(firsts[nonterminal],firsts[sides[1].split()[0]])    
                else:
                    firsts[nonterminal] = set.union(firsts[nonterminal],first(sides[1].split()[0]))    
    return firsts[nonterminal]

def follow(nonterminal):                                  
    for line in input.splitlines():
        line = line.strip()
        lines = line.split('->')
        right = lines[1].strip()
        left = lines[0].strip()
        rights = right.split()
        if nonterminal in rights:
            if rights.index(nonterminal) == len(rights) - 1: 
                if left == nonterminal:
                    continue 
                if follows[left]:
                    follows[nonterminal] = set.union(follows[left] , follows[nonterminal] )
                else:
                    follows[nonterminal] = set.union(follow(left) , follows[nonterminal] )
            elif rights[rights.index(nonterminal) + 1] in TERMINALS:
                follows[nonterminal].add(rights[rights.index(nonterminal) + 1])
            elif rights[rights.index(nonterminal) + 1] in NON_TERMINALS:    # A => a B C
                if '@' in firsts[rights[rights.index(nonterminal) + 1]]:
                    follows[nonterminal] = set.union(firsts[rights[rights.index(nonterminal) + 1]] - {'@'} , follows[nonterminal] )
                    if left != nonterminal:
                        if follows[left]:
                            follows[nonterminal] = set.union(follows[left] , follows[nonterminal] )
                        else:
                            follows[nonterminal] = set.union(follow(left) , follows[nonterminal] )
                else:
                    follows[nonterminal] = set.union(firsts[rights[rights.index(nonterminal) + 1]] , follows[nonterminal] )
    
    return follows[nonterminal]


def main(tokens, token_type, file):
    get_input()
    find_nonTerminals()
    for nonterminal in NON_TERMINALS: 
        firsts[nonterminal] = set() 
        follows[nonterminal] = set()

    for nonterminal in NON_TERMINALS:       
        first(nonterminal)

    follows['InitiateSt']= { '$' }
    for nonterminal in NON_TERMINALS:
        follow(nonterminal)

    # change the firsts and follows to arrays
    for key in firsts.keys():
        firsts[key] = list(firsts[key])
    for key in follows.keys():
        follows[key] = list(follows[key])

    create_prods_dict()
    create_table()
    if parse(tokens, token_type):
        file = file.split('.')[0]
        dot.render(directory=f'../output/{file}/parser-output', view=False)
    else:
        raise ParseError('error in parsing')



if __name__ == '__main__':
    main()

