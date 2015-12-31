app = angular.module('olhovivo.app', ['ngResource']);

app.factory('Resource', function($resource){
    return $resource("/api/resources", {}, {
        query: {method: "GET", isArray: true}
    });
});

app.controller('ResourceController', function($scope, Resource){
    $scope.resources = [];
    $scope.chartDiv = document.getElementById('chart');
    $scope.data = [["Categoria", "Total Ano"]];
    $scope.options = {
        title: "Recursos por Categoria",
        is3D: true
    }

    $scope.drawChart = function(){
        var chart = new google.visualization.PieChart($scope.chartDiv);
        var data = google.visualization.arrayToDataTable($scope.data);
        chart.draw(data, $scope.options);
    }

    Resource.query(function(resources){
        $scope.resources = resources;

        for (var i=0; i<resources.length; i++){
            var resource = resources[i];
            $scope.data.push([resource.category, resource.total_year]);
        }

        $scope.drawChart();
    })

});

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(function() {
    angular.bootstrap(document.body, ['olhovivo.app']);
});
