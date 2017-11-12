# uPyPortal
A captive portal for MicroPython using ESP32 (WeMos)

#### Disclaimer
I assume no responsibility for the usage of this code and post. The book "The Hacker Playbook 2: Practical Guide to Penetration Testing - Peter Kim" says
> Just remember, ONLY test systems on which you have written permission. Just Google the term “hacker jailed” and you will see plenty of different examples where young teens have been sentenced to years in prison for what they thought was a “fun time.” There are many free platforms where legal hacking is allowed and will help you further educate yourself.
>

# Requirements

<table class="uk-table uk-table-hover components">
<tr>
<td><img src="https://lemariva.com/storage/blogs_imgs/wemos/wemos-min.png" width="30px" alt="WeMos"> </td><td> WeMos WiFi ESP32 Development Tool</td>
<td align="right">x 1</td>
<td align="right" style="vertical-align:middle">
<a href="https://www.banggood.com/WeMos-WiFi-Bluetooth-Battery-ESP32-Development-Tool-p-1164436.html?p=QW0903761303201409LG" target="_blank">
buy
</a>
</td>
</tr>
<tr>
<td><img src="https://lemariva.com/storage/blogs_imgs/wemos/inr-18650-min.png" width="30px" alt="INR18650"> </td><td> INR18650 3.7v Battery</td>
<td align="right">x 1</td>
<td align="right" style="vertical-align:middle">
<a href="https://www.banggood.com/4PCS-Samsung-INR18650-30Q-3000mAh-Unprotected-Button-Top-18650-Battery-p-1067185.html?p=QW0903761303201409LG" target="_blank">
buy</a>
<a href="https://www.banggood.com/1PCS-NR18650-30Q-3000mah-20A-Power-Li-ion-Battery-for-Samsung-p-981565.html?p=QW0903761303201409LG" target="_blank">
buy</a>
</td>
</tr>
<tr>
<td><img src="https://lemariva.com/storage/language_logos/compressed/python2_logo-min.png" width="30px" alt="Python"> </td><td> MicroPython</td>
<td align="right"></td>
<td align="right" style="vertical-align:middle">
<a href="http://micropython.org/download#esp32" target="_blank">
download
</a>
<a href="https://lemariva.com/blog/2017/10/micropython-getting-started" target="_blank">
tutorial
</a>
</td>
</tr>
<tr>
<td><img src="https://lemariva.com/storage/language_logos/compressed/python2_logo-min.png" width="30px" alt="Python"> </td><td> uPyPortal</td>
<td align="right"></td>
<td align="right" style="vertical-align:middle">
<a href="https://github.com/lemariva/uPyPortal" target="_blank">
download
</a>
</td>
</tr>
</table>

# DIY
* Read the following blog article: https://goo.gl/3jQzQV

# Credits

* For the logging data, I took the files from <a href="http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/" target="_blank">notes-pico<i class="uk-icon-justify uk-icon-link"></i></a> and modified them.
* For DNS fake code I wrote a `dns.py` file using info from <a href="http://www.tranquilidadtecnologica.com/2006/04/servidor-fake-dns-en-python.html" target="_blank">here<i class="uk-icon-justify uk-icon-link"></i></a> mirrored <a href="http://code.activestate.com/recipes/491264-mini-fake-dns-server/" target="_blank">here<i class="uk-icon-justify uk-icon-link"></i></a>.
