# Qué hace este bot?
Este bot vigila la página web que tú desees asegurándose que el servidor está
funcionando correctamente. Si el servidor se ha caído,
[@ServulitoBot](https://twitter.com/ServulitoBot) enviará un mensaje de texto
al celular que tú escojas, además de emitir notificaciones vía *mentions* en
tuiter además de *direct message*.

### Cómo instalar y configurar @ServulitoBot
Tú puedes instalar este bot en tu computadora al hacer click en **Download**.
Además deberas abrir una cuenta en <http://plivo.com>. [@ServulitoBot](https://twitter.com/ServulitoBot)
ordenará a Plivo que envíe un mensaje de texto al determinado celular avisando
que el servidor se ha caído.

Es necesario que en el *Dashboard* de Plivo consigas tus llaves **AUTH ID** y
**AUTH TOKEN** (ver imagen).

![](plivio_keys.png)

También debes crear un *app* en tu cuenta de tuiter y obtener las **llaves** de
autenticación para que tu tuiterbot pueda enviar mensajes. En esta dirección
creas tu **app** y obtienes tus llaves: <https://dev.twitter.com/apps>.

Una vez que tengas tus llaves, debes cambiar de nombre al archivo
``config.py.bak`` por ``config.py``. Luego simplemente copias y pegas tus
llaves dentro del campo correspondiente en el archivo.

    # Twitter Consumer keys
    key = "aquiVaTuLlavePrincipal"
    secret = "aquiVaTuLLaveSecreta"
    token = "ponesAquiTuToken"
    token_secret = "AquiPonesTuTokenSecreto"

    # keys from http://plivo.com
    auth_id = ""
    auth_token = ""


# Dependencias
    sudo pip install flask plivo
    sudo pip install requests
