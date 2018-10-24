(function (ng) {

    var mod = ng.module("materia", ['ui.router']);

    mod.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/x");

        $stateProvider

            .state('reservaHorario', {
                url: "/materia/:id",
                param: {
                    id: null
                },
                views: {
                    'content': {
                        templateUrl: 'materia/reservaHorario.html',
                        controller: 'materiaController'
                    }
                }
            })

	}]);

})(window.angular);



(function (ng) {

    var mod = ng.module("Materia");
    mod.constant("materiaContext", "api/materia");

    mod.controller('materiaController', ['$scope', '$http', 'materiaContext', '$state',

		function ($scope, $http, reservasContext, $state) {


            if (($state.params.id !== undefined) && ($state.params.id !== null)) {

                // 'http://localhost:8080/Alohandes_IT1/rest/personas/operadores/'+ $state.params.id +'/propuestas'
                $http.get('http://edushare.pythonanywhere.com/admin/edushareApp/materia/materias/' + $state.params.id + '/reservas').then(function (response) {
                    $scope.reservas = response.data;
                });

                $http.get('http://edushare.pythonanywhere.com/admin/edushareApp/materia/materias/' + $state.params.id).then(function (response) {
                    $scope.reservas_colectivas = response.data;
                });


            };


	}

	]);
})(window.angular);