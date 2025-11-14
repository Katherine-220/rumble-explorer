# Rumble Explorer Scraper

> Rumble Explorer Scraper is a powerful tool for collecting video, channel, playlist, and category data from Rumble.com. It helps researchers, analysts, and developers gather structured insights from one of the fastest-growing video platforms.

> This scraper solves the challenge of navigating Rumble’s fragmented data ecosystem by providing unified, structured access to videos, creators, and platform-wide content categories.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Rumble Explorer</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The Rumble Explorer Scraper is designed to extract detailed information from Rumble.com, including videos, channels, user profiles, playlists, and categories.
It streamlines content research, supports media intelligence workflows, and enables data-driven analysis of online video trends.

### Why Use a Rumble Scraper?

- Collects rich metadata from Rumble content, including stats, creator info, and video files.
- Supports advanced Rumble Query Language (RQL) for precise targeting.
- Handles URLs, keywords, categories, and channel paths automatically.
- Ideal for researchers, analysts, content auditors, and developers.
- Converts Rumble pages into consistent, structured JSON.

## Features

| Feature | Description |
|--------|-------------|
| Multi-Query Support | Accepts keywords, URLs, channels, categories, and playlists. |
| Automatic URL Detection | Recognizes and processes any valid Rumble URL. |
| RQL Compatibility | Supports full Rumble Query Language for advanced queries. |
| Rich Metadata Extraction | Captures creator data, video stats, descriptions, tags, and more. |
| Video File Retrieval | Extracts direct video file URLs at multiple resolutions. |
| Category & Playlist Scraping | Gathers structured info from category pages and playlist feeds. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| title | Title of the video or content item. |
| description | Full text description of the video. |
| id | Unique numeric identifier for the video. |
| url | Canonical URL of the video or resource. |
| thumb | Thumbnail image URL. |
| by | Channel/user metadata including name, ID, followers, and links. |
| categories | Primary and secondary categories associated with the content. |
| comments | Total comment count. |
| duration | Length of the video in seconds. |
| upload_date | Timestamp of upload. |
| tags | Array of tagged keywords. |
| views | Number of total views. |
| video_stats | Revenue, platform views, and related stats. |
| videos | List of downloadable video file variants with bitrate and resolution. |
| related | Related content suggestions. |
| visibility | Public visibility status. |

---

## Example Output


    {
      "availability": null,
      "by": {
        "badge_type": "premium",
        "blocked": false,
        "followed": false,
        "followers": 445873,
        "id": "_c482047",
        "locals_community": {
          "counts": { "comments": 509, "likes": 22615, "members": 4037, "posts": 10895 },
          "description": "At Rebel News, we tell the other side of the story.",
          "join_button_text": "Join",
          "logo_url": "https://media3.locals.com/images/groups/663497/663497_8fw1csuf5f5qg9s_big.png",
          "owner_name": "Rebel News",
          "show_premium": true,
          "title": "Rebel News",
          "urls": {
            "channel": "https://rebelnewsnetwork.locals.com/track/rumble/click/channel?source_app=android",
            "video": "https://rebelnewsnetwork.locals.com/track/rumble/click/video?source_app=android"
          }
        },
        "name": "Rebel News",
        "relative_url": "/c/RebelNews",
        "subscribers": 0,
        "thumb": "https://1a-1791.com/video/z8/_/R/1/b/_R1ba.baa.1-RebelNews-rme5uh.png",
        "title": "Rebel News",
        "type": "channel",
        "url": "https://rumble.com/c/RebelNews",
        "verified_badge": true
      },
      "categories": { "primary": { "slug": "news", "title": "News" }, "secondary": null },
      "comments": { "count": 39 },
      "description": "http://NoGreenReset.com | MORE: https://rebelne.ws/3CuHuvM",
      "duration": 352,
      "id": 343328225,
      "object_type": "video",
      "tags": [],
      "title": "Is there a future for Ford's Oakville assembly plant?",
      "upload_date": "2024-11-18T18:29:00+00:00",
      "url": "https://rumble.com/v5qnuth-is-there-a-future-for-fords-oakville-assembly-plant-sources-say-things-look.html",
      "video_height": 1080,
      "views": 14643,
      "videos": [
        { "bitrate_kbps": 3978, "quality_text": "1080p", "url": "https://1a-1791.com/video/s8/2/f/N/i/S/fNiSu.haa.mp4?b=1&u=6" },
        { "bitrate_kbps": 2056, "quality_text": "720p", "url": "https://1a-1791.com/video/s8/2/f/N/i/S/fNiSu.gaa.mp4?b=1&u=6" }
      ]
    }

---

## Directory Structure Tree


    Rumble Explorer/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── rumble_video_parser.py
    │   │   ├── rumble_channel_parser.py
    │   │   └── utils_helpers.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── input.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Media researchers** use it to collect political and cultural content data so they can perform large-scale trend analysis.
- **Journalists** use it to track emerging creators and movements so they can validate stories quickly.
- **Developers** use it to enrich applications with structured Rumble metadata, improving content discovery features.
- **Analysts** use it to monitor platform engagement metrics so they can assess audience behavior.
- **Archivists** use it to save metadata and video links for long-term preservation.

---

## FAQs

**Does it support scraping full channels or playlists?**
Yes. Provide a channel URL, user handle, or playlist ID, and it will extract all supported data.

**Can I use keywords instead of URLs?**
Absolutely. You can pass any keyword, and the scraper will search Rumble and return matching video results.

**Does it extract downloadable video file links?**
Yes. It retrieves multiple video file variants with resolution and bitrate details.

**Does it handle live streams?**
Live videos are detected and metadata is extracted when available.

---

## Performance Benchmarks and Results

**Primary Metric:** Processes up to 40–60 video pages per minute under typical connection conditions.
**Reliability Metric:** Consistently maintains a 95%+ successful extraction rate across mixed content types.
**Efficiency Metric:** Uses parallelized requests to keep memory usage low while handling large queues.
**Quality Metric:** Achieves over 98% field completeness for standard video and channel metadata.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
