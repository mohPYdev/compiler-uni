import string
import Preprocessor

# constants
LETTER_NUMBER = [x for x in string.ascii_letters] + [str(x) for x in range(10)]
OPERATORS = [")" , "(" , ":",  ',',  ';', '{', '}', '=', '<', '>', '+', '-', '*', '/', '%', '&', '|', '!' ]
special_ops = ['+' , '-' , '=' , '!' , '&' , '|']
not_special = [x for x in OPERATORS if x not in special_ops]
Number = ['0','1','2','3','4','5','6','7','8','9']


class State:
    def __init__(self , isFinal , Ttype) -> None:
        self.isFinal = isFinal
        self.Ttype = Ttype

def isDiff(nb):
    if nb not in LETTER_NUMBER :
        return True
    return False

states = [
    State(True , 'ID'),State(True , 'ID'),State(True , 'keyword'),State(True , 'ID'),State(True , 'keyword'),State(True , 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'keyword'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'keyword'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'ID'),State(True, 'ID'),State(True, 'keyword'),State(True, 'ID'),State(True, 'ID'),
    State(True, 'ID'),State(True, 'keyword') , State(True , 'operator') , State(True , 'operator') , State(True,'Number'),
    State(True , ''),State(True , ''), State(True , 'String') , State(True , 'operator')
    ]
print(len(states))

