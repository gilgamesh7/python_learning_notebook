import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    #  Pandas example using builder pattern

    import pandas as pd

    df = pd.DataFrame()
    return


@app.cell
def _(mo):
    mo.md(r"""# [Ways to Define Functions in Python](https://youtu.be/OdDI-5PBpSk?si=FC0bBIxiOYGxaL5x)""")
    return


@app.cell
def _():
    # Simple

    def greet(name:str)->str:
        return(f"Hello {name}")

    print(greet("Leah"))
    return


@app.cell
def _():
    # Lambda

    greet_lambda = lambda name: f"Hello {name}"

    print(greet_lambda("Leah"))
    return


@app.cell
def _():
    # Partial Function Application

    from functools import partial

    def power(base:int, exponent:int)-> int:
        return base**exponent

    square = partial(power, exponent=2)
    two_power = partial(power,base=2)

    print(f"{power(5,3)=}")
    print(f"{square(base=5)=}")
    print(f"{two_power(exponent=5)=}")
    return


@app.cell
def _():
    # decorators

    from typing import Any, Callable
    from functools import wraps

    def print_result(
            fmt:str = "Result : ",
        ) -> Callable[[Callable[[Any],Any]], Callable[[Any],Any]]:
        def decorator(func: Callable[[Any],Any]) -> Callable[[Any],Any]:
            @wraps(func)
            def wrapper(x: Any)-> Any:
                result = func(x)
                print(fmt.format(result))
                return result

            return wrapper

        return decorator

    @print_result(fmt="Computed Value => {}")
    def double(number: int)-> int:
        return number*2

    double(15)

    return


@app.cell
def _():
    # Class + dunder method

    class Greeter:
        def __call__(self, name: str)-> str:
            return f"Hello {name}"

    greet_dunder = Greeter()
    print(greet_dunder("Kristin"))

    return


@app.cell
def _():
    # Adding values to a function
    def main()-> None:
        print("Soolam veri Karuppu")

    main.my_property = "Karuppusamy"
    print(main.my_property)
    return


@app.cell
def _(add):
    # exec

    exec("def add(x:int, y:int): return x+y")

    print(add(4,6))
    return


@app.cell
def _():
    # eval

    add_func = eval("lambda x,y: x+y")
    print(add_func(5,6))
    return


@app.cell
def _():
    # types.new 

    import types

    DynamicFunction = types.new_class(
        "DynamicFunction",
        (),
        {},
        exec_body=lambda ns: ns.update({"__call__": lambda self,x: x*3})
    )
    triple = DynamicFunction()

    print(triple(6))
    return (types,)


@app.cell
def _(types):
    # Manually from Byte Code
    # WILL NOT WORK in 3.10 + !

    # 3.10 Bytecode
    # 0 LOAD_FAST 0 (x)
    # 2 LOAD_CONST 1 (42)
    # 4 BINARY_ADD
    # 6 RETURN_VALUE

    bytecode = bytes(
        [
            124,
            0, # LOAD_FAST x (arg 0)
            100,
            1, # LOAD_CONST 42 (arg 1)
            23,
            0,  # BINARY_ADD
            83,
            0,  # RETURN_VALUE
        ]
    )


    constants = (None, 42)
    varnames = ("x",)

    # Create a CodeType for 3.10
    code = types.CodeType(
        1,  # co_argcount
        0,  # co_posonlyargcount
        0,  # co_kwonlyargcount
        1,  # co_nlocals
        2,  # co_stacksize
        0x43,  # co_flags (OPTIMIZED | NEWLOCALS | NOFREE)
        bytecode,  # co_code
        constants,  # co_consts
        (),  # co_names
        varnames,  # co_varnames
        "<manual>",  # co_filename
        "add_42",  # co_name
        1,  # co_firstlineno
        b"\x00\x01",  # co_lnotab
        (),  # co_freevars
        (),  # co_cellvars
    )

    func = types.FunctionType(code, globals(), "add_42")

    print(func(5))  # ✅ Output: 47


    return


@app.cell
def _(mo):
    mo.md(r"""# [Class methods in APIs](https://youtu.be/Ov8JsEnNLCM?si=ZMUopDQZtXcfHAIw)""")
    return


@app.cell
def _():
    from pydantic import BaseModel, EmailStr
    from uuid import uuid4
    import json

    fake_user_db = {
        str(uuid4()) : {"id": str(uuid4()), "name": "John Doe", "email": "john.doe@example.com"},
        str(uuid4()): {"id": str(uuid4()), "name": "Jane Smith", "email": "jane.smith@example.com"},
        str(uuid4()): {"id": str(uuid4()), "name": "Raj Patel", "email": "raj.patel@example.com"}
    }

    class User(BaseModel):
        id: str
        name : str
        email : EmailStr

        @classmethod
        def find(cls, token:str)-> list["User"]:
            # json_data = json.dumps(fake_user_db, indent=4)

            return [cls(**user) for user in fake_user_db.values()]

            # return [user for user in fake_user_db.values()]


    print(User.find("secret_token")) 
    print(f"\n")

    # [User(id='04aaff2c-96fe-45a5-a44d-ac7c5ff19900', name='John Doe', email='john.doe@example.com'), User(id='b2fc851d-8edd-40ac-9d0f-0bee655a5f77', name='Jane Smith', email='jane.smith@example.com'), User(id='dc7e0322-a646-41c1-b525-e9b18eb3e18c', name='Raj Patel', email='raj.patel@example.com')]

    # [{'id': '33c38c93-6305-457e-984c-8eb35b75c54b', 'name': 'John Doe', 'email': 'john.doe@example.com'}, {'id': '64bd7a22-ae67-469d-9501-7d370e3c0f1a', 'name': 'Jane Smith', 'email': 'jane.smith@example.com'}, {'id': '9a69fd31-2961-43c0-989d-5653f71c3b89', 'name': 'Raj Patel', 'email': 'raj.patel@example.com'}]

    return


