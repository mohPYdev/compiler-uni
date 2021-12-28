import os

labels = dict()

def Preprocessor(filename):
    filename = filename.replace('"', '')
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith('#define'):
                index = lines.index(line)
                labels[line.split()[1]] = ' '.join(line.split()[2:])
                
                # lines.remove(line)
                lines[index]= ''
                # if len(lines) != 0:
                #     line = lines[index]

            elif '//' in line:
                lines[lines.index(line)] = line.replace(line[line.index('//'):], '')

            elif line.startswith('#include'):
                Preprocessor('./lexical/' + line.split()[1])
                lines[lines.index(line)] = ""



        # if len(lines) == 0:
        #     for label in labels.keys():
        #         if label in line:
        #             line = line.replace(line, labels[label])

        else:
            for line in lines:
                for label in labels.keys():
                    if label in line:
                        lines[lines.index(line)] = line.replace(label, labels[label])
    # for line in lines:
    #     print(line)

    with open('./lexical/cleanedSource.txt' , 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    p =os.path.join(os.path.dirname(__file__) , 'source.txt')
    # Preprocessor("source.txt")
    Preprocessor(p)



