
def extract_data_lists(lines):

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
        #arc_list.append(int(isShort)*300)
        arc_list.append(int(isShort))
        ref_current_list.append(int(reference))

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


fname_list = [
    'data/data_1.txt',
    'data/data_2.txt',
    'data/data_3.txt',
    'data/data_4.txt']

fname_list_mod = [
    'data/data_1_final.txt',
    'data/data_2_final.txt',
    'data/data_3_final.txt',
    'data/data_4_final.txt']

with open("data/data_joined_final.txt", "w") as f_joined:

    for fname in fname_list:
        ## Open data file
        with open(fname) as f:
            content = f.readlines()

        content = content[50000:]

        current_list, voltage_list, arc_list, ref_current_list, idx_tuples = extract_data_lists(content)

        arc_list_mod = arc_list.copy()
        for start, end in idx_tuples:
            cut = int((end-start)*0.9)
            idx = start+cut
            while idx <= end:
                arc_list_mod[idx] = 0
                idx += 1

        # import matplotlib
        # import matplotlib.pyplot as plt
        # plt.figure(1)
        # plt.plot(arc_list, 'g')
        # plt.plot(voltage_list, 'b')
        # plt.plot(current_list, 'r')
        # plt.plot(arc_list_mod, 'y')
        # plt.legend()
        # plt.show()

        outfile_name = fname[:-4]+"_final.txt"

        with open(outfile_name, "w") as outfile:
            for idx in range(len(current_list)):
                line = "{}\t{}\t{}\t{}\n".format(
                    current_list[idx],
                    voltage_list[idx],
                    arc_list_mod[idx],
                    ref_current_list[idx])

                outfile.write(line)
                f_joined.write(line)
