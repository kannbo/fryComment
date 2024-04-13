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

# Comment.js
## comment.jsとは
このコードではどうしてもJSがある程度できる方のみ使えるコードになってしまいます。できる方はそれでいいですが、初心者向けに用意しました。<br>
Comment.jsは簡単,使いやすいをモットーとしてできました。<br>
どうしても簡単なので複雑なことはできませんが、そこはご理解ご協力いただけると幸いです
## 関数一覧
こちらです
<ul>
  <li><code>comments</code>-コメントのURLを指定します。引数はx,URLを入力します</li>
  <li><code>setid</code>-コメントのidを指定します引数はx,URLを入力します</li>
  <li><code>get</code>-コメントをjsonで取得します</li>
  <li><code>list</code>-コメントをHTMLで取得します。引数はx。xは一つの要素のHTMLを入力します。$textで内容,$nameで名前、$timeで時間です。</li>
  <li><code>enter</code>-コメントをID"comment"に出力します。引数はx,HTMLを入力します。listと同じです</li>
</ul>

## 使用
<code><script src="https://kannbo.github.io/fryComment/comment.js"></script></code><br>
このコードを張ると使用できます。<br><code><script>
console.log(document.getElementById("comment").innerHTML)
comment.comments("dsds")
comment.setid("dsds")
comment.enter("$name:$text<br>")
</script></code>
<!--<style>
  code{
    display:block;
  }
</style>-->
