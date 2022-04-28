import csv


def latex_to_table(filename):
    #stores events as [start states], [next states], ['event', event type]
    #stores actions as [start states], [next states], ['human/machine', movement action (if applicable), communication action (if applicable)]
    with open(filename) as csvfile:
        table = []
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            #print(row)
            [start,next,cause] = row
            cause = cause.split(",")
            #print(cause)
            if len(cause)==2:
                event = cause[1]
                entry = ["event",event]
            else:
                cause = cause[0].split("_")
                if cause[0] == "human":
                    human_action = cause[1]
                    if human_action == ("pushbutton"):
                        entry = ["human","", human_action]
                    else:
                        entry = ["human", human_action, ""]
                elif cause[0] == "machine":
                    machine_action = cause[1]
                    entry = ["machine",machine_action, ""]
            new_row = [start.split(","), next.split(","), entry]
            #print(new_row)
            table.append(new_row)
        return table





