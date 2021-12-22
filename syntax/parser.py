import sys , os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Lexical'))
import lexical

# get the tokens from lexical analyser
tokens , token_type = lexical.main()


firsts = dict()
follows = dict()

productions = dict()
table = dict()
input = str()

def get_input():
    pass

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