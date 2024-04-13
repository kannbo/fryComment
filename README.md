# FlyCommentの使い方
## flyCommentのURL
https://frycomment.onrender.com がFlyCommentのURLです。
## flyCommentの準備
作成パスワードでIDを作成するのでメモ、URLは自由な文字列を入力して作成するを押す<br>
https://frycomment.onrender.com/comment/(入力したURL)/id_make を開き作成パスワードに作成パスワードを入力<br>
作成完了なら第一は成功!<br>
## flyCommentの作成
コメント欄を作成するには、formのPostアクションを使用します。<br>
https://frycomment.onrender.com/comment/(入力したURL)/(id)/add あてにtext nameの要素のあるformを作成する。<br>
それで投稿フォームは完量しました!!<br>
## flyCommentの確認
https://frycomment.onrender.com/comment/(入力したURL)/(id)/html/(HTMLのコード)<br>
HTMLのコードには<br>
<ul>
  <li><code>$name</code>-投稿主の名前</li>
  <li><code>$text</code>-内容</li>
  <li><code>$time</code>-投稿時間</li>
</ul>
を使用できます。<br>またJsonで取得できます。https://frycomment.onrender.com/comment/(入力したURL)/(id)/json<br>
から取得します。
##おわり
これであなたも簡単にchatを作れます!!
