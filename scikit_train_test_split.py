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


if __name__ == "__main__":
    app.run()
