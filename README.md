# Cold Outreach Pipeline for B2B SaaS — Research Project

## Phase 1 — Environment Setup

| Tool                   | Notes                                                    |
| ---------------------- | -------------------------------------------------------- |
| VS Code                | Primary editor (switched from Cursor — see issues below) |
| GitHub Desktop         | Repository management                                    |
| Python 3.12            | Scripting and automation                                 |
| youtube-transcript-api | YouTube transcript collection via API                    |

## What Happened

I already had VS Code installed, so when I first set up Cursor I just imported my existing setup — extensions came over cleanly. Found Claude Code and Codex in the Extensions panel, installed both, went through the login flows. Used GitHub Desktop to clone and open the repo.

Ended up switching back to VS Code partway through. Cursor had a conflict with its own bundled Claude Code extension that I couldn't fully resolve, and VS Code was already configured exactly how I like it.

Total setup time was roughly 25-30 minutes, most of it spent troubleshooting the issues below.

## Issues

**Claude Login Page was Down**
Hit a "Claude will return soon" screen on first auth attempt. Turned out to be a temporary Anthropic outage. Waited, tried again, same error. Clearing browser cache and cookies fixed it — not obvious, but it worked.

**Claude Code Showing up Twice**
After installing the extension, two "Claude Code" entries appeared in the sidebar. One had broken images. Cursor apparently bundles its own internal copy, so installing the extension manually creates a conflict. Uninstalling removed both; reinstalling brought both back. Couldn't find a clean fix, so I switched to VS Code instead.

**Windows Execution Policy**
Setting up the Python virtual environment threw a security error — Windows blocks venv activation scripts by default. Fixed it with `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`. Wrote a small script to revert the setting if needed later.

**Windows Defender**
Right after fixing the execution policy, Defender blocked pip inside the venv folder. Added the project folder as an exception in Defender settings and it worked fine after that.

---

## Phase 2 — Research Project

### Topic chosen: Cold Outreach Pipeline for B2B SaaS

I picked this one because it felt the most directly tied to real growth outcomes — pipeline, revenue, meetings booked. It's also what B2B SaaS companies actually hire junior growth people to do, so it felt like the most useful thing to go deep on. There's a strong community of practitioners who share specific, verifiable results rather than just generic advice.

### Repository Structure

    research/
    ├── sources.md                        # All 10 experts with links and annotations
    ├── linkedin-posts/                   # Posts organized by author folder
    │   ├── nick-abraham/
    │   ├── alex-berman/
    │   ├── josh-braun/
    │   ├── patrick-spychalski/
    │   ├── jason-bay/
    │   ├── will-aitken/
    │   ├── eric-nowoslawski/
    │   ├── kellen-casebeer/
    │   ├── jesse-ouellette/
    │   └── yurii-veremchuk/
    ├── youtube-transcripts/              # Transcripts pulled via Python script
    │   ├── patrick-spychalski/
    │   └── alex-berman/
    └── other/

    fetch_transcripts.py                  # Script used to collect YouTube transcripts
    requirements.txt                      # Python dependencies

### The 10 Experts

I tried to find people who actually run campaigns, not just write about them. Follower count wasn't the criteria — content quality was. Four people got swapped during research after finding their LinkedIn was mostly promotional posts, conference photos, or off-topic content. The replacements were chosen based on what they were actually publishing.

| #   | Expert             | Why they're here                                              |
| --- | ------------------ | ------------------------------------------------------------- |
| 1   | Nick Abraham       | Runs 140k inboxes for 300 clients — shares real campaign data |
| 2   | Alex Berman        | Created the 3C Method, 500k+ meetings booked for clients      |
| 3   | Josh Braun         | Focuses on buyer psychology over tactics — rare angle         |
| 4   | Patrick Spychalski | Very tactical step-by-step content, strong YouTube presence   |
| 5   | Jason Bay          | Mobile-first frameworks, offer-based CTAs with real data      |
| 6   | Will Aitken        | Intent signals and micro-sequencing, very structured content  |
| 7   | Eric Nowoslawski   | Clay automation, sends 1.5M emails/month, ex-Clay team        |
| 8   | Kellen Casebeer    | Message-market fit, contrarian takes grounded in real results |
| 9   | Jesse Ouellette    | Technical deliverability and email validation infrastructure  |
| 10  | Yurii Veremchuk    | 9 years at Woodpecker, copywriting and objection handling     |

### Content Collected

| Type                | Count |
| ------------------- | ----- |
| LinkedIn posts      | 35    |
| YouTube transcripts | 9     |
| Total               | 44    |

LinkedIn posts were collected manually — there's no reliable free API for LinkedIn, so each post was read, evaluated, and saved as a markdown file. Anything purely promotional or off-topic was left out.

YouTube transcripts were pulled using a Python script I built with `youtube-transcript-api`. No API key needed. The script fetches the raw transcript and saves it as a markdown file in the right folder automatically. Running it for 9 videos took about 10 seconds.

### Key Observations

A few things that stood out after reading through all 44 pieces of content:

**Getting to the inbox is now harder than writing good copy.** Nick Abraham, Jesse Ouellette, Eric Nowoslawski, and Yurii Veremchuk all spend a significant portion of their content on domain setup, warmup periods, inbox rotation, and bounce rates. Deliverability used to be an afterthought — now it's the foundation everything else sits on.

**There's a real debate about intent signals.** Will Aitken is a strong advocate for stacking multiple signals to prioritize outreach. Kellen Casebeer thinks signals are mostly noise and that static ICP fit should come first. Both are credible and both make compelling arguments — this isn't a resolved question in the space.

**Most campaigns fail because of the offer, not the copy.** At least five of the ten experts arrive at this independently. Kellen Casebeer's message-market fit framework, Alex Berman's offer formula, Eric Nowoslawski's 3 pillars — they all point to the same root cause. Writing better subject lines won't fix a weak value proposition.

**Buyer psychology is the missing piece in most outreach.** Josh Braun's content is almost entirely about how prospects think and feel — concepts like linguistic softeners, preserving prospect dignity, and the gravity of the status quo. None of the other nine experts go anywhere near this territory, yet it directly explains why technically correct outreach still gets ignored.

**AI is being used for data enrichment, not copywriting.** The most sophisticated practitioners — Eric Nowoslawski, Patrick Spychalski, Will Aitken — are using AI to extract signals from job postings, enrich lead lists in Clay, and automate research workflows. The popular narrative of AI writing cold emails at scale doesn't match what the best people in the space are actually doing.

---

_OS: Windows 11 · Editor: VS Code · Repo management: GitHub Desktop · Research compiled May 2026_
