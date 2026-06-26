import logging
import os
import threading
import asyncio
from flask import Flask
from telegram import Bot, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

# ─────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
CHANNEL_ID = "@DigitalSkillupNG"
GROUP_ID = os.environ.get("GROUP_ID", "YOUR_GROUP_ID_HERE")
AFFILIATE_LINK = os.environ.get("AFFILIATE_LINK", "YOUR_AFFILIATE_LINK_HERE")
TIMEZONE = pytz.timezone("Africa/Lagos")

# ─────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────
# FLASK KEEP-ALIVE
# ─────────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "PilotHQ Bot is running! 🚀"

@flask_app.route("/health")
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()

# ─────────────────────────────────────────
# 28-DAY CONTENT CALENDAR
# ─────────────────────────────────────────
def get_posts():
    link = os.environ.get("AFFILIATE_LINK", "YOUR_AFFILIATE_LINK_HERE")
    return [
        # WEEK 1 — Foundation
        """👋 Welcome to Digital Skillup NG!

This channel is for Nigerians who want to earn real income using digital skills and the internet.

Every day I'll share tips, tools, opportunities, and resources that actually work.

No fluff. No scam. Just real talk.

Drop a 🔥 if you're ready to learn and earn.""",

        """💡 5 digital skills Nigerians are using to earn ₦100k+ monthly:

1. Copywriting
2. Graphic Design
3. Video Editing
4. Social Media Management
5. Freelance Writing

The best part? You can learn any of these online in 30–90 days.

Which one interests you most? Comment below 👇""",

        """🧵 A guy I know started learning graphic design in January with just his phone.

By March he was already charging ₦15,000 per logo.
By June he hit ₦80,000 in one month.

He didn't have a laptop. He didn't have connections.
He just had the right knowledge and took action.

The difference between where you are and where you want to be is usually just ONE skill.

Tomorrow I'll share a resource that can help you start. Stay tuned 👀""",

        f"""✅ As promised — here's a resource I recommend:

This course teaches you exactly how to start earning with digital skills step by step.

I checked it out and it's solid. It has helped people go from zero to earning in under 60 days.

Price is affordable but the value is way more than that.

Get it here 👉 {link}

Any questions? Drop them below and I'll answer 👇""",

        f"""❓ "I don't have a laptop, can I still learn digital skills?"
Yes. Many people start with just a smartphone.

❓ "I have no experience at all"
Good. Most courses start from zero.

❓ "Is this another scam?"
I get it. Nigeria has made us suspicious.
That's why I only share things I've verified.

The course I shared yesterday is legit.
Still available 👉 {link}""",

        """🗣️ Quick question for this community:

What is your biggest challenge when it comes to making money online?

A) I don't know where to start
B) I start but don't finish
C) I have no money to invest
D) I don't believe it's possible for me

Be honest. Your answer helps me know how to help you better 👇""",

        f"""💬 Someone on this channel took action and got the course this week.

They messaged saying they've already finished module 1 and learned their first practical skill.

Small steps. Real progress.

If you haven't grabbed it yet, link is still here 👉 {link}

New week, new content dropping tomorrow.
Tell a friend about this channel 🙏""",

        # WEEK 2 — Education
        """📌 How to start freelancing with zero experience:

Step 1 — Pick ONE skill (design, writing, video editing)
Step 2 — Learn it for 30 days (YouTube + free courses)
Step 3 — Create 3 sample projects (even fake ones)
Step 4 — Open a profile on Fiverr or Selar
Step 5 — Price low to get first reviews
Step 6 — Raise your price as reviews grow

That's the whole roadmap. No secret formula. Just execution.""",

        """🛠️ Free tools Nigerians are using to earn online:

• Canva — graphic design (free)
• CapCut — video editing (free)
• ChatGPT — writing & content (free)
• Telegram — building audiences (free)
• Selar — selling digital products (free to list)
• Fiverr — selling services (free to join)

You have everything you need already.
The question is — are you using them?""",

        """🚫 Myth: "You need a laptop to make money online"

Reality: Thousands of Nigerians earn six figures monthly using only their Android phone.

Canva mobile. CapCut mobile. Telegram mobile. Fiverr mobile.

Stop waiting for the perfect setup.
Start with what you have. Upgrade as you earn.

Your phone is a money machine. Learn to use it.""",

        """💰 Platforms that actually pay Nigerians:

• Selar — sell your own digital products
• Expertnaire — promote others' products (affiliate)
• Fiverr — sell your skills globally
• Upwork — freelancing for bigger clients
• Telegram — build audience, promote products
• YouTube — content + affiliate + AdSense

Pick ONE. Master it. Then expand.
Trying all at once = mastering none.""",

        """🇳🇬 Real story:

Chisom was a corper earning ₦33,000/month.
She learned social media management during NYSC.
Started taking clients at ₦20,000/month each.

By the time service year ended she had 4 clients.
That's ₦80,000/month — more than most entry-level jobs.

She never wrote a single CV.
She just built a skill and showed up consistently.

Your turn.""",

        f"""🔍 Deep dive: Why I recommend this course

Here's exactly what you get:

✅ Step by step lessons from beginner to earning
✅ Practical assignments not just theory
✅ Works with just a smartphone
✅ Nigerian context — not foreign examples
✅ Lifetime access once you buy

This is the resource I wish I had when starting out.

Get it here 👉 {link}""",

        """📊 Week 2 recap:

This week we covered:
• How to start freelancing from zero
• Free tools you can use today
• Why your phone is enough
• Platforms that pay Nigerians
• A real success story

Share this channel with one person who needs this 🙏

Week 3 starts tomorrow — we're going deeper 🔥""",

        # WEEK 3 — Social Proof
        """📈 What ₦10,000 invested in the right course can return:

If you learn graphic design:
→ One logo = ₦10,000 – ₦50,000
→ 3 clients/month = ₦30,000 – ₦150,000

If you learn copywriting:
→ One sales page = ₦20,000 – ₦100,000
→ 2 clients/month = ₦40,000 – ₦200,000

The ROI on digital skills is unmatched.
No other investment gives you this return this fast.""",

        """📖 Case study: How Emeka made his first ₦10k online

Week 1: Learned basic Canva design (YouTube, free)
Week 2: Created 5 sample logos
Week 3: Posted samples in 3 Facebook groups
Week 4: Got his first client — paid ₦10,000 for a logo

Total time: 1 month
Total investment: ₦0
Total earned: ₦10,000

He didn't wait to be perfect. He started ugly and improved.
That's the only strategy that works.""",

        """💡 How to price your digital service as a beginner:

Don't price by your experience.
Price by the VALUE you deliver to the client.

A logo that helps a business look professional = worth ₦15,000+
A social media post that brings in customers = worth ₦5,000+
A CV that gets someone a job = worth ₦10,000+

Start slightly below market rate to get reviews.
Raise price every 3–5 clients.

Never work for free. Even ₦2,000 is better than free.""",

        """🤔 Free learning vs Paid courses — which is better?

Free learning:
✅ Zero cost
✅ Lots of content on YouTube
❌ Scattered, no structure
❌ Takes longer to get results

Paid courses:
✅ Structured step by step
✅ Faster results
✅ Usually includes community/support
❌ Costs money upfront

Verdict: Start free to explore. Go paid when you're serious.""",

        f"""🗳️ Quick poll:

What skill would you most like to learn?

Reply with the number:

1️⃣ Graphic Design
2️⃣ Copywriting
3️⃣ Video Editing
4️⃣ Social Media Management
5️⃣ Affiliate Marketing

Your answer helps me create better content for you 👇

P.S — Whatever you pick, this course covers the foundation 👉 {link}""",

        f"""🚀 This week alone, people who took action got results.

One person finished the course and landed their first client.
Another said they didn't believe it would work — but it did.

These are real people. Real results.

The only difference between them and you is one decision.

Make it here 👉 {link}

Offer won't be at this price forever.""",

        """💪 You're closer than you think.

Most people quit 3 feet from gold.
They try for 2 weeks, see no results, and give up.

But the people who win? They just stayed a little longer.

This week — commit to ONE skill.
Learn it every day for 30 days.
Don't measure results until day 30.

Tag someone who needs to hear this 👇""",

        # WEEK 4 — Conversion
        f"""📋 How to make your first ₦50k online — step by step:

Step 1: Pick a skill (design, writing, video)
Step 2: Learn it using a structured course
Step 3: Create 3–5 sample projects
Step 4: Join 5 Nigerian Facebook/Telegram groups in your niche
Step 5: Offer your service at an introductory price
Step 6: Deliver excellently, ask for a review
Step 7: Repeat until you hit ₦50k

That's the entire blueprint.

The course that covers Step 2 perfectly 👉 {link}""",

        f"""⭐ What people are saying:

"I was skeptical at first but this course changed everything for me"

"Finally a course that's practical and not just theory"

"I made back the course fee in my first week of applying what I learned"

"Best investment I made this year honestly"

These are real testimonials from real buyers.

Join them here 👉 {link}""",

        f"""🛡️ "I've been scammed before and I'm scared to invest again"

I hear you. Nigeria has burned a lot of us.

Here's why this is different:
• It's on Selar — a verified Nigerian platform
• The creator is credible with a real track record
• You get the full product immediately after payment
• No promises of overnight millions — just real skills

Your fear is valid. But letting fear stop you forever is the real loss.

Take a calculated risk here 👉 {link}""",

        f"""⏰ Heads up:

The price of this course may increase soon as more people discover it.

Right now you can still get it at the current price.

I can't guarantee how long this stays.

Lock in your access now 👉 {link}

Don't be the person who says "I wish I had done this earlier" """,

        f"""💎 Free tip that will change how you think about money:

Stop trading time for money (salary/wages).
Start trading VALUE for money (skills/products).

A skill can be sold infinite times.
Your time can only be sold once.

The fastest way to make this shift?
Learn a high-income digital skill.

The best resource I've found for this 👉 {link}""",

        f"""📣 Direct talk today:

You've been on this channel for weeks now.
You've read the tips. You've seen the stories.
You know what to do.

The only thing left is a decision.

Are you going to keep watching others win?
Or are you going to take ONE step today?

That step is here 👉 {link}

I believe in you. Now believe in yourself.""",

        f"""🙏 Thank you for being part of Digital Skillup NG this month.

We've covered:
✅ What digital skills pay in Nigeria
✅ How to start with just a phone
✅ Real success stories
✅ Free tools and platforms
✅ Step by step blueprints

Month 2 starts tomorrow — we're going even deeper.

Invite ONE person to this channel today. Help someone else win.

And if you haven't taken action yet — there's no better time than now 👉 {link}

See you tomorrow 🔥""",
    ]

