comment={
comments:function(x){
  this.comment_name=x
},
setid:function(x){
  this.comment_id=x
},
get:function(){
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    const data = xhr.responseText;
    console.log(data)
    return data
  } else {
    return `Error: ${xhr.status}`
  }}
  console.log(`https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/json`)
  xhr.open("GET", `https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/json`,true);
  xhr.send(null);
},
comment_id:"",comment_name:"",
list:function(x){
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    const data = xhr.responseText;
    console.log(data)
    return data
  } else {
    return `Error: ${xhr.status}`
  }}
  console.log(`https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/html/${x}`)
  xhr.open("GET", `https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/html/${x}`,true);
  xhr.send(null);
},
enter:function(x,y){
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    const data = xhr.responseText;
    console.log(document.getElementById("comment").innerHTML)
    document.getElementById("comment").innerHTML = data
  } else {
    return `Error: ${xhr.status}`
  }}
  console.log(`https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/html/${x}`)
  xhr.open("GET", `https://commentserver.pythonanywhere.com/comment/${this.comment_name}/${this.comment_id}/html/${x}`,true);
  xhr.send(null);
},
version:"v.0.01"
}
