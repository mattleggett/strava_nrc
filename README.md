# Linking NRC Data with Strava
## Script to hopefully align strava data with nrc

### Get auth token for NRC
This is one of the more difficult steps as Nike don't make it easy to get a bearer token.
I will update the quickest steps here when completed; for now I shall explain one possible way of generating a bearer token.

For me, my main source for this initial approach was this [gist](https://gist.github.com/niw/858c1ecaef89858893681e46db63db66)
(After going about this in a very hacky way, there may be better alternatives from reading some comments in the gist.)

**Problem**: It is currently not possible to access the necessary API token from logging into [https://www.nike.com/gb/member/profile]() and inspecting the request network headers for one of the form `Authorization: Bearer base64EncodedString`. \
Now I believe it is possible to actually find this from a specific *https://unite/...* url request here, but it was not the approach I used.

Instead, from research, I found the Bearer token by using [Charles](https://www.charlesproxy.com/documentation/welcome/), the web debugging proxy application with my iPhone (the biggest issue for me in this process was making sure I had SSL Proxy enabled - more on this further down).
The mostly followed the [Charles docs](https://www.charlesproxy.com/documentation/faqs/using-charles-from-an-iphone/) but have summarised the important points below.

  1. On mac, run `brew install --cask charles`
  2. To get your local ip address on mac, run `ipconfig getifaddr en0`
  3. On your iPhone Settings, go to:
        - Wi-Fi
        - Tap the blue *i*
        - Scroll to the bottom and select Configure Proxy
        - Use Manual, set the Server to your ip address found in 2, and the default port is 8888 (leave Authentication off)
  4. Then go to [https://chls.pro/ssl]() where you should be prompted to download this SSL certificate
  5. Back in Settings you should be prompted to verify the new downloaded profile. Then, go to:
        - General
        - About
        - Certificate Trust Settings
        - Find the Charles Proxy CA and slide to enable full trust
  6. Back on your machine, open Charles and accept any default settings on startup( you should start seeing requests pop up on the left hand panel if connected to the internet)
  7. Open up the NRC app on your phone, and you should see requests coming from multiple sources related to Nike
  8. Navigate down the structure of any of these requests to the lowest level, and here you will be able to click on Contents and read the headers associated with that request
  9. Copy the Authorization header
  10. Undo the trust settings for your certificate and remove the SSL Proxy in your phone settings
