$(document).ready(function(){
    if($('body').height()>window.screen.height){
        $('footer').css('position','static');
    }
    searchAjax();
  });

function searchAjax(){
    $('.searchText').keyup(function(){
        var text = $('.searchText').val();
        var type = $('.searchType').val();
        if(text!=''){
            
            $.ajax({
                type: "GET",
                url: "/search",
                data:{ searchText:text, searchType:type},
                dataType:'json',
                contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                success:function(result){
                    var str="";
                    if(result.length>0){
                        for(var i=0; i<result.length; i++){
                            str+='<div class="villainBlock">'
                            +'<a href="detail/'+result[i].pk+'/">'
                            +'<div class = "villainClass">'+result[i].major
                            +'<br>강의명 : '+result[i].className
                            +'</div><div class = "villainName">'+result[i].name
                            +'</div><div class = "villainBomb">'+result[i].bomb
                            +' 폭탄</div></a></div>';
                        }
                        $('.searchBlock').html(str);
                        $('.searchBlock').css('text-align','left');
                    }else{
                        str="검색 결과가 없습니다"
                        $('.searchBlock').css('text-align','center'); //검색 결과가 없을 때
                    }
                    $('.originalBlock').css('display','none');
                    $('.searchBlock').css('display','block');
                    $('.searchBlock').html(str);
                },
                error : function (e) {console.log('error:'+e.status);}
            })
        } else {
            $('.originalBlock').css('display','block');
            $('.searchBlock').css('display','none'); //입력창이 비어있을 때
        }
    });
}