import math

def extract_data_lists(lines, scale_arc=False):

    current_list = []
    voltage_list = []
    arc_list = []
    ref_current_list = []

    idx_tuples = []
    short = False
    start = 0

    for line in lines:
        x = line.strip()
        current, voltage, isShort, reference = x.split()

        current_list.append(int(current))
        voltage_list.append(int(voltage))

        if scale_arc:
            arc_list.append(int(isShort)*300)
        else:
            arc_list.append(int(isShort))

        ref_current_list.append(int(reference))

        if int(isShort):
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

    return current_list, voltage_list, arc_list, ref_current_list, idx_tuples

def get_short_sample_avg(idx_tuples):
    size_dict = {}
    for start, end in idx_tuples:
        size = end - start
        if size not in size_dict.keys():
            size_dict[float(size)] = 1
        else:
            size_dict[float(size)] += 1

    # for key in sorted(size_dict.keys()):
    #     print("{} : {}".format(key, size_dict[key]))
    return size_dict

def get_short_sample_avg_range(idx_tuples):
    size_dict = {"10 >": 0, "50 >": 0, "100 >": 0, "150 >": 0, "300 >": 0, "300 <": 0, }

    for start, end in idx_tuples:
        size = end - start

        if size < 10:
            size_dict["10 >"] += 1
        elif size > 10 and size < 50:
            size_dict["50 >"] += 1
        elif size > 50 and size < 100:
            size_dict["100 >"] += 1
        elif size > 100 and size < 150:
            size_dict["150 >"] += 1
        elif size > 150 and size < 300:
            size_dict["300 >"] += 1
        else:
            size_dict["300 <"] += 1

    for key in sorted(size_dict.keys()):
        print("{} : {}".format(key, size_dict[key]))

def plot_data(arc_list, voltage_list, current_list, arc_list_mod):
    import matplotlib
    import matplotlib.pyplot as plt
    plt.figure(1)
    plt.plot(arc_list, 'g')
    plt.plot(voltage_list, 'b')
    plt.plot(current_list, 'y')
    plt.plot(arc_list_mod, 'r')
    plt.legend()
    plt.show()


fname_list = [
    'data/data_1.txt',
    'data/data_2.txt',
    'data/data_3.txt',
    'data/data_4.txt']

fname_list_cut_first_90p = [
    'data/data_1_cut_first_90p.txt',
    'data/data_2_cut_first_90p.txt',
    'data/data_3_cut_first_90p.txt',
    'data/data_4_cut_first_90p.txt']

fname_list_cut_last_10p = [
    'data/data_1_cut_last_10p.txt',
    'data/data_2_cut_last_10p.txt',
    'data/data_3_cut_last_10p.txt',
    'data/data_4_cut_last_10p.txt']


## Open data file
#with open(fname_list[0]) as f:
#with open(fname_list_cut_first_90p[0]) as f:
with open(fname_list_cut_last_10p[0]) as f:
    content = f.readlines()

content = content[50000:55000]

current_list, voltage_list, arc_list, ref_current_list, idx_tuples = extract_data_lists(content, scale_arc=True)

arc_list_mod = arc_list.copy()
for start, end in idx_tuples:
    #cut = int((end-start)*0.9)
    cut = math.ceil((end-start)*0.9)
    idx = start+cut
    while idx <= end:
        arc_list_mod[idx] = 0
        idx += 1

cut_region = arc_list.copy()
for start, end in idx_tuples:
    cut = math.ceil((end-start)*0.1)
    idx = start
    while idx <= end-cut:
        cut_region[idx] = 0
        idx += 1

#plot_data(arc_list, voltage_list, current_list, arc_list_mod)
#plot_data(arc_list, voltage_list, arc_list_mod, cut_region)
import matplotlib
import matplotlib.pyplot as plt
plt.figure(1)
#plt.plot(current_list, 'y')
plt.plot(arc_list, 'y')
plt.plot(voltage_list, 'b')
#plt.plot(arc_list_mod, 'g')
#plt.plot(cut_region, 'r')
plt.legend()
plt.show()
