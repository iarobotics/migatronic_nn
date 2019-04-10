
import math

def extract_data_lists_old(lines):

    current_list = []
    voltage_list = []
    arc_list = []
    ref_current_list = []

    idx_tuples = []
    short = False
    start = 0

    idx = 0
    for line in lines:
        x = line.strip()
        current, voltage, isShort, reference = x.split()

        current_list.append(int(current))
        voltage_list.append(int(voltage))
        #arc_list.append(int(isShort)*300)
        arc_list.append(int(isShort))
        ref_current_list.append(int(reference))

        if int(isShort):
            short = True
            if start == 0:
                #start = lines.index(line)
                start = idx
                #print('Got START idx: {}'.format(start))
        else:
            if short:
                #end = lines.index(line)
                end = idx
                #print('Got END idx: {}'.format(end))
                #print('Sample len idx: {}'.format(end-start))

                idx_tuples.append((start, end))
                short = False
                start = 0
            else:
                pass

    return current_list, voltage_list, arc_list, ref_current_list, idx_tuples

def extract_data_lists(lines):

    current_list = []
    voltage_list = []
    arc_list = []
    ref_current_list = []

    idx_tuples = []
    short = False
    start = 0

    for idx, line in enumerate(lines):
        x = line.strip()
        current, voltage, isShort, reference = x.split()

        current_list.append(int(current))
        voltage_list.append(int(voltage))
        arc_list.append(int(isShort))
        ref_current_list.append(int(reference))

        if int(isShort):
            short = True
            if start == 0:
                start = idx
        else:
            if short:
                end = idx
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
    plt.plot(current_list, 'r')
    plt.plot(arc_list_mod, 'y')
    plt.legend()
    plt.show()


fname_list = [
    'data/data_1.txt',
    'data/data_2.txt',
    'data/data_3.txt',
    'data/data_4.txt']

with open("data/data_joined_cut_first_90p.txt", "w") as f_joined:

    for fname in fname_list:
        ## Open data file
        with open(fname) as f:
            content = f.readlines()

        content = content[50000:]

        current_list, voltage_list, arc_list, ref_current_list, idx_tuples = extract_data_lists(content)

        cut_region = arc_list.copy()
        for start, end in idx_tuples:
            if end - start <= 10:
                continue
            else:
                cut = math.ceil((end-start)*0.2)
                idx = start
                while idx < end-cut:
                    cut_region[idx] = 0
                    idx += 1

        ## Generate an arc with the first 90% samples set to 0 (non-arc)
        outfile_name = fname[:-4]+"_cut_first_90p.txt"
        with open(outfile_name, "w") as outfile_first_90p:
            for idx in range(len(current_list)):
                line = "{}\t{}\t{}\t{}\n".format(
                    current_list[idx],
                    voltage_list[idx],
                    cut_region[idx],
                    ref_current_list[idx])

                outfile_first_90p.write(line)
                f_joined.write(line)
