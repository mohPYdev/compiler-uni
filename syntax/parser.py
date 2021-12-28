import sys , os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Lexical'))
import lexical

# get the tokens from lexical analyser
tokens , token_type = lexical.main()

TERMINALS = ['true', 'false' , 'NUMCONST' , 'CHARCONST' , 'STRINGCONST', '?','@','int' , 'float' , 'char' , 'double' , 'ID', 'Number' , 'if' , 'else' , 'while' , 'for' , 'break', 'continue' , 'case' , 'switch' , 'static' , 'return', ")" , "(" , ":",  ',',  ';', '{', '}', '=', '<', '>', '+', '-', '*', '/', '%', '&', '|', '!', '++','--','==','+=', '-=' , '||' , '&&', '[', ']' , '<=' , '>=' , '!=']
NON_TERMINALS = []

firsts = dict()
follows = dict()

productions = dict()
table = dict()
input = str()
# input = '''program -> declList 
# declList ->  decl declList^
# declList^ ->  decl declList^ 
# declList^ -> @
# decl -> varDecl
# decl -> funDecl
# varDecl -> int
# funDecl -> float'''
# input = '''E -> T E^
#     E^ -> + T E^
#     E^ -> @
#     T -> F T^
#     T^ -> * F T^
#     T^ -> @
#     F -> ( E )
#     F -> int''' 

def get_input():
    global input
    x = os.path.join(os.path.dirname(__file__), 'actualGramm.txt')
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
    for nonterminal in table.keys():
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

def parse():
    pass

def draw_tree():
    pass

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




def main():
    get_input()
    find_nonTerminals()
    for nonterminal in NON_TERMINALS: 
        firsts[nonterminal] = set() 
        follows[nonterminal] = set()

    for nonterminal in NON_TERMINALS:       
        first(nonterminal)

    follows['program']= { '$' }
    # follows['E'] = { '$' }
    for nonterminal in NON_TERMINALS:
        follow(nonterminal)



if __name__ == '__main__':
    main()

