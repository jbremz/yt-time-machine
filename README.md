# YT Time Machine

Browse your YouTube watch history like a time machine. Filter by date, search by title or channel, and re-watch videos with autoplay — all from a local web page. Now with authentic Geocities flair.

## Setup

### 1. Download your YouTube history from Google Takeout

1. Go to [Google Takeout](https://takeout.google.com/)
2. Click **Deselect all** at the top
3. Scroll down and check **YouTube and YouTube Music**
4. Click **All YouTube data included**, then click **Deselect all**
5. Check only **history**
6. Make sure the format for history is set to **HTML** (this is the default)
7. Click **OK**, then scroll down and click **Next step**
8. Choose your delivery method (email download link is fine), file type, and size
9. Click **Create export**
10. Wait for the email, download and unzip the archive
11. Find the file at: `Takeout/YouTube and YouTube Music/history/watch-history.html`

### 2. Parse the data

Copy `watch-history.html` into this directory, then run:

```bash
make parse
```

This generates `data.json` from the HTML file.

### 3. Serve locally

The app needs to be served over HTTP (not `file://`) because it fetches `data.json`:

```bash
make serve
```

Then open [http://localhost:8000](http://localhost:8000).

Or do both steps at once:

```bash
make dev
```

Run `make help` to see all available commands. Use `PORT=3000 make serve` to change the port.

## Features

- **Date range filter** — pick any start/end date
- **Calendar picker** — visual month-view calendar with activity dots showing which days have watch history; click a day or click two days to set a range
- **Search** — filter by video title or channel name
- **"This day in..."** — see what you watched on today's date in previous years, with a mini calendar card
- **Random Day** — jump to a random day in your history (also the default on page load)
- **Shuffle** — randomize the order of filtered results
- **Autoplay** — videos play one after another automatically
- **Keyboard shortcuts** — `Shift+N`: next, `Shift+P`: previous, `Shift+S`: shuffle, `Shift+R`: random day
- **Geocities aesthetic** — Comic Sans, rainbow text, animated GIFs, marquee, spinning UFOs, and a fake visitor counter

## Files

| File | Description |
|------|-------------|
| `index.html` | The web app (single file, no dependencies) |
| `parse.py` | Parses `watch-history.html` into `data.json` |
| `Makefile` | Shortcuts for common commands (`make help`) |
| `assets/` | Retro GIFs sourced from the Geocities archive |
| `data.json` | Generated video data (not committed) |
| `watch-history.html` | Your Takeout export (not committed) |

## Asset credits

Retro GIFs sourced from [geocities.restorativland.org](https://geocities.restorativland.org/), a restored visual gallery of the archived Geocities sites.
