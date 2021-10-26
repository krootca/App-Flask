var gotoUP=document.getElementById('GOTOUP');
var num=1;
function GOTO() {
	if (num==1) {
		goto.className="goto";
		goto.scrollIntoView()
		window.scroll(0,2900)
		num=2;
	}else{
		goto.className="goto2";
		goto.scrollIntoView()
		window.scroll(0,2900)
		num=1;
	}
			
};
function GotoUp() {
	window.scroll(0,0)
};