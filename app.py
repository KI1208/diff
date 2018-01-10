import re
import csv
# import sys

# dirfilename = sys.argv[1]
# originaldl = sys.argv[2]
# targetdl = sys.argv[3]

def change_driveletter(filename, originalletter, targetletter):
    f = open(filename)
    flines = f.readlines()
    f.close()
    output = []
    for line in flines:
        if originalletter + ':\\' in line:
            output.append(re.sub(originalletter + ':', targetletter + ':', line))
            # print('A', output)
        else:
            output.append(line)
            # print('B', line)

    return output





def format_output(inputlist):
    dirname = ''
    output = []
    for line in inputlist:
        if line.rstrip().split(maxsplit=3) == [] or '個のファイル' in line:  # len(line) == 0 or line is '\r\n':
            print('A', line.rstrip().split(maxsplit=3))  # For Debug
            pass

        elif 'のディレクトリ' in line:
            print('B', line.rstrip().split(maxsplit=3))  # For Debug
            dirname = line.rstrip().split(maxsplit=3)[0]

        elif '<DIR>' in line:
            print('C', line.rstrip().split(maxsplit=3))  # For Debug
            date = line.rstrip().split(maxsplit=3)[0]
            time = line.rstrip().split(maxsplit=3)[1]
            filename = line.rstrip().split(maxsplit=3)[3]
            # output.append([date, time, '0', dirname + '\\' + filename + '\\'])

        else:
            print('D', line.rstrip().split(maxsplit=3))  # For Debug
            try:
                date = line.rstrip().split(maxsplit=3)[0]
                time = line.rstrip().split(maxsplit=3)[1]
                size = line.rstrip().split(maxsplit=3)[2]
                filename = line.rstrip().split(maxsplit=3)[3]
                output.append([date, time, size, dirname + '\\' + filename])
            except IndexError as e:
                print(e)

    return output


def write_csv(inputlist,filename):
    with open(filename, 'w', newline='') as csvfile:
        for line in inputlist:
            csv.writer(csvfile).writerow(line)



# before = change_driveletter('dir_before.txt', 'D', 'E')
# formattedbefore = format_output(before)
# write_csv(formattedbefore, 'before.csv')

after = change_driveletter('dir_after.txt', 'D', 'E')
formattedafter = format_output(after)
write_csv(formattedafter, 'after.csv')