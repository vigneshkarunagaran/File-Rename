import shutil, os, re

datePattern = re.compile(r"""^(.*?)     #text
((0|1)?\d)-                             #month
((0|1|2|3)?\d)-                         #date
((19|20)\d\d)                           #year
(.*?)$                                  #text
""", re.VERBOSE)

if not os.path.exists(r'F:\PyCharm\samplee\rename'):
    os.makedirs(r'F:\PyCharm\samplee\rename')

for americaName in os.listdir(r'F:\PyCharm\samplee\original'):
    check = datePattern.search(americaName)
    if check == None:
        continue
    before = check.group(1)
    month = check.group(2)
    date = check.group(4)
    year = check.group(6)
    after = check.group(8)

    euroName = before + date + '-' + month + '-' + year + after

    renameFrom = os.path.join(r'F:\PyCharm\samplee\original', americaName)
    renameTo = os.path.join(r'F:\PyCharm\samplee\rename', euroName)

    print(renameFrom,'\t', renameTo)

    shutil.move(renameFrom, renameTo)
    #newline


