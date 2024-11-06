import marimo

__generated_with = "0.9.15"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 1""")
    return


@app.cell
def __(mo):
    widget_1 = mo.ui.radio(
        options={"?": None, "CLI": 1, "TUI": 2, "GUI": 3, "FBI": 4},
        value="?",
    )

    comments_1 = mo.ui.text_area(debounce=False)

    mo.md(f"""## Question 1

    L'acronyme (🇺🇸) désignant un programme "en ligne de commande", destiné à être utilisé dans un terminal est :

    {widget_1}

    Commentaires:

    {comments_1}

    """)
    return comments_1, widget_1


@app.cell
def __(mo):
    widget_2 = mo.ui.radio(
        options={
            "?": None,
            "hello.py": 1,
            "python hello.py": 2,
            "pixi hello.py": 3,
            "pixi python hello.py": 3,
            "pixi run python hello.py": 4,
            "pixi run python run hello.py": 5,
        },
        value="?",
    )


    comments_2 = mo.ui.text_area(debounce=False)


    mo.md(f"""
    ## Question 2

    Pour exécuter le programme `hello.py` du répertoire courant avec l'interpréteur Python fourni par `pixi`, vous tapez la commande :

    {widget_2} 

    Commentaires :

    {comments_2}



    """)
    return comments_2, widget_2


@app.cell
def __(mo):
    widget_3 = mo.ui.text_area(debounce=False)

    comments_3 = mo.ui.text_area(debounce=False)


    mo.md(f"""
    ## Question 3

    Quelle est la fonction de la commande `which` (en bash) ou `Get-Command` (avec powershell) ?

    Réponse :
    {widget_3}

    Commentaires :
    {comments_3}
    """)
    return comments_3, widget_3


@app.cell
def __(mo):
    widget_4 = mo.ui.array([mo.ui.checkbox()] * 3)
    comments_4 = mo.ui.text_area(debounce=False)

    mo.md(
        f"""## Question 4

    Pour permettre à une personne de reconstituer exactement sur sa machine l'environnement pixi de mon projet, je partage avec elle

     - {widget_4[0]} mon dossier `.pixi`

     - {widget_4[1]} mon fichier `pixi.lock`

     - {widget_4[2]} mon fichier `pixi.toml`

    Commentaires :

    {comments_4}

    """
    )
    return comments_4, widget_4


@app.cell
def __(mo):
    widget_5 = mo.ui.radio(
        options={
            "?": None,
            "dans le répertoire courant": 1,
            "dans le répertoire 'C:\Program Files' pour Windows ou '/usr/bin' sur Linux et OSX": 2,
            "dans la liste de répertoires spécifiée par la variable d'environnement PATH": 3,
            "dans tout le système de fichiers": 4,
        },
        value="?",
    )

    comments_5 = mo.ui.text_area(debounce=False)


    mo.md(f"""
    ## Question 5

    Lorsque je tape `firefox` dans mon terminal, le système recherche un fichier exécutable du même nom

    {widget_5}


    Commentaires :

    {comments_5}


    """)
    return comments_5, widget_5


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


@app.cell(hide_code=True)
def __(
    comments_1,
    comments_2,
    comments_3,
    comments_4,
    comments_5,
    pprint,
    widget_1,
    widget_2,
    widget_3,
    widget_4,
    widget_5,
):
    widgets = [widget_1, widget_2, widget_3, widget_4, widget_5]
    comments = [comments_1, comments_2, comments_3, comments_4, comments_5]
    answer = pprint.pformat([
        {f"Question {i+1}": widget.value, f"Comment {i+1}": comment.value} for i, (widget, comment) in enumerate(zip(widgets, comments))
    ], indent=4)


    return answer, comments, widgets


@app.cell
def __(mo):
    autosave = mo.ui.checkbox(label="autosave to answer.py", value=True)
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
