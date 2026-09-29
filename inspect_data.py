import scipy.io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

files = {
    'Healthy': '97.mat',
    'Inner Race Fault': '105.mat',
    'Ball Fault': '118.mat',
    'Outer Race Fault': '130.mat'
}

print("--- Inspecting CWRU Dataset Keys ---\n")

for label, fname in files.items():
    file_path = os.path.join(DATA_DIR, fname)
    if os.path.exists(file_path):
        mat_data = scipy.io.loadmat(file_path)
        signal_keys = [k for k in mat_data.keys() if not k.startswith('__')]
        print(f"[{label}] ({file_path}):")
        for key in signal_keys:
            print(f"  -> {key} (Shape: {mat_data[key].shape})")
        print("-" * 40)
    else:
        print(f"File missing: {file_path}")
