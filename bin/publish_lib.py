import os
import array as arr

limit_fr = 0
limit_to = 100


chapters = [
    '000-Intro',
    '010-CHAOS',
    '020-ENERGY',
    '030-ORDER',
    '040-THE_LAWS',
    '050-REASON',
    '060-INFORMATION',
    '070-STRUCTURE',
    '075-The_Thologram',
    '080-INSTANCES',
    '090-MIND',
    '100-FIELDS',
    '110-APPLICATION_OF_AWARENESS',
    '120-PREDETERMINISM',
    '510-A-About_This_Book',
    '520-C-Tholonic_Math',
    '530-D-Greek_Gods',
    '540-E-Hidden_Images',
    '550-F-An_Unexpected_Pattern',
    '580-I-Market_Data',
    '590-J-Structured_Water',
    '600-K-Sidis',
    '610-L-Thologram_and_Religion',


#    '700-X-indexes',
#    'Index',
#    'Index-by-Category'
]


H = "/home/jw/books/tholonia"
S = "Latest"


def concat():

    # CX=f"{H}/bin/DELIMG.sh '{H}/chapters/*.pdf' "
    # print(CX)
    # os.system(CX)

    clist = ""
    for c in chapters:
        clist += f"{H}/chapters/INDEXED/{c}.pdf "
    # cmd = f"pdftk {clist} cat output {H}/{S}/THOLONIA_THE_BOOK.pdf"
    cmd = f"pdftk {clist} cat output {H}/chapters/INDEXED/THOLONIA_THE_BOOK.pdf"
    print(cmd)
    os.system(cmd)

    # CX=f"{H}/bin/DELIMG.sh '{H}/chapters/THOLONIA_THE_BOOK.pdf' "
    # print(CX)
    # os.system(CX)


def delpage():
    blank = arr.array = [1, 5, 11, 16, 24, 50, 82, 97, 197, 209, 248, 262, 280, 288, 292, 297, 302, 321, 328, 334, 340, 344, 420, 421]

    pre = "pdftk ~/books/tholonia/chapters/THOLONIA_THE_BOOK.pdf cat"
    pages = ""
    final = "output x.pdf"
    for i in range(len(blank) - 1):
        fr = blank[i] + 1
        to = blank[i + 1] - 1
        pages += f"{fr}-{to} "

    pages = pages.replace("-426", "-end")
    cmd = f"{pre} {pages} {final}"
    print(cmd)
    os.system(cmd)
