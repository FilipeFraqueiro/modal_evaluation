import matplotlib.pyplot as plt
import pandas as pd
# 1
# 2
# 3
# 4
# 5
def modal_analysis(sum_threshold, fraction_threshold, cut_off, limit_freqs_low, limit_freqs_high, frequencies, fraction, sum_, DOF):
    text_out = ""
    print(DOF, ":")
    text_out += DOF + ":" + "\n"

    for freq, T1_fraction, T1_sum in zip(frequencies, fraction, sum_):
        # verify if fraction is higher than the threshold
        if T1_fraction > fraction_threshold:
            # if it is verify if it lies between the danger zone
            for freq_low, freq_high in zip(limit_freqs_low, limit_freqs_high):
                if freq_low <= freq <= freq_high:
                    print("Frequency :", freq, "\tFraction: ", T1_fraction, "\tPROBLEMATIC!!!")
                    text_out += "Frequency :" + str(freq) + "\tFraction: " + str(T1_fraction) + "\tPROBLEMATIC!!!" + "\n"
        
        # break loop if the sum gets bigger than the threshold
        if T1_sum > sum_threshold:
            print("Limit frequency: ", freq, "\tSum: ", T1_sum*100)
            text_out += "Limit frequency: " + str(freq) + "\tSum: " + str(T1_sum*100) + "\n"
            break


    frequencies = frequencies[:cut_off]
    fraction = [val * 100 for val in fraction[:cut_off]]

    return frequencies, fraction, text_out
# 1
# 2
# 3
# 4
# 5
def main(file_name, sum_threshold, fraction_threshold, cut_off):
    text_out = ""

    # read data from excel
    df = pd.read_excel(file_name)

    fig, axs = plt.subplots(nrows=3, ncols=2)

    # thresholds
    # sum_threshold = 0.85
    # fraction_threshold = 0.03

    # number of frequencies to represent
    # set to -1 to show all
    # cut_off = -1
    if cut_off == -1:
        cut_off = len(df)

    # bar plot bars width
    w = 1

    # engine frequencies limits
    band = 0.065

    # engine frequencies
    engine_freqs = [68, 136, 204, 272]

    # engine frequencies low limit
    limit_freqs_low = [freq - band * freq for freq in engine_freqs]

    # engine frequencies high limit
    limit_freqs_high = [freq + band * freq for freq in engine_freqs]

    # print engine frequencies limits
    for freq_low, freq_high in zip(limit_freqs_low, limit_freqs_high):
        print("[ ", freq_low, "\t", freq_high, " ]")
        

    # define data to show
    fraction_data = ["T1_FRACTION", "T2_FRACTION", "T3_FRACTION", "R1_FRACTION", "R2_FRACTION", "R3_FRACTION"]
    sum_data = ["T1_SUM", "T2_SUM", "T3_SUM", "R1_SUM", "R2_SUM", "R3_SUM"]
    DOF_data = ["T1", "T2", "T3", "R1", "R2", "R3"]
    colors = ["r", "g", "b"] * 2
    frequencies = df["Frequency"]

    position = [w, ]
    
    i = 0
    j = 0
    for data1, data2, DOF, color in zip(fraction_data, sum_data, DOF_data, colors):
        fraction = df[data1]
        sum_ = df[data2]

        # analyse the data
        freqs, frac, text_out_ = modal_analysis(sum_threshold, fraction_threshold, cut_off, limit_freqs_low, limit_freqs_high, frequencies, fraction, sum_, DOF)
        text_out += text_out_

        # increment j axis
        if i == 3:
            j = 1
            i = 0

        # plot limit bands
        for freq_low, freq_high in zip(limit_freqs_low, limit_freqs_high):
            axs[i, j].fill_between([freq_low, freq_high], [100, 100], color=(0, 0, 1, 0.3))
        
        # plot the bars
        axs[i, j].bar(freqs, frac, width=w, align='center', alpha=1, color=color, label=DOF)

        i += 1


    # plot details
    fig.suptitle("Modal Analysis")
    axs[0, 0].set_title("Translation DOF's")
    axs[0, 1].set_title("Rotation DOF's")
    axs[2, 0].set_xlabel("Frequency [Hz]")
    axs[2, 1].set_xlabel("Frequency [Hz]")
    axs[1, 0].set_ylabel("Percentage [%]")

    # save figure
    fig.savefig('modal_plots.png')
    
    # show plot
    plt.show()

    return text_out
# 1
# 2
# 3
# 4
# 5
if __name__ == "__main__":
    file_name = "modal_inputs.xlsx"
    main(file_name, 0.85, 0.03, -1) 