function VpsSpeedTestResult($scope,$http) {
 $http.post('vps',{'uri':'http://fra-de-ping.vultr.com/vultr.com.100MB.bin','hours':3}).success(function(data) {
    $scope.result = data;
  });
}
PhoneListCtrl.$inject = ['$scope', '$http'];