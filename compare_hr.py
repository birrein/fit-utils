"""
Heart Rate Data Comparison Script

This script reads heart rate data from two FIT files and plots a comparison between the two data sets.

Usage:
    1. Ensure you have the `fitparse` and `matplotlib` libraries installed.
       You can install these using pip:
       $ pip install fitparse matplotlib

    2. Place the FIT files in a directory named 'fit' in the same directory as this script.
       Update the file paths in the `main` function if necessary.

    3. Run the script:
       $ python script_name.py

"""
import fitparse
import matplotlib.pyplot as plt


def read_heart_rate_data(file_path):
    fitfile = fitparse.FitFile(file_path)
    heart_rates = []

    for record in fitfile.get_messages("record"):
        for record_data in record:
            if record_data.name == "heart_rate":
                heart_rates.append(record_data.value)

    return heart_rates


def plot_heart_rate_comparison(hr_data1, hr_data2, label1, label2):
    plt.figure(figsize=(10, 5))

    plt.plot(hr_data1, label=label1)
    plt.plot(hr_data2, label=label2)
    plt.xlabel("Muestras")
    plt.ylabel("Frecuencia Cardíaca (BPM)")
    plt.title("Comparación de Frecuencia Cardíaca")
    plt.legend()
    plt.show()


def main():
    file_path1 = "fit/tp-2725125.2024-07-11-02-20-15-247Z.GarminPing.AAAAAGaPQV5UumZS.fit"
    file_path2 = "fit/zwift-activity-1650478932568309776.fit"

    label1 = "Garmin - Fenix 7"
    label2 = "Zwift - Whoop"

    hr_data1 = read_heart_rate_data(file_path1)
    hr_data2 = read_heart_rate_data(file_path2)

    plot_heart_rate_comparison(hr_data1, hr_data2, label1, label2)


if __name__ == "__main__":
    main()
