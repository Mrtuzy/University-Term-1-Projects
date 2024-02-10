def main():
    isContinue = True
    # these arrays for organization 
    file_names = ["categories.txt","products.txt","portions.txt"]
    insert_texts = ["category","product","portion"]
    # for result
    bill = []
    total = 0
    # main loop
    while isContinue:
        selection = "null"
        text = "Welcome to the Store"
        received_product = []
        # secondary loop for product selection
        for index in range(3):
            # I collect data, print and redefined variables every iteration
            data = prepareInfo(file_names[index],selection)
            printMenu(data,text)
            try :
                selection,text = getUserInput(data,index,insert_texts[index])
            except ValueError:
                print("PLEASE TYPE IN CORRECT FORMAT\n")
                selection,text = getUserInput(data,index,insert_texts[index])
            # collecting product's fields
            received_product.append(text) 
        total += float(selection)    
        received_product.append(selection)
        bill.append(received_product)
        isContinue = input("Would you like to complete the order (y, n)?") == "y"   
    printBill(bill,total)
# printing bill
def printBill(bill,total):
    print("\nOrder Recipe")
    print("===================================================================================================================")
    for product in bill:
        print("{:<25} {:<35} {:<20} {:<3}$".format(*product))
    print("===================================================================================================================")
    fomat_total = "{0:.2f}".format(total)
    print(f"Total:{fomat_total}$")
# that func get important datas according to user choice
def getUserInput(data,index,insert_text):
    user_input = int(input(f"Please select the {insert_text}: "))
    text_value = data[user_input-1][1]
    format_input = data[user_input-1][0]
    if index != 0:
        format_input = data[user_input-1][2]
    
    return format_input,text_value
#print menu according to data    
def printMenu(data,text):
    print(f"-----------\n{text}\n-----------")
    counter = 0
    for i in data:
        print(f"{counter+1}. {data[counter][1]}")
        counter += 1
# if selection isn't null than collect data according to selection if its null then collect everything
def prepareInfo(file_name,user_selection = "null"):
    infos = []
    file = open(file_name,"r")
    lines = file.readlines()
    if user_selection != "null":
        for line in lines:
            clean_line = removeSymbols(line)
            format_line = clean_line.split(";")
            if format_line[0] == user_selection:
                infos.append(format_line)
    else:
        for line in lines:
            clean_line = removeSymbols(line)
            format_line = clean_line.split(";")
            infos.append(format_line)

    file.close()
    return infos
# cleaning the text
def removeSymbols(text):
    symbols = ["#","\n"]
    for digit in text:
        for symbol in symbols:
            if digit == symbol:
                text = text.replace(symbol,"") 
    return text

main()
