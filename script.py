# import matplotlib
# import matplotlib.pyplot as plt
import numpy as np

def plot():
    #[1011, 1005, 1000, 992]
    # x axis values
    x = time_list
    # corresponding y axis values

    y1 = current_list
    y2 = voltage_list
    y3 = short_list

    # plotting the line 1 points
    plt.plot(x, y1, label = "Measured current")

    # line 2 points
    # plotting the line 2 points
    plt.plot(x, y2, label = "Measured Voltage")

    # line 2 points
    # plotting the line 2 points
    plt.plot(x, y3, label = "Short-circuit")

    # naming the x axis
    plt.xlabel('time (s)')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title('Two lines on same graph!')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

def separate_short(lines):
    current_list = []
    voltage_list = []
    short_list = []
    ref_list = []
    for line in lines:
        current, voltage, isShort, reference = line.split()
        current_list.append(float(current))
        voltage_list.append(float(voltage))
        short_list.append(int(isShort)*1000)
        ref_list.append(float(reference))

        if int(isShort) == 1:
            with open("data/short.txt", "a") as outfile:
                outfile.write(line+'\n')
        else:
            with open("data/non_short.txt", "a") as outfile:
                outfile.write(line+'\n')

def join_data(fname_list: None):
    content = []
    for fname in fname_list:
        with open(fname) as f:
            lines = f.readlines()
            content.extend(lines[50000:])

    with open("data/data_joined_mod.txt", "a") as outfile:
        outfile.writelines(content)

def modify_short(lines):

    idx_tuples = []
    short = False
    start = 0

    for line in lines:
        x = line.strip()
        current, voltage, isShort, reference = x.split()

        if int(isShort) == 1:
            short = True
            if start == 0:
                start = lines.index(line)
                #print('Got START idx: {}'.format(start))
        else:
            if short:
                end = lines.index(line)
                #print('Got END idx: {}'.format(end))
                #print('Sample len idx: {}'.format(end-start))

                idx_tuples.append((start, end))
                short = False
                start = 0
            else:
                pass
    return idx_tuples


def modify_content(content: None, fname: str):
    idx_tuples = modify_short(content)

    start, end = idx_tuples[0]
    cut = int((end-start)*0.9)

    for start, end in idx_tuples:
        for line in content[start+cut:end]:
            #print("OLD: {}".format(line))
            x = line.strip()
            current, voltage, isShort, reference = x.split()
            isShort = 0
            idx = content.index(line)
            content[idx] = "{}\t{}\t{}\t{}\n".format(current, voltage, isShort, reference)
            #print("NEW: {}".format(content[idx]))

    with open(fname, "w") as outfile:
        outfile.writelines(content)


# fname_list = ['data/data_1.txt',
#               'data/data_2.txt',
#               'data/data_3.txt',
#               'data/data_4.txt',
#               'data/data_joined.txt']

# for fname in fname_list:
#     with open(fname) as f:
#         content = f.readlines()
#     dest_name = fname+'_mod'
#     modify_content(content, dest_name)


fname_list_mod = ['data/data_1.txt_mod',
                  'data/data_2.txt_mod',
                  'data/data_3.txt_mod',
                  'data/data_4.txt_mod']

join_data(fname_list_mod)
