
# qrcode

## QR Code info

`https://en.wikipedia.org/wiki/QR_code`

## QR Code standards

`https://www.qrcode.com/en/about/version.html`

## Image Encoding

This is interesting.

You can encode any image using `data:<mime-type>;base64,<base64>` and paste it to any browser.

Step 1 : find a small image (png, gif, avif, jpeg-xl or svg)

Step 2 : encode it in base64 and add `data:<mime-type>;base64,` in front of the text (replace `<mime-type>`). The result should be less than 2950 octets ( `https://elmah.io/tools/base64-image-encoder/` )

Step 3 : generate QR code ( `https://qr.15c.me/qr.html` thanks to `https://github.com/six-two/qr.html` )

Here is the result :

    SVG: https://ibb.co/hWGSY4d ​

    AVIF: https://ibb.co/R9Tjy6z

In order to decode I use ZXing Team's Barecode Scanner (Android). I copy the text and paste it to firefox or chrome. This should work with opera, and any other browser...

Avif might be the best choice because the compressed image can be smaller the 2 ko and the image is still visually good.

Source: `https://www.reddit.com/r/compression/comments/147cj7a/can_a_qr_code_store_a_large_image_without/`
