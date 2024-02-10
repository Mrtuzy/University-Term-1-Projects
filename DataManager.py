import os
###### READ ME #################
# I add a new future that we can save previous file creaion. I added for debugging but ı think is useful with this 
# you can add or do other operation previous file for example you create file and exit than you run again
# now you can add something and exit again. If you create a file with this program you can edit any time.
#Please check first Main part.
def Create(query):
    #Get datas
    split_query = query.split()
    file_name_str = split_query[2]
    file_name = f"./{file_name_str}.txt"
    attributes = split_query[4]
    attributes_with_id = "id,"+split_query[4]
    #Create File
    if "id" in attributes:
        print("You cannot create a file with attribute 'id'.")
    elif os.path.isfile(file_name):
        file = open(file_name,"w")
        file.write(attributes_with_id)
        file.close() 
        print("There was already such a file. It is removed and then created again.")
    else:
        file = open(file_name,"w")
        file.write(attributes_with_id)
        file.close() 
        print("Corresponding file was successfully created.")
    return file_name_str,attributes_with_id.split(",")
def Delete(query):
    # Get datas
    split_query = query.split()
    file_name_str = split_query[2]
    file_name = f"./{file_name_str}.txt"
    #Delete file
    if os.path.isfile(file_name):
         os.remove(file_name)
         print("Corresponding file was successfully deleted.")
    else:
        print("There is no such file.")
    return file_name_str
def Display(files):
    counter = 1
    print(f"Number of files: {len(files)}")
    for file in files:
        print(f"{counter}) {file}:",",".join(files[file]["attributes"]))
        counter += 1
def Add(query,files):
    #get datas
    split_query = query.split()
    query_attributes = split_query[1]
    query_attributes_with_id = "id,"+split_query[1]
    file_name_str = split_query[3]
    file_name = f"./{file_name_str}.txt"
    ### file exception
    if os.path.isfile(file_name):
        len_attributes = len(files[file_name_str]["attributes"])
        len_query_attributes = len(query_attributes_with_id.split(","))
        #Controls
        if len_attributes != len_query_attributes:
            print("Numbers of attributes do not match.")
        else:

            file = open(file_name,"r")
            lines = file.readlines()
            file.close()
            file = open(file_name,"a")
            last_id = lines[-1].split(",")[0]
            if last_id.isdigit():
                id = str(int(last_id)+1)
            else:
                id = 1
            #Add
            file.write(f"\n{id},{query_attributes}")
            # modify files
            files[file_name_str]["lines"].append(f"{id},{query_attributes}")
            print(f"New line was successfully added to books with id= {id}.")
    else:
        print("There is no such a file")
def Remove(query,files):
    # get datas
    split_query = query.split()
    query_condition_str = split_query[5]
    file_name_str = split_query[3]
    file_name = f"./{file_name_str}.txt"
    if os.path.isfile(file_name):
        # file operation
        file = open(file_name,"r")
        lines = file.readlines()[1:]
        file.close()
        file = open(file_name,"w")
        #Remove
        file.write(",".join(files[file_name_str]["attributes"]))
        delete_counter = 0
        for line in lines:
            line = line.replace("\n","")
            if "==" in query_condition_str:
                query_condition_elements = query_condition_str.split("==")
                try:
                    column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                    value = query_condition_elements[1]
                    if not (line.split(",")[column] == value):
                        file.write("\n"+line)
                    else:
                        files[file_name_str]["lines"].remove(line)
                        delete_counter += 1 
                except ValueError:
                    print(f"Your query contains an unknown attribute: {query_condition_elements[0]}")            
            else:
                query_condition_elements = query_condition_str.split("!=")
                try:
                    column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                    value = query_condition_elements[1]
                    if not (line.split(",")[column] != value):
                        file.write("\n"+line)
                    else:
                        files[file_name_str]["lines"].remove(line)
                        delete_counter += 1
                except ValueError:
                    print(f"Your query contains an unknown attribute: {query_condition_elements[0]}")         
        if delete_counter > 0:
            print(f" {delete_counter} lines were successfully removed.")  
    else:
        print("There is no such a file")