# ─────────────────────────────────────────
# POST TRACKER
# ─────────────────────────────────────────
post_index = {"current": 0}

# ─────────────────────────────────────────
# SCHEDULED POST TO CHANNEL
# ─────────────────────────────────────────
async def send_daily_post(bot: Bot):
    posts = get_posts()
    idx = post_index["current"]
    if idx < len(posts):
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=posts[idx]
            )
            logger.info(f"✅ Sent post {idx + 1} of {len(posts)}")
            post_index["current"] += 1
        except Exception as e:
            logger.error(f"❌ Failed to send post: {e}")
    else:
        logger.info("📭 All 28 posts sent. Calendar complete.")

# ─────────────────────────────────────────
# /start COMMAND
# ─────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm the Digital Skillup NG bot.\n\n"
        "I post daily digital income tips to our channel.\n\n"
        "📢 Join us here: t.me/DigitalSkillupNG\n\n"
        "Type *link* to get our top recommended resource 🔥",
        parse_mode="Markdown"
    )

# ─────────────────────────────────────────
# HANDLE GROUP + PRIVATE MESSAGES
# Bot responds in the community group and
# in private chat — covers both use cases
# ─────────────────────────────────────────
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    # Ignore messages from the bot itself
    if update.message.from_user and update.message.from_user.is_bot:
        return

    text = update.message.text.lower()
    link = os.environ.get("AFFILIATE_LINK", "YOUR_AFFILIATE_LINK_HERE")
    name = update.message.from_user.first_name if update.message.from_user else "Friend"

    if any(word in text for word in ["link", "how to start", "get it", "buy", "course", "where"]):
        await update.message.reply_text(
            f"🔥 Here you go {name}!\n\n"
            f"👉 {link}\n\n"
            f"Get it now while the price is still this low! 💪"
        )

    elif any(word in text for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        await update.message.reply_text(
            f"👋 Hey {name}! Welcome to the Digital Skillup NG community.\n\n"
            f"Feel free to ask any questions here — we're all learning and growing together 🔥\n\n"
            f"Type *link* anytime to get our top recommended resource.",
            parse_mode="Markdown"
        )

    elif any(word in text for word in ["scam", "legit", "real", "trust", "fake"]):
        await update.message.reply_text(
            f"✅ Totally valid concern {name} — Nigeria has burned a lot of us.\n\n"
            f"Everything shared on this channel is verified before we recommend it.\n\n"
            f"The course we promote is on Selar — a trusted Nigerian platform — and you get "
            f"instant access after payment. No funny business.\n\n"
            f"Check it out yourself 👉 {link}"
        )

    elif any(word in text for word in ["free", "money", "earn", "income", "pay"]):
        await update.message.reply_text(
            f"💰 Great question {name}!\n\n"
            f"The fastest way to start earning online:\n"
            f"1. Pick one skill\n"
            f"2. Learn it properly\n"
            f"3. Offer it to people who need it\n\n"
            f"We have a course that walks you through this step by step 👉 {link}"
        )

    elif any(word in text for word in ["thank", "thanks", "helpful", "great", "nice"]):
        await update.message.reply_text(
            f"🙏 You're welcome {name}! That's what we're here for.\n\n"
            f"Keep showing up daily — consistency is everything 🔥"
        )

    else:
        # Default response for any other message
        await update.message.reply_text(
            f"👋 Thanks for your message {name}!\n\n"
            f"For daily digital income tips follow our channel 👉 t.me/DigitalSkillupNG\n\n"
            f"Type *link* to get our top recommended resource 🔥",
            parse_mode="Markdown"
        )

# ─────────────────────────────────────────
# WELCOME NEW GROUP MEMBERS
# ─────────────────────────────────────────
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.new_chat_members:
        return
    for member in update.message.new_chat_members:
        if member.is_bot:
            continue
        name = member.first_name or "Friend"
        await update.message.reply_text(
            f"👋 Welcome, {name}!\n\n"
            f"You just joined the *Digital Skillup NG Community* — great decision!\n\n"
            f"📌 Read the pinned posts to get started.\n"
            f"💬 Ask any questions — we answer everything here.\n"
            f"📢 Follow our main channel 👉 t.me/DigitalSkillupNG\n\n"
            f"Let's get you earning! 🔥",
            parse_mode="Markdown"
        )

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
async def main():
    keep_alive()

    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))

    # Welcome new group members
    app.add_handler(MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome_new_member
    ))

    # Respond to messages in group AND private chat
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    ))

    # Scheduler — posts to channel at 8AM WAT daily
    scheduler = AsyncIOScheduler(timezone=TIMEZONE)
    scheduler.add_job(
        send_daily_post,
        trigger="cron",
        hour=8,
        minute=0,
        kwargs={"bot": app.bot}
    )
    scheduler.start()

    logger.info("🚀 PilotHQ Bot is running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)

    # Keep running forever
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
