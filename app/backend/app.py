import os
from dotenv import load_dotenv
from aiohttp import web
from rtmt import RTMiddleTier
from aiohttp import ClientSession
from typing import Optional



if __name__ == "__main__":
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    print(f"--- {openai_api_key}")

    app = web.Application()

    rtmt = RTMiddleTier("wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01", openai_api_key)

    rtmt.attach_to_app(app, "/realtime")

    app.add_routes([web.get('/', lambda _: web.FileResponse('./static/index.html'))])
    app.router.add_static('/', path='./static', name='static')
    web.run_app(app, host='localhost', port=8765)

