from client import (
    Client,
    new_client,
    client_deposit,
    withdraw_client,
    transfer_client,
    borrowing_client,
    change_information,
    paying_of_debts,
    see_account,
)

from workers import (
    Workers,
    new_worker,
    Accountant_work,
    managment,
)

from design import (
    View_services,
    the_rules,

)


list_client = [
    Client("Ahmed Benali", "1980/01/01", "10000000000000000000", "+213 500 100 100", 12500, "100001", 3200),
    Client("Mohamed Benali", "1981/02/02", "10000000000000000001", "+213 501 107 113", 26250, "100002", 6900),
    Client("Yacine Benali", "1982/03/03", "10000000000000000002", "+213 502 114 126", 40000, "100003", 10600),
    Client("Karim Benali", "1983/04/04", "10000000000000000003", "+213 503 121 139", 53750, "100004", 14300),
    Client("Sofiane Benali", "1984/05/05", "10000000000000000004", "+213 504 128 152", 67500, "100005", 18000),
    Client("Amine Benali", "1985/06/06", "10000000000000000005", "+213 505 135 165", 81250, "100006", 21700),
    Client("Ilyes Benali", "1986/07/07", "10000000000000000006", "+213 506 142 178", 95000, "100007", 25400),
    Client("Nassim Benali", "1987/08/08", "10000000000000000007", "+213 507 149 191", 108750, "100008", 29100),
    Client("Walid Benali", "1988/09/09", "10000000000000000008", "+213 508 156 204", 122500, "100009", 32800),
    Client("Adel Benali", "1989/10/10", "10000000000000000009", "+213 509 163 217", 136250, "100010", 36500),
    Client("Bilal Benali", "1990/11/11", "10000000000000000010", "+213 510 170 230", 150000, "100011", 40200),
    Client("Samir Benali", "1991/12/12", "10000000000000000011", "+213 511 177 243", 163750, "100012", 43900),
    Client("Riad Benali", "1992/01/13", "10000000000000000012", "+213 512 184 256", 177500, "100013", 47600),
    Client("Anis Benali", "1993/02/14", "10000000000000000013", "+213 513 191 269", 191250, "100014", 51300),
    Client("Hichem Benali", "1994/03/15", "10000000000000000014", "+213 514 198 282", 205000, "100015", 55000),
    Client("Reda Benali", "1995/04/16", "10000000000000000015", "+213 515 205 295", 218750, "100016", 58700),
    Client("Oussama Benali", "1996/05/17", "10000000000000000016", "+213 516 212 308", 232500, "100017", 62400),
    Client("Islam Benali", "1997/06/18", "10000000000000000017", "+213 517 219 321", 246250, "100018", 66100),
    Client("Fares Benali", "1998/07/19", "10000000000000000018", "+213 518 226 334", 260000, "100019", 69800),
    Client("Lotfi Benali", "1999/08/20", "10000000000000000019", "+213 519 233 347", 273750, "100020", 73500),
    Client("Salim Benali", "2000/09/21", "10000000000000000020", "+213 520 240 360", 287500, "100021", 77200),
    Client("Nabil Benali", "2001/10/22", "10000000000000000021", "+213 521 247 373", 301250, "100022", 80900),
    Client("Kamel Benali", "2002/11/23", "10000000000000000022", "+213 522 254 386", 315000, "100023", 84600),
    Client("Tarek Benali", "2003/12/24", "10000000000000000023", "+213 523 261 399", 328750, "100024", 88300),
    Client("Mourad Benali", "2004/01/25", "10000000000000000024", "+213 524 268 412", 342500, "100025", 92000),
    Client("Chafik Benali", "2005/02/26", "10000000000000000025", "+213 525 275 425", 356250, "100026", 95700),
    Client("Ayoub Benali", "2006/03/27", "10000000000000000026", "+213 526 282 438", 370000, "100027", 99400),
    Client("Rafik Benali", "1980/04/28", "10000000000000000027", "+213 527 289 451", 383750, "100028", 103100),
    Client("Sami Benali", "1981/05/01", "10000000000000000028", "+213 528 296 464", 397500, "100029", 6800),
    Client("Imad Benali", "1982/06/02", "10000000000000000029", "+213 529 303 477", 411250, "100030", 10500),
    Client("Ahmed Haddad", "1983/07/03", "10000000000000000030", "+213 530 310 490", 425000, "100031", 14200),
    Client("Mohamed Haddad", "1984/08/04", "10000000000000000031", "+213 531 317 503", 438750, "100032", 17900),
    Client("Yacine Haddad", "1985/09/05", "10000000000000000032", "+213 532 324 516", 452500, "100033", 21600),
    Client("Karim Haddad", "1986/10/06", "10000000000000000033", "+213 533 331 529", 466250, "100034", 25300),
    Client("Sofiane Haddad", "1987/11/07", "10000000000000000034", "+213 534 338 542", 480000, "100035", 29000),
    Client("Amine Haddad", "1988/12/08", "10000000000000000035", "+213 535 345 555", 493750, "100036", 32700),
    Client("Ilyes Haddad", "1989/01/09", "10000000000000000036", "+213 536 352 568", 507500, "100037", 36400),
    Client("Nassim Haddad", "1990/02/10", "10000000000000000037", "+213 537 359 581", 521250, "100038", 40100),
    Client("Walid Haddad", "1991/03/11", "10000000000000000038", "+213 538 366 594", 535000, "100039", 43800),
    Client("Adel Haddad", "1992/04/12", "10000000000000000039", "+213 539 373 607", 548750, "100040", 47500),
    Client("Bilal Haddad", "1993/05/13", "10000000000000000040", "+213 540 380 620", 562500, "100041", 51200),
    Client("Samir Haddad", "1994/06/14", "10000000000000000041", "+213 541 387 633", 576250, "100042", 54900),
    Client("Riad Haddad", "1995/07/15", "10000000000000000042", "+213 542 394 646", 590000, "100043", 58600),
    Client("Anis Haddad", "1996/08/16", "10000000000000000043", "+213 543 401 659", 603750, "100044", 62300),
    Client("Hichem Haddad", "1997/09/17", "10000000000000000044", "+213 544 408 672", 617500, "100045", 66000),
    Client("Reda Haddad", "1998/10/18", "10000000000000000045", "+213 545 415 685", 631250, "100046", 69700),
    Client("Oussama Haddad", "1999/11/19", "10000000000000000046", "+213 546 422 698", 645000, "100047", 73400),
    Client("Islam Haddad", "2000/12/20", "10000000000000000047", "+213 547 429 711", 658750, "100048", 77100),
    Client("Fares Haddad", "2001/01/21", "10000000000000000048", "+213 548 436 724", 672500, "100049", 80800),
    Client("Lotfi Haddad", "2002/02/22", "10000000000000000049", "+213 549 443 737", 686250, "100050", 84500),
    Client("Salim Haddad", "2003/03/23", "10000000000000000050", "+213 500 450 750", 700000, "100051", 88200),
    Client("Nabil Haddad", "2004/04/24", "10000000000000000051", "+213 501 457 763", 713750, "100052", 91900),
    Client("Kamel Haddad", "2005/05/25", "10000000000000000052", "+213 502 464 776", 727500, "100053", 95600),
    Client("Tarek Haddad", "2006/06/26", "10000000000000000053", "+213 503 471 789", 741250, "100054", 99300),
    Client("Mourad Haddad", "1980/07/27", "10000000000000000054", "+213 504 478 802", 755000, "100055", 103000),
    Client("Chafik Haddad", "1981/08/28", "10000000000000000055", "+213 505 485 815", 768750, "100056", 6700),
    Client("Ayoub Haddad", "1982/09/01", "10000000000000000056", "+213 506 492 828", 782500, "100057", 10400),
    Client("Rafik Haddad", "1983/10/02", "10000000000000000057", "+213 507 499 841", 796250, "100058", 14100),
    Client("Sami Haddad", "1984/11/03", "10000000000000000058", "+213 508 506 854", 810000, "100059", 17800),
    Client("Imad Haddad", "1985/12/04", "10000000000000000059", "+213 509 513 867", 823750, "100060", 21500),
    Client("Ahmed Boudiaf", "1986/01/05", "10000000000000000060", "+213 510 520 880", 837500, "100061", 25200),
    Client("Mohamed Boudiaf", "1987/02/06", "10000000000000000061", "+213 511 527 893", 851250, "100062", 28900),
    Client("Yacine Boudiaf", "1988/03/07", "10000000000000000062", "+213 512 534 906", 865000, "100063", 32600),
    Client("Karim Boudiaf", "1989/04/08", "10000000000000000063", "+213 513 541 919", 878750, "100064", 36300),
    Client("Sofiane Boudiaf", "1990/05/09", "10000000000000000064", "+213 514 548 932", 892500, "100065", 40000),
    Client("Amine Boudiaf", "1991/06/10", "10000000000000000065", "+213 515 555 945", 906250, "100066", 43700),
    Client("Ilyes Boudiaf", "1992/07/11", "10000000000000000066", "+213 516 562 958", 920000, "100067", 47400),
    Client("Nassim Boudiaf", "1993/08/12", "10000000000000000067", "+213 517 569 971", 933750, "100068", 51100),
    Client("Walid Boudiaf", "1994/09/13", "10000000000000000068", "+213 518 576 984", 947500, "100069", 54800),
    Client("Adel Boudiaf", "1995/10/14", "10000000000000000069", "+213 519 583 997", 961250, "100070", 58500),
    Client("Bilal Boudiaf", "1996/11/15", "10000000000000000070", "+213 520 590 110", 975000, "100071", 62200),
    Client("Samir Boudiaf", "1997/12/16", "10000000000000000071", "+213 521 597 123", 988750, "100072", 65900),
    Client("Riad Boudiaf", "1998/01/17", "10000000000000000072", "+213 522 604 136", 1002500, "100073", 69600),
    Client("Anis Boudiaf", "1999/02/18", "10000000000000000073", "+213 523 611 149", 1016250, "100074", 73300),
    Client("Hichem Boudiaf", "2000/03/19", "10000000000000000074", "+213 524 618 162", 1030000, "100075", 77000),
    Client("Reda Boudiaf", "2001/04/20", "10000000000000000075", "+213 525 625 175", 1043750, "100076", 80700),
    Client("Oussama Boudiaf", "2002/05/21", "10000000000000000076", "+213 526 632 188", 1057500, "100077", 84400),
    Client("Islam Boudiaf", "2003/06/22", "10000000000000000077", "+213 527 639 201", 1071250, "100078", 88100),
    Client("Fares Boudiaf", "2004/07/23", "10000000000000000078", "+213 528 646 214", 1085000, "100079", 91800),
    Client("Lotfi Boudiaf", "2005/08/24", "10000000000000000079", "+213 529 653 227", 1098750, "100080", 95500),
    Client("Salim Boudiaf", "2006/09/25", "10000000000000000080", "+213 530 660 240", 1112500, "100081", 99200),
    Client("Nabil Boudiaf", "1980/10/26", "10000000000000000081", "+213 531 667 253", 1126250, "100082", 102900),
    Client("Kamel Boudiaf", "1981/11/27", "10000000000000000082", "+213 532 674 266", 1140000, "100083", 6600),
    Client("Tarek Boudiaf", "1982/12/28", "10000000000000000083", "+213 533 681 279", 1153750, "100084", 10300),
    Client("Mourad Boudiaf", "1983/01/01", "10000000000000000084", "+213 534 688 292", 1167500, "100085", 14000),
    Client("Chafik Boudiaf", "1984/02/02", "10000000000000000085", "+213 535 695 305", 1181250, "100086", 17700),
    Client("Ayoub Boudiaf", "1985/03/03", "10000000000000000086", "+213 536 702 318", 1195000, "100087", 21400),
    Client("Rafik Boudiaf", "1986/04/04", "10000000000000000087", "+213 537 709 331", 1208750, "100088", 25100),
    Client("Sami Boudiaf", "1987/05/05", "10000000000000000088", "+213 538 716 344", 1222500, "100089", 28800),
    Client("Imad Boudiaf", "1988/06/06", "10000000000000000089", "+213 539 723 357", 1236250, "100090", 32500),
    Client("Ahmed Mansouri", "1989/07/07", "10000000000000000090", "+213 540 730 370", 1250000, "100091", 36200),
    Client("Mohamed Mansouri", "1990/08/08", "10000000000000000091", "+213 541 737 383", 1263750, "100092", 39900),
    Client("Yacine Mansouri", "1991/09/09", "10000000000000000092", "+213 542 744 396", 1277500, "100093", 43600),
    Client("Karim Mansouri", "1992/10/10", "10000000000000000093", "+213 543 751 409", 1291250, "100094", 47300),
    Client("Sofiane Mansouri", "1993/11/11", "10000000000000000094", "+213 544 758 422", 1305000, "100095", 51000),
    Client("Amine Mansouri", "1994/12/12", "10000000000000000095", "+213 545 765 435", 1318750, "100096", 54700),
    Client("Ilyes Mansouri", "1995/01/13", "10000000000000000096", "+213 546 772 448", 1332500, "100097", 58400),
    Client("Nassim Mansouri", "1996/02/14", "10000000000000000097", "+213 547 779 461", 1346250, "100098", 62100),
    Client("Walid Mansouri", "1997/03/15", "10000000000000000098", "+213 548 786 474", 1360000, "100099", 65800),
    Client("Adel Mansouri", "1998/04/16", "10000000000000000099", "+213 549 793 487", 1373750, "100100", 69500),
    Client("Bilal Mansouri", "1999/05/17", "10000000000000000100", "+213 500 800 500", 1387500, "100101", 73200),
    Client("Samir Mansouri", "2000/06/18", "10000000000000000101", "+213 501 807 513", 1401250, "100102", 76900),
    Client("Riad Mansouri", "2001/07/19", "10000000000000000102", "+213 502 814 526", 1415000, "100103", 80600),
    Client("Anis Mansouri", "2002/08/20", "10000000000000000103", "+213 503 821 539", 1428750, "100104", 84300),
    Client("Hichem Mansouri", "2003/09/21", "10000000000000000104", "+213 504 828 552", 1442500, "100105", 88000),
    Client("Reda Mansouri", "2004/10/22", "10000000000000000105", "+213 505 835 565", 1456250, "100106", 91700),
    Client("Oussama Mansouri", "2005/11/23", "10000000000000000106", "+213 506 842 578", 1470000, "100107", 95400),
    Client("Islam Mansouri", "2006/12/24", "10000000000000000107", "+213 507 849 591", 1483750, "100108", 99100),
    Client("Fares Mansouri", "1980/01/25", "10000000000000000108", "+213 508 856 604", 1497500, "100109", 102800),
    Client("Lotfi Mansouri", "1981/02/26", "10000000000000000109", "+213 509 863 617", 1511250, "100110", 6500),
    Client("Salim Mansouri", "1982/03/27", "10000000000000000110", "+213 510 870 630", 1525000, "100111", 10200),
    Client("Nabil Mansouri", "1983/04/28", "10000000000000000111", "+213 511 877 643", 1538750, "100112", 13900),
    Client("Kamel Mansouri", "1984/05/01", "10000000000000000112", "+213 512 884 656", 1552500, "100113", 17600),
    Client("Tarek Mansouri", "1985/06/02", "10000000000000000113", "+213 513 891 669", 1566250, "100114", 21300),
    Client("Mourad Mansouri", "1986/07/03", "10000000000000000114", "+213 514 898 682", 1580000, "100115", 25000),
    Client("Chafik Mansouri", "1987/08/04", "10000000000000000115", "+213 515 905 695", 1593750, "100116", 28700),
    Client("Ayoub Mansouri", "1988/09/05", "10000000000000000116", "+213 516 912 708", 1607500, "100117", 32400),
    Client("Rafik Mansouri", "1989/10/06", "10000000000000000117", "+213 517 919 721", 1621250, "100118", 36100),
    Client("Sami Mansouri", "1990/11/07", "10000000000000000118", "+213 518 926 734", 1635000, "100119", 39800),
    Client("Imad Mansouri", "1991/12/08", "10000000000000000119", "+213 519 933 747", 1648750, "100120", 43500),
    Client("Ahmed Belkacem", "1992/01/09", "10000000000000000120", "+213 520 940 760", 1662500, "100121", 47200),
    Client("Mohamed Belkacem", "1993/02/10", "10000000000000000121", "+213 521 947 773", 1676250, "100122", 50900),
    Client("Yacine Belkacem", "1994/03/11", "10000000000000000122", "+213 522 954 786", 1690000, "100123", 54600),
    Client("Karim Belkacem", "1995/04/12", "10000000000000000123", "+213 523 961 799", 1703750, "100124", 58300),
    Client("Sofiane Belkacem", "1996/05/13", "10000000000000000124", "+213 524 968 812", 1717500, "100125", 62000),
    Client("Amine Belkacem", "1997/06/14", "10000000000000000125", "+213 525 975 825", 1731250, "100126", 65700),
    Client("Ilyes Belkacem", "1998/07/15", "10000000000000000126", "+213 526 982 838", 1745000, "100127", 69400),
    Client("Nassim Belkacem", "1999/08/16", "10000000000000000127", "+213 527 989 851", 1758750, "100128", 73100),
    Client("Walid Belkacem", "2000/09/17", "10000000000000000128", "+213 528 996 864", 1772500, "100129", 76800),
    Client("Adel Belkacem", "2001/10/18", "10000000000000000129", "+213 529 103 877", 1786250, "100130", 80500),
    Client("Bilal Belkacem", "2002/11/19", "10000000000000000130", "+213 530 110 890", 1800000, "100131", 84200),
    Client("Samir Belkacem", "2003/12/20", "10000000000000000131", "+213 531 117 903", 1813750, "100132", 87900),
    Client("Riad Belkacem", "2004/01/21", "10000000000000000132", "+213 532 124 916", 1827500, "100133", 91600),
    Client("Anis Belkacem", "2005/02/22", "10000000000000000133", "+213 533 131 929", 1841250, "100134", 95300),
    Client("Hichem Belkacem", "2006/03/23", "10000000000000000134", "+213 534 138 942", 1855000, "100135", 99000),
    Client("Reda Belkacem", "1980/04/24", "10000000000000000135", "+213 535 145 955", 1868750, "100136", 102700),
    Client("Oussama Belkacem", "1981/05/25", "10000000000000000136", "+213 536 152 968", 1882500, "100137", 6400),
    Client("Islam Belkacem", "1982/06/26", "10000000000000000137", "+213 537 159 981", 1896250, "100138", 10100),
    Client("Fares Belkacem", "1983/07/27", "10000000000000000138", "+213 538 166 994", 1910000, "100139", 13800),
    Client("Lotfi Belkacem", "1984/08/28", "10000000000000000139", "+213 539 173 107", 1923750, "100140", 17500),
    Client("Salim Belkacem", "1985/09/01", "10000000000000000140", "+213 540 180 120", 1937500, "100141", 21200),
    Client("Nabil Belkacem", "1986/10/02", "10000000000000000141", "+213 541 187 133", 1951250, "100142", 24900),
    Client("Kamel Belkacem", "1987/11/03", "10000000000000000142", "+213 542 194 146", 1965000, "100143", 28600),
    Client("Tarek Belkacem", "1988/12/04", "10000000000000000143", "+213 543 201 159", 1978750, "100144", 32300),
    Client("Mourad Belkacem", "1989/01/05", "10000000000000000144", "+213 544 208 172", 1992500, "100145", 36000),
    Client("Chafik Belkacem", "1990/02/06", "10000000000000000145", "+213 545 215 185", 2006250, "100146", 39700),
    Client("Ayoub Belkacem", "1991/03/07", "10000000000000000146", "+213 546 222 198", 2020000, "100147", 43400),
    Client("Rafik Belkacem", "1992/04/08", "10000000000000000147", "+213 547 229 211", 2033750, "100148", 47100),
    Client("Sami Belkacem", "1993/05/09", "10000000000000000148", "+213 548 236 224", 2047500, "100149", 50800),
    Client("Imad Belkacem", "1994/06/10", "10000000000000000149", "+213 549 243 237", 2061250, "100150", 54500)
]


