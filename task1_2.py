from fastapi import FastAPI, Request
import secrets

from sqlalchemy import select, insert
from starlette.responses import RedirectResponse, HTMLResponse

from db import urls, conn

app = FastAPI()


@app.get("/create")
async def create(full: str, request: Request):
    sql = select(urls).where(urls.c.full == full)
    res = conn.execute(sql).fetchone()
    host = request.client.host
    if res is not None:
        short = res[0]
    else:
        short = secrets.token_urlsafe(16)
        conn.execute(insert(urls).values(short=short, full=full))
    return HTMLResponse(f"""
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <a href="http://{host}:8000/{short}">http://{host}:8000/{short}</a>
        </body>
    </html>
    """)


@app.get("/{short}")
async def redirect(short: str):
    sql = select(urls).where(urls.c.short == short)
    res = conn.execute(sql).fetchone()
    if res is None:
        return {"message": "error"}
    else:
        full = res[1]
        return RedirectResponse(f"{full}")
