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


// log.htmlのjsここから

// 任意のタブにURLからリンクするための設定
function link (hashIDName){
	if(hashIDName){
		//タブ設定
		$('.tab li').find('a').each(function() { //タブ内のaタグ全てを取得
			var idName = $(this).attr('href'); //タブ内のaタグのリンク名（例）#lunchの値を取得
			if(idName == hashIDName){ //リンク元の指定されたURLのハッシュタグ（例）http://example.com/#lunch←この#の値とタブ内のリンク名（例）#lunchが同じかをチェック
				var parentElm = $(this).parent(); //タブ内のaタグの親要素（li）を取得
				$('.tab li').removeClass("active"); //タブ内のliについているactiveクラスを取り除き
				$(parentElm).addClass("active"); //リンク元の指定されたURLのハッシュタグとタブ内のリンク名が同じであれば、liにactiveクラスを追加
				//表示させるエリア設定
				$(".area").removeClass("is-active"); //もともとついているis-activeクラスを取り除き
				$(hashIDName).addClass("is-active"); //表示させたいエリアのタブリンク名をクリックしたら、表示エリアにis-activeクラスを追加
			}
		});
	}
}

//タブをクリックしたら
$('.tab a').on('click', function() {
	var idName = $(this).attr('href'); //タブ内のリンク名を取得
	link (idName);//設定したタブの読み込みと
  console.log(idName)
	return false;//aタグを無効にする
});

// 上記の動きをページが読み込まれたらすぐに動かす
$(window).on('load', function () {
  $('.tab li:first-of-type').addClass("active"); //最初のliにactiveクラスを追加
  $('.area:first-of-type').addClass("is-active"); //最初の.areaにis-activeクラスを追加
  var hashName = "#log_before"; //リンク元の指定されたURLのハッシュタグを取得
  console.log(hashName)
  link (hashName);//設定したタブの読み込み
});

// log.htmlのjsここまで


// ↓以下payment.htmlでエラーが起きるみたいなので一旦コメントアウト

// const btn = document.getElementById("btn");
// const modal = document.getElementById("modal2");

// btn ? console.log(btn) : console.log("nothing");
// modal ? console.log(modal) : console.log("no modal");

// btn.addEventListener("click", () => {
//   console.log("click!!");
//   modal.style.display = "flex";
// });