list_worker = [
    Workers("Karim Haddad", "70000001", 90000, "+213 551 200 110", "manager", "112134"),
    Workers("Nabil Haddad", "70000002", 55000, "+213 552 203 117", "cashier", "987356"),
    Workers("Sofiane Haddad", "70000003", 70000, "+213 553 206 124", "accountant", "123496"),
    Workers("Amine Haddad", "70000004", 45000, "+213 554 209 131", "security", "321478"),
    Workers("Yacine Haddad", "70000005", 90500, "+213 555 212 138", "manager", "112134"),
    Workers("Mohamed Benali", "70000006", 55500, "+213 556 215 145", "cashier", "987356"),
    Workers("Ahmed Benali", "70000007", 70500, "+213 557 218 152", "accountant", "123496"),
    Workers("Walid Benali", "70000008", 45500, "+213 558 221 159", "security", "321478"),
    Workers("Riad Benali", "70000009", 91000, "+213 559 224 166", "manager", "112134"),
    Workers("Hichem Benali", "70000010", 56000, "+213 560 227 173", "cashier", "987356"),
    Workers("Samir Mansouri", "70000011", 71000, "+213 551 230 180", "accountant", "123496"),
    Workers("Tarek Mansouri", "70000012", 46000, "+213 552 233 187", "security", "321478"),
    Workers("Fares Mansouri", "70000013", 91500, "+213 553 236 194", "manager", "112134"),
    Workers("Adel Mansouri", "70000014", 56500, "+213 554 239 201", "cashier", "987356"),
    Workers("Bilal Mansouri", "70000015", 71500, "+213 555 242 208", "accountant", "123496"),
    Workers("Nassim Belkacem", "70000016", 46500, "+213 556 245 215", "security", "321478"),
    Workers("Oussama Belkacem", "70000017", 92000, "+213 557 248 222", "manager", "112134"),
    Workers("Ilyes Belkacem", "70000018", 57000, "+213 558 251 229", "cashier", "987356"),
    Workers("Mourad Belkacem", "70000019", 72000, "+213 559 254 236", "accountant", "123496"),
    Workers("Kamel Belkacem", "70000020", 47000, "+213 560 257 243", "security", "321478"),
    Workers("Rafik Rahmani", "70000021", 92500, "+213 551 260 250", "manager", "112134"),
    Workers("Sami Rahmani", "70000022", 57500, "+213 552 263 257", "cashier", "987356"),
    Workers("Imad Rahmani", "70000023", 72500, "+213 553 266 264", "accountant", "123496"),
    Workers("Reda Rahmani", "70000024", 47500, "+213 554 269 271", "security", "321478"),
    Workers("Ayoub Rahmani", "70000025", 93000, "+213 555 272 278", "manager", "112134"),
    Workers("Karim Boudiaf", "70000026", 58000, "+213 556 275 285", "cashier", "987356"),
    Workers("Nabil Boudiaf", "70000027", 73000, "+213 557 278 292", "accountant", "123496"),
    Workers("Sofiane Boudiaf", "70000028", 48000, "+213 558 281 299", "security", "321478"),
    Workers("Amine Boudiaf", "70000029", 93500, "+213 559 284 306", "manager", "112134"),
    Workers("Yacine Boudiaf", "70000030", 58500, "+213 560 287 313", "cashier", "987356"),
    Workers("Mohamed Saidi", "70000031", 73500, "+213 551 290 320", "accountant", "123496"),
    Workers("Ahmed Saidi", "70000032", 48500, "+213 552 293 327", "security", "321478"),
    Workers("Walid Saidi", "70000033", 94000, "+213 553 296 334", "manager", "112134"),
    Workers("Riad Saidi", "70000034", 59000, "+213 554 299 341", "cashier", "987356"),
    Workers("Hichem Saidi", "70000035", 74000, "+213 555 302 348", "accountant", "123496"),
    Workers("Samir Ferhat", "70000036", 49000, "+213 556 305 355", "security", "321478"),
    Workers("Tarek Ferhat", "70000037", 94500, "+213 557 308 362", "manager", "112134"),
    Workers("Fares Ferhat", "70000038", 59500, "+213 558 311 369", "cashier", "987356"),
    Workers("Adel Ferhat", "70000039", 74500, "+213 559 314 376", "accountant", "123496"),
    Workers("Bilal Ferhat", "70000040", 49500, "+213 560 317 383", "security", "321478"),
    Workers("Nassim Meziane", "70000041", 95000, "+213 551 320 390", "manager", "112134"),
    Workers("Oussama Meziane", "70000042", 60000, "+213 552 323 397", "cashier", "987356"),
    Workers("Ilyes Meziane", "70000043", 75000, "+213 553 326 404", "accountant", "123496"),
    Workers("Mourad Meziane", "70000044", 50000, "+213 554 329 411", "security", "321478"),
    Workers("Kamel Meziane", "70000045", 95500, "+213 555 332 418", "manager", "112134"),
    Workers("Rafik Kaci", "70000046", 60500, "+213 556 335 425", "cashier", "987356"),
    Workers("Sami Kaci", "70000047", 75500, "+213 557 338 432", "accountant", "123496"),
    Workers("Imad Kaci", "70000048", 50500, "+213 558 341 439", "security", "321478"),
    Workers("Reda Kaci", "70000049", 96000, "+213 559 344 446", "manager", "112134"),
    Workers("Ayoub Kaci", "70000050", 61000, "+213 560 347 453", "cashier", "987356")
]


