# pilothq-bot
An Auto responder bot on telegram 

# PilotHQ Bot — Deployment Guide

## What This Bot Does
- Posts all 28 days of content automatically to your Telegram channel
- Posts daily at 8:00 AM WAT (West Africa Time)
- Welcomes new members automatically
- Responds to keywords like "link", "how to start", "buy" with your affiliate link
- Responds to greetings naturally

---

## Files
- `bot.py` — main bot code
- `requirements.txt` — Python dependencies
- `render.yaml` — Render deployment config

---

## Step 1 — Push to GitHub

1. Create a new repo on GitHub (name it `pilothq-bot`)
2. Upload these 3 files:
   - `bot.py`
   - `requirements.txt`
   - `render.yaml`

---

## Step 2 — Deploy on Render

1. Go to render.com → New → Web Service
2. Connect your GitHub repo
3. Render will auto-detect `render.yaml`
4. Go to **Environment Variables** and add:

| Key | Value |
|-----|-------|
| `BOT_TOKEN` | Your token from BotFather |
| `AFFILIATE_LINK` | Your Selar affiliate link |

5. Click **Deploy**

---

## Step 3 — Test Your Bot

1. Open Telegram
2. Find `@PilotHQBot`
3. Send `/start`
4. Send `link`
5. Check that it responds correctly

---

## Changing Post Time

In `bot.py` find this line:

```python
scheduler.add_job(
    send_daily_post,
    trigger="cron",
    hour=8,   # ← change this (24hr format)
    minute=0, # ← change this
    ...
)
```

Change `hour=8` to any hour you want.
Example: `hour=20` = 8:00 PM WAT

---

## Adding Your Affiliate Link Later

Go to Render dashboard → Your service → Environment Variables
→ Update `AFFILIATE_LINK` value → Redeploy

No need to touch the code at all.

---

## Troubleshooting

**Bot not posting to channel?**
→ Make sure `@PilotHQBot` is added as admin with "Post Messages" permission

**Bot not responding to messages?**
→ Check your BOT_TOKEN is correct in environment variables

**Posts not going out at 8am?**
→ Render free tier may spin down. Consider upgrading to Render Starter ($7/month) for reliability
