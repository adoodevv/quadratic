import pandas as pd
import numpy as np

def find_roots(coefficients):
    a, b, c = coefficients
    # Calculate the discriminant
    delta = b ** 2 - 4 * a * c

    # Check if roots are real or complex
    if delta > 0:
        root1 = (-b + np.sqrt(delta)) / (2 * a)
        root2 = (-b - np.sqrt(delta)) / (2 * a)
        return root1, root2
    elif delta == 0:
        root = -b / (2 * a)
        return root,
    else:
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(abs(delta)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


def process_excel(input_file, output_file):
    df = pd.read_excel(input_file)

    coefficients = df[['a', 'b', 'c']].values

    df['Roots'] = df.apply(lambda row: find_roots(row[['a', 'b', 'c']]), axis=1)

    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_file = "input_data.xlsx"
    output_file = "output_data.xlsx"

    process_excel(input_file, output_file)