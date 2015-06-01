var myapp = angular.module("app", ['chart.js']);

myapp.controller("VpsSpeedTestResult", function($rootScope,$scope,$http){
  $scope.options={scaleOverride : true,
          scaleSteps : 10,
          scaleStepWidth : 50,
          scaleStartValue : 0,};
  var update=function(url)
  {
    var name=url.name;
    var _url=url.url;
    if(url==undefined)
    {
      return;
    }
    $scope.labels=null;
    $scope.data=null;
    $scope.series =null;
    $http.post('vpstest',{'uri':_url,'hours':24}).success(function(data) {
    labels=new Array();
    speed=new Array();
    var speedAdd=0;
    var averageArray=new Array();
    reversedData=data.reverse();
    for(var i=0;i<reversedData.length;i++)
    {
      labels.push(reversedData[i]['monitorTime']);
      speed.push(reversedData[i]['speed']);
      speedAdd+=reversedData[i]['speed'];
      averageArray.push(speedAdd/(i+1));

    }
      $scope.labels=labels;
      $scope.data =[speed,averageArray];
      $scope.series =[name,'average'];
    }
    );
  }
 
  var unreg=$rootScope.$on('update', function(e,args){
                update(args);
            });
  $scope.$on('$destroy',function(){
    unreg();
  });
});

myapp.controller('VpsUrlList',function ($rootScope,$scope,$http) {
 $http.post('vpsurllist').success(function(data) {
    $scope.urls = data;
  });
  $scope.click=function(url,name){
  $rootScope.$emit('update',url);
 }
 $scope.doubleClickEdit=function  ($event) {
 	$event.target.readOnly=false;
 }
 $scope.doneEdit=function($event,url){
  var newValue=$event.target.value;
  $http.post('modifyvpsname',{'uri':url.url,'name':newValue}).success(function(){
    $('.alert-holder').html('URL已成功更新').fadeIn(300).delay(3000).fadeOut(2000);  
  });
  
 }

});