def main():

    # read the file
    source_text = ''
    Preprocessor.Preprocessor('./lexical/source.txt')
    with open('./lexical/cleanedSource.txt' , 'r') as f:
        source_text = f.read()
        # print(source_text)
        f.close()

        toID = {x : states[5] for x in LETTER_NUMBER}
        tokens = []
        type_token =[]

        # DFA
        dfa = {
            states[0] : dict(toID , **{'i': states[1] , 'b': states[6], 'c': states[11], 'd': states[25],
                        'e': states[31], 'f': states[35], 'l': states[42], 'r': states[46], 'w': states[52], 'p': states[57],
                        'v': states[63], 'm': states[67], 's': states[71], ')': states[92], '(': states[92], ':': states[92], 
                        ',': states[92], ';': states[92], '{': states[92], '}': states[92], '=': states[86], '<': states[92], 
                        '>': states[92], '+': states[86], '-': states[86], '*': states[92], '/': states[92], '%': states[92],
                        '&': states[86], '|': states[86], '!': states[86], '0': states[88], '1': states[88], '2': states[88],
                        '3': states[88], '4': states[88], '5': states[88], '6': states[88], '7': states[88], '8': states[88],
                        '9': states[88], '"': states[90]}),
            states[1] : dict( toID , **{'f' : states[2] , 'n': states[3]}),
            states[2] :  toID,
            states[3] : dict(toID , **{'t' : states[4]}),
            states[4] :  toID,
            states[5] :  toID,
            states[6] :  dict(toID , **{'r': states[7]}),
            states[7] :  dict(toID , **{'e': states[8]}),
            states[8] :  dict(toID , **{'a': states[9]}),
            states[9] :  dict(toID , **{'k': states[10]}),
            states[10] :  toID,
            states[11] :  dict(toID , **{'a': states[12], 'h': states[15], 'o': states[18]}),
            states[12] :  dict(toID , **{'s': states[13]}),
            states[13] :  dict(toID , **{'e': states[14]}),
            states[14] :  toID,
            states[15] :  dict(toID , **{'a': states[16]}),
            states[16] :  dict(toID , **{'r': states[17]}),
            states[17] :  toID,
            states[18] :  dict(toID , **{'n': states[19]}),
            states[19] :  dict(toID , **{'t': states[20]}),
            states[20] :  dict(toID , **{'i': states[21]}),
            states[21] :  dict(toID , **{'n': states[22]}),
            states[22] :  dict(toID , **{'u': states[23]}),
            states[23] :  dict(toID , **{'e': states[24]}),
            states[24] :  toID,
            states[25] :  dict(toID , **{'o': states[26]}),
            states[26] :  dict(toID , **{'u': states[27]}),
            states[27] :  dict(toID , **{'b': states[28]}), 
            states[28] :  dict(toID , **{'l': states[29]}),
            states[29] :  dict(toID , **{'e': states[30]}),
            states[30] :  toID,
            states[31] :  dict(toID , **{'l': states[32]}),
            states[32] :  dict(toID , **{'s': states[33]}),
            states[33] :  dict(toID , **{'e': states[34]}),
            states[34] :  toID,
            states[35] :  dict(toID , **{'l': states[36], 'o': states[40]}),
            states[36] :  dict(toID , **{'o': states[37]}),
            states[37] :  dict(toID , **{'a': states[38]}),
            states[38] :  dict(toID , **{'t': states[39]}),
            states[39] :  toID,
            states[40] :  dict(toID , **{'r': states[41]}),
            states[41] :  toID,
            states[42] :  dict(toID , **{'o': states[43]}),
            states[43] :  dict(toID , **{'n': states[44]}),
            states[44] :  dict(toID , **{'g': states[45]}),
            states[45] :  toID,
            states[46] :  dict(toID , **{'e': states[47]}),
            states[47] :  dict(toID , **{'t': states[48]}),
            states[48] :  dict(toID , **{'u': states[49]}),
            states[49] :  dict(toID , **{'r': states[50]}),
            states[50] :  dict(toID , **{'n': states[51]}),
            states[51] :  toID,
            states[52] :  dict(toID , **{'h': states[53]}),
            states[53] :  dict(toID , **{'i': states[54]}),
            states[54] :  dict(toID , **{'l': states[55]}),
            states[55] :  dict(toID , **{'e': states[56]}),
            states[56] :  toID,
            states[57] :  dict(toID , **{'r': states[58]}),
            states[58] :  dict(toID , **{'i': states[59]}),
            states[59] :  dict(toID , **{'n': states[60]}),
            states[60] :  dict(toID , **{'t': states[61]}),
            states[61] :  dict(toID , **{'f': states[62]}),
            states[62] :  toID,
            states[63] :  dict(toID , **{'o': states[64]}),
            states[64] :  dict(toID , **{'i': states[65]}),
            states[65] :  dict(toID , **{'d': states[66]}),
            states[66] :  toID,
            states[67] :  dict(toID , **{'a': states[68]}),
            states[68] :  dict(toID , **{'i': states[69]}),
            states[69] :  dict(toID , **{'n': states[70]}),
            states[70] :  toID,
            states[71] :  dict(toID , **{'w': states[72], 't': states[77], 'c': states[82]}),
            states[72] :  dict(toID , **{'i': states[73]}),
            states[73] :  dict(toID , **{'t': states[74]}),
            states[74] :  dict(toID , **{'c': states[75]}),
            states[75] :  dict(toID , **{'h': states[76]}),
            states[76] :  toID,
            states[77] :  dict(toID , **{'a': states[78]}),
            states[78] :  dict(toID , **{'t': states[79]}),
            states[79] :  dict(toID , **{'i': states[80]}),
            states[80] :  dict(toID , **{'c': states[81]}),
            states[81] :  toID,
            states[82] :  dict(toID , **{'a': states[83]}),
            states[83] :  dict(toID , **{'n': states[84]}),
            states[84] :  dict(toID , **{'f': states[85]}),
            states[85] :  toID,
            states[86] : {x : states[87] for x in special_ops},
            states[87] : dict({x : states[0] for x  in  LETTER_NUMBER} , **{x : states[89] for x in special_ops}),
            states[88] : dict({x : states[88] for x in Number} , **{x : states[89] for x in list(string.ascii_letters)}),
            states[89] : {x : states[89] for x in LETTER_NUMBER},  # not a token
            states[90] : dict({x : states[90] for x  in (LETTER_NUMBER + OPERATORS)} , **{'"' : states[91]}),
            } 


        # starting state
        s = states[0]
        token = ''
        nb = ''
        i = 0
        s_len = len(source_text)

        for c in source_text:
            x = dfa.get(s).get(c)
            if i < s_len - 1 : nb = source_text[i + 1]
            else: nb = ' '

            # print('test' , nb , 'char' , c)
            if x is not None :
                s = x
                if s == states[86]:
                    token += c
                    # print('86')
                    if nb not in special_ops:
                        tokens.append(token)
                        type_token.append(s.Ttype)
                        s = states[0]
                        token = ''
                elif s == states[89]:
                    s = states[0]
                    token = ''

                elif s == states[92]:
                    token += c
                    tokens.append(token)
                    type_token.append(s.Ttype)
                    token = ''
                    s = states[0]
                
                elif s == states[87]:
                    if nb not in special_ops:
                        token += c
                        tokens.append(token)
                        type_token.append(s.Ttype)
                        token = ''
                        s = states[0]

                elif s == states[90]:
                    token += c
                elif s == states[91]:
                    token += c
                    tokens.append(token)
                    type_token.append(s.Ttype)
                    token = ''
                    s = states[0]


                elif s.isFinal and isDiff(nb) :
                    token += c
                    tokens.append(token)
                    type_token.append(s.Ttype)
                    # print(token)
                    s = states[0]
                    token = ''

                else:
                    token += c
                    # print('not')
            # if isDiff(nb):
            #     s = states[0]
            #     token = ''
            i += 1


        # printing 
        # for i in range(len(tokens)):
        #     print(tokens[i] , ' : ' , type_token[i])
        
        return tokens , type_token



if __name__ == '__main__':
    tokens , typeT = main()
    # printing 
    for i in range(len(tokens)):
        print(tokens[i] , ' : ' , typeT[i])
    