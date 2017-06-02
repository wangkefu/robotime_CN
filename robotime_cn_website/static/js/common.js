$(".brands ul li:nth-child(1)").each(function(){
	$(this).click(function(){
		if($(document).width()>=974){
			return
		}else{
			console.log('ss')
			$(this).siblings().slideToggle()
		}
	})
})

$(".xs_to").each(function(){
	$(this).mouseenter(function(){
		if($(document).width()>=751){
			$(".down_menu_wraper").show()
			$(this).children("div").show()
			$(this).children("div").css({"position":"absolute","padding-left":"0px"})
		}
		
	})
	$(this).mouseleave(function(){
		if($(document).width()>=751){
			$(".down_menu_wraper").hide()
			$(this).children("div").hide()
		}
	})
	$(this).children('a').click(function(){
		if($(document).width()<751){
			$(this).siblings().slideToggle()
			$(this).siblings().css({"position":"static","padding-left":"25px"})
			console.log('ssss')
			return false
		}
	})
	
})
window.onresize = function(){
//	console.log($(document).width())
}
