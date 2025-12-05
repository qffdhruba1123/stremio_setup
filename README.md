# Stremio Guide
Step-by-Step Instructions to set up Stremio

## Setup

### Setting up the application

I recommend you complete the initial setup on a computer due to a web browser is needed.

1.  Go to [Stremio](https://web.strem.io/)
2.  Create an account
3.  Go to Addon Section (puzzle icon on the left bar)
4.  Uninstall WatchHub and Public Domain Movies from the addon section.

### Setting up the content

Get a Real-Debrid Subscription from [here](http://real-debrid.com/?id=15891876).
1. Create an account.
2. Get a Premium Subscription from the "Premium Offers" section. (You can get a 15 day subscription to test it out, but I suggest getting the 180 day subscription as thats the best value)
3. Get your API Key from [here](https://real-debrid.com/apitoken) (You will need this in the next step)

Now, we are going to install [Torrentio](https://torrentio.strem.fun/).

* **Providers:** default
* **Sorting:** default
* **Priority foreign language:** defaults to English. Change it if that is not your preferred language.
* **Exclude qualities/resolutions:** check "screener" and "cam" to filter out low-quality videos. You can also check "4k" if your connection is not fast enough to reproduce high-quality videos.
* **Max results per quality:** 10
* **Video size limit:** leave empty. If you have a slow connection or limited bandwidth, you can limit the video size. For instance: 2GB, 800MB (2GB for movies and 800MB for TV shows).
* **Debrid provider:** select "Real-Debrid" here
* **Debrid API Key:** paste your API key that you got in the previous step here without any spaces.
* **Debrid options (optional):** check "Don't show download to debrid links" and "Don't show debrid catalog."
* Click on **install**

**Note**

If install does not work, you can "Copy link address" from the install button, go to the Addon Section on Stremio, click on "Add addon", paste the copied URl, click "Add" and then "Install".
Check if **Torentio RD** has appeared in your addon list. If it is there, you are good to go, if not or if you just have Torrentio without the RD, uninstall the addon and try the previous section again.

**Note**

This is the last step for the basic setup. Now, go and enjoy your favorite movies and TV shows.

Although, if you want to improve the experience, please keep reading.

## How to add streaming platforms catalogs

Besides the default catalogs (lists), which cannot be removed, we can add additional ones to the home through addons.

[Streaming Catalogs](https://7a82163c306e-stremio-netflix-catalog-addon.baby-beamup.club/) provides us with listings of the most popular streaming platforms.

* Go to the link
* Change "Filter providers by country" to "Any"
* Select all the services that you want
* Click on **install**

**Note**

If install does not work, you can copy the URL from the "Manual install URL:" field go to the Addon Section on Stremio, click on "Add addon", paste the copied URl, click "Add" and then "Install".

Once you are done selecting the platforms and finished with the installation, you will see new catalogs based on those selections.

## Can I watch live TV?

Yes, you can. My recommendation is the [USA TV addon](https://stremio-addons.net/addons/usa-tv) that offers over 160 US channels in HD, including news and sports.

## FAQ

### What is Stremio?

Stremio is a free streaming app that lets you watch movies, TV shows, live channels, and more.

### What platforms are supported?

The application currently supports Windows, Mac, Linux (including Steam Deck), Android, Android TV, Samsung TVs (2019+), LG TVs (2020+), IOS, and Web.

### What differentiates it from other streaming apps?

Among its many cool features, the highlight is its add-on system, which allows us to expand what we can watch, including copyrighted content. **Torrentio is the most popular.**

### What is Torrentio?

It is an add-on that provides torrent streams from scraped torrent providers. Currently, it supports YTS, EZTV, RARBG, 1337X, The Pirate Bay, and KickassTorrents, among others. The addon also supports debrid services.

### What is a debrid service?

A debrid service is an unrestricted multi-hoster that allows you to stream and download videos instantly at the best speeds. In plain English, the debrid services act as a proxy between the BitTorrent tracker and you, so you download the content directly from their servers at high speed. Most of the content is already cached, meaning you can instantly access it.

### Do I really need to get a debrid service?

My recommendation is yes, get one. Why?

* High-speed downloads, no buffering. Yes, including 4K content (your experience might vary based on your internet connection).
* If you live in a country where internet providers monitor torrent activity, you are safe with one.
* Content may be available even after the original source is no longer available.
* A small cost gets you a Netflix-like experience for as little as $3 US dollars per month.

If you live in a country where torrenting is allowed or have a VPN and are okay with some buffering here and there, you can skip it.

### Debrid providers

My recommendation is **Real Debrid** due to its excellent cost-value benefit (just ignore the drama from a few months ago; it is still the best option for most). If you get the 6-month subscription, the monthly cost is around $3 US dollars. Another alternatives are **AllDebrid** or **TorBox**, which are at a similar price.

**Note:** You cannot use the service from several locations at once. You are allowed to connect from unlimited devices as long as they use the same public IP address. If you do, you risk having your account banned.

**TorBox**, **Premiumize**, and **EasyDebrid** don't have this limitation.

There are other options compatible with Torrentio, but the cost tends to be much higher. Although some may offer additional features:

* Premiumize
* Debrid-Link
* Offcloud
* Put.io
* EasyDebrid
* TorBox

You can find here a detailed post comparing content cached on the different debrid services.

### Is it safe to use?

Yes, as long as you take normal precautions. For instance, always download the app from official sources.

### Is it legal?

The application itself is legal. However, depending on the addons you install, some might not.

### Do I need a VPN?

It depends. If you are using a debrid service, you **DO NOT** need a VPN to safely stream content on Stremio, regardless of whether you live in a torrent-friendly country or not. Although, you might still want to get one to improve your security outside Stremio.

Countries like Spain, Switzerland, and Poland are safe regarding torrenting. Mexico, The Netherlands, and much of Eastern Europe tolerate or ignore it. However, Australia, Canada, UK, and US are stricter.

Please research about the situation of the country you live in. If it is not part of the friendly ones, you must pay for a debrid service (recommended) or a VPN.

### Do I have to repeat the setup process on every device?

No. Stremio is cloud-based. Whatever you change in your account will be reflected across devices, including add-ons, library, in-progress content, etc. Just install the app and log in with your credentials.

### Stremio is not available for my device. Can I still use it?

Yes, you just need a web browser. If Stremio is not supported by your device or you don't want to install the app, Stremio offers a web client. Just access `https://web.stremio.com/`, enter your credentials, and you are good to go.

### iPhone/iPad support

As of August 2025, the Stremio team has released a native IOS app. You can install it from the store. More info here.

You can also enjoy the full experience through the web client along with an external player. The details of how to set it up can be found in Stremio's blog.

**Both options require a debrid service, it WON'T work without one.**

### Where can I find more add-ons?

You can find them in the add-ons section within the app or on this excellent community list or search this subreddit. If you cannot find it in those places, it is very likely that doesn't exist.

### Can I mark the content as watched on my Trakt account?

Yes. Go to settings and log into your Trakt account (not present on Android TV). Stremio will automatically mark it as watched once you finish watching a movie or TV Show.

The above guide has been inspired by this Reddit [poost](https://www.reddit.com/r/StremioAddons/comments/17833ms/stremio_all_you_need_to_know/)
