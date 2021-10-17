// index.htmlのjsここから

//アコーディオンをクリックした時の動作
$(".title").on("click", function () {
  //タイトル要素をクリックしたら
  var findElm = $(this).next(".box"); //直後のアコーディオンを行うエリアを取得し
  $(findElm).slideToggle(); //アコーディオンの上下動作

  if ($(this).hasClass("close")) {
    //タイトル要素にクラス名closeがあれば
    $(this).removeClass("close"); //クラス名を除去し
  } else {
    //それ以外は
    $(this).addClass("close"); //クラス名closeを付与
  }
});

// index.htmlのjsここまで

const btn = document.getElementById("btn");
const modal = document.getElementById("modal2");

btn ? console.log(btn) : console.log("nothing");
modal ? console.log(modal) : console.log("no modal");

btn.addEventListener("click", () => {
  console.log("click!!");
  modal.style.display = "flex";
});