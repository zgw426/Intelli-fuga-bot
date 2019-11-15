# fugaしか答えない残念なBotに8万語の辞書を持たせてインテリBotにした話

- 自作の辞書APIとLINEBotを連携して、言葉の意味を教えてくれるBotを作りました。
- 作り方は、こちら
  - [fugaしか答えない残念なBotに8万語の辞書を持たせてインテリBotにした話](https://qiita.com/zgw426/items/5e9d9ed7c40d976d3055)


# 概要

- 辞書データは、[日本語WordNet](http://compling.hss.ntu.edu.sg/wnja/) を使わせていただきました。
- AWSのAPI Gateway + Lambda + DynamoDBで辞書機能を持つAPIを作りました。
- DynamoDBにはWordNetのデータを加工してインポートしました。
- DynamoDBへのデータインポートは、AWS Data Pipelineを使いました。
