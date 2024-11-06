import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 0""")
    return


@app.cell
def __(mo):
    radiogroup = mo.ui.radio(
        options={"I don't know": None, "one": 1, "two": 2, "three": 3},
        value="I don't know",
        label="pick a number",
    )

    mo.md(f"""

    ## Question 1

    What's your favorite number?


    {radiogroup}
    """)
    return (radiogroup,)


@app.cell(hide_code=True)
def __(mo):
    checkboxes = mo.ui.array([mo.ui.checkbox()] * 3)
    return (checkboxes,)


@app.cell
def __(checkboxes, mo):
    mo.md(f"""
    ## Question 2

    Multiple answers:

      - {checkboxes[0]} Choice 1

      - {checkboxes[1]} Choice 2
        
      - {checkboxes[2]} Choice 3


    """)
    return


@app.cell
def __(mo):
    text = mo.ui.text(label="Type a short text here:", debounce=False)
    mo.md(f"""
    ## Question 3

    {text}
    """)
    return (text,)


@app.cell
def __(mo):
    text_area = mo.ui.text_area(debounce=False)
    return (text_area,)


@app.cell
def __(mo, text_area):
    mo.md(f"""
    ## Question 4

    Type a multiline text:
    {text_area}
    """)
    return


@app.cell
def __(mo):
    code = mo.ui.code_editor(language="python", value="if True:\n    pass", min_height=100)
    return (code,)


@app.cell
def __(code, mo):
    mo.md(f"""
    ## Question 5

    Type some Python code here:
    {code}
    """)
    return


@app.cell
def __(mo):
    mo.md("""## Validation""")
    return


@app.cell
def __():
    import pprint
    import urllib
    return pprint, urllib


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(checkboxes, code, pprint, radiogroup, text, text_area):
    widgets = [radiogroup, checkboxes, text, text_area, code]
    answer = pprint.pformat({f"Question {i+1}": widget.value for i, widget in enumerate(widgets)}, indent=4)
    return answer, widgets


@app.cell
def __(mo):
    autosave = mo.ui.checkbox(label="autosave", value=True)
    autosave
    return (autosave,)


@app.cell
def __(answer, autosave):
    if autosave.value:
        with open("answer.py", mode="tw", encoding="utf-8") as file:
            file.write(answer)
    return (file,)


@app.cell
def __(answer, mo, urllib):
    to = "Sebastien.Boisgerault@minesparis.psl.eu"
    subject = "Quizz AP #1"
    body = answer

    q = urllib.parse.quote


    mailto = f"mailto:{to}?subject={q(subject)}&body={q(body)}"


    mo.vstack(
        [
            mo.md(f"""
    Email the following text to {mo.icon('luctext_area:mail')} `Sebastien.Boisgerault@minesparis.psl.eu`
    ```python
    {answer}
    ```
    """),
            mo.Html(f"""
    <div>
      <style>
        #send {{
          text-decoration: none;
          background-color: #EEEEEE;
          color: #333333;
          padding: 2px 6px 2px 6px;
          border-top: 1px solid #CCCCCC;
          border-right: 1px solid #333333;
          border-bottom: 1px solid #333333;
          border-left: 1px solid #CCCCCC;
        }}
        </style>
        <a id="send" href="{mailto}">Send your answer</a>
    <div>
    """),
        ]
    )
    return body, mailto, q, subject, to


if __name__ == "__main__":
    app.run()
