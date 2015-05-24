var myapp = angular.module("app", ['chart.js']);

myapp.controller("VpsSpeedTestResult", function($rootScope,$scope,$http){
  var update=function(url)
  {
    if(url==undefined)
    {
      return;
    }
    $scope.labels=null;
    $scope.data=null;
    $http.post('vpstest',{'uri':url,'hours':24}).success(function(data) {
    labels=new Array();
    speed=new Array();
    reversedData=data.reverse();
    for(var i=0;i<reversedData.length;i++)
    {
      labels.push(reversedData[i]['monitorTime']);
      speed.push(reversedData[i]['speed']);
    }
      $scope.labels=labels;
      $scope.data =[speed];
      $scope.url=url;
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
  $scope.click=function(url){
  $rootScope.$emit('update',url);
 }

});