def Modify(query,files):
    # get datas
    split_query = query.split()
    query_condition_str = split_query[7]
    file_name_str = split_query[3]
    file_name = f"./{file_name_str}.txt"
    if os.path.isfile(file_name):
        modify_column =  files[file_name_str]["attributes"].index(split_query[1])
        modify_value = split_query[5]
        # file operation
        file = open(file_name,"r")
        lines = file.readlines()[1:]
        file.close()
        file = open(file_name,"w")
        #Modify
        file.write(",".join(files[file_name_str]["attributes"]))
        line_index = 0
        modify_count = 0
        for line in lines:
            line = line.replace("\n","")
            if "==" in query_condition_str:
                query_condition_elements = query_condition_str.split("==")
                try:
                    condition_column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                    condition_value = query_condition_elements[1]
                    if not (line.split(",")[condition_column] == condition_value):
                        file.write("\n"+line)
                    else:
                        modify_line_list = line.split(",")
                        modify_line_list[modify_column] = modify_value
                        modify_line =",".join(modify_line_list)
                        file.write("\n"+modify_line)
                        files[file_name_str]["lines"][line_index] = modify_line
                        modify_count += 1
                except ValueError:
                    print(f"Your query contains an unknown attribute: {query_condition_elements[0]}")
            else:
                query_condition_elements = query_condition_str.split("!=")
                try:
                    condition_column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                    condition_value = query_condition_elements[1]
                    if not (line.split(",")[condition_column] != condition_value):
                        file.write("\n"+line)
                    else:
                        modify_line_list = line.split(",")
                        modify_line_list[modify_column] = modify_value
                        modify_line =",".join(modify_line_list)
                        file.write("\n"+modify_line)
                        files[file_name_str]["lines"][line_index] = modify_line
                        modify_count += 1
                except ValueError:
                    print(f"Your query contains an unknown attribute: {query_condition_elements[0]}")
            line_index += 1
        print(f"{modify_count} were successfully modify")
    else:
        print("There is no such a file")
def Fetch(query,files):
    split_query = query.split()
    attributes_str = split_query[1]
    attributes = attributes_str.split(",")
    file_name_str = split_query[3]
    condition_str = split_query[5]
    lines = files[file_name_str]["lines"]
    condition_check_count = 0
    condition_check_list = []
    for line in lines:
        if "==" in condition_str:
            query_condition_elements = condition_str.split("==")
            if query_condition_elements[0] in files[file_name_str]["attributes"]:
                condition_column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                condition_value = query_condition_elements[1]
                if line.split(",")[condition_column] == condition_value:
                        condition_check_list.append(line)
                        condition_check_count += 1
            else:
                print("Your query conta ins an unknown attribute .") 
                break        
        else:
            query_condition_elements = condition_str.split("!=")
            if query_condition_elements[0] in files[file_name_str]["attributes"]:
                condition_column = files[file_name_str]["attributes"].index(query_condition_elements[0])
                condition_value = query_condition_elements[1]
                if line.split(",")[condition_column] != condition_value:
                    condition_check_list.append(line)
                    condition_check_count += 1
            else:
                print("Your query conta ins an unknown attribute .")  
                break
    print(f"Number of lines in file {file_name_str}:",len(files[file_name_str]["lines"])) 
    print(f"Number of lines that hold the condition:",len(condition_check_list)) 
    attributes_data = []
    for line in condition_check_list:
        attributes_row = [] 
        split_line = line.split(",") 
        for attribute in attributes:
            attribute_column = files[file_name_str]["attributes"].index(attribute)
            attributes_row.append(split_line[attribute_column])
        attributes_data.append(attributes_row)
    print_table(attributes_data,attributes)        
        
def print_table(data, headers):
    # Print column headers
    empty = ""
    header_row = f"|{empty:^10}".join(headers)
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))

    # Print data rows
    for row in data:
        row_str = f"|{empty:<10}".join(row)
        print(row_str)

    print("-" * len(header_row))
def Main():
    # Our files stored in a dict like below
    files = {} # {"filename":{"attributes":[1,2,3],"lines":[1,2,3]}}
    # our files.txt format is like below
    #filename-1,2,3-1,2,3|3,4,5
    #otherfilename-1,2,3-1,2,3|3,4,5
    ###################################
    # this part for saving previous edit and creation If you exit the program ıt will save your creations
    # in below we get datas on files.txt
    file_text = "./files.txt"
    if not (os.path.isfile(file_text)):
        data = open(file_text,"a")
        data.close()
    data = open(file_text,"r")
    lines = data.readlines()
    for line in lines:
        split_line = line.split("-")
        filename = split_line[0]
        attributes = split_line[1]
        lines = split_line[2]
        files[filename] = {}
        files[filename]["attributes"] = []
        files[filename]["lines"] = []
        files[filename]["attributes"] = attributes.replace("\n","").split(",")
        files[filename]["lines"] = lines.replace("\n","").replace("null|","").split("|")
    data.close()
    #################################
    while True:
        #print(files) #for debugging
        print("What is your Query?")
        query = input()
        #we check the operation
        if query == "exit":
            break
        elif query.startswith("create file"):
            filename,attributes = Create(query)
            files[filename] = {}
            files[filename]["attributes"] = attributes
            files[filename]["lines"] = []
        elif query.startswith("delete file"):
            filename = Delete(query)
            files.pop(filename)
        elif query.startswith("display files"):
            Display(files)
        elif query.startswith("add"):
            Add(query,files)
        elif query.startswith("remove lines"):
            Remove(query,files)
        elif query.startswith("modify"):
            Modify(query,files)
        elif query.startswith("fetch"):
            Fetch(query,files)
        else:
            print("Invalid query.")
    #########################
    # we write again all changing and creations to the files.txt
    data = open(file_text,"w")
    for info in files:
        data.write(f"{info}-")
        data.write(",".join(files[info]["attributes"])+"-")
        if files[info]["lines"] == []:
            data.write("null")
        else:
            data.write("|".join(files[info]["lines"]))
        data.write("\n")
    data.close()

Main()
