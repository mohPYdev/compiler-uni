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
tokens = []
type_token =[]
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

dfa = {
    states[0] : dict(toID , **{'i': states[1] , 'b': states[6]}),
    states[1] : {'f' : states[2] , 'n': states[3]},
    states[2] :  {},
    states[3] : {'t' : states[4]},
    states[4] :  {},
    states[5] :  {}
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