# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"105229.0","system":"med"},{"code":"107494.0","system":"med"},{"code":"11761.0","system":"med"},{"code":"12500.0","system":"med"},{"code":"162.0","system":"med"},{"code":"17094.0","system":"med"},{"code":"172.0","system":"med"},{"code":"18755.0","system":"med"},{"code":"20222.0","system":"med"},{"code":"21104.0","system":"med"},{"code":"21503.0","system":"med"},{"code":"21633.0","system":"med"},{"code":"22501.0","system":"med"},{"code":"24136.0","system":"med"},{"code":"26368.0","system":"med"},{"code":"28456.0","system":"med"},{"code":"2945.0","system":"med"},{"code":"30210.0","system":"med"},{"code":"30272.0","system":"med"},{"code":"30975.0","system":"med"},{"code":"3193.0","system":"med"},{"code":"32149.0","system":"med"},{"code":"3437.0","system":"med"},{"code":"3733.0","system":"med"},{"code":"41149.0","system":"med"},{"code":"42008.0","system":"med"},{"code":"4231.0","system":"med"},{"code":"476.0","system":"med"},{"code":"48257.0","system":"med"},{"code":"59107.0","system":"med"},{"code":"60169.0","system":"med"},{"code":"65839.0","system":"med"},{"code":"66711.0","system":"med"},{"code":"8014.0","system":"med"},{"code":"93511.0","system":"med"},{"code":"96880.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('psoriasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psoriasis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psoriasis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psoriasis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
