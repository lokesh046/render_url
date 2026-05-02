# 🔄 Render Keep-Alive

Keeps your **Render free-tier backend** alive 24/7 by pinging it every 14 minutes via GitHub Actions — preventing the automatic 15-minute inactivity shutdown.

---

## 📁 Repo Structure

```
render-keep-alive/
├── .github/
│   └── workflows/
│       └── keep_alive.yml     # GitHub Actions workflow (auto-pings Render)
├── health_endpoint.py         # Reference: health route to add to your FastAPI app
└── README.md
```

---

## 🚀 Setup Instructions

### Step 1: Add `/health` route to your FastAPI backend

Open your `api_gateway/main.py` and add this route:

```python
@app.get("/health")
async def health():
    return {"status": "ok"}
```

Deploy this change to Render.

---

### Step 2: Add your Render URL as a GitHub Secret

1. Go to this repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Set:
   - **Name:** `RENDER_URL`
   - **Value:** `https://your-app-name.onrender.com`
4. Click **Add secret**

---

### Step 3: Push this repo to GitHub

```bash
git init
git add .
git commit -m "Initial keep-alive setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/render-keep-alive.git
git push -u origin main
```

---

### Step 4: Test manually

1. Go to **Actions** tab in this repo
2. Click **Keep Render Alive** → **Run workflow**
3. Check the logs — you should see:
   ```
   ✅ Server is alive!
   ```

---

## ⚙️ How It Works

| Detail | Value |
|---|---|
| Ping interval | Every 14 minutes |
| Render shutdown threshold | 15 minutes inactivity |
| GitHub Actions free minutes used | ~3,085 / month (within 2,000 min limit*) |
| Endpoint pinged | `GET /health` |

> *GitHub Actions free tier provides 2,000 minutes/month for private repos and unlimited for public repos.

---

## 🛠 Customization

To change the ping interval, edit the cron expression in `.github/workflows/keep_alive.yml`:

```yaml
- cron: '*/14 * * * *'   # every 14 minutes (recommended)
- cron: '*/10 * * * *'   # every 10 minutes (use only for public repos)
```

---

## 📌 Related Project

Backend repo: [lokesh046/backend](https://github.com/lokesh046/backend)
