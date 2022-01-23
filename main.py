
import sys , os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Lexical'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'syntax'))
import Preprocessor 
import lexical
import parser



def main():
    os.chdir('c_files')
    for file in os.listdir():
        if file.endswith(".c"):
            Preprocessor.Preprocessor(f'{file}')
            tokens, type_token = lexical.main(f'{file}')
            parser.main(tokens, type_token, file)
    
main()