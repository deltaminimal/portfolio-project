# Cursor Setup

## Tools Installed

| Tool                  | Notes                                               |
| --------------------- | --------------------------------------------------- |
| Cursor IDE            | [cursor.com](https://cursor.com)                    |
| Claude Code Extension | Extensions panel → logged in with Anthropic account |
| Codex Extension       | Extensions panel → logged in with OpenAI account    |

## What Happened

I already had VS Code installed on my system, so I just imported my personal setup when installing Cursor. All my existing extensions came over cleanly, no manual reinstalling. Found Claude Code and Codex in the Extensions panel, installed both, went through the login flows. Used GitHub Desktop to clone the repo and opened it straight in Cursor from there.

Whole thing took maybe 25-30 minutes, most of which was spent on research and trying to fix the issues below.

## Issues

**Claude Login Page was Down**

Hit a "Claude will return soon" screen the first time I tried to authenticate. Turned out to be a temporary outage on Anthropic's end, nothing to do with the setup. Waited a few minutes, tried again, same error screen. What actually fixed it was clearing browser cache and cookies. Not obvious at all, but after that the auth went through.

**Claude Code Showing up Twice**

After installing the extension, two entries named "Claude Code" appeared in the sidebar. One had broken images on the welcome screen. Uninstalling removed both; reinstalling brought both back. Turns out Cursor bundles its own internal copy, so adding the extension manually creates a conflict — the one with broken assets is Cursor's built-in version failing to load its resources.

Tried disabling one, restarting, pinning — nothing worked. It seems to be a Cursor bug (Will investigate further).

---

_OS: Windows 11 · Editor: Cursor (latest) · Repo Management: GitHub Desktop_
