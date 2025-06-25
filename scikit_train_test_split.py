import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # [Split Your Dataset With scikit-learn's train_test_split()](https://realpython.com/train-test-split-python-data/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-07-15)

    ## [Link to code](https://github.com/realpython/materials/tree/master/sklearn-train-test-split/)

    ### Packages to add
    - python -m pip install "scikit-learn==1.5.0"
    """
    )
    return


@app.cell
def _():
    import numpy as np
    from sklearn.model_selection import train_test_split
    return np, train_test_split


@app.cell
def _(np):
    # Simple example

    # inputs - Predictors
    x = np.arange(1,25).reshape(12,2)
    # Outputs - Responses
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

    print(f"{x=}")
    print(f"{y=}")
    return x, y


@app.cell
def _(train_test_split, x, y):
    # Simple data set - defaults

    x_train, x_test, y_train, y_test = train_test_split(x,y)

    print(f"{x_train=}")
    print(f"{x_test=}")
    print(f"{y_train=}")
    print(f"{y_test=}")
    return


@app.cell
def _(train_test_split, x, y):
    # Simple data set - choose the size of the test set and get a reproducible result

    x_train_2, x_test_2, y_test_2, y_train_2 = train_test_split(x, y, test_size=4, random_state=4)

    print(f"{x_train_2=}")
    print(f"{x_test_2=}")
    print(f"{y_train_2=}")
    print(f"{y_test_2=}")
    return


@app.cell
def _(train_test_split, x, y):
    # Simple Data Set - stratify to get same ratio of zeros and ones as the original y array, classifying an imbalanced dataset

    x_train_3, x_test_3, y_test_3, y_train_3 = train_test_split(x, y, test_size=4, random_state=4, stratify=y)

    print(f"{x_train_3=}")
    print(f"{x_test_3=}")
    print(f"{y_train_3=}")
    print(f"{y_test_3=}")
    return


@app.cell
def _(train_test_split, x, y):
    # Simple Data Set - you can turn off data shuffling and random split 

    x_train_4, x_test_4, y_test_4, y_train_4 = train_test_split(x, y, test_size=4, shuffle=False)

    print(f"{x_train_4=}")
    print(f"{x_test_4=}")
    print(f"{y_train_4=}")
    print(f"{y_test_4=}")
    return


@app.cell
def _():
    from sklearn.linear_model import LinearRegression

    return (LinearRegression,)


@app.cell
def _(np):
    x2 = np.arange(20).reshape(-1,1)
    y2 = np.array([5, 12, 11, 19, 30, 29, 23, 40, 51, 54, 74,62, 68, 73, 89, 84, 89, 101, 99, 106])

    print(f"{x2=}")
    print(f"{y2=}")
    return x2, y2


@app.cell
def _(train_test_split, x2, y2):
    # dataset is divided into a training set with twelve observations and a test set with eight observations
    x_train_5, x_test_5, y_train_5, y_test_5 = train_test_split(x2, y2, test_size=8, random_state=0)

    print(f"{x_train_5=}")
    print(f"{x_test_5=}")
    print(f"{y_train_5=}")
    print(f"{y_test_5=}")
    return x_test_5, x_train_5, y_test_5, y_train_5


@app.cell
def _(LinearRegression, x_train_5, y_train_5):
    # use the training set to fit the model

    model = LinearRegression().fit(x_train_5, y_train_5)

    print(f"Best Intercept : {model.intercept_}")
    print(f"Best slope : {model.coef_}")
    return (model,)


@app.cell
def _(model, x_test_5, x_train_5, y_test_5, y_train_5):
    print(f"Coefficient of distribution using training data : {model.score(x_train_5, y_train_5)}")
    print(f"Coefficient of distribution using testing data : {model.score(x_test_5, y_test_5)}")
    return


@app.cell
def _(model, np, x_test_5, x_train_5, y_test_5, y_train_5):
    # Plot data with line of regression

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))

    plt.scatter(x_train_5, y_train_5, color='blue', label='Training data', s=80, marker='o')
    plt.scatter(x_test_5, y_test_5, color='red', label='Test data', s=80, marker='^')

    # Regression line
    x_line = np.linspace(0, 20, 100).reshape(-1, 1)  # Smooth line from 0 to 20
    y_line = model.predict(x_line)
    plt.plot(x_line, y_line, color='green', label='Regression line', linewidth=2)


    plt.legend()
    plt.grid(True)

    plt.show()
    return


if __name__ == "__main__":
    app.run()
