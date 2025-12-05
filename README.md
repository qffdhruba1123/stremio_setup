# Stremio Guide
Step-by-Step Instructions to set up Stremio

## Setup

### Setting up the application

I recommend you complete the initial setup on a computer due to a web browser is needed.

1.  Go to [Stremio](https://web.strem.io/)
2.  Create an account
3.  Uninstall WatchHub and Public Domain Movies from the addon section.

**Note:** if you own an Android-based device that doesn't include Google Play Store, for instance, a Fire TV. You either need to download the app through an alternative store like Aurora Store, Aptoide, APKPure or sideload the apk (a quick search will teach you how to do it if it is your first time).

### Setting up the content

Now, we are going to install Torrentio from `https://torrentio.strem.fun/`.

* **Providers:** default
* **Sorting:** default
* **Priority foreign language:** defaults to English. Change it if that is not your preferred language.
* **Exclude qualities/resolutions:** check "screener" and "cam" to filter out low-quality videos. You can also check "4k" if your connection is not fast enough to reproduce high-quality videos.
* **Max results per quality:** 10
* **Video size limit:** leave empty. If you have a slow connection or limited bandwidth, you can limit the video size. For instance: 2GB, 800MB (2GB for movies and 800MB for TV shows).
* **Debrid provider (optional):** if you pay for a subscription, select your provider.
* **Debrid API Key (optional):** click "here" and follow the steps to get your API key based on your provider.
* **Debrid options (optional):** check "Don't show download to debrid links" and "Don't show debrid catalog."
* Click in **install**

**Note:** if you want to install a backup add-on, please take a look at Comet, MediaFusion, TorrentsDB, or Piratebay+ (torrent-only).

You can find the full stream addons list here.

This is the last step for the basic setup. Now, go and enjoy your favorite movies and TV shows.

Although, if you want to improve the experience, please keep reading.

## How to add streaming platforms catalogs

Besides the default catalogs (lists), which cannot be removed, we can add additional ones to the home through addons.

**Streaming Catalogs** provides us with listings of the most popular streaming platforms.

Once you are done selecting the platforms and finished with the installation, you will see new catalogs based on those selections.

## Customized catalogs

This is where things get interesting. It is cool to add new catalogs based on the content from streaming platforms, but if you are like me, you probably don't care much about which platform the content comes from and more about the content itself.

The **Trakt addon** is the tool that will allow us to create an experience tailored specifically to us.

### What is Trakt?

It is a media tracking service that helps users sync their TV shows and movies across numerous platforms and devices.

### Setting up the Trakt Lists addon

Install the **Trakt addon** from the addons section or from here

The standard Trakt lists are static. In other words, if the owner of the list or collaborators don't maintain them, the content won't get updated. This might be okay for some types of lists, but dynamic lists are generally a better option. That's when **MDBList** and **couchmoney** come to the rescue.

* **MDBList**
    It offers a plethora of filters to match our search criteria. For example, we could create a list where action movies from 2010 to the present with over 60 rank on Rotten Tomatoes order by release date are shown. We can create up to 4 lists with a free account. A Trakt account is required if we want to create our own lists.
* **Couchmoney**
    It also creates custom lists based on recently watched, trending, or a specific list. We can filter the content by date, genre, language, and popularity. We can create up to 10 lists. A Trakt account is required.

Now that we have covered the basics, let's go and add a few lists.

Thanks to other users, we are not required to create our own lists. Instead, we will use **public lists** which do not need a Trakt account. I recommend you take a look at the **MDBList lists from Gary and Riz**.

Once you have found the ones you are interested in, we will add them through the Trakt addon. To easily find the list, use the search function, including the username and the list name. For instance: "garycrawfordgc horror".

The steps to add lists created by Couchmoney are the same. Keep in mind that you are going to need a Trakt account and some content marked as watched for the tool to be able to start making suggestions.

Once you are done adding the lists, it should look something like this:

**Note:** you can use a combination of static public and own Trakt lists, public and own dynamic lists created by MDBList, and own dynamic lists created by couchmoney.

Click install, and tadaaaaaa!

**Note:** you **DO NOT** need a Trakt TV account if you add public lists. It is only required if you want to access your own private lists (Watch List or Recommendations, for example) or if you want to keep track of what you have watched (scrobbling).

## Include ratings over the covers

**Rating Poster Database** has recently introduced a free tier that allows you to display IMDB, Metacritic, and Rotten Tomatoes ratings over the covers. The most popular catalogs addons include support for it, including Streaming Catalogs, Cyberflix Catalog, Trakt.tv, among others.

Go to RPBD website and create a Patreon account to get a free key. Once you have received it, introduce it in the addon/s you have chosen, and it would look like this:

That concludes the advanced setup. Congratulations, you are ready to enjoy the ultimate streaming experience!!!

## Can I watch live TV?

Yes, you can. My recommendation is the **USA TV addon** that offers over 160 US channels in HD, including news and sports.

## How to watch anime on the platform

Torrentio, along with other popular add-ons, provides most of the content. However, it is recommended to install **Anime Kitsu** to make sure the metadata is resolved correctly.

## How to watch Asian dramas

The most popular add-ons provide some Asian content. If you want to expand the chances of finding what you are looking for, please install the **StreamAsia add-on**. More info can be found here in the official addon post.

## How can I change the order of my addons?

Stremio currently doesn't allow users to change the order in which their installed addons appear on the home screen. As a workaround, it is common for users to remove and re-install add-ons in the order they want them to appear. This is a tedious and cumbersome process as you can imagine.

**Addon Manager** uses the internal Stremio API to manipulate addon order without having to add/remove them.

**Note:** the default lists cannot be removed, but you can push them down or you can use **Hidden Cinemeta**.

**Stremio Account Bootstrapper** already does this for you.

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
