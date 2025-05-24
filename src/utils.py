import matplotlib.pyplot as plt

def plot_bar(df, column, title):
    plt.figure(figsize=(6,3))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.show()

def plot_pie(df, column, title):
    plt.figure(figsize=(5,5))
    df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(title)
    plt.ylabel('')
    plt.show()

def plot_scatter(df, x_col, y_col, title):
    plt.figure(figsize=(6,4))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.show()