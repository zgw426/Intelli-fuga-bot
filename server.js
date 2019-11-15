'use strict';

const express = require('express');
const line = require('@line/bot-sdk');
const axios = require('axios');
const PORT = process.env.PORT || 3000;

const config = {
    channelSecret: '',
    channelAccessToken: ''
};

const app = express();

app.post('/webhook', line.middleware(config), (req, res) => {
    console.log(req.body.events);
    Promise
      .all(req.body.events.map(handleEvent))
      .then((result) => res.json(result));
});

const client = new line.Client(config);

function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    return Promise.resolve(null);
  }

  let mes = ''
  mes = '『' + event.message.text + '』の意味は…'
  getNodeVer(event.source.userId , event.message.text);

  return client.replyMessage(event.replyToken, {
    type: 'text',
    text: mes
  });
}

const getNodeVer = async (userId, argKey) => {
    //辞書API
    let apiUrl = 'https://xxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/demo?test_id='+ argKey;
    apiUrl = encodeURI(apiUrl); // URLエンコード
    const res = await axios.get( apiUrl );

    console.log(res.data.name);
    await client.pushMessage(userId, {
        type: 'text',
        text: res.data.name,
    });
}

app.listen(PORT);
console.log(`Server running at ${PORT}`);