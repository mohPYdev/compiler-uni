import string

LETTER_NUMBER = [x for x in string.ascii_letters] + [str(x) for x in range(10)]
# print(LETTER_NUMBER)


def isDiff(nb):
    if nb not in LETTER_NUMBER:
        return True
    return False


class State:
    def __init__(self , isFinal , Ttype) -> None:
        self.isFinal = isFinal
        self.Ttype = Ttype

source_text = 'int main(){  int n,i,m=0,flag=0;    printf ("Enter the number to check prime:");   scanf("%d",&n);   m=n/2;   for (i=2;i<=m;i++)   {   if(n%i==0)   {   printf ("Number is not prime");   flag=1;   break;   }   }   if (flag==0)   printf ("Number is prime");    return 0;  }'  

states = [
    State(False , 'ID'),State(False , 'ID'),State(True , 'keyword'),State(False , 'ID'),State(True , 'keyword'),State(True , 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),
    State(True, 'keyword'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),
    State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(True, 'keyword'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),
    State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),
    State(False, 'ID'),State(False, 'ID'),State(False, 'ID'),State(True, 'keyword'),State(False, 'ID'),State(False, 'ID'),
    State(False, 'ID'),State(True, 'keyword')
    ]

toID = {x : states[5] for x in LETTER_NUMBER}

tokens = []
type_token =[]

dfa = {
    states[0] : dict(toID , **{'i': states[1] , 'b': states[6], 'c': states[11], 'd': states[25],
                'e': states[31], 'f': states[35], 'l': states[42], 'r': states[46], 'w': states[52], 'p': states[57],
                'v': states[63], 'm': states[67], 's': states[71]}),
    states[1] : {'f' : states[2] , 'n': states[3]},
    states[2] :  {},
    states[3] : {'t' : states[4]},
    states[4] :  {},
    states[5] :  {},
    states[6] :  {'r': states[7]},
    states[7] :  {'e': states[8]},
    states[8] :  {'a': states[9]},
    states[9] :  {'k': states[10]},
    states[10] :  {},
    states[11] :  {'a': states[12], 'h': states[15], 'o': states[18]},
    states[12] :  {'s': states[13]},
    states[13] :  {'e': states[14]},
    states[14] :  {},
    states[15] :  {'a': states[16]},
    states[16] :  {'r': states[17]},
    states[17] :  {},
    states[18] :  {'n': states[19]},
    states[19] :  {'t': states[20]},
    states[20] :  {'i': states[21]},
    states[21] :  {'n': states[22]},
    states[22] :  {'u': states[23]},
    states[23] :  {'e': states[24]},
    states[24] :  {},
    states[25] :  {'o': states[26]},
    states[26] :  {'u': states[27]},
    states[27] :  {'b': states[28]},
    states[28] :  {'l': states[29]},
    states[29] :  {'e': states[30]},
    states[30] :  {},
    states[31] :  {'l': states[32]},
    states[32] :  {'s': states[33]},
    states[33] :  {'e': states[34]},
    states[34] :  {},
    states[35] :  {'l': states[36], 'o': states[40]},
    states[36] :  {'o': states[37]},
    states[37] :  {'a': states[38]},
    states[38] :  {'t': states[39]},
    states[39] :  {},
    states[40] :  {'r': states[41]},
    states[41] :  {},
    states[42] :  {'o': states[43]},
    states[43] :  {'n': states[44]},
    states[44] :  {'g': states[45]},
    states[45] :  {},
    states[46] :  {'e': states[47]},
    states[47] :  {'t', states[48]},
    states[48] :  {'u': states[49]},
    states[49] :  {'r': states[50]},
    states[50] :  {'n': states[51]},
    states[51] :  {},
    states[52] :  {'h': states[53]},
    states[53] :  {'i': states[54]},
    states[54] :  {'l': states[55]},
    states[55] :  {'e': states[56]},
    states[56] :  {},
    states[57] :  {'r': states[58]},
    states[58] :  {'i': states[59]},
    states[59] :  {'n': states[60]},
    states[60] :  {'t': states[61]},
    states[61] :  {'f': states[62]},
    states[62] :  {},
    states[63] :  {'o': states[64]},
    states[64] :  {'i': states[65]},
    states[65] :  {'d': states[66]},
    states[66] :  {},
    states[67] :  {'a': states[68]},
    states[68] :  {'i': states[69]},
    states[69] :  {'n': states[70]},
    states[70] :  {},
    states[71] :  {'w': states[72], 't': states[77], 'c': states[82]},
    states[72] :  {'i': states[73]},
    states[73] :  {'t': states[74]},
    states[74] :  {'c': states[75]},
    states[75] :  {'h': states[76]},
    states[76] :  {},
    states[77] :  {'a': states[78]},
    states[78] :  {'t': states[79]},
    states[79] :  {'i': states[80]},
    states[80] :  {'c': states[81]},
    states[81] :  {},
    states[82] :  {'a': states[83]},
    states[83] :  {'n': states[84]},
    states[84] :  {'f': states[85]},
    states[85] :  {}
    } 

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
        if s.isFinal and isDiff(nb) :
            token += c
            tokens.append(token)
            type_token.append(s.Ttype)
            # print(token)
            s = states[0]
            token = ''

        else:
            token += c
            # print('not')
    if isDiff(nb):
        s = states[0]
        token = ''
    i += 1

print(tokens)
print(type_token)