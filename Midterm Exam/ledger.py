from os import path

def readfile (inpath):
    # open file creating a context so that it is automatically created
    # and process line by line in to a list of strings
    with open(inpath, 'r') as infileobject:
        lines = infileobject.readlines()
    ledger = []
    for line in lines:
        columns = line.split("\t")
        if len(columns) == 4:
            entrydate = columns[0]
            explanation = columns[1]
            
            
            debittext = columns[2]
            debittext = debittext.replace(",",".")
            debit = float (debittext)
            
            credittext = columns[3]
            credittext = credittext.replace(",",".")
            credit = float(credittext)
            
            entry = (entrydate, explanation, debit, credit)
            # print(entry)
            ledger.append(entry)
    return ledger

def processledger(ledger):
    sumdebit = 0.0
    sumcredit = 0.0    
    for entry in ledger:
        debit = entry[2]
        sumdebit = sumdebit + debit
        credit = entry[3]
        sumcredit = sumcredit + credit    
    balance = 0.0
    if sumdebit >= sumcredit:
        balance = sumdebit - sumcredit
        print("This account balance is", balance, "(Debit)")
    else:
        balance = sumcredit - sumdebit
        print("This account balance is", balance, "(Credit)")
    return

# create file path
path = path.realpath("./")
# windows
path = path.replace("\\", "/")
filepath=path + "/Tab Seperated Ledger.txt"
print("Processing file at: ", filepath)

# process input file
ledger = readfile(filepath)
# process ledger
processledger(ledger)
