from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory containing CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI with CSS</title>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Hello, KAT!</h1>
            </header>
            <main>
                <section class="intro">
                <p>Hey Kat, I made this webpage just for you!</p>
                <p>Hope you like the pink theme!</p>
            </section>
            #     <section class="love-message">
            #         <p>Feel free to customize and impress!</p>
            #         <p>Enjoy!</p>
            #     </section>
            # </main>
            # <footer>
            #     <p>From: Your Secret Admirer</p>
            # </footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5005)
