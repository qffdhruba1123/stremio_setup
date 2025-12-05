# 🎬 Stremio Setup Guide
Step-by-Step Instructions to set up Stremio for the Best Experience. This will allow you to stream whatever content you want to enjoy
---

## ⚙️ Initial Setup (Mandatory)

I highly recommend you complete the initial setup on a computer, as a web browser is needed for the addon installation process.

### 1. Setting Up the Stremio Application

1.  Go to [Stremio](https://web.strem.io/).
2.  **Create an account** (or log in).
3.  Go to the **Add-on Section** (the puzzle piece icon on the left sidebar).
4.  Uninstall the default add-ons: **WatchHub** and **Public Domain Movies**.

### 2. Setting Up the Content Source (Real-Debrid)

To ensure high-quality, buffer-free streaming, a debrid service is essential.

1.  Get a Real-Debrid subscription from [here](http://real-debrid.com/?id=15891876).
2.  **Create an account.**
3.  Get a **Premium Subscription** from the "Premium Offers" section. (The 180-day subscription usually offers the best value).
4.  Get your **API Key** from [here](https://real-debrid.com/apitoken). (You will need this in the next step).

### 3. Installing and Configuring the Torrentio Add-on

Torrentio is the core add-on that links Stremio to Real-Debrid.

Now, we are going to install [Torrentio](https://torrentio.strem.fun/) with your Real-Debrid key.

| Configuration Setting | Recommended Value | Notes |
| :--- | :--- | :--- |
| **Providers** | `default` | Use default torrent providers. |
| **Sorting** | `default` | Use the default sorting method. |
| **Priority foreign language** | `defaults to English` | Change this only if English is not your preferred language. |
| **Exclude qualities/resolutions** | Check **`screener`** and **`cam`** | This filters out low-quality video streams. You can also check **`4k`** if your internet connection is slow. |
| **Max results per quality** | `10` | Limits the number of results to keep the list clean. |
| **Video size limit** | `leave empty` | Leave empty for the best quality. If you have slow internet or limited bandwidth, you can set a limit (e.g., `2GB` for movies, `800MB` for TV shows). |
| **Debrid provider** | Select **`Real-Debrid`** | This is crucial for high-speed streaming. |
| **Debrid API Key** | **Paste your API key here** | Paste the key obtained in the previous step, without any spaces. |
| **Debrid options (optional)** | Check: **`Don't show download to debrid links`** and **`Don't show debrid catalog`** | Hides unnecessary links from the search results. |
| **Final Step** | Click on **`install`** | |

> **Installation Note:**
> If the direct install button does not work, you can **"Copy link address"** from the install button, go to the **Add-on Section** on Stremio, click on **"Add addon"**, paste the copied URL, click **"Add"**, and then **"Install"**.

* **Verification:** Check if **Torrentio RD** has appeared in your add-on list. If it is there, you are all set. If you only see "Torrentio" without the "RD," uninstall the add-on and try the installation section again.

---

### 🎉 Basic Setup Complete!

This is the last step for the basic setup. You can now go and enjoy your favorite movies and TV shows across all your linked devices.
Simply download the [Stremio App](https://www.stremio.com/downloads) (they have an app on almost all platforms) and log in with your account, your setup will be included with your account.

*If you want to further improve the experience, please keep reading.*

---

## ✨ Optimizing Your Stremio Experience

### How to Add Streaming Platform Catalogs

You can add additional catalogs (content lists) to your Stremio home screen, besides the default ones.

[Streaming Catalogs](https://7a82163c306e-stremio-netflix-catalog-addon.baby-beamup.club/) provides listings based on popular streaming platforms.

1.  Go to the link.
2.  Change "Filter providers by country" to **"Any."**
3.  Select all the streaming services you want to see catalogs for (e.g., Netflix, Prime Video, Hulu).
4.  Click on **`install`**.

> **Installation Note:**
> If direct install does not work, copy the URL from the **"Manual install URL:"** field, go to the **Add-on Section** on Stremio, click on **"Add addon"**, paste the copied URL, click **"Add"**, and then **"Install."**

Once installed, you will see new catalogs on your home screen based on your selections.

### Can I Watch Live TV?

Yes, you can. A popular option is the [USA TV addon](https://stremio-addons.net/addons/usa-tv), which offers over 160 US channels in HD, including news and sports.

---

## ❓ Frequently Asked Questions (FAQ)

### What is Stremio?

Stremio is a free streaming application that allows you to watch movies, TV shows, live channels, and more, leveraging a community-driven add-on system.

### What platforms are supported?

The application currently supports **Windows, Mac, Linux** (including Steam Deck), **Android, Android TV, Samsung TVs** (2019+), **LG TVs** (2020+), **iOS**, and the **Web** client.

### What differentiates Stremio from other streaming apps?

Its highlight is the **add-on system**, which expands what you can watch, including the ability to stream copyrighted content via services like Torrentio.

### What is Torrentio?

It is a popular add-on that provides stream links by scraping torrent content from providers like YTS, EZTV, 1337X, and The Pirate Bay. Crucially, it supports **debrid services**.

### What is a debrid service?

A debrid service is an unrestricted multi-hoster that acts as a proxy between you and the BitTorrent network. It allows you to stream and download content instantly at high speeds directly from their servers. Most content is already **cached**, meaning you get instant access with no connection to other torrent peers.

### Do I really need a debrid service?

My recommendation is **yes**. Here’s why:

* **High-Speed, No Buffering:** Stream high-resolution content (including 4K) without buffering (experience may vary based on your internet connection).
* **Safety/Privacy:** If you live in a country that monitors torrent activity, the debrid service keeps your activity safe.
* **Reliability:** Content is often available even if the original torrent source goes offline.
* **Cost:** A small monthly cost (around $3 USD for a 6-month Real-Debrid subscription) provides a high-quality, Netflix-like experience.

If you live in a torrent-friendly country, use a VPN, and are okay with occasional buffering, you can technically skip it, but the experience will be noticeably worse.

### Debrid Provider Recommendations

**Real-Debrid** is the top recommendation due to its excellent cost-to-value ratio and massive cached library. The 6-month subscription makes the monthly cost very low.

Alternatives include **AllDebrid** or **TorBox**, which are similarly priced.

> **Important Usage Note:**
> You **cannot** use Real-Debrid from multiple geographic locations (different public IP addresses) at once. Doing so risks having your account banned. You can, however, connect from unlimited devices as long as they all share the same public IP address. **TorBox, Premiumize, and EasyDebrid** do not have this IP limitation.

### Is Stremio safe to use?

Yes, as long as you take normal precautions, such as always downloading the application from official sources.

### Is Stremio legal?

The application itself is legal. However, depending on the add-ons you install (especially those accessing copyrighted material), the content streaming *might not* be legal in your jurisdiction.

### Do I need a VPN?

If you are using a **debrid service** (like Real-Debrid) with Stremio, you **DO NOT** need a VPN for safe streaming, as the debrid service handles the torrenting connection. You might still want a VPN for general internet security outside of Stremio.

If you are not using a debrid service, you should research your country's laws. Countries like the US, UK, Canada, and Australia are stricter regarding torrenting, while Spain, Switzerland, and Poland are generally considered safe. **If your country is strict, you MUST use a debrid service (recommended) or a VPN.**

### Do I have to repeat the setup process on every device?

No. Stremio is cloud-based. Add-ons, your library, and in-progress content are linked to your account and will sync across all your devices once you log in.

### iPhone/iPad Support

As of August 2025, the Stremio team has released a native iOS app, installable from the App Store.

Alternatively, you can use the full experience through the web client along with an external player.

> **Crucial Note for iOS/iPadOS:**
> **Both options require a debrid service; it WILL NOT work without one.**

### Where can I find more add-ons?

Look in the add-ons section within the app, on excellent community lists, or search relevant subreddits.

### Can I mark content as watched on my Trakt account?

Yes. Go to **Settings** and log into your **Trakt** account (this option is not present on Android TV). Stremio will automatically mark a movie or TV show as watched once you finish it.

The above guide has been inspired by this Reddit [post](https://www.reddit.com/r/StremioAddons/comments/17833ms/stremio_all_you_need_to_know/)
