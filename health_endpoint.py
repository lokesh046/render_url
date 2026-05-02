from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    """Health check endpoint used by GitHub Actions to keep Render alive."""
    return {"status": "ok"}


# -----------------------------------------------------------
# HOW TO INTEGRATE INTO YOUR EXISTING api_gateway/main.py
# -----------------------------------------------------------
# Copy ONLY the route below into your existing FastAPI app:
#
#   @app.get("/health")
#   async def health():
#       return {"status": "ok"}
#
# That's it! You do NOT need to use this file directly.
# -----------------------------------------------------------