# The main program connects the client, worker, and design modules.
def main():
 while True:
    first_choice = superficial_design()

    if first_choice == "Customer Use":
        second_choice = intermediate_design_client()

        if second_choice == "Deposit money":
            name = input("Enter your full name: ")
            number_account = input("Enter your account number: ")
            balance = int(input("Enter the balance you want to deposit: "))
            client_deposit(list_client, name, number_account, balance)

        elif second_choice == "Withdraw money":
            name = input("Enter your full name: ")
            number_account = input("Enter your account number: ")
            balance = int(input("Enter the balance you want to withdraw: "))
            withdraw_client(list_client, name, number_account, balance)

        elif second_choice == "Transfar money":
            name_tran = input("Enter the sender name: ")
            number_account_tr = input("Enter the sender account number: ")
            name_received = input("Enter the receiver name: ")
            number_account_received = input("Enter the receiver account number: ")
            number_balance = int(input("Enter the balance you want to transfer: "))
            transfer_client(list_client, name_tran,number_account_tr,name_received,number_account_received,number_balance)

        elif second_choice == "Open new account":
            client = new_client()
            list_client.append(client)
            print("------the account was added to the bank------")

        elif second_choice == "Borrowing money":
            name = input("Enter your full name: ")
            number_account = input("Enter your account number: ")
            balance = int(input("Enter the balance you want to borrow: "))
            borrowing_client(list_client, name, number_account, balance)

        elif second_choice == "Take a look at our services":
            View_services()

        elif second_choice == "Paying off debts":
            name = input("Enter your full name: ")
            number_account = input("Enter your account number: ")
            payment = int(input("Enter the balance you want to pay: "))
            paying_of_debts(list_client, name, number_account, payment)

        elif second_choice == "See your account":
            number_account = input("Enter your account number: ")
            see_account(list_client, number_account)

        elif second_choice == "Change information":
            name = input("Enter your full name: ")
            number_account = input("Enter your account number: ")
            change_information(list_client, name, number_account)



    elif first_choice == "Employee Use":
        worker_choice = workers_design()

        if worker_choice == "Accounting Departement":
            name = input("Enter worker full name: ")
            cart_id = input("Enter worker cart_ID: ")
            Accountant_work(list_worker, list_client, name, cart_id)

        elif worker_choice == "New Worker":
            worker = new_worker()
            if worker is not None:
                list_worker.append(worker)
                print("------the worker was added to the bank------")

        elif worker_choice == "Managment Office":
            managment(list_worker, list_client)

    else:
        the_rules()

