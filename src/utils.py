import matplotlib.pyplot as plt

def grafico_barra(df, coluna, titulo):
    plt.figure(figsize=(6,3))
    df[coluna].value_counts().plot(kind='bar', color='skyblue')
    plt.title(titulo)
    plt.show()

def grafico_pizza(df, coluna, titulo):
    plt.figure(figsize=(5,5))
    df[coluna].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(titulo)
    plt.ylabel('')
    plt.show()

def grafico_dispersao(df, x_col, y_col, titulo):
    plt.figure(figsize=(6,4))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(titulo)
    plt.show()