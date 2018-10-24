(function (ng) {

    var mod = ng.module("monitor", ['ui.router']);

    mod.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/x");

        $stateProvider

            .state('reservaHorario', {
                url: "/monitor/:id",
                param: {
                    id: null
                },
                views: {
                    'content': {
                        templateUrl: 'monitor/reservaHorarios.html',
                        controller: 'monitorController'
                    }
                }
            })

	}]);

})(window.angular);



(function (ng) {

    var mod = ng.module("onitor");
    mod.constant("monitorContext", "api/monitor");

    mod.controller('monitorController', ['$scope', '$http', 'monitorContext', '$state',

		function ($scope, $http, reservasContext, $state) {


            if (($state.params.id !== undefined) && ($state.params.id !== null)) {

                // 'http://localhost:8080/Alohandes_IT1/rest/personas/operadores/'+ $state.params.id +'/propuestas'
                $http.get('http://edushare.pythonanywhere.com/admin/edushareApp/monitor/' + $state.params.id + '/reservas').then(function (response) {
                    $scope.reservas = response.data;
                });

                $http.get('http://edushare.pythonanywhere.com/admin/edushareApp/monitor/' + $state.params.id).then(function (response) {
                    $scope.reservas_colectivas = response.data;
                });


            };


	}

	]);
})(window.angular);