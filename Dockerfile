FROM kenhv/kensurbot:debian

RUN set -ex \
    && git clone -b master https://github.com/samuca78/LBot /root/userbot \
    && chmod 777 /root/userbot

WORKDIR /root/userbot/

CMD ["python3", "-m", "userbot"]