@app.cell
def _(mo):
    mo.md(r"""**[Builder for HTML page](https://youtu.be/2f1FkGQTarc?si=EKWlKxoA1b7lBkCS)**""")
    return


@app.cell
def _():
    from dataclasses import dataclass

    @dataclass
    class HTMLPage:
        title: str
        body: str

        def render(self)-> str:
            return f"""
                <html>
                    <head>
                        <title> {self.title} </title>
                    </head>
                    <body>
                        {self.body}
                    </body>
                </html>
            """

    page = HTMLPage(
        title="In God we Trust",
        body="<h1>In God We Trust</h1><p> All others must pay cash</p>"
    )

    print(page.render())

    return HTMLPage, dataclass


@app.cell
def _(HTMLPage, mo):
    # Use builder for above

    from typing import Self

    class HTMLBuilder():
        def __init__(self, title: str):
            self.title = title
            self.body_content = []

        def add_heading(self, text: str, level: int=1)-> Self :
            self.body_content.append(f"<h{level}> {text} </h{level}>")

            return self

        def add_paragraph(self, text: str)-> Self:
            self.body_content.append(f"<p> {text} </p>")

            return self

        def build(self)-> HTMLPage:
            body = "\n".join(self.body_content)
            return HTMLPage(title=self.title, body=body)

    page1 = HTMLBuilder("In God We Trust").add_heading("Webpage using builder pattern").add_paragraph("A paragraph being built using builder pattern").build()
    # builder.add_heading("Webpage using builder pattern")
    # builder.add_paragraph("A paragraph being built using builder pattern")
    # page1 = builder.build()

    print(page1.render())
    mo.Html(page1.render())
    return


@app.cell
def _(mo):
    #  Pandas example using builder pattern

    import pandas as pd

    df = pd.DataFrame({"A":[1,2],"B":[3,4]})
    print(f"No Styling : \n {df.to_html()}\n\n")


    styled = (
        df.style.set_caption("Styled Dataframe").background_gradient(cmap="viridis").format("{:.2f}")
    )
    print(f"Styled : \n {styled.to_html()}")


    mo.Html(styled.to_html())
    # mo.Html(df.to_html())
    return


@app.cell
def _(mo):
    mo.md(r"""#[10 Standard Library Modules That Make Python Insanely Powerful](https://youtu.be/eZ9RqnkJxsk?si=0spzpzaGT1EOpNrR)""")
    return


@app.cell
def _(dataclass):
    # Dataclasses Frozen & nit frozen

    @dataclass
    class Customer:
        name: str
        age: int
        tier: str

    new_customer = Customer("Vidatdhu Karuppu", 100, "Platinum")
    print(new_customer)
    new_customer.name = "Enga Karuppu Samy"
    print(new_customer)

    @dataclass(frozen=True)
    class CustomerFrozen:
        name: str
        age: int
        tier: str

    new_customer_f = CustomerFrozen("Vidatdhu Karuppu", 100, "Platinum")
    print(new_customer_f)
    new_customer_f.name = "Enga Karuppu Samy"


    return


@app.cell
def _():
    # Pathlib

    from pathlib import Path
    base = Path("/Users")
    print(base)

    my_root = base / "vrbabu"
    print(my_root)

    no_dir = base / "doofus"
    if no_dir.exists():
        print(f"{no_dir} exists")
    else :
        print(f"{no_dir} does not exist")

    cwd = Path.cwd()
    print(cwd)
    for file in cwd.iterdir():
        if file.is_file():
            print(file.stat().st_size)
    return


@app.cell
def _():
    # functools
    from functools import cache, partial

    @cache
    def calculate_power(base: int, exponent:int)-> int:
        return base ** exponent

    print(calculate_power(2,4))

    calculate_square = partial(calculate_power, exponent=2)
    print(calculate_square(8))
    return


@app.cell
def _():
    # graphlib

    from graphlib import TopologicalSorter

    ts = TopologicalSorter[str]()

    ts.add("compile", "fetch_sources")
    ts.add("test", "compile")
    ts.add("package", "test")
    ts.add("deploy", "package")
    ts.add("fetch_sources")

    order = list(ts.static_order())

    print(f"Execution Order : {order}")
    return


if __name__ == "__main__":
    app.run()
