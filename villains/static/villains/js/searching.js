$(document).ready(function(){
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
                            str+='<div id="villainBlock">'
                            +'<a href="detail/'+result[i].pk+'/">'
                            +'<h1>빌런 이름 : '+result[i].name
                            +'</h1><h3>대학:'+result[i].univ
                            +'</h3><h3>전공:'+result[i].major
                            +'</h3><h3>수업명: '+result[i].className
                            +'</h3><h3>bomb:'+result[i].bomb
                            +'</h3></div><br>';
                        }
                        $('.originalBlock').css('display','none');
                        $('.searchBlock').css('display','block');
                        $('.searchBlock').html(str);
                    }else{
                        $('.originalBlock').css('display','none');
                        $('.searchBlock').css('display','block');
                        str="검색 결과가 없습니다" //검색 결과가 없을 때
                    }
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