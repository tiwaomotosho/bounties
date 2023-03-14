import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")


def read_file(input_file, delimiter, has_header=True, names=None):
    if has_header:
        return pd.read_csv(input_file, delimiter=r"{}+".format(delimiter))
    else:
        return pd.read_csv(
            input_file, delimiter=r"{}+".format(delimiter), header=None, names=names
        )


# Graph style
# Graph style
# plt.rcParams['font.size'] = 8
# plt.rcParams['lines.linewidth'] = 2
# plt.rcParams['lines.marker'] = 'o'


# # Line graph
# def line_graph(input_file, x_col, y_col, title):
#     data = pd.read_csv(input_file, delimiter=delimiter)
#     sns.lineplot(data=data, x=x_col, y=y_col)
#     plt.xlabel(x_col)
#     plt.ylabel(y_col)
#     plt.title(title)
#     plt.show()


# Bar chart
def bar_chart(input_file, x_col, y_col, title):
    df = read_file(input_file, delimiter, has_header=has_header, names=names)
    # print(data)
    sns.set_style("darkgrid")
    sns.barplot(x=df.columns[0], y=df.columns[1], data=df)
    plt.title("Bar Chart", fontsize=18)
    plt.xlabel("X Label", fontsize=14)
    plt.ylabel("Y Label", fontsize=14)
    plt.show()


# Example usage
if __name__ == "__main__":
    input_file = "sample-bar.txt"
    # x_col = "Year"
    # y_col = "Revenue"
    # title = "Revenue by Year"
    # line_graph(input_file, x_col, y_col, title)

    # Input file format
    delimiter = " "  # or ','
    has_header = False
    names = ["Col1", "Col2"]
    x_col = "Col1"
    y_col = "Col2"
    title = "Sample Title"
    bar_chart(input_file, x_col, y_col, title)

    # print(read_file("sample-bar.txt", delimiter, False, ["Col1", "Col2"]))
