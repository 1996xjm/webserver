let data_arr = [[
	{
		url:"https://mp.weixin.qq.com/s/T6DzjpPAh5RnZX0MQ4QNgw",
		title:"Webinar精选 | 远在南海没人管？2万公里外的太空有人凝视着你",
		src:"https://mmbiz.qpic.cn/mmbiz_jpg/iaZ3fI1HIWc0P7cSl2qrMCOOyia2vsnjt7pscIuoZFic2hZ98wSkskBsVkTAa4FnRsnj64CKxBq64t2VHjoJCXrAQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1"

	},
	{
		url:"https://mp.weixin.qq.com/s/65u_HhfkaOpZ87uBk2yQtg",
		title:"Webinar精选 | 来听江豚保护者畅聊与江豚的那些故事！",
		src:"https://mmbiz.qpic.cn/mmbiz_jpg/iaZ3fI1HIWc0CrjbJicaqTrloRsQc7dsuc2qibK03pI3A6ia4JBWmzlRv0iaibkj9ZL8Yr8xc9n6ygGibHo522JS9wQQA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1"

	},
	{
		url:"https://mp.weixin.qq.com/s/-d-EiEiVV2RE3sQzwyN87w",
		title:"Webinar精选 | 我国首批限额捕捞试点，浙北梭子蟹和你必须知道的那些事",
		src:"http://mmbiz.qpic.cn/mmbiz_gif/iaZ3fI1HIWc1KK1Q6RqTpMJnZjLcySTYjgGD43gOUnbfj9EakoyxbETOCKb8rTVos00Kn4Kf2qfMOsoRpyJ5gHw/0?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1"

	}
	],[{
		url:"https://mp.weixin.qq.com/s/uaffwdr0pST5XS_iR9_j4A",
		title:"Webinar精选 | 来听海南环保圈达人聊湿地保护与社区发展！",
		src:"https://mmbiz.qpic.cn/mmbiz_jpg/iaZ3fI1HIWc3bZC3dH4MNxsQTaLB8TL8mgDx4Bx3f5Bh5wX4yhmtmEg6av8JWe1TvkfVUhEYmWtlMNUQGrRxhJQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1"

	}]];
	let content_box = document.getElementById('content')

data_arr.forEach(function(ele){

	let webinar_main_box = document.createElement('div')
	webinar_main_box.id = "webinar-main-box";
		let str = ''
	ele.forEach(function(ele){
		str +=`<div class="webinar-item-box" data-url="${ele.url}"><div class="img-box"><img class="" src="${ele.src}"></div><div class="text-box">${ele.title}</div></div>`
	});
	webinar_main_box.innerHTML = str;
	content_box.appendChild(webinar_main_box);
	webinar_main_box.onclick=function(res){
		console.log(res)
		let path_arr = res.path;
		path_arr.forEach(function(ele){
			if(ele.className == "webinar-item-box"){
				console.log(ele.dataset.url);
				window.open(ele.dataset.url);
			}
		})
	}
})
