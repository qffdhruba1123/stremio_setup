# 🚀 Current Addon Setup
Will be updated as I make any changes.  
Please make sure to have completed the [initial setup](https://github.com/qffdhruba1123/stremio_setup/blob/main/README.md) before trying to add any of the addons below.  
The addons are listed in the order installed.

## 🔑 Required API Keys  
- **Your Real-Debrid Key** > [Get the key](https://real-debrid.com/apitoken)
- **Google Gemini API Key** > [Get the key](https://aistudio.google.com/app/apikey) (You need to generate a key here, there is a free tier with enough rate limits for individual use.)
- **TMDB API Key** > [Get the key](https://www.themoviedb.org/settings/api) (Create an account and generate a key, free tier has generous limits.)
- **TVDB API Key** > [Get the key](https://thetvdb.com/api-information) (Create an account and generate a key, free tier has generous limits.)
- **Fanart.tv API Key** > [Get the key](https://fanart.tv/get-an-api-key/) (Create an account and generate a personal key, free tier has generous limits.)
- **RPDB API Key** > [Get the key](https://ratingposterdb.com/) (Click "See Plans" > Join their Patreon > get a free API key)
- **MDBList API Key** > [Get the key](https://mdblist.com/) (Create an account and generate a key, free tier has generous limits.)

## 🤖 [AI Search](https://stremio.itcon.au/aisearch/configure)
- **Description**: AI-powered movie and series recommendations.
- **Configuration**: According to your preference.
- **Comment**: Untick "Show AI Recommendations on Homepage" under Advanced Options to make sure your homepage is not cluttered.

## 📺 [Trakt Tv](https://2ecbbd610840-trakt.baby-beamup.club/configure/)
- **Description**: Addon for getting Trakt's public and user lists, recommendations, and watch list.
- **Configuration**: According to your preference.
- **Comment**: I like having the trending lists and search enabled to enhance content discovery.

## 🧠 [AIOMetadata | ElfHosted](https://aiometadata.elfhosted.com/configure/)
- **Description**: A metadata addon for power users that utilizes sources like TMDB, TVDB, TVMaze, MyAnimeList, and IMDB. As configuration can be a bit involved, feel free to use the config file below, you can add you own api keys after import.
- **Configuration**: [Config File](https://github.com/qffdhruba1123/stremio_setup/blob/main/aiometadata-config.json). Make sure to enter the required API Keys. To import config file go to "Configuration" tab and then click "Import Configuration", and then enter your API Keys on the "Integration" tab.

## 📊 [Ratings](https://72059fbbd1e5-stremio-addon-ratings.baby-beamup.club/configure/#/)
- **Description**: Displays scores and age ratings (such as IMDB episode and MyAnimeList) at the top of your streams.
- **Configuration**: According to your preference.

## 🛠️ [Statusio](https://statusio.elfhosted.com/configure)
- **Description**: Shows premium status and days remaining across multiple debrid providers.
- **Configuration**: Needs to be configured with your Real-Debrid API Key. Other configuration options should be selected according to your preference.

## 🔗 [AIOStreams Stable](https://aiostreamsfortheweebsstable.midnightignite.me/stremio/configure)
- **Description**: Consolidates multiple Stremio addons and debrid services into a single, easily configurable interface. As configuration can be a bit involved, feel free to use the config file below, you can add you own api keys after import.
- **Configuration**: [Template File](https://github.com/qffdhruba1123/stremio_setup/blob/main/aiostream-template.json). Make sure to enter the required API Keys, including your Real-Debrid API Key. To load template, go to "Save and Install" option on the left, "Import" and then "Import Template".

## 🌊 [MediaFusion | ElfHosted RD](https://mediafusion.elfhosted.com/configure)
- **Description**: Universal Stremio addon for Movies, Series, Live TV, and Sports Events.
- **Configuration**: Needs to be configured with your Real-Debrid API Key. Other configuration options should be selected according to your preference.

## ⚡ [Torrentio RD](https://torrentio.strem.fun/configure)
- **Description**: Provides torrent streams from various scraped providers, enhanced with Real-Debrid support.
- **Configuration**: Needs to be configured with your Real-Debrid API Key. Other configuration options should be selected according to your preference.
- **Comment**: Torrentio has been sporadic in its availability, which is why I highly recommend adding Comet and MediaFusion. Make sure to set them up with your Real-Debrid Key.

## ☄️ [Comet | RD](https://comet.elfhosted.com/configure)
- **Description**: A fast torrent and debrid search addon.
- **Configuration**: Needs to be configured with your Real-Debrid API Key. Other configuration options should be selected according to your preference.

## ☁️ [Debrid Search](https://68d69db7dc40-debrid-search.baby-beamup.club/configure)
- **Description**: Stremio Addon to search downloads and torrents in your Debrid cloud
- **Configuration**: Needs to be configured with your Real-Debrid API Key.
- **Comment**: This is useful in cases when a scraper addon occasionally requests the file on Real-Debrid but throws an error when starting the stream. This addon will pickup that file, and you can use the link generated by this addon to stream instead of the link by the scraper.

## ↕️ Final order of addons
This list includes all addons in the final setup, including the default pre-installed addons.
Use this tool to change order of addons: [Stremio Addon Manager](https://stremio-addon-manager.vercel.app/)
- AI Search
- Trakt Tv
- AIOMetadata
- Cinemeta
- Local Files
- OpenSubtitles
- OpenSubtitles v3
- Ratings
- Statusio
- AIOStreams
- MediaFusion
- Torrentio
- Comet
- Debrid Search

