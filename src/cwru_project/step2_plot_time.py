import argparse
import os

import matplotlib.pyplot as plt
import scipy.io


def main():
    parser = argparse.ArgumentParser(description="Plot CWRU healthy vs faulty signal")
    parser.add_argument(
        "--data-dir",
        default="data",
        help="folder containing the .mat files (default: data)",
    )
    args = parser.parse_args()

    healthy_data = scipy.io.loadmat(os.path.join(args.data_dir, '97.mat'))
    faulty_data = scipy.io.loadmat(os.path.join(args.data_dir, '105.mat'))

    healthy_signal = healthy_data['X097_DE_time'][:1000]
    faulty_signal = faulty_data['X105_DE_time'][:1000]

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(healthy_signal, color='green')
    plt.title('Healthy Motor Signal (Time Domain)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(faulty_signal, color='red')
    plt.title('Inner Race Fault Signal (Time Domain)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()