def superficial_design():
    print("---------hello in zaki bank---------")
    print("1)Customer Use\n2)Employee Use\n3)The rules and notes\n--In every input request don't enter the number and the symbol-- ")
    first_choise=input("Enter your choise:")
    ls=["Customer Use","Employee Use","The rules and notes"]
    for tyu in range(5):
     if first_choise not in ls:
        print("you must take one of the three choise:")
        first_choise=input("1)Customer Use\n2)Employee Use\n3)The rules and notes\nEnter your choise: ")
    return first_choise
def intermediate_design_client():
    print("----How we can help you----")
    second_choise_client=input("1)Deposit money\n2)Withdraw money\n3)Transfar money\n4)Open new account\n5)Borrowing money\n6)Take a look at our services\n7)Paying off debts\n8)See your account\n9)Change information\nEnter you choise: ")
    ls=["Deposit money","Withdraw money","Transfar money","Open new account","Borrowing money","Take a look at our services","Paying off debts","See your account","Change information"]
    for st in range(5):
       if second_choise_client not in ls:
        second_choise_client=input("you must take choise from those choises:\n1)Deposit money\n2)Withdraw money\n3)Transfar money\n4)Open new account\n5)Brrowing money\n6)Take a look at our services\n7)Paying off debts\n8)See your account\n9)Change information\nEnter you choise: ")
    return second_choise_client
def workers_design():
     request=input("1)Accounting Departement\n2)New Worker\n3)Managment Office\nEnter yuor choise: ")
     list_work=["Accounting Departement","New Worker","Managment Office"]
     for dfg in range(5):
       if request not in list_work:
        request=input("You must take choise from the three choise\n1)Accounting Department\n2)New Worker\n3)Managment Office")
     return request


if __name__=="__main__":
    main